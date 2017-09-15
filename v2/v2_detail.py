from urllib.request import urlopen

from bs4 import BeautifulSoup
import requests
import json

import const


def v2_get_detail(app, category, id):
    if app == 'qdaily':
        result = get_qdaily_detail(category, id)
    elif app == 'one':
        result = get_one_detail(category, id)
    elif app == '36kr':
        result = get_36kr_detail(category, id)
    elif app == 'sspai':
        result = get_sspai_detail(category, id)
    elif app == 'juzi':
        result = get_juzi_detail(category, id)
    elif app == 'yike':
        result = get_yike_detail(category, id)
    elif app == 'zhihu':
        result = get_zhihu_detail(category, id)
    elif app == 'tmt':
        result = get_tmt_detail(category, id)
    elif app == 'mark':
        result = get_mark_detail(category, id)
    else:
        return 'error'
    return json.dumps(result, ensure_ascii=False)
    pass


def get_qdaily_detail(category, id):
    url = const.v2_base_categories['qdaily']['detail'] + id + '.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    head = soup.find('div', attrs={'class': 'article-detail-hd'})
    head_soup = BeautifulSoup(str(head), 'html.parser')
    title = head_soup.find('h1', attrs={'class': 'title'}).text
    author = head_soup.find('div', attrs={'class': 'author'}).text
    date = head_soup.find('span', attrs={'class': 'date'}).text
    content = soup.find('div', attrs={'class': 'article-detail-bd'})
    content_soup = BeautifulSoup(str(content), 'html.parser')
    items = content_soup.find_all(name=['p', 'img', 'h3', 'h2', 'li'])

    content_list = []
    for i in range(len(items)):
        item = items[i]
        h = ''
        txt = ''
        img = ''
        li = ''
        if item.name == 'h3' or item.name == 'h2':
            h = item.text
        elif item.name == 'li':
            li = item.text.strip()
        elif item.name == 'p':
            txt = item.text
        elif item.name == 'img':
            img = item['data-src']
        if txt.strip()[:4] == 'p.p1':
            txt = ''
        if h != '' or txt != '' or img != '' or li != '':
            info = const.get_default_content_item()
            info['h'] = h
            info['txt'] = txt
            info['img'] = img
            info['li'] = li
            content_list.append(info)

    result = const.get_default_detail_item()
    result['title'] = title
    result['author'] = author
    result['date'] = date
    result['content'] = content_list
    return result


def get_one_detail(category, id):
    if category == '1':
        url = const.v2_base_categories['one']['detail_article'] + id
    elif category == '2':
        url = const.v2_base_categories['one']['detail_serial'] + id
    elif category == '3':
        url = const.v2_base_categories['one']['detail_question'] + id
    elif category == '4':
        url = const.v2_base_categories['one']['detail_music'] + id
    elif category == '5':
        url = const.v2_base_categories['one']['detail_movie'] + id
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
        info = const.get_default_content_item()
        info['txt_cen'] = i.text.strip()
        content_list.append(info)
    except:
        pass

    if len(contents) > 1:
        content = contents[1]
        asker = soup.find('div', attrs={'class': 'text-askers'}).text.strip()
        info = const.get_default_content_item()
        info['txt_cen'] = asker
        content_list.append(info)
        question = contents[0].text
        info = const.get_default_content_item()
        info['txt'] = question
        content_list.append(info)
        answer = soup.find('div', attrs={'class': 'text-answers'}).text.strip()
        info = const.get_default_content_item()
        info['txt_cen'] = answer
        content_list.append(info)
    else:
        content = contents[0]

    content_soup = BeautifulSoup(str(content), 'html.parser')
    items = content_soup.find_all(name=['p', 'img'])[1:]
    for i in range(len(items)):
        item = items[i]
        txt = ''
        img = ''
        txt_cen = ''
        if item.name == 'p':
            try:
                if item['style'] == 'text-align: center;':
                    txt_cen = item.text
            except:
                txt = item.text.strip()
        elif item.name == 'img':
            img = item['src']
        if img == 'http://image.wufazhuce.com/music_copyright_2_2.png' or img == 'http://image.wufazhuce.com/music_copyright_1.png':
            continue
        if txt != '' or img != '' or txt_cen != '':
            info = const.get_default_content_item()
            info['txt'] = txt
            info['img'] = img
            info['txt_cen'] = txt_cen
            content_list.append(info)
    for i in range(len(editors)):
        editor = editors[i].text
        info = const.get_default_content_item()
        info['txt_cen'] = editor
        content_list.append(info)
    result = const.get_default_detail_item()
    result['title'] = title
    result['subtitle'] = subtitle
    result['author'] = author
    result['content'] = content_list
    return result
    pass


