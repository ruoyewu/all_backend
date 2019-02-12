import json

from flask import Flask


app = Flask(__name__)

from v2 import v2_main
from v3 import v3_main

app.register_blueprint(v2_main.v2_app)
app.register_blueprint(v3_main.v3_app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://debian-sys-maint:NfGi6vUSCsMIZyqt@localhost:3306/all?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.debug = False


# @app.before_request
# def rsa_test():
#     if request.method == 'POST':
#         secret = request.form['secret']
#         text = util.decrypt_rsa(secret)
#         print(text)
#         t = int(text)
#         print(t)
#         print(int(time()))
#         if abs(int(time()) - t) > 60:
#             return {
#                 'result': False,
#                 'info': "invalid secret",
#                 'content': ''
#             }


@app.route('/test', methods=['GET', 'POST'])
def test():
    return 'test'


@app.errorhandler(500)
def error_500(e):
    result = {
        'result': False,
        'info': 'server error or arguments invalid',
        'content': ''
    }
    return json.dumps(result, ensure_ascii=False)


@app.errorhandler(404)
def error_404(e):
    result = {
        'result': False,
        'info': 'url not found',
        'content': ''
    }
    return json.dumps(result, ensure_ascii=False)


# app.run(port=3421)
