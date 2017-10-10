import datetime
import requests
import json

import time
from bs4 import BeautifulSoup
from v3 import v3_const


def v3_get_list(name, category, page):
    if name == 'one':
        return _v3_get_one_list(category, page)
    elif name == 'ifanr':
        return _v3_get_ifanr_list(category, page)
    elif name == 'sspai':
        return _v3_get_sspai_list(category, page)
    elif name == 'qdaily':
        return _v3_get_qdaily_list(category, page)
    elif name == '36kr':
        return _v3_get_36kr_list(category, page)
    elif name == 'juzi':
        return _v3_get_juzi_list(category, page)


def _v3_get_one_list(category, page):
    if category == 'home':
        url = v3_const.v3_categories['one']['home'] + page + '/0'
        content_list = requests.get(url).json()['data']['content_list']
    else:
        url = v3_const.v3_categories['one'][category] + page
        content_list = requests.get(url).json()['data']

    list = []
    next = ''
    for i in range(len(content_list)):
        item = content_list[i]
        id = item['item_id']
        cat = item['category']
        title = item['title']
        forward = item['forward']
        image = item['img_url']
        date = item['post_date']
        # 如果 author{} 项不存在，则会导致抛出错误
        try:
            author = item['author']['user_name']
        except:
            author = ''
        try:
            type = item['tag_list'][0]['title']
        except:
            if category == '1':
                type = '阅读'
            elif category == '2':
                type = '连载'
            elif category == '3':
                type = '问答'
            elif category == '4':
                type = '音乐'
            elif category == '5':
                type = '影视'
            else:
                type = '一个'
        url = item['share_url']
        pic_info = item['pic_info']
        words_info = item['words_info']
        next = item['id']
        info = v3_const.v3_get_default_list_item()
        info['id'] = id
        info['category_id'] = cat
        info['title'] = title
        info['forward'] = forward
        info['image'] = image
        info['date'] = date
        info['author'] = author
        info['original_url'] = url
        info['type'] = type
        info['other_info'] = pic_info + '|' + words_info
        list.append(info)

    if category == 'home':
        old_date = list[0]['date'][:10].split('-')
        now = datetime.date(int(old_date[0]), int(old_date[1]), int(old_date[2])) - datetime.timedelta(days=1)
        next = str(now)

    result = {
        "name": "one",
        "category": category,
        "next": next,
        "list": list
    }
    return json.dumps(result, ensure_ascii=False)


def _v3_get_ifanr_list(category, page):
    if page == "0":
        page = "1"
    url = v3_const.v3_categories['ifanr'][category] + page
    content_list = requests.get(url).json()['data']

    list = []
    next = str(int(page) + 1)
    for i in range(len(content_list)):
        item = content_list[i]
        id = str(item['ID'])
        title = item['title']
        author = item['author']
        date = item['pubDate']
        image = item['image']
        forward = item['excerpt']
        url = item['link']
        type = item['category']
        content = item['content']
        info = v3_const.v3_get_default_list_item()
        info['id'] = id
        info['title'] = title
        info['author'] = author
        info['date'] = date
        info['image'] = image
        info['original_url'] = url
        info['forward'] = forward
        info['type'] = type
        info['content'] = __v3_get_ifanr_detail(content)
        list.append(info)

    result = {
        'name': 'ifanr',
        'category': category,
        'next': next,
        'list': list
    }
    return json.dumps(result, ensure_ascii=False)


def _v3_get_sspai_list(category, page):
    offset = str(int(page) * 10)
    next = int(page) + 1
    url = v3_const.v3_categories['sspai'][category] + offset
    content_list = requests.get(url).json()['list']

    list = []
    for i in range(len(content_list)):
        item = content_list[i]
        id = str(item['id'])
        title = item['title']
        forward = item['promote_intro']
        image = 'https://cdn.sspai.com/' + item['banner']
        url = 'https://sspai.com/post/' + id
        author = item['author']['nickname']
        t = item['released_at']
        timeArray = time.localtime(t)
        date = time.strftime('%Y-%m-%d %H:%M:%S', timeArray)
        try:
            type = item['tags'][0]['title']
        except:
            type = '推荐'
        info = v3_const.v3_get_default_list_item()
        info['id'] = id
        info['title'] = title
        info['author'] = author
        info['date'] = date
        info['image'] = image
        info['forward'] = forward
        info['original_url'] = url
        info['type'] = type
        list.append(info)

    result = {
        'name': 'sspai',
        'category': category,
        'next': next,
        'list': list
    }
    return json.dumps(result, ensure_ascii=False)


