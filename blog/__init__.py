from flask import Flask
from flask_flatpages import FlatPages, pygments_style_defs

app = Flask(__name__)
pages = FlatPages()

APP_SETTINGS = "app.cfg"

app.config.from_pyfile(APP_SETTINGS)
pages.init_app(app)

import blog.views