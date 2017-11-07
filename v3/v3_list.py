import datetime
import requests
import json

import time
from bs4 import BeautifulSoup
from v3 import v3_const


def v3_get_list(name, category, page):
    if name == 'one':
        if category == 'home':
            url = v3_const.v3_categories[name][category] + page + '/0'
        else:
            url = v3_const.v3_categories[name][category] + page
        content = requests.get(url).json()
        return _v3_get_one_list(category, page, content)
    elif name == 'ifanr':
        if page == '0':
            page = '1'
        url = v3_const.v3_categories[name][category] + page
        content = requests.get(url).json()
        return _v3_get_ifanr_list(category, page, content)
    elif name == 'sspai':
        url = v3_const.v3_categories['sspai'][category] + page
        content = requests.get(url).json()
        return _v3_get_sspai_list(category, page, content)
    elif name == 'qdaily':
        url = v3_const.v3_categories['qdaily'][category] + page
        content = requests.get(url).json()
        return _v3_get_qdaily_list(category, page, content)
    elif name == '36kr':
        url = v3_const.v3_categories['36kr'][category] + page
        content = requests.get(url).json()
        return _v3_get_36kr_list(category, page, content)
    elif name == 'juzi':
        if page == '0':
            page = '1'
        url = v3_const.v3_categories['juzi'][category] + page
        content = requests.get(url).json()
        return _v3_get_juzi_list(category, page, content)
    elif name == 'geography':
        url = v3_const.v3_categories['geography']['home'] + page
        content = requests.get(url).json()
        return _v3_get_geography_list(category, page, content)
    elif name == '500px':
        url = v3_const.v3_categories['500px'][category] + page
        content = requests.get(url).json()
        return _v3_get_500px_list(category, page, content)
    elif name == 'guokr':
        if category == 'home':
            if page == '0':
                url = v3_const.v3_categories['guokr']['home_index']
            else:
                url = v3_const.v3_categories['guokr']['home'] + page
        else:
            url = v3_const.v3_categories['guokr'][category] + page
        content = requests.get(url).json()
        return _v3_get_guokr_list(category, page, content)
    elif name == 'kaiyan':
        if category == 'home' or category == 'weekly':
            url = v3_const.v3_categories['kaiyan'][category]
        else:
            url = v3_const.v3_categories['kaiyan'][category] + page
        content = requests.get(url).json()
        return _v3_get_kaiyan_list(category, page, content)
    elif name == 'vmovie':
        if category == 'home':
            url = v3_const.v3_categories[name][category] + page
        else:
            if page == '0':
                page = '1'
            url = v3_const.v3_categories[name][category] + page
        content = requests.get(url).json()
        return _v3_get_vmovie_list(category, page, content)
    elif name == 'dgtle':
        url = v3_const.v3_categories[name][category] + page
        content = requests.get(url).text
        return _v3_get_dgtle_list(category, page, content)


def v3_get_list2(name, category, page, content):
    if name == 'one':
        return _v3_get_one_list(category, page, content)
    elif name == 'ifanr':
        return _v3_get_ifanr_list(category, page, content)
    elif name == 'sspai':
        return _v3_get_sspai_list(category, page, content)
    elif name == 'qdaily':
        return _v3_get_qdaily_list(category, page, content)
    elif name == '36kr':
        return _v3_get_36kr_list(category, page, content)
    elif name == 'juzi':
        return _v3_get_juzi_list(category, page, content)
    elif name == 'geography':
        return _v3_get_geography_list(category, page, content)
    elif name == '500px':
        return _v3_get_500px_list(category, page, content)
    elif name == 'guokr':
        return _v3_get_guokr_list(category, page, content)
    elif name == 'kaiyan':
        return _v3_get_kaiyan_list(category, page, content)
    elif name == 'vmovie':
        return _v3_get_vmovie_list(category, page, content)
    elif name == 'dgtle':
        return _v3_get_dgtle_list(category, page, content)


