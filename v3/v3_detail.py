from urllib.request import urlopen

from bs4 import BeautifulSoup
import requests
import json

from v3 import v3_const, v3_sql


def v3_detail(name, category, id):
    key = name + '_' + category + '_' + id
    result = v3_sql.get_article(key)
    if result == 'no':
        if name == 'one':
            result = _v3_one_detail(category, id)
        elif name == 'sspai':
            result = _v3_sspai_detail(category, id)
        elif name == 'qdaily':
            result = _v3_qdaily_detail(category, id)
        elif name == '36kr':
            result = _v3_36kr_detail(category, id)
        v3_sql.put_article(key, result)
    return result


def _v3_one_detail(category, id):
    if category == '1':
        url = v3_const.v3_categories['one']['detail_article'] + id
    elif category == '2':
        url = v3_const.v3_categories['one']['detail_serial'] + id
    elif category == '3':
        url = v3_const.v3_categories['one']['detail_question'] + id
    elif category == '4':
        url = v3_const.v3_categories['one']['detail_music'] + id
    elif category == '5':
        url = v3_const.v3_categories['one']['detail_movie'] + id
    else:
        url = ''
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find(name=['p', 'div'], attrs={'class': 'text-title'}).text.strip()
    try:
        subtitle = soup.find('p', attrs={'class': 'text-subtitle'}).text.strip()
    except:
        subtitle = ''
    try:
        author = soup.find(name=['p', 'div'], attrs={'class': ['text-simple-author', 'text-author']}).text.strip()
    except:
        author = ''

    contents = soup.find_all('div', attrs={'class': 'text-content'})
    editors = soup.find_all('p', attrs={'text-editor'})
    content_list = []
    try:
        i = soup.find('div', attrs={'class': 'text-music-info'})
        info = {"type": v3_const.v3_item_type['text_cen'], 'info': i.text.strip().replace('"', '\'')}
        content_list.append(info)
    except:
        pass

    if len(contents) > 1:
        content = contents[1]
        asker = soup.find('div', attrs={'class': 'text-askers'}).text.strip()
        info = {'type': v3_const.v3_item_type['text_cen'], 'info': asker.replace('"', '\'')}
        content_list.append(info)
        question = contents[0].text
        info = {'type': v3_const.v3_item_type['text'], 'info': question.replace('"', '\'')}
        content_list.append(info)
        answer = soup.find('div', attrs={'class': 'text-answers'}).text.strip()
        info = {'type': v3_const.v3_item_type['text_cen'], 'info': answer.replace('"', '\'')}
        content_list.append(info)
    else:
        content = contents[0]

    content_soup = BeautifulSoup(str(content), 'html.parser')
    items = content_soup.find_all(name=['p', 'img'])[1:]
    for i in range(len(items)):
        item = items[i]
        type = v3_const.v3_item_type['text']
        info = ''
        if item.name == 'p':
            info = item.text
            try:
                if item['style'] == 'text-align: center;':
                    type = '7'
            except:
                pass
        elif item.name == 'img':
            type = v3_const.v3_item_type['image']
            info = item['src']
        if info == 'http://image.wufazhuce.com/music_copyright_2_2.png' or info == 'http://image.wufazhuce.com/music_copyright_1.png':
            info = ''
        if info != '':
            info = info.replace('"', '\'')
            content_list.append({'type': type, 'info': info})
    for i in range(len(editors)):
        editor = editors[i].text
        info = {'type': v3_const.v3_item_type['text_cen'], 'info': editor.replace('"', '\'')}
        content_list.append(info)
    result = v3_const.v3_get_default_detail_item()
    result['title'] = title
    result['subtitle'] = subtitle
    result['author'] = author
    result['content'] = content_list
    return json.dumps(result, ensure_ascii=False)


def _v3_sspai_detail(category, id):
    url = v3_const.v3_categories['sspai']['detail'] + id
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('article')
    content_soup = BeautifulSoup(str(content), 'html.parser')
    title = content.h1.text
    head_content = content_soup.find('div', attrs={'class': 'meta'})
    author = head_content.h4.text
    date = head_content.time.text

    content_list = []
    content = content_soup.find('div', attrs={'id': 'article-content'})
    content_soup = BeautifulSoup(str(content.div.div), 'html.parser')
    items = content_soup.find_all(name=['p', 'img', 'h2', 'li', 'h4', 'dt', 'h3'])
    for i in range(len(items)):
        item = items[i]
        type = v3_const.v3_item_type['text']
        info = ''
        if item.name == 'p' or item.name == 'dt':
            info = item.text.strip()
        elif item.name == 'img':
            type = v3_const.v3_item_type['image']
            info = item['src']
        elif item.name == 'li':
            type = v3_const.v3_item_type['li']
            info = item.text.strip()
        elif item.name == 'h2':
            type = v3_const.v3_item_type['h1']
            info = item.text
        elif item.name == 'h3':
            type = v3_const.v3_item_type['h2']
            info = item.text
        elif item.name == 'h4':
            type = v3_const.v3_item_type['h3']
            info = item.text
        if info != '':
            info = info.replace('"', '\'')
            content_list.append({'type': type, 'info': info})

    result = v3_const.v3_get_default_detail_item()
    result['title'] = title
    result['author'] = author
    result['date'] = date
    result['content'] = content_list
    return json.dumps(result, ensure_ascii=False)