def get_36kr_detail(category, id):
    url = const.v2_base_categories['36kr']['detail'] + id
    response = requests.get(url).json()['data']
    title = response['catch_title']
    content = response['content']
    content_list = []
    content_soup = BeautifulSoup(str(content), 'html.parser')
    items = content_soup.find_all(name=['p', 'img', 'h3'])
    for i in range(len(items)):
        item = items[i]
        h = ''
        txt = ''
        img = ''
        if item.name == 'h3':
            h = item.text
        elif item.name == 'p':
            txt = item.text
        elif item.name == 'img':
            img = item['src']
        if h != '' or txt != '' or img != '':
            info = const.get_default_content_item()
            info['h'] = h
            info['txt'] = txt
            info['img'] = img
            content_list.append(info)

    result = const.get_default_detail_item()
    result['title'] = title
    result['content'] = content_list
    return result
    pass


def get_sspai_detail(category, id):
    url = const.v2_base_categories['sspai']['detail'] + id
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
    items = content_soup.find_all(name=['p', 'img', 'h2', 'li', 'h4'])
    for i in range(len(items)):
        item = items[i]
        txt = ''
        img = ''
        h = ''
        li = ''
        if item.name == 'h2':
            h = item.text.strip()
        elif item.name == 'p' or item.name == 'h4':
            txt = item.text.strip()
        elif item.name == 'img':
            img = item['src']
        elif item.name == 'li':
            li = item.text.strip()
        if h != '' or txt != '' or img != '' or li != '':
            info = const.get_default_content_item()
            info['txt'] = txt
            info['h'] = h
            info['img'] = img
            info['li'] = li
            content_list.append(info)
    result = const.get_default_detail_item()
    result['title'] = title
    result['author'] = author
    result['date'] = date
    result['content'] = content_list
    return result
    pass


def get_juzi_detail(category, id):
    url = const.v2_base_categories['juzi']['detail'] + id + ".html"
    response = requests.get(url)
    print(url)
    print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')

    content_list = []
    content = soup.find('article', attrs={'id': 'juzi_info'})
    content_soup = BeautifulSoup(str(content), 'html.parser')
    items = content_soup.find_all(name=['p', 'img', 'h1'])
    for i in range(len(items)):
        item = items[i]
        txt = ''
        img = ''
        h = ''
        if item.name == 'p':
            txt = item.text.strip()
        elif item.name == 'img':
            img = item['data-original']
        elif item.name == 'h1':
            h = item.text
        if txt != '' or img != '' or h != '':
            info = const.get_default_content_item()
            info['h'] = h
            info['txt'] = txt
            info['img'] = img
            content_list.append(info)
    result = const.get_default_detail_item()
    result['content'] = content_list
    return result
    pass


def get_yike_detail(category, id):
    url = const.v2_base_categories['yike']['detail'] + id
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    content_list = []
    content = soup.find('div', attrs={'id': 'content'})
    content_soup = BeautifulSoup(str(content), 'html.parser')
    items = content_soup.find_all(name=['p', 'img'])
    for i in range(len(items)):
        item = items[i]
        txt = ''
        img = ''
        txt_cen = ''
        if item.name == 'p':
            try:
                if item['class'] == ['img_desc']:
                    txt_cen = item.text
                else:
                    txt = item.text
            except:
                txt = item.text
        elif item.name == 'img':
            img = item['src']
        if txt != '' or img != '' or txt_cen != '':
            info = const.get_default_content_item()
            info['txt'] = txt
            info['img'] = img
            info['txt_cen'] = txt_cen
            content_list.append(info)

    result = const.get_default_detail_item()
    result['content'] = content_list
    return result


