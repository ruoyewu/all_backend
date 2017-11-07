import json
import os

from flask import Blueprint, request, send_from_directory
from werkzeug.utils import secure_filename

from v3 import v3_list, v3_detail, v3_sql, v3_const

file_dir = '/home/ubuntu/project/file/all/avatar/'
# file_dir = ' /Users/wuruoye/Documents/python/all_app/avatar/'

v3_app = Blueprint('v3', __name__, url_prefix='/v3')


@v3_app.route('/')
def v3_index():
    return 'this is v3 page'


@v3_app.route('/app/api')
def v3_get_api():
    try:
        name = request.args['name']
        list = v3_const.v3_api[name]
        category_list = []
        for category in list:
            category_list.append({'category': category, 'api': list[category]})
        result = True
        info = '请求成功'
    except:
        category_list = []
        result = False
        info = 'arguments name is invalid'

    result = {
        'result': result,
        'info': info,
        'content': category_list
    }
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/article/list')
def v3_get_list():
    name = request.args['name']
    category = str(request.args['category'])
    page = request.args['page']
    data = v3_list.v3_get_list(name, category, page)
    result = {
        'result': True,
        'info': '请求成功',
        'content': data
    }

    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/article/list2', methods=['POST'])
def v3_get_list2():
    name = request.form['name']
    category = request.form['category']
    page = request.form['page']
    content = request.form['content']
    if name == 'dgtle':
        data = v3_list.v3_get_list2(name, category, page, content)
    else:
        data = v3_list.v3_get_list2(name, category, page, json.loads(content))
    result = {
        'result': True,
        'info': '请求成功',
        'content': data
    }
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/article/detail')
def v3_get_detail():
    name = request.args['name']
    category = str(request.args['category'])
    id = str(request.args['id'])
    data = v3_detail.v3_detail(name, category, id)

    result = {
        'result': True,
        'info': '请求成功',
        'content': data
    }

    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/comment/add', methods=['POST'])
def v3_add_comment():
    time = int(request.form['time'])
    username = int(request.form['userid'])
    content = request.form['content'].strip()
    key = request.form['key']
    parent = int(request.form['parent'])

    result = v3_sql.put_comment(key, time, username, content, parent)
    result = {
        'result': True,
        'info': '添加评论',
        'content': result
    }
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/comment/love', methods=['POST'])
def v3_put_love():
    id = int(request.form['id'])
    userid = int(request.form['userid'])
    love = request.form['love']
    result = v3_sql.set_comment_love(id, userid, love)
    result = {
        'result': True,
        'info': '评论点赞',
        'content': result
    }
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/comment/get')
def v3_get_comment():
    userid = int(request.args['userid'])
    key = request.args['key']
    below = int(request.args['time'])

    result = v3_sql.get_comment_list(key, below, userid)
    result = {
        'result': True,
        'info': '获取评论列表',
        'content': result
    }
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/comment/get_user')
def v3_get_comment_user():
    userid = int(request.args['userid'])
    time = int(request.args['time'])

    result = v3_sql.get_comment_list_parent(userid, time)
    result = {
        'result': True,
        'info': '获取用户被评论列表',
        'content': result
    }
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/comment/delete')
def v3_delete_comment():
    id = int(request.args['id'])

    result = v3_sql.delete_comment(id)
    result = {
        'result': True,
        'info': '删除评论',
        'content': result
    }
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/article/info')
def v3_get_article_info():
    key = request.args['key']
    username = int(request.args['userid'])

    result = v3_sql.get_article_info(key, username)
    result = {
        'result': True,
        'info': '文章信息',
        'content': result
    }
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/article/love')
def v3_set_article_love():
    key = request.args['key']
    username = int(request.args['userid'])
    love = request.args['love']

    result = v3_sql.set_love(key, username, love)
    result = {
        'result': True,
        'info': '文章点赞',
        'content': result
    }
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/user/login')
def v3_user_login():
    name = request.args['username']
    password = request.args['password']

    result = v3_sql.user_login(name, password)
    result = {
        'result': True,
        'info': '用户登录',
        'content': result
    }
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/user/sign')
def v3_user_sign():
    name = request.args['username']
    password = request.args['password']

    result = v3_sql.user_sign(name, password)
    result = {
        'result': True,
        'info': '用户注册',
        'content': result
    }
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/user/avatar', methods=['POST'])
def v3_user_avatar():
    file = request.files['file']
    userid = request.form['userid']
    filename = secure_filename(file.filename)
    file.save(os.path.join(file_dir, userid + ".avatar"))
    result = {
        'result': True,
        'info': '头像上传',
        'content': filename
    }
    return result


@v3_app.route('/user/avatar/<userid>')
def v3_user_avatar_get(userid):
    return send_from_directory(file_dir, userid + ".avatar")


@v3_app.route('/favorite/put', methods=['POST'])
def v3_favorite_put():
    username = int(request.form['userid'])
    info = request.form['info']
    time = int(request.form['time'])
    key = request.form['key']
    favorite = request.form['favorite']

    result = v3_sql.put_favorite(username, time, info, key, favorite)
    result = {
        'result': True,
        'info': '收藏文章',
        'content': result
    }
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/favorite/get')
def v3_favorite_get():
    username = int(request.args['userid'])
    time = int(request.args['time'])

    result = v3_sql.get_favorite_time(username, time)
    result = {
        'result': True,
        'info': '获取收藏文章列表',
        'content': result
    }
    return json.dumps(result, ensure_ascii=False)