def _v3_qdaily_detail(category, id):
    url = v3_const.v3_categories['qdaily']['detail'] + id + '.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    # return response.text
    soup = BeautifulSoup(response.text, 'html.parser')
    head = soup.find('div', attrs={'class': 'article-detail-hd'})
    head_soup = BeautifulSoup(str(head), 'html.parser')
    title = head_soup.find('h1', attrs={'class': 'title'}).text
    author = head_soup.find('div', attrs={'class': 'author'}).text
    date = head_soup.find('span', attrs={'class': 'date'}).text

    content_list = []
    content = soup.find('div', attrs={'class': 'detail'})
    content_soup = BeautifulSoup(str(content), 'html.parser')
    items = content_soup.find_all(name=['p', 'img', 'h3', 'h2', 'li', 'blockquote', 'figcaption'])

    for i in range(len(items)):
        item = items[i]
        type = v3_const.v3_item_type['text']
        info = ''
        if item.name == 'p':
            info = item.text

            if len(content_list) > 0 and info in content_list[len(content_list) - 1]['info']:
                info = ''
            elif info.strip()[:4] == 'p.p1':
                info = ''
        elif item.name == 'img':
            type = v3_const.v3_item_type['image']
            info = item['data-src']
        elif item.name == 'h3':
            type = v3_const.v3_item_type['h1']
            info = item.text
        elif item.name == 'h4':
            type = v3_const.v3_item_type['h2']
            info = item.text
        elif item.name == 'li':
            type = v3_const.v3_item_type['li']
            info = item.text
        elif item.name == 'blockquote':
            type = v3_const.v3_item_type['quote']
            info = item.text.strip()
        elif item.name == 'figcaption':
            type = v3_const.v3_item_type['text_cen']
            info = item.text

        if info != '':
            info = info.replace('"', '\'')
            content_list.append({'type': type, 'info': info})

    result = v3_const.v3_get_default_detail_item()
    result['title'] = title
    result['author'] = author
    result['date'] = date
    result['content'] = content_list
    return json.dumps(result, ensure_ascii=False)
    pass


def _v3_36kr_detail(category, id):
    url = v3_const.v3_categories['36kr']['detail'] + id
    response = requests.get(url).json()['data']
    title = response['catch_title']
    content = response['content']

    content_list = []
    content_soup = BeautifulSoup(str(content), 'html.parser')
    items = content_soup.find_all(name=['p', 'img', 'h3', 'strong'])

    for i in range(len(items)):
        item = items[i]
        type = v3_const.v3_item_type['text']
        info = ''
        if item.name == 'p':
            info = item.text
        elif item.name == 'img':
            type = v3_const.v3_item_type['image']
            info = item['src']
        elif item.name == 'h3':
            type = v3_const.v3_item_type['h1']
            info = item.text
        elif item.name == 'strong':
            size = len(content_list)
            if size > 0 and content_list[size - 1]['info'] == item.text:
                if content_list[size - 1]['type'] == v3_const.v3_item_type['h1']:
                    info = ''
                elif content_list[size - 1]['type'] == v3_const.v3_item_type['text']:
                    content_list[size - 1]['type'] = v3_const.v3_item_type['h2']
                    info = ''
            else:
                type = v3_const.v3_item_type['h2']
                info = item.text
        if info != '':
            if '"' in info:
                info = info.replace('"', '\'')
            content_list.append({'type': type, 'info': info})

    result = v3_const.v3_get_default_detail_item()
    result['title'] = title
    result['content'] = content_list
    return json.dumps(result, ensure_ascii=False)


def _v3_juzi_detail(category, id):
    url = v3_const.v3_categories['juzi']['detail'] + id + '.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    content_list = []
    content = soup.find('article', attrs={'id': 'juzi_info'})
    content_soup = BeautifulSoup(str(content), 'html.parser')
    items = content_soup.find_all(name=['p', 'img', 'h1'])

    for i in range(len(items)):
        item = items[i]
        type = v3_const.v3_item_type['text']
        info = ''
        if item.name == 'p':
            info = item.text
        elif item.name == 'img':
            type = v3_const.v3_item_type['image']
            info = item['data-original']
        elif item.name == 'h1':
            type = v3_const.v3_item_type['h1']
            info = item.text

        if info != '':
            info = info.replace('"', '\'')
            content_list.append({'type': type, 'info': info})

    result = v3_const.v3_get_default_detail_item()
    result['content'] = content_list
    return json.dumps(result, ensure_ascii=False)

