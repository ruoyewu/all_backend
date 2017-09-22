import json

from flask import Blueprint, request

from v3 import v3_list, v3_detail, v3_comment, v3_love

v3_app = Blueprint('v3', __name__, url_prefix='/v3')


@v3_app.route('/')
def v3_index():
    return 'this is v3 page'


@v3_app.route('/article/list')
def v3_get_list():
    name = request.args['name']
    category = str(request.args['category'])
    page = str(request.args['page'])

    return v3_list.v3_get_list(name, category, page)
    pass


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
    username = request.form['username']
    content = request.form['content'].strip()
    key = request.form['key']
    parent = int(request.form['parent'])

    result = v3_comment.add_comment(key, time, username, content, parent)
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/comment/get')
def v3_get_comment():
    key = request.args['key']
    below = int(request.args['time'])

    result = v3_comment.get_comment(key, below)
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/article/info')
def v3_get_article_info():
    key = request.args['key']
    username = request.args['username']

    result = v3_love.get_article_info(key, username)
    return json.dumps(result, ensure_ascii=False)


@v3_app.route('/article/love')
def v3_set_article_love():
    key = request.args['key']
    username = request.args['username']
    love = request.args['love']

    result = v3_love.set_article_love(key, username, love)
    return json.dumps(result, ensure_ascii=False)

