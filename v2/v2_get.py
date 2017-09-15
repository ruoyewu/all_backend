from urllib.parse import unquote
from urllib.request import urlopen

import datetime
import requests
import json

import time
from bs4 import BeautifulSoup

import const


def v2_get_list(app, category, id):
    if app == 'one':
        result = _get_one_list(category, id)
    elif app == 'ifanr':
        result = _get_ifanr_list(category, id)
    elif app == 'qdaily':
        result = _get_qdaily_list(category, id)
    elif app == '36kr':
        result = _get_36kr_list(category, id)
    elif app == 'sspai':
        result = _get_sspai_list(category, id)
    elif app == 'juejin':
        result = _get_juejin_list(category, id)
    elif app == 'juzi':
        result = _get_juzi_list(category, id)
    elif app == 'yike':
        result = _get_yike_list(category, id)
    elif app == 'zhihu':
        result = _get_zhihu_list(category, id)
    elif app == 'geography':
        result = _get_geography_list(category, id)
    elif app == '500px':
        result = _get_500px_list(category, id)
    elif app == 'tmt':
        result = _get_tmt_list(category, id)
    elif app == 'crazy_read':
        result = _get_read_list(category, id)
    elif app == 'kaiyan':
        result = _get_kaiyan_list(category, id)
    elif app == 'vmovie':
        result = _get_vmovie_list(category, id)
    elif app == 'mark':
        result = _get_mark_list(category, id)
    elif app == 'guokr':
        result = _get_guokr_list(category, id)
    else:
        result = ''
    response = {'content': result, 'app': app, 'category': category}
    return json.dumps(response, ensure_ascii=False)
    pass


def _get_one_list(category, id):
    if category == 'home':
        number = _get_one_index_list()[int(id)]
        url = const.v2_base_categories['one']['home'] + number + '/0'
        content_list = requests.get(url).json()['data']['content_list']
        list = _get_one_content_list(False, content_list)
    else:
        url = const.v2_base_categories['one'][category] + id
        content_list = requests.get(url).json()['data']
        list = _get_one_content_list(True, content_list)
    return list
    pass


def _get_ifanr_list(category, id):
    id = str(int(id) + 1)
    url = const.v2_base_categories['ifanr'][category] + id
    content_list = requests.get(url).json()['data']
    result = _get_ifanr_content_list(content_list)
    return result


def _get_qdaily_list(category, id):
    url = const.v2_base_categories['qdaily'][category] + id
    data = requests.get(url).json()['data']
    next = data['last_key']
    content_list = data['feeds']
    return _get_qdaily_content_list(content_list, next)


def _get_36kr_list(category, id):
    url = const.v2_base_categories['36kr'][category] + id
    content_list = requests.get(url).json()['data']['items']
    result = _get_36kr_content_list(content_list)
    return result
    pass


def _get_sspai_list(category, id):
    offset = int(id) * 10
    url = const.v2_base_categories['sspai'][category] + str(offset)
    content_list = requests.get(url).json()['list']
    result = _get_sspai_content_list(content_list)
    return result


def _get_juejin_list(category, id):
    url = const.v2_base_categories['juejin'][category] + id
    content_list = requests.get(url).json()['d']['entrylist']
    result = _get_juejin_content_list(content_list)
    return result


def _get_juzi_list(category, id):
    id = str(int(id) + 1)
    url = const.v2_base_categories['juzi'][category] + id
    content_list = requests.get(url).json()['data']['list']
    result = _get_juzi_content_list(content_list)
    return result


def _get_yike_list(category, id):
    d = datetime.datetime.now()
    date = d - datetime.timedelta(days=int(id))
    id = str(date)[:10]
    url = const.v2_base_categories['yike'][category] + id
    content_list = requests.get(url).json()['posts']
    result = _get_yike_content_list(content_list)
    return result


def _get_zhihu_list(category, id):
    if id == '0':
        url = const.v2_base_categories['zhihu']['latest']
    else:
        url = const.v2_base_categories['zhihu']['before'] + id
    response = urlopen(url)
    data = json.loads(response.read().decode())
    content_list = data['stories']
    next = data['date']
    result = _get_zhihu_content_list(next, content_list)
    return result


