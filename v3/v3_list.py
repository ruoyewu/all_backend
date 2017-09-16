import datetime
import requests
import json

import time
from bs4 import BeautifulSoup
from v3 import v3_const


def v3_get_list(name, category, page):
    if name == 'one':
        return _v3_get_one_list(category, page)


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