def get_zhihu_detail(category, id):
    url = const.v2_base_categories['zhihu']['detail'] + id
    response = urlopen(url)
    data = json.loads(response.read().decode())
    content = data['body']
    soup = BeautifulSoup(content, 'html.parser')

    content_list = []
    titles = soup.find_all('h2', attrs={'class': 'question-title'})
    for i in range(len(titles)):
        title = titles[i].text
        print(title)
        if title == '':
            continue
        info = const.get_default_content_item()
        info['h'] = title

    contents = soup.find_all('div', attrs={'class': 'content'})
    for i in range(len(contents)):
        content = contents[i]
        content_soup = BeautifulSoup(str(content), 'html.parser')
        items = content_soup.find_all(name=['p', 'img', 'h2', 'blockquote'])
        for i in range(len(items)):
            item = items[i]
            txt = ''
            img = ''
            h = ''
            if item.name == 'p' or item.name == 'blockquote':
                txt = item.text
            elif item.name == 'h2':
                h = item.text
            elif item.name == 'img':
                img = item['src']
            if txt != '' or img != '' or h != '':
                info = const.get_default_content_item()
                info['h'] = h
                info['txt'] = txt
                info['img'] = img
                content_list.append(info)

    result = const.get_default_detail_item()
    result['content'] = content_list
    return result


def get_tmt_detail(category, id):
    url = const.v2_base_categories['tmt']['detail'] + id + '.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('div', attrs={'class': 'inner'})
    content_soup = BeautifulSoup(str(content), 'html.parser')

    content_list = []
    items = content_soup.find_all(name=['p', 'img', 'h2'])
    for i in range(len(items)):
        item = items[i]
        txt = ''
        img = ''
        h = ''
        print(item)
        if item.name == 'p':
            txt = item.text.strip()
            print(len(content_list))
            if len(content_list) > 0:
                if txt == content_list[len(content_list) - 1]['txt']:
                    txt = ''
        elif item.name == 'h2':
            h = item.text
            if len(content_list) > 0:
                if h == content_list[len(content_list) - 1]['txt']:
                    content_list.pop(len(content_list) - 1)
        elif item.name == 'img':
            img = item['src']
        if txt != '' or h != '' or img != '':
            info = const.get_default_content_item()
            info['h'] = h
            info['img'] = img
            info['txt'] = txt
            content_list.append(info)
    result = const.get_default_detail_item()
    result['content'] = content_list
    return result


def get_mark_detail(category, id):
    body = {
        'uid': '580287',
        'muid': 'BLug54qV6Mut0iU9VuPABA==',
        'id': str(id)
    }
    response = requests.post(const.v2_base_categories['mark']['detail'], data=body)
    content = response.json()['data']['content']
    content_soup = BeautifulSoup(content, 'html.parser')

    content_list = []
    content = content_soup.find('div', attrs={'class': 'content'})
    content_soup = BeautifulSoup(str(content), 'html.parser')
    contents = content_soup.find_all(name=['p', 'img'])
    for i in range(len(contents)):
        item = contents[i]
        img = ''
        txt = ''
        txt_cen = ''
        print(item)
        if item.name == 'img':
            try:
                img = item['data-ke-src']
            except:
                print(item)
        elif item.name == 'p':
            try:
                if item['style'] == 'line-height: 25.6px; text-align: center;':
                    txt_cen = item.text
                else:
                    txt = item.text.strip()
            except:
                txt = item.text.strip()
        if img != '' or txt != '' or txt_cen != '':
            info = const.get_default_content_item()
            info['img'] = img
            info['txt'] = txt
            info['txt_cen'] = txt_cen
            content_list.append(info)
    result = const.get_default_detail_item()
    result['content'] = content_list
    return result


if __name__ == '__main__':
    v2_get_detail('juzi', 'home', '144124')