def _v3_get_one_list(category, page, content):
    if category == 'home':
        content_list = content['data']['content_list']
    else:
        content_list = content['data']

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
    return result


def _v3_get_ifanr_list(category, page, content):
    content_list = content['data']

    list = []
    if page == '0':
        page = '1'
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
    return result


def _v3_get_sspai_list(category, page, content):
    next = str(int(page) + 10)
    content_list = content['list']

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
    return result


def _v3_get_qdaily_list(category, page, content):
    data = content['data']
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
    return result


def _v3_get_36kr_list(category, page, content):
    content_list = content['data']['items']

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
    return result


def _v3_get_juzi_list(category, page, content):
    content_list = content['data']['list']

    list = []
    for i in range(len(content_list)):
        item = content_list[i]
        try:
            id = str(item['id'])
        except:
            continue
        title = item['title']
        try:
            image = item['pic']
        except:
            image = item['gif'][0]['thumb']
        age = item['publish_time']
        author = item['author']['name']
        try:
            type = item['cat']['name']
        except:
            type = 'gif'
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

    if page == '0':
        page = '1'
    next = str(int(page) + 1)
    result = {
        'name': 'juzi',
        'category': category,
        'list': list,
        'next': next
    }
    return result


def _v3_get_guokr_list(category, page, content):
    content_list = content['result']

    list = []
    for i in range(len(content_list)):
        item = content_list[i]
        id = str(item['id'])
        type = item['source_name']
        title = item['title']
        image = item['headline_img']
        author = item['author']
        forward = item['summary']
        url = item['link_v2']
        time_millis = str(item['date_picked']).split('.')[0] + '000'
        info = v3_const.v3_get_default_list_item()
        info['id'] = id
        info['type'] = type
        info['title'] = title
        info['image'] = image
        info['author'] = author
        info['forward'] = forward
        info['original_url'] = url
        info['time_millis'] = time_millis
        list.append(info)

    if category != 'home':
        next = str(int(page) + 10)
    else:
        next = list[-1]['id']
    result = {
        'name': 'guokr',
        'category': category,
        'list': list,
        'next': next
    }
    return result


def _v3_get_kaiyan_list(category, page, content):
    content_list = content['itemList']

    list = []
    for i in range(len(content_list)):
        item = content_list[i]
        if item['type'] == 'video':
            data = item['data']
        elif item['type'] == 'followCard':
            data = item['data']['content']['data']
        else:
            continue

        id = str(data['id'])
        title = data['title']
        forward = data['description']
        image = data['cover']['detail']
        type = data['category']
        video = data['playUrl']
        try:
            url = data['webUrl']['raw']
        except:
            url = ''
        try:
            author = data['author']['name']
        except:
            author = ''
        info = v3_const.v3_get_default_list_item()
        info['id'] = id
        info['title'] = title
        info['forward'] = forward
        info['image'] = image
        info['type'] = type
        info['video'] = video
        info['original_url'] = url
        info['author'] = author
        info['open_type'] = v3_const.v3_open_type['video']
        list.append(info)

    next = str(int(page) + 10)
    result = {
        'name': 'kaiyan',
        'category': category,
        'list': list,
        'next': next
    }
    return result


def _v3_get_geography_list(category, page, content):
    next_url = content['nextUrl']
    nexts = next_url.split('&')
    next = nexts[len(nexts) - 1][12:]
    content_list = content['articles']

    list = []
    for i in range(len(content_list)):
        item = content_list[i]
        id = str(item['articleId'])
        title = item['title']
        forward = item['snippet']
        image = item['images'][0]['url']
        url = item['webUrl']
        info = v3_const.v3_get_default_list_item()
        info['id'] = id
        info['title'] = title
        info['forward'] = forward
        info['image'] = image
        info['original_url'] = url
        info['open_type'] = v3_const.v3_open_type['image']
        info['img_list'] = [image]
        list.append(info)

    result = {
        'name': 'geography',
        'category': category,
        'list': list,
        'next': next
    }
    return result


