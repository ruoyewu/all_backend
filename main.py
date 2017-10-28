from flask import Flask

from v2 import v2_main
from v3 import v3_main

app = Flask(__name__)
app.register_blueprint(v2_main.v2_app)
app.register_blueprint(v3_main.v3_app)

app.debug = True

# app.run(port=3421)