def _get_geography_list(category, id):
    url = const.v2_base_categories['geography']['home'] + id
    data = requests.get(url).json()
    next_url = data['nextUrl']
    nexts = next_url.split('&')
    next = nexts[len(nexts) - 1][12:]
    content_list = data['articles']
    result = _get_geography_content_list(next, content_list)
    return result


def _get_500px_list(category, id):
    url = const.v2_base_categories['500px'][category] + id
    data = requests.get(url).json()
    next_url = data['nextUrl']
    nexts = next_url.split('&')
    next = nexts[len(nexts) - 1][12:]
    content_list = data['articles']
    result = _get_500px_content_list(next, content_list)
    return result


def _get_tmt_list(category, id):
    offset = str(int(id) * 10)
    header = {'app_version': '8.2.0', 'device': 'android'}
    url = const.v2_base_categories['tmt'][category] + offset
    content_list = requests.get(url, headers=header).json()['data']
    result = _get_tmt_content_list(content_list)
    return result


def _get_read_list(category, id):
    id = str(int(id) * 3)
    url = const.v2_base_categories['crazy_read'][category] + id
    header = {"Cookie":
                "pgv_pvi=1609469952; pgv_si=s5351038976; data_bizuin=3551017240; "
                "data_ticket=LVGFpCisY8EJ+ohluISUQcjPMalYtDUO/cbygqDu5DjAfG2Btgro+ezddNSKHBXV; "
                "ua_id=sqNG2X2MCvqtMnN2AAAAAOM8czv32Q0WbZWVILaTRNA=; slave_user=gh_ede794eb7f55; "
                "slave_sid=a2hkeUtHblpPMW56MVJTazhZbURwZXpzSGxzSzAwTFFtNGplVWtjOTAxM0N3QkhpYWFOd09VUzM4Y2RTelFLNzZEU1lKODNGdWJMWXJYdmJqbXFvcHFnX3JTQTYxY2tWNk9UNGt6ME5GVjhJQnlpNmhCQWN3QWlSZkp5WnFSNnM2M0x2ZVlNYlRWMXlwRnVD; bizuin=3557015317; mobileUV=1_15da113936f_e8f0c; referHost=wk.75510010.com; mreferrerHost=; sd_userid=9761501646975335; sd_cookie_crttime=1501646975335; pgv_pvid=369540729; pgv_info=pgvReferrer=https://qt.qq.com/v/hero/h5_player.html&ssid=s6891569936; wxtokenkey=ebbc7e3d7847806780451633a88c10300597ac60e537835d1158af9aaf33190d; wxuin=3149256718; pass_ticket=80mAjbtf9RH5P8Fnq1q/6nM9Moav4v4SK2n+IsZu92B+cGrRzQkgcCRYQ0ek17lm; wap_sid2=CI6w190LElxBNzJlWFNvNHFNMVlVcm9mV3VMUlNPTHRyZmdEMlJoSWVXM2ZFdnV0c21vWFF4SldtYjZFdV82YThBaFR3bmVPcjlHM2RXX3lmYUh2aHhUMEVLSzJrWlVEQUFBfjCM18rMBTgMQJRO "
              }
    data = requests.get(url, headers=header).json()['general_msg_list']
    list = json.loads(data)['list']
    result = _get_read_content_list(list)
    return result


def _get_kaiyan_list(category, id):
    if category == 'home' or category == 'weekly':
        url = const.v2_base_categories['kaiyan'][category]
    else:
        offset = str(int(id) * 10)
        url = const.v2_base_categories['kaiyan'][category] + offset
    data = requests.get(url).json()['itemList']
    result = _get_kaiyan_content_list(data)
    return result


def _get_vmovie_list(category, id):
    if category == 'home':
        if id == '0':
            url = const.v2_base_categories['vmovie']['home']
            data = requests.get(url).json()['data']['today']
            next = data['lastid']
            list = data['list']
        else:
            url = const.v2_base_categories['vmovie']['home_last'] + id
            data = requests.get(url).json()['data']
            next = data['lastid']
            list = data['list']
    else:
        id = str(int(id) + 1)
        url = const.v2_base_categories['vmovie'][category] + id
        next = ''
        list = requests.get(url).json()['data']
    result = _get_vmovie_content_list(next, list)
    return result