def _v3_get_qdaily_list(category, page):
    url = v3_const.v3_categories['qdaily'][category] + page
    data = requests.get(url).json()['data']
    next = data['last_key']
    content_list = data['feeds']

    list = []
    for i in range(len(content_list)):
        item = content_list[i]
        try:
            image = item['image']
        except:
            image = ''
        post = item['post']
        id = str(post['id'])
        title = post['title']
        forward = post['description']
        date = post['publish_time'][:19]
        type = post['category']['title']
        url = 'http://m.qdaily.com/mobile/articles/' + id + '.html'
        info = v3_const.v3_get_default_list_item()
        info['id'] = id
        info['image'] = image
        info['title'] = title
        info['forward'] = forward
        info['date'] = date
        info['type'] = type
        info['original_url'] = url
        if image != '':
            list.append(info)

    result = {
        'name': 'qdaily',
        'category': category,
        'next': next,
        'list': list
    }
    return json.dumps(result, ensure_ascii=False)


def _v3_get_36kr_list(category, page):
    url = v3_const.v3_categories['36kr'][category] + page
    content_list = requests.get(url).json()['data']['items']

    list = []
    for i in range(len(content_list)):
        item = content_list[i]
        id = str(item['id'])
        title = item['title']
        forward = item['summary']
        image = item['cover']
        date = item['published_at']
        type = item['column']['name']
        author = item['user']['name']
        url = 'http://36kr.com/p/' + id + '.html'
        info = v3_const.v3_get_default_list_item()
        info['id'] = id
        info['title'] = title
        info['forward'] = forward
        info['image'] = image
        info['date'] = date
        info['type'] = type
        info['author'] = author
        info['original_url'] = url
        list.append(info)

    next = list[len(list) - 1]['id']
    result = {
        'name': '36kr',
        'category': category,
        'list': list,
        'next': next
    }
    return json.dumps(result, ensure_ascii=False)


def _v3_get_juzi_list(category, page):
    if page == '0':
        page = '1'
    url = v3_const.v3_categories['juzi'][category] + page
    content_list = requests.get(url).json()['data']['list']

    list = []
    for i in range(len(content_list)):
        item = content_list[i]
        id = str(item['id'])
        title = item['title']
        image = item['pic']
        age = item['publish_time']
        author = item['author']['name']
        type = item['cat']['name']
        url = 'http://m.happyjuzi.com/article/' + id + '.html'
        info = v3_const.v3_get_default_list_item()
        info['id'] = id
        info['title'] = title
        info['image'] = image
        info['age'] = age
        info['author'] = author
        info['type'] = type
        info['original_url'] = url
        list.append(info)

    next = str(int(page) + 1)
    result = {
        'name': 'juzi',
        'category': category,
        'list': list,
        'next': next
    }
    return json.dumps(result, ensure_ascii=False)


def __v3_get_ifanr_detail(content):
    list = []
    soup = BeautifulSoup(str(content), 'html.parser')
    items = soup.find_all(name=['p', 'img', 'h3', 'blockquote'])

    for i in range(len(items)):
        item = items[i]
        type = v3_const.v3_item_type['text']
        info = ''
        if item.name == 'p':
            info = item.text
            try:
                if item['style'] == 'text-align: center;':
                    type = v3_const.v3_item_type['text_cen']
            except:
                pass
            if len(list) > 0 and info in list[len(list) - 1]['info']:
                info = ''
        elif item.name == 'img':
            info = item['src']
            type = v3_const.v3_item_type['image']
        elif item.name == 'h3':
            info = item.text
            type = v3_const.v3_item_type['h1']
        elif item.name == 'blockquote':
            info = item.text
            type = v3_const.v3_item_type['quote']

        if info.strip() != '':
            list.append({'type': type, 'info': info})

    return list


