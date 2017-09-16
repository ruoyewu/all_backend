from urllib.request import urlopen

from bs4 import BeautifulSoup
import requests
import json

from v3 import v3_const


def v3_detail(name, category, id):
    if name == 'one':
        return _v3_one_detail(category, id)
    pass


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
        info = {"type": "7", 'info': i.text.strip()}
        content_list.append(info)
    except:
        pass

    if len(contents) > 1:
        content = contents[1]
        asker = soup.find('div', attrs={'class': 'text-askers'}).text.strip()
        info = {'type': '7', 'info': asker}
        content_list.append(info)
        question = contents[0].text
        info = {'type': '1', 'info': question}
        content_list.append(info)
        answer = soup.find('div', attrs={'class': 'text-answers'}).text.strip()
        info = {'type': '7', 'info': answer}
        content_list.append(info)
    else:
        content = contents[0]

    content_soup = BeautifulSoup(str(content), 'html.parser')
    items = content_soup.find_all(name=['p', 'img'])[1:]
    for i in range(len(items)):
        item = items[i]
        if item.name == 'p':
            info = item.text
            type = '1'
            try:
                if item['style'] == 'text-align: center;':
                    type = '7'
            except:
                type = '1'
        elif item.name == 'img':
            type = '2'
            info = item['src']
        if info == 'http://image.wufazhuce.com/music_copyright_2_2.png' or info == 'http://image.wufazhuce.com/music_copyright_1.png':
            info = ''
        if info != '':
            content_list.append({'type': type, 'info': info})
    for i in range(len(editors)):
        editor = editors[i].text
        info = {'type': '7', 'info': editor}
        content_list.append(info)
    result = v3_const.v3_get_default_detail_item()
    result['title'] = title
    result['subtitle'] = subtitle
    result['author'] = author
    result['content'] = content_list
    return json.dumps(result, ensure_ascii=False)
