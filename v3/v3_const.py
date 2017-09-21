def v3_get_default_list_item():
    return { 'id': '', 'title': '', 'forward': '', 'author': '', 'image': '', 'video': '',
             'date': '', 'time_millis': '', 'age': '', 'original_url': '', 'content': [],
             'type': '', 'category_id': '', 'open_type': '1', 'other_info': ''}


def v3_get_default_detail_item():
    return {'title': '', 'subtitle': '', 'author': '', 'date': '', 'content': [], 'serial_list': []}


v3_categories = {
    'one': {
        'home': 'https://v3.wufazhuce.com:8000/api/channel/one/',
        'read': 'https://v3.wufazhuce.com:8000/api/channel/reading/more/',
        'music': 'https://v3.wufazhuce.com:8000/api/channel/music/more/',
        'movie': 'https://v3.wufazhuce.com:8000/api/channel/movie/more/',
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
    },
    'qdaily': {
        'home': 'http://www.qdaily.com/homes/articlemore/',
        'long': 'http://www.qdaily.com/tags/tagmore/1068/',
        'image': 'http://www.qdaily.com/tags/tagmore/1615/',
        'top': 'http://www.qdaily.com/tags/tagmore/29/',
        'commerce': 'http://www.qdaily.com/categories/categorymore/18/',
        'intel': 'http://www.qdaily.com/categories/categorymore/4/',
        'design': 'http://www.qdaily.com/categories/categorymore/17/',
        'fashion': 'http://www.qdaily.com/categories/categorymore/19/',
        'amuse': 'http://www.qdaily.com/categories/categorymore/3/',
        'city': 'http://www.qdaily.com/categories/categorymore/5/',
        'game': 'http://www.qdaily.com/categories/categorymore/54/',
        'detail': 'http://m.qdaily.com/mobile/articles/'
    },
    '36kr': {
        'home': 'http://36kr.com/api/info-flow/main_site/posts?column_id=&per_page=10&b_id=',
        'early': 'http://36kr.com/api//post?column_id=67&per_page=10&b_id=',
        'company': 'http://36kr.com/api//post?column_id=23&per_page=10&b_id=',
        'create': 'http://36kr.com/api//post?column_id=102&per_page=10&b_id=',
        'consume': 'http://36kr.com/api//post?column_id=180&per_page=10&b_id=',
        'what': 'http://36kr.com/api//post?column_id=186&per_page=10&b_id=',
        'skill': 'http://36kr.com/api//post?column_id=103&per_page=10&b_id=',
        'video': 'http://36kr.com/api//post?column_id=18&per_page=10&b_id=',
        'play': 'http://36kr.com/api//post?column_id=24&per_page=10&b_id=',
        'new': 'http://36kr.com/api//post?column_id=66&per_page=10&b_id=',
        'deep': 'http://36kr.com/api//post?column_id=70&per_page=10&b_id=',
        'research': 'http://36kr.com/api//post?column_id=71&per_page=10&b_id=',
        'policy': 'http://36kr.com/api//post?column_id=101&per_page=10&b_id=',
        'industry': 'http://36kr.com/api//post?column_id=104&per_page=10&b_id=',
        'interview': 'http://36kr.com/api//post?column_id=107&per_page=10&b_id=',
        'career': 'http://36kr.com/api//post?column_id=109&per_page=10&b_id=',
        'early_report': 'http://36kr.com/api//post?column_id=110&per_page=10&b_id=',
        'dujiaoshou': 'http://36kr.com/api//post?column_id=113&per_page=10&b_id=',
        'shangxueyuan': 'http://36kr.com/api//post?column_id=114&per_page=10&b_id=',
        'silicon_valley': 'http://36kr.com/api//post?column_id=115&per_page=10&b_id=',
        'abroad_create': 'http://36kr.com/api//post?column_id=116&per_page=10&b_id=',
        'creator': 'http://36kr.com/api//post?column_id=117&per_page=10&b_id=',
        'comment': 'http://36kr.com/api//post?column_id=118&per_page=10&b_id=',
        'raise_funds': 'http://36kr.com/api//post?column_id=119&per_page=10&b_id=',
        'car': 'http://36kr.com/api//post?column_id=120&per_page=10&b_id=',
        'feature': 'http://36kr.com/api//post?column_id=121&per_page=10&b_id=',
        'commerce_info': 'http://36kr.com/api//post?column_id=169&per_page=10&b_id=',
        'yike': 'http://36kr.com/api//post?column_id=170&per_page=10&b_id=',
        'intel': 'http://36kr.com/api//post?column_id=171&per_page=10&b_id=',
        'new_commerce': 'http://36kr.com/api//post?column_id=173&per_page=10&b_id=',
        'fengkou': 'http://36kr.com/api//post?column_id=177&per_page=10&b_id=',
        'new_wind': 'http://36kr.com/api//post?column_id=178&per_page=10&b_id=',
        'share_economy': 'http://36kr.com/api//post?column_id=181&per_page=10&b_id=',
        'focus_economy': 'http://36kr.com/api//post?column_id=182&per_page=10&b_id=',
        'commerce_100': 'http://36kr.com/api//post?column_id=183&per_page=10&b_id=',
        'one_more': 'http://36kr.com/api//post?column_id=184&per_page=10&b_id=',
        'ai_is': 'http://36kr.com/api//post?column_id=185&per_page=10&b_id=',
        'silicon_think': 'http://36kr.com/api//post?column_id=187&per_page=10&b_id=',
        'ku_100': 'http://36kr.com/api//post?column_id=188&per_page=10&b_id=',
        'tide_intel': 'http://36kr.com/api//post?column_id=189&per_page=10&b_id=',
        'employ_100': 'http://36kr.com/api//post?column_id=190&per_page=10&b_id=',
        'read': 'http://36kr.com/api//post?column_id=192&per_page=10&b_id=',
        'other': 'http://36kr.com/api//post?column_id=72&per_page=10&b_id=',
        'detail': 'http://36kr.com/api/post/'
    },
    'sspai': {
        'home': 'https://sspai.com/api/v1/articles?limit=10&type=recommend_to_home&sort=recommend_to_home_at&offset=',
        'matrix': 'https://sspai.com/api/v1/articles?limit=10&is_matrix=1&sort=matrix_at&offset=',
        'efficient': 'https://sspai.com/api/v1/articles?limit=10&has_tag=1&tag=效率工具&type=recommend_to_home&offset=',
        'photo': 'https://sspai.com/api/v1/articles?limit=10&has_tag=1&tag=手机摄影&type=recommend_to_home&offset=',
        'life': 'https://sspai.com/api/v1/articles?limit=10&has_tag=1&tag=生活方式&type=recommend_to_home&offset=',
        'game': 'https://sspai.com/api/v1/articles?limit=10&has_tag=1&tag=游戏&type=recommend_to_home&offset=',
        'hard': 'https://sspai.com/api/v1/articles?limit=10&has_tag=1&tag=硬件&type=recommend_to_home&offset=',
        'people': 'https://sspai.com/api/v1/articles?limit=10&has_tag=1&tag=人物&type=recommend_to_home&offset=',
        'mac': 'https://sspai.com/api/v1/articles?limit=20&has_tag=1&tag=mac&offset=',
        'ios': 'https://sspai.com/api/v1/articles?limit=20&has_tag=1&tag=ios&offset=',
        'android': 'https://sspai.com/api/v1/articles?limit=20&has_tag=1&tag=android&offset=',
        'detail': 'https://sspai.com/post/'
    },
    'juejin': {
        'home': 'https://timeline-merger-ms.juejin.im/v1/get_entry_by_timeline?src=web&limit=10&type=post&category'
                '=all&before=',
        'android': 'https://timeline-merger-ms.juejin.im/v1/get_entry_by_timeline?src=web&limit=10&type=post&category'
                   '=5562b410e4b00c57d9b94a92&before=',
        'web_design': 'https://timeline-merger-ms.juejin.im/v1/get_entry_by_timeline?src=web&limit=10&type=post'
                      '&category=5562b415e4b00c57d9b94ac8&before=',
        'web_server': 'https://timeline-merger-ms.juejin.im/v1/get_entry_by_timeline?src=web&limit=10&type=post'
                      '&category=5562b419e4b00c57d9b94ae2&before=',
        'ios': 'https://timeline-merger-ms.juejin.im/v1/get_entry_by_timeline?src=web&limit=10&type=post&category'
               '=5562b405e4b00c57d9b94a41&before=',
        'design': 'https://timeline-merger-ms.juejin.im/v1/get_entry_by_timeline?src=web&limit=10&type=post&category'
                  '=5562b41de4b00c57d9b94b0f&before=',
        'product': 'https://timeline-merger-ms.juejin.im/v1/get_entry_by_timeline?src=web&limit=10&type=post&category'
                   '=569cbe0460b23e90721dff38&before=',
        'tool': 'https://timeline-merger-ms.juejin.im/v1/get_entry_by_timeline?src=web&limit=10&type=post&category'
                '=5562b422e4b00c57d9b94b53&before=',
        'read': 'https://timeline-merger-ms.juejin.im/v1/get_entry_by_timeline?src=web&limit=10&type=post&category'
                '=5562b428e4b00c57d9b94b9d&before=',
        'intel': 'https://timeline-merger-ms.juejin.im/v1/get_entry_by_timeline?src=web&limit=10&type=post&category'
                 '=57be7c18128fe1005fa902de&before= '
    },
    'juzi': {
        'home': 'http://api.app.happyjuzi.com/article/list/home?ver=3.8.2&page=',
        'amuse': 'http://api.app.happyjuzi.com/article/list/channel?ver=3.8.2&id=27&page=',
        'movie': 'http://api.app.happyjuzi.com/article/list/channel?ver=3.8.2&id=32&page=',
        'fashion': 'http://api.app.happyjuzi.com/article/list/channel?ver=3.8.2&id=26&page=',
        'beauty': 'http://api.app.happyjuzi.com/article/list/channel?ver=3.8.2&id=102&page=',
        'funny': 'http://api.app.happyjuzi.com/article/list/channel?ver=3.8.2&id=61&page=',
        'life': 'http://api.app.happyjuzi.com/article/list/channel?ver=3.8.2&id=95&page=',
        'plan': 'http://api.app.happyjuzi.com/article/list/channel?ver=3.8.2&id=241&page=',
        'detail': 'http://m.happyjuzi.com/article/'
    },
    'yike': {
        'home': 'https://moment.douban.com/api/stream/date/',
        'detail': 'https://moment.douban.com/post/'
    },
    'zhihu': {
        'latest': 'https://news-at.zhihu.com/api/4/stories/latest',
        'before': 'https://news-at.zhihu.com/api/4/stories/before/',
        'detail': 'https://daily.zhihu.com/api/4/story/'
    },
    'geography': {
        'home': 'https://api.qingmang.me/v2/article.list?category_id=p196&token=c400a7e21688496ca3e7f17c6b0d1846'
                '&page_cursor='
    },
    '500px': {
        'home': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p280'
                '&page_cursor=',
        'hot':  'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3473'
                '&page_cursor=',
        'abstract': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3475'
                '&page_cursor=',
        'animal': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3477'
                '&page_cursor=',
        'black': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3479'
                '&page_cursor=',
        'famous': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3481'
                '&page_cursor=',
        'city': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3483'
                '&page_cursor=',
        'commerce': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3485'
                '&page_cursor=',
        'music': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3487'
                '&page_cursor=',
        'family': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3489'
                '&page_cursor=',
        'fashion': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3491'
                '&page_cursor=',
        'movie': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3493'
                '&page_cursor=',
        'art': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3495'
                '&page_cursor=',
        'food': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3497'
                '&page_cursor=',
        'news': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3499'
                '&page_cursor=',
        'scenery': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3501'
                '&page_cursor=',
        'tiny': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3503'
                '&page_cursor=',
        'nature': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3505'
                '&page_cursor=',
        'people': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3507'
                '&page_cursor=',
        'act': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3509'
                '&page_cursor=',
        'sport': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3511'
                '&page_cursor=',
        'calm': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3513'
                '&page_cursor=',
        'street': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3515'
                '&page_cursor=',
        'traffic': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3517'
                '&page_cursor=',
        'travel': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3519'
                '&page_cursor=',
        'under_water': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id'
                       '=p3521&page_cursor=',
        'city_explore': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id'
                        '=p3523&page_cursor=',
        'wedding': 'https://api.qingmang.me/v2/article.list?token=c400a7e21688496ca3e7f17c6b0d1846&category_id=p3525'
                '&page_cursor='
    },
    'tmt': {
        'home': 'https://api.tmtpost.com/v1/lists/home?limit=10&offset=',
        'fast': 'https://api.tmtpost.com/v1/posts/list/category/2581216?&fields=authors;thumb_image;number_of_reads;summary'
                '&limit=10&offset=',
        'create': 'https://api.tmtpost.com/v1/posts/list/category/2446155?&fields=authors;thumb_image;number_of_reads;summary'
                '&limit=10&offset=',
        'company': 'https://api.tmtpost.com/v1/posts/list/category/2446153?&fields=authors;thumb_image;number_of_reads;summary'
                '&limit=10&offset=',
        'car': 'https://api.tmtpost.com/v1/posts/list/category/2573550?&fields=authors;thumb_image;number_of_reads;summary'
                '&limit=10&offset=',
        'amuse': 'https://api.tmtpost.com/v1/posts/list/category/2446157?&fields=authors;thumb_image;number_of_reads;summary'
                '&limit=10&offset=',
        'professional': 'https://api.tmtpost.com/v1/posts/list/category/2573543?&fields=authors;thumb_image;number_of_reads;summary'
                '&limit=10&offset=',
        'english': 'https://api.tmtpost.com/v1/posts/list/category/2573634?&fields=authors;thumb_image;number_of_reads;summary'
                '&limit=10&offset=',
        'detail': 'http://www.tmtpost.com/'
    },
    'crazy_read': {
        'home': 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MjM5Mzk0OTI2MA%3D%3D&count=3'
                '&pass_ticket=80mAjbtf9RH5P8Fnq1q%2F6nM9Moav4v4SK2n%2BIsZu92B%2BcGrRzQkgcCRYQ0ek17lm&f=json&offset='
    },
    'kaiyan': {
        'home': 'http://baobab.kaiyanapp.com/api/v4/tabs/selected?udid=e6ff9949782643bb9f5be5e930d1459d2f53088a&vc'
                '=218&vn=3.9.0&deviceModel=ONEPLUS%20A5000&first_channel=eyepetizer_PP_market&last_channel'
                '=eyepetizer_PP_market&system_version_code=25&lastStartId=',
        'weekly': 'http://baobab.kaiyanapp.com/api/v4/rankList/videos?strategy=weekly&udid'
                  '=e6ff9949782643bb9f5be5e930d1459d2f53088a&vc=218&vn=3.9.0&deviceModel=ONEPLUS%20A5000'
                  '&first_channel=eyepetizer_PP_market&last_channel=eyepetizer_PP_market&system_version_code=25',
        'life': 'http://baobab.kaiyanapp.com/api/v4/categories/videoList?num=10&strategy=date&id=36&start=',
        'sport': 'http://baobab.kaiyanapp.com/api/v4/categories/videoList?num=10&strategy=date&id=18&start=',
        'idea': 'http://baobab.kaiyanapp.com/api/v4/categories/videoList?num=10&strategy=date&id=2&start=',
        'adv': 'http://baobab.kaiyanapp.com/api/v4/categories/videoList?num=10&strategy=date&id=14&start=',
        "music": 'http://baobab.kaiyanapp.com/api/v4/categories/videoList?num=10&strategy=date&id=20&start=',
        "travel": 'http://baobab.kaiyanapp.com/api/v4/categories/videoList?num=10&strategy=date&id=6&start=',
        'fashion': 'http://baobab.kaiyanapp.com/api/v4/categories/videoList?num=10&strategy=date&id=24&start=',
        'notes': 'http://baobab.kaiyanapp.com/api/v4/categories/videoList?num=10&strategy=date&id=22&start=',
        'starter': 'http://baobab.kaiyanapp.com/api/v4/categories/videoList?num=10&strategy=date&id=4&start=',
        'game': 'http://baobab.kaiyanapp.com/api/v4/categories/videoList?num=10&strategy=date&id=30&start=',
        'pet': 'http://baobab.kaiyanapp.com/api/v4/categories/videoList?num=10&strategy=date&id=26&start=',
        'animation': 'http://baobab.kaiyanapp.com/api/v4/categories/videoList?num=10&strategy=date&id=10&start=',
        'technology': 'http://baobab.kaiyanapp.com/api/v4/categories/videoList?num=10&strategy=date&id=32&start=',
        'plot': 'http://baobab.kaiyanapp.com/api/v4/categories/videoList?num=10&strategy=date&id=12&start=',
        'amuse': 'http://baobab.kaiyanapp.com/api/v4/categories/videoList?num=10&strategy=date&id=28&start=',
        'advance': 'http://baobab.kaiyanapp.com/api/v4/categories/videoList?num=10&strategy=date&id=8&start=',
        'show': 'http://baobab.kaiyanapp.com/api/v4/categories/videoList?num=10&strategy=date&id=38&start=',
        'collect': 'http://baobab.kaiyanapp.com/api/v4/categories/videoList?num=10&strategy=date&id=34&start='
    },
    'vmovie': {
        'home': 'https://app.vmovier.com/apiv3/index/index',
        'home_last': 'https://app.vmovier.com/apiv3/index/getIndexPosts/lastid/',
        'hot': 'https://app.vmovier.com/apiv3/post/getPostByTab?size=10&tab=hot&p=',
        'idea': 'https://app.vmovier.com/apiv3/post/getPostInCate?size=10&cateid=6&p=',
        'travel': 'https://app.vmovier.com/apiv3/post/getPostInCate?size=10&cateid=11&p=',
        'adv': 'https://app.vmovier.com/apiv3/post/getPostInCate?size=10&cateid=13&p=',
        'amuse': 'https://app.vmovier.com/apiv3/post/getPostInCate?size=10&cateid=8&p=',
        'love': 'https://app.vmovier.com/apiv3/post/getPostInCate?size=10&cateid=12&p=',
        'plot': 'https://app.vmovier.com/apiv3/post/getPostInCate?size=10&cateid=17&p=',
        'sport': 'https://app.vmovier.com/apiv3/post/getPostInCate?size=10&cateid=10&p=',
        'animation': 'https://app.vmovier.com/apiv3/post/getPostInCate?size=10&cateid=16&p=',
        'lizhi': 'https://app.vmovier.com/apiv3/post/getPostInCate?size=10&cateid=7&p=',
        'music': 'https://app.vmovier.com/apiv3/post/getPostInCate?size=10&cateid=18&p=',
        'science': 'https://app.vmovier.com/apiv3/post/getPostInCate?size=10&cateid=23&p=',
        'advance': 'https://app.vmovier.com/apiv3/post/getPostInCate?size=10&cateid=43&p=',
        'note': 'https://app.vmovier.com/apiv3/post/getPostInCate?size=10&cateid=24&p=',
        'mix': 'https://app.vmovier.com/apiv3/post/getPostInCate?size=10&cateid=44&p=',
        'experiment': 'https://app.vmovier.com/apiv3/post/getPostInCate?size=10&cateid=45&p=',
        'life': 'https://app.vmovier.com/apiv3/post/getPostInCate?size=10&cateid=78&p=',
        'detail': 'https://app.vmovier.com/apiv3/post/view?postid='
    },
    'caixin': {
        'home': 'http://m.search.caixin.com/search/latest/mobjson.jsp?size=10&page=',
        'finance': 'http://tag.caixin.com/news/homeInterface.jsp?subject=100300177;100602264;100602261;100602262'
                   ';100300470;100300179;100796345&count=10&callback=jQuery21309670029016702477_1503311622420&_'
                   '=1503311622435&start=',
        'company': '',
        'politics': '',
        'economy': '',
        'world': '',
        'idea': '',
        'figure': '',
        'culture': ''
    },
    'mark': {
        'home': 'http://api.markapp.cn/v160/singles/list',
        'detail': 'http://api.markapp.cn/mark_web/singles/detail'
    },
    "guokr": {
        'home_index': 'http://apis.guokr.com/handpick/v2/article.json?retrieve_type=by_touch_move&move_type=down',
        'home': 'http://apis.guokr.com/handpick/v2/article.json?retrieve_type=by_touch_move&move_type=up&refresh_pick_id=',
        'science': 'http://apis.guokr.com/handpick/v2/article.json?retrieve_type=by_offset&limit=10&category=science&offset=',
        'game': 'http://apis.guokr.com/handpick/v2/article.json?retrieve_type=by_offset&limit=10&category=game&offset=',
        'gossip': 'http://apis.guokr.com/handpick/v2/article.json?retrieve_type=by_offset&limit=10&category=gossip&offset=',
        'funny': 'http://apis.guokr.com/handpick/v2/article.json?retrieve_type=by_offset&limit=10&category=funny&offset=',
        'life': 'http://apis.guokr.com/handpick/v2/article.json?retrieve_type=by_offset&limit=10&category=life&offset=',
        'health': 'http://apis.guokr.com/handpick/v2/article.json?retrieve_type=by_offset&limit=10&category=health&offset=',
        'learning': 'http://apis.guokr.com/handpick/v2/article.json?retrieve_type=by_offset&limit=10&category=learning&offset=',
        'humanities': 'http://apis.guokr.com/handpick/v2/article.json?retrieve_type=by_offset&limit=10&category=humanities&offset=',
        'nature': 'http://apis.guokr.com/handpick/v2/article.json?retrieve_type=by_offset&limit=10&category=nature&offset=',
        'entertainment': 'http://apis.guokr.com/handpick/v2/article.json?retrieve_type=by_offset&limit=10&category=entertainment&offset='
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
    'quote': '8',
    'h3': '9'
}
