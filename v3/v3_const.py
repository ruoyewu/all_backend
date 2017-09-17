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
    },
    'ifanr': {
        'home': 'http://www.ifanr.com/api/v3.0/?action=ifr_latest&posts_per_page=10&appkey=k0umfuztmirn5v73z3ij&sign'
                '=93dbaa08a7876dc852c64ae8547aebc7&paged=',
        'app': 'http://www.ifanr.com/api/v3.0/?action=ifr_latest&posts_per_page=10&appkey=k0umfuztmirn5v73z3ij&sign'
                '=93dbaa08a7876dc852c64ae8547aebc7&post_type=app&paged=',
        'coolBuy': 'http://www.ifanr.com/api/v3.0/?action=ifr_latest&posts_per_page=10&appkey=k0umfuztmirn5v73z3ij&sign'
                '=93dbaa08a7876dc852c64ae8547aebc7&post_type=coolbuy&paged=',
        'video': 'http://www.ifanr.com/api/v3.0/?action=ifr_latest&posts_per_page=10&appkey=k0umfuztmirn5v73z3ij&sign'
                '=93dbaa08a7876dc852c64ae8547aebc7&post_type=video&paged=',
        'product': 'http://www.ifanr.com/api/v3.0/?action=ifr_latest&posts_per_page=10&appkey=k0umfuztmirn5v73z3ij&sign'
                '=93dbaa08a7876dc852c64ae8547aebc7&category_id=1774&paged=',
        'people': 'http://www.ifanr.com/api/v3.0/?action=ifr_latest&posts_per_page=10&appkey=k0umfuztmirn5v73z3ij&sign'
                '=93dbaa08a7876dc852c64ae8547aebc7&category_id=57269&paged=',
        'company': 'http://www.ifanr.com/api/v3.0/?action=ifr_latest&posts_per_page=10&appkey=k0umfuztmirn5v73z3ij&sign'
                '=93dbaa08a7876dc852c64ae8547aebc7&category_id=19&paged=',
        'image': 'http://www.ifanr.com/api/v3.0/?action=ifr_latest&posts_per_page=10&appkey=k0umfuztmirn5v73z3ij&sign'
                '=93dbaa08a7876dc852c64ae8547aebc7&category_id=57906&paged=',
        'adv': 'http://www.ifanr.com/api/v3.0/?action=ifr_latest&posts_per_page=10&appkey=k0umfuztmirn5v73z3ij&sign'
                '=93dbaa08a7876dc852c64ae8547aebc7&category_id=64265&paged=',
        'create': 'http://www.ifanr.com/api/v3.0/?action=ifr_latest&posts_per_page=10&appkey=k0umfuztmirn5v73z3ij&sign'
                '=93dbaa08a7876dc852c64ae8547aebc7&category_id=33330&paged=',
        'early': 'http://www.ifanr.com/api/v3.0/?action=ifr_latest&posts_per_page=10&appkey=k0umfuztmirn5v73z3ij&sign'
                '=93dbaa08a7876dc852c64ae8547aebc7&category_id=57268&paged=',
        'car': 'http://www.ifanr.com/api/v3.0/?action=ifr_latest&posts_per_page=10&appkey=k0umfuztmirn5v73z3ij&sign'
                '=93dbaa08a7876dc852c64ae8547aebc7&category_id=33328&paged=',
        'game': 'http://www.ifanr.com/api/v3.0/?action=ifr_latest&posts_per_page=10&appkey=k0umfuztmirn5v73z3ij&sign'
                '=93dbaa08a7876dc852c64ae8547aebc7&category_id=782&paged=',
        'special': 'http://www.ifanr.com/api/v3.0/?action=ifr_latest&posts_per_page=10&appkey=k0umfuztmirn5v73z3ij&sign'
                '=93dbaa08a7876dc852c64ae8547aebc7&category_id=1769&paged=',
        'life': 'http://www.ifanr.com/api/v3.0/?action=ifr_latest&posts_per_page=10&appkey=k0umfuztmirn5v73z3ij&sign'
                '=93dbaa08a7876dc852c64ae8547aebc7&category_id=54067&paged=',
        'fanr': 'http://www.ifanr.com/api/v3.0/?action=ifr_latest&posts_per_page=10&appkey=k0umfuztmirn5v73z3ij&sign'
                '=93dbaa08a7876dc852c64ae8547aebc7&category_id=60394&paged=',
        'test': 'http://www.ifanr.com/api/v3.0/?action=ifr_latest&posts_per_page=10&appkey=k0umfuztmirn5v73z3ij&sign'
                '=93dbaa08a7876dc852c64ae8547aebc7&category_id=49180&paged=',
        'rank': 'http://www.ifanr.com/api/v3.0/?action=ifr_latest&posts_per_page=10&appkey=k0umfuztmirn5v73z3ij&sign'
                '=93dbaa08a7876dc852c64ae8547aebc7&category_id=13508&paged='
    }
}

# 每一个 item 都对应着打开方式
v3_open_type = {
    'article': '1',
    'original_url': '2',
    'image': '3',
    'video': '4'
}

v3_item_type = {
    'text': '1',
    "image": '2',
    "video": '3',
    'h1': '4',
    'h2': '5',
    'li': '6',
    'text_cen': '7',
    'quote': '8'
}