def _get_mark_list(category, id):
    start = str(int(id) * 10)
    body = {
        'uid': '580287',
        'muid': 'BLug54qV6Mut0iU9VuPABA==',
        'start': start,
        'count': '10'
    }
    response = requests.post(const.v2_base_categories['mark'][category], data=body)
    list = response.json()['data']
    result = _get_mark_content_list(list)
    return result


def _get_guokr_list(category, id):
    if category == 'home':
        if id == '0':
            url = const.v2_base_categories['guokr']['home_index']
        else:
            url = const.v2_base_categories['guokr']['home'] + id
    else:
        offset = str(int(id) * 10)
        url = const.v2_base_categories['guokr'][category] + offset
    data = requests.get(url).json()['result']
    result = _get_guokr_content_list(category, data)
    return result


def _get_one_index_list():
    response = requests.get(const.v2_base_categories['one']['index'])
    data = response.json()['data']
    return data


def _get_one_content_list(isNext, list):
    contents = []
    for i in range(len(list)):
        item = list[i]
        id = str(item['id'])
        category = str(item['category'])
        item_id = str(item['item_id'])
        title = item['title']
        forward = item['forward']
        image = item['img_url']
        date = item['post_date']
        url = item['share_url']
        try:
            author = item['author']['user_name']
        except:
            author = ''
        pic_author = item['pic_info']
        word_author = item['words_info']
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
        if isNext:
            next = id
        else:
            next = ''
        info = const.get_default_list_item()
        info['id'] = item_id
        info['category'] = category
        info['title'] = title
        info['forward'] = forward
        info['image'] = image
        info['date'] = date
        info['author'] = author
        info['original_url'] = url
        info['pic_author'] = pic_author
        info['word_author'] = word_author
        info['type'] = type
        info['next'] = next
        contents.append(info)
    return contents


def _get_ifanr_content_list(list):
    contents = []
    for i in range(len(list)):
        item = list[i]
        id = str(item['ID'])
        title = item['title']
        author = item['author']
        date = item['pubDate']
        image = item['image']
        forward = item['excerpt']
        type = item['category']
        url = item['link']
        content = item['content']
        info = const.get_default_list_item()
        info['id'] = id
        info['title'] = title
        info['author'] = author
        info['date'] = date
        info['image'] = image
        info['forward'] = forward
        info['type'] = type
        info['original_url'] = url
        info['content'] = _get_ifanr_content_info(content)
        contents.append(info)
    return contents


def _get_qdaily_content_list(list, next):
    contents = []
    for i in range(len(list)):
        item = list[i]
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
        info = const.get_default_list_item()
        info['id'] = id
        info['title'] = title
        info['forward'] = forward
        info['date'] = date
        info['type'] = type
        info['image'] = image
        info['next'] = next
        info['original_url'] = url
        if image != '':
            contents.append(info)
    return contents


def _get_36kr_content_list(list):
    contents = []
    for i in range(len(list)):
        item = list[i]
        id = str(item['id'])
        title = item['title']
        forward = item['summary']
        image = item['cover']
        date = item['published_at']
        type = item['column']['name']
        author = item['user']['name']
        url = 'http://36kr.com/p/' + id + '.html'
        info = const.get_default_list_item()
        info['id'] = id
        info['title'] = title
        info['forward'] = forward
        info['image'] = image
        info['date'] = date
        info['type'] = type
        info['author'] = author
        info['next'] = id
        info['original_url'] = url
        contents.append(info)
    return contents


def _get_sspai_content_list(list):
    contents = []
    for i in range(len(list)):
        item = list[i]
        id = str(item['id'])
        title = item['title']
        t = item['released_at']
        timeArray = time.localtime(t)
        date = time.strftime('%Y-%m-%d %H:%M:%S', timeArray)
        author = item['author']['nickname']
        try:
            type = item['tags'][0]['title']
        except:
            type = '推荐'
        forward = item['promote_intro']
        image = 'https://cdn.sspai.com/' + item['banner']
        url = 'https://sspai.com/post/' + id
        info = const.get_default_list_item()
        info['id'] = id
        info['title'] = title
        info['date'] = date
        info['author'] = author
        info['type'] = type
        info['forward'] = forward
        info['image'] = image
        info['original_url'] = url
        contents.append(info)
    return contents


