import json

import requests
from flask import Flask

from v2 import v2_main

app = Flask(__name__)
app.register_blueprint(v2_main.v2_app)


if __name__ == '__main__':
    # test()
    app.run(debug=True)

