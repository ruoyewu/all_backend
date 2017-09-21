import json

from flask import Blueprint, request

from v3 import v3_list, v3_detail, v3_comment

v3_app = Blueprint('v3', __name__, url_prefix='/v3')


@v3_app.route('/')
def v3_index():
    return 'this is v3 page'


@v3_app.route('/list/<name>/<category>/<page>')
def v3_get_list(name, category, page):
    return v3_list.v3_get_list(name, category, page)
    pass


@v3_app.route('/detail/<name>/<category>/<id>')
def v3_get_detail(name, category, id):
    return v3_detail.v3_detail(name, category, id)
    pass


@v3_app.route('/comment/add')
def v3_add_comment():
    time = int(request.args['time'])
    username = request.args['username']
    content = request.args['content']
    key = request.args['key']
    parent = int(request.args['parent'])

    result, info = v3_comment.add_comment(key, time, username, content, parent)
    print(result, info)
    data = {
        'result': result,
        'info': info
    }
    return json.dumps(data, ensure_ascii=False)


@v3_app.route('/comment/get')
def v3_get_comment():
    key = request.args['key']
    below = int(request.args['time'])

    result, info, list = v3_comment.get_comment(key, below)

    data = {
        'result': result,
        'info': info,
        'list': list
    }
    return json.dumps(data, ensure_ascii=False)
