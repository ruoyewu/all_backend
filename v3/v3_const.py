def v3_get_default_list_item():
    return { 'id': '', 'title': '', 'forward': '', 'author': '', 'image': '', 'video': '',
             'date': '', 'time_millis': '', 'age': '', 'original_url': '', 'content': [],
             'type': '', 'category_id': '', 'open_type': '1', 'other_info': ''}


def v3_get_default_detail_item():
    return {'title': '', 'subtitle': '', 'author': '', 'date': '', 'content': [], 'serial_list': []}


v3_categories = {
    'one': {
        'home': 'http://v3.wufazhuce.com:8000/api/channel/one/',
        'read': 'http://v3.wufazhuce.com:8000/api/channel/reading/more/',
        'music': 'http://v3.wufazhuce.com:8000/api/channel/music/more/',
        'movie': 'http://v3.wufazhuce.com:8000/api/channel/movie/more/',
        'detail_article': 'http://m.wufazhuce.com/article/',
        'detail_serial': 'http://m.wufazhuce.com/serial/',
        'detail_question': 'http://m.wufazhuce.com/question/',
        'detail_music': 'http://m.wufazhuce.com/music/',
        'detail_movie': 'http://m.wufazhuce.com/movie/'
    }
}

# 每一个 item 都对应着打开方式
v3_open_type = {
    'article': '1',
    'original_url': '2',
    'image': '3',
    'video': '4'
}
