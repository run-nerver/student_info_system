from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin_login'
login_manager.login_message_category = 'warning'
login_manager.login_message = u'请先登录！'
from huojingyuan import routes