def _get_juejin_content_list(list):
    contents = []
    for i in range(len(list)):
        item = list[i]
        next = item['createdAt']
        date = next[:10] + ' ' + next[11:19]
        title = item['title']
        author = item['user']['username']
        forward = item['content']
        image = item['screenshot']
        url = item['originalUrl']
        type = item['category']['name']
        info = const.get_default_list_item()
        info['next'] = next
        info['title'] = title
        info['date'] = date
        info['author'] = author
        info['forward'] = forward
        info['image'] = image
        info['original_url'] = url
        info['type'] = type
        contents.append(info)
    return contents


def _get_juzi_content_list(list):
    contents = []
    for i in range(len(list)):
        item = list[i]
        try:
            id = str(item['id'])
        except:
            continue
        title = item['title']
        try:
            image = item['pic']
        except:
            image = item['gif'][0]['thumb']
        try:
            type = item['cat']['name']
        except:
            type = 'gif'
        author = item['author']['name']
        age = item['publish_time']
        url = 'http://m.happyjuzi.com/article/' + id + '.html'
        category = item['type']
        info = const.get_default_list_item()
        info['id'] = id
        info['title'] = title
        info['image'] = image
        info['type'] = type
        info['author'] = author
        info['age'] = age
        info['original_url'] = url
        if category == 0:
            contents.append(info)
    return contents


def _get_yike_content_list(list):
    contents = []
    for i in range(len(list)):
        item = list[i]
        date = item['published_time']
        url = item['url']
        title = item['title']
        forward = item['abstract']
        type = item['column']
        id = url.split('/')[4]
        if type.strip() == '':
            type = '一刻'
        try:
            image = item['thumbs'][0]['medium']['url']
        except:
            image = ''
        try:
            author = item['author']['name']
        except:
            author = '一刻编辑'
        info = const.get_default_list_item()
        info['id'] = id
        info['title'] = title
        info['date'] = title
        info['original_url'] = url
        info['forward'] = forward
        info['date'] = date
        info['type'] = type
        info['image'] = image
        info['author'] = author
        contents.append(info)
    return contents


def _get_zhihu_content_list(next, list):
    contents = []
    for i in range(len(list)):
        item = list[i]
        title = item['title']
        id = str(item['id'])
        image = item['images'][0]
        url = 'http://daily.zhihu.com/story/' + id
        info = const.get_default_list_item()
        info['id'] = id
        info['title'] = title
        info['image'] = image
        info['next'] = next
        info['original_url'] = url
        contents.append(info)
    return contents


def _get_geography_content_list(next, list):
    contents = []
    for i in range(len(list)):
        item = list[i]
        id = str(item['articleId'])
        title = item['title']
        forward = item['snippet']
        image = item['images'][0]['url']
        url = item['webUrl']
        info = const.get_default_list_item()
        info['id'] = id
        info['title'] = title
        info['forward'] = forward
        info['image'] = image
        info['original_url'] = url
        info['next'] = next
        contents.append(info)
    return contents


def _get_500px_content_list(next, list):
    contents = []
    for i in range(len(list)):
        item = list[i]
        id = str(item['articleId'])
        image = item['images'][0]['url']
        info = const.get_default_list_item()
        info['id'] = id
        info['image'] = image
        info['next'] = next
        contents.append(info)
    return contents


def _get_tmt_content_list(list):
    contents = []
    for i in range(len(list)):
        item = list[i]
        try:
            id = str(item['post_guid'])
        except:
            continue
        title = item['title']
        forward = item['summary']
        image = item['thumb_image']['original'][0]['url']
        age = item['human_time_published']
        url = item['short_url']
        author = item['authors'][0]['username']
        info = const.get_default_list_item()
        info['id'] = id
        info['title'] = title
        info['forward'] = forward
        info['image'] = image
        info['age'] = age
        info['original_url'] = url
        info['author'] = author
        contents.append(info)
    return contents