def _v3_get_500px_list(category, page, content):
    next_url = content['nextUrl']
    nexts = next_url.split('&')
    next = nexts[len(nexts) - 1][12:]
    content_list = content['articles']

    list = []
    for i in range(len(content_list)):
        item = content_list[i]
        id = str(item['articleId'])
        image = item['images'][0]['url']
        url = item['webUrl']
        info = v3_const.v3_get_default_list_item()
        info['id'] = id
        info['image'] = image
        info['original_url'] = url
        info['open_type'] = v3_const.v3_open_type['image']
        info['img_list'] = [image]
        list.append(info)

    result = {
        'name': '500px',
        'category': category,
        'list': list,
        'next': next
    }
    return result


def _v3_get_vmovie_list(category, page, content):
    if category == 'home':
        data = content['data']
        next = data['lastid']
        content_list = data['list']
    else:
        if page == '0':
            page = '1'
        next = str(int(page) + 1)
        content_list = content['data']

    list = []
    for i in range(len(content_list)):
        item = content_list[i]
        id = str(item['postid'])
        title = item['title']
        image = item['image']
        type = item['cates'][0]['catename']
        detail = requests.get(v3_const.v3_categories['vmovie']['detail'] + id).json()['data']
        forward = detail['intro']
        video = detail['content']['video'][0]['qiniu_url']
        if video == '':
            video = detail['content']['video'][0]['progressive'][0]['qiniu_url']
        url = 'http://www.vmovier.com/' + id
        time_millis = detail['publish_time'] + '000'
        info = v3_const.v3_get_default_list_item()
        info['id'] = id
        info['title'] = title
        info['image'] = image
        info['forward'] = forward
        info['type'] = type
        info['video'] = video
        info['original_url'] = url
        info['time_millis'] = time_millis
        info['open_type'] = v3_const.v3_open_type['video']
        list.append(info)

    result = {
        'name': 'vmovie',
        'category': category,
        'list': list,
        'next': next
    }
    return result


def _v3_get_dgtle_list(category, page, content):
    content = content.replace('<![CDATA[', '')
    content_soup = BeautifulSoup(content, 'html.parser')
    content_list = content_soup.find_all(name=['dl'])

    if page == '0':
        page = '1'
    next = str(int(page) + 1)

    list = []
    for i in range(len(content_list)):
        item = content_list[i]
        item_soup = BeautifulSoup(str(item), 'html.parser')
        title_item = item_soup.find('dt', attrs={'class': ['zjj_title']})
        title = title_item.text
        url = title_item.a['href']
        id = url.split('-')[1]
        forward = item_soup.find('dd', attrs={'class': ['cr_summary']}).text
        age = item_soup.find('div', attrs={'class': ['article_date']}).text
        author = item_soup.find('div', attrs={'class': ['cr_author']}).text
        type = item_soup.find('div', attrs={'class': ['portallist_cat']}).text
        try:
            image = item.dd.a['style'].split('\'')[1]
        except:
            image = ''
        info = v3_const.v3_get_default_list_item()
        info['id'] = id
        info['title'] = title
        info['image'] = image
        info['original_url'] = url
        info['forward'] = forward
        info['age'] = age
        info['author'] = author
        info['type'] = type
        list.append(info)

    result = {
        'name': 'dgtle',
        'category': category,
        'next': next,
        'list': list
    }
    return result


def __v3_get_ifanr_detail(content):
    list = []
    soup = BeautifulSoup(str(content), 'html.parser')
    items = soup.find_all(name=['p', 'img', 'h3', 'blockquote', 'li', 'iframe'])

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
        elif item.name == 'li':
            type = v3_const.v3_item_type['li']
            info = item.text
        elif item.name == 'iframe':
            try:
                info = item['src']
            except:
                info = ''
            type = v3_const.v3_item_type['video']

        if info.strip() != '':
            list.append({'type': type, 'info': info.strip()})

    return list


