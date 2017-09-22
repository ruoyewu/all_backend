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


@v3_app.route('/comment/add', methods=['POST'])
def v3_add_comment():
    time = int(request.form['time'])
    username = request.form['username']
    content = request.form['content']
    key = request.form['key']
    parent = int(request.form['parent'])

    result, info = v3_comment.add_comment(key, time, username, content, parent)
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
    if len(list) > 0:
        next = list[len(list) - 1]['time']
    else:
        next = -1

    data = {
        'result': result,
        'info': info,
        'list': list,
        'next': next
    }
    return json.dumps(data, ensure_ascii=False)

