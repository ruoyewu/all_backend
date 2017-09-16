from flask import Blueprint

from v3 import v3_list, v3_detail

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
