import json
import os

from flask import Blueprint, request, send_from_directory
from werkzeug.utils import secure_filename

from v3 import v3_list, v3_detail, v3_sql, v3_const

file_dir = '/home/ubuntu/project/all_python/file/avatar/'

v3_app = Blueprint('v3', __name__, url_prefix='/v3')


@v3_app.route('/')
def v3_index():
    return 'this is v3 page'


@v3_app.route('/app/api')
def v3_get_api():
    name = request.args['name']

    list = v3_const.v3_api[name]
    category_list = []
    for category in list:
        category_list.append({'category': category, 'api': list[category]})
    return json.dumps(category_list, ensure_ascii=False)


@v3_app.route('/article/list')
def v3_get_list():
    name = request.args['name']
    category = str(request.args['category'])
    page = request.args['page']

    return v3_list.v3_get_list(name, category, page)


@v3_app.route('/article/list2', methods=['POST'])
def v3_get_list2():
    name = request.form['name']
    category = request.form['category']
    page = request.form['page']
    content = request.form['content']
    if name == 'dgtle':
        return v3_list.v3_get_list2(name, category, page, content)
    else:
        return v3_list.v3_get_list2(name, category, page, json.loads(content))


@v3_app.route('/article/detail')
def v3_get_detail():
    name = request.args['name']
    category = str(request.args['category'])
    id = str(request.args['id'])

    return v3_detail.v3_detail(name, category, id)
    pass


@v3_app.route('/comment/add', methods=['POST'])
def v3_add_comment():
    time = int(request.form['time'])
    username = int(request.form['userid'])
    content = request.form['content'].strip()
    key = request.form['key']
    parent = int(request.form['parent'])

    result = v3_sql.put_comment(key, time, username, content, parent)
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/comment/get')
def v3_get_comment():
    key = request.args['key']
    below = int(request.args['time'])

    result = v3_sql.get_comment_list(key, below)
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/comment/delete')
def v3_delete_comment():
    id = int(request.args['id'])

    result = v3_sql.delete_comment(id)
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/article/info')
def v3_get_article_info():
    key = request.args['key']
    username = int(request.args['userid'])

    result = v3_sql.get_article_info(key, username)
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/article/love')
def v3_set_article_love():
    key = request.args['key']
    username = int(request.args['userid'])
    love = request.args['love']

    result = v3_sql.set_love(key, username, love)
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/user/login')
def v3_user_login():
    name = request.args['username']
    password = request.args['password']

    result = v3_sql.user_login(name, password)
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/user/sign')
def v3_user_sign():
    name = request.args['username']
    password = request.args['password']

    result = v3_sql.user_sign(name, password)

    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/user/avatar', methods=['POST'])
def v3_user_avatar():
    file = request.files['image']
    userid = request.form['userid']
    filename = secure_filename(file.filename)
    file.save(os.path.join(file_dir, userid + ".avatar"))
    return filename


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
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/favorite/get')
def v3_favorite_get():
    username = int(request.args['userid'])
    time = int(request.args['time'])

    result = v3_sql.get_favorite_time(username, time)
    return json.dumps(result, ensure_ascii=False)
