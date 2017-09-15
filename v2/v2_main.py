from flask import Blueprint

from v2 import v2_get, v2_detail

v2_app = Blueprint("v2", __name__, url_prefix='/v2')


@v2_app.route('/')
def v2_index():
    return 'this is v2 page'


@v2_app.route('/list/<app>/<category>/<id>')
def v2_get_list(app, category, id):
    return v2_get.v2_get_list(app, category, id)
    pass


@v2_app.route('/detail/<app>/<category>/<id>')
def v2_get_detail(app, category, id):
    return v2_detail.v2_get_detail(app, category, id)
    pass