def _get_read_content_list(list):
    contents = []
    for i in range(len(list)):
        item = list[i]['app_msg_ext_info']
        id = str(item['fileid'])
        title = item['title']
        forward = item['digest']
        image = item['cover']
        url = item['content_url']
        info = const.get_default_list_item()
        info['id'] = id
        info['title'] = title
        info['forward'] = forward
        info['image'] = image
        info['original_url'] = url
        contents.append(info)
        multi_list = item['multi_app_msg_item_list']
        for j in range(len(multi_list)):
            multi_item = multi_list[j]
            id = str(multi_item['fileid'])
            title = multi_item['title']
            forward = multi_item['digest']
            image = multi_item['cover']
            url = multi_item['content_url']
            info = const.get_default_list_item()
            info['id'] = id
            info['title'] = title
            info['forward'] = forward
            info['image'] = image
            info['original_url'] = url
            contents.append(info)
    return contents


def _get_kaiyan_content_list(list):
    contents = []
    for i in range(len(list)):
        item = list[i]
        print(item['type'])
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
        video = data['playUrl']
        url = data['webUrl']['raw']
        type = data['category']
        try:
            author = data['author']['name']
        except:
            author = ''
        info = const.get_default_list_item()
        info['id'] = id
        info['title'] = title
        info['forward'] = forward
        info['image'] = image
        info['video'] = video
        info['original_url'] = url
        info['author'] = author
        info['type'] = type
        contents.append(info)
    return contents


def _get_vmovie_content_list(next, list):
    contents = []
    for i in range(len(list)):
        item = list[i]
        id = str(item['postid'])
        title = item['title']
        image = item['image']
        type = item['cate'][0]['catename']
        content = requests.get(const.v2_base_categories['vmovie']['detail'] + id).json()['data']
        forward = content['intro']
        video = content['content']['video'][0]['qiniu_url']
        url = 'http://www.vmovier.com/' + id
        info = const.get_default_list_item()
        info['id'] = id
        info['title'] = title
        info['image'] = image
        info['type'] = type
        info['forward'] = forward
        info['video'] = video
        info['original_url'] = url
        info['next'] = next
        contents.append(info)
    return contents


def _get_mark_content_list(list):
    contents = []
    for i in range(len(list)):
        item = list[i]
        id = str(item['id'])
        title = item['name']
        image = item['img_url']
        timeMillis = item['publish_time']
        url = 'http://mark.intlime.com/singles/share/id/' + id
        info = const.get_default_list_item()
        info['id'] = id
        info['title'] = title
        info['time_millis'] = timeMillis
        info['image'] = image
        info['original_url'] = url
        contents.append(info)
    return contents


def _get_guokr_content_list(category, list):
    contents = []
    for i in range(len(list)):
        item = list[i]
        type = item['source_name']
        id = str(item['id'])
        title = item['title']
        image = item['headline_img']
        author = item['author']
        forward = item['summary']
        time_millis = item['date_created']
        url = item['link_v2']
        if category == 'home':
            next = id
        else:
            next = ''
        info = const.get_default_list_item()
        info['id'] = id
        info['type'] = type
        info['title'] = title
        info['iamge'] = image
        info['author'] = author
        info['forward'] = forward
        info['time_millis'] = time_millis
        info['original_url'] = url
        info['next'] = next
        contents.append(info)
    return contents


def _get_ifanr_content_info(content):
    list = []
    soup = BeautifulSoup(str(content), 'html.parser')
    items = soup.find_all(name=['p', 'img', 'h3'])
    for i in range(len(items)):
        item = items[i]
        txt = ''
        img = ''
        h = ''
        if item.name == 'p':
            txt = item.text.strip()
        elif item.name == 'h3':
            h = item.text.strip()
        elif item.name == 'img':
            img = item['src']
        if txt != '' or img != '' or h != '':
            info = const.get_default_content_item()
            info['txt'] = txt
            info['img'] = img
            info['h'] = h
            list.append(info)
    return list


if __name__ == '__main__':
    pass
