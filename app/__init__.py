import os
import click

from app.config.setting import config

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

db = SQLAlchemy()
csrf = CSRFProtect()
bootstrap = Bootstrap()
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["50 per hour"]
)
login_manager = LoginManager()


def register_blueprint(app):
    from app.web import admin_login as login_blueprint
    app.register_blueprint(login_blueprint, url_prefix='/admin')

    from app.web import admin_edit as edit_blueprint
    app.register_blueprint(edit_blueprint, url_prefix='/admin_edit')

    from app.web import student as student_blueprint
    app.register_blueprint(student_blueprint, url_prefix='/student')

    from app.web import print_all as print_all_blueprint
    app.register_blueprint(print_all_blueprint, url_prefix='/print_all')

    from app.web import weixin as weixin_back_blueprint
    app.register_blueprint(weixin_back_blueprint, url_prefix='/weixin_back')

    # 为 某一个蓝图 取消csrf保护
    csrf.exempt(weixin_back_blueprint)

    # 为 某一个蓝图 取消csrf保护
    csrf.exempt(student_blueprint)
    csrf.exempt(edit_blueprint)

def error_page(app):
    @app.errorhandler(404)
    @limiter.exempt
    def miss(error):
        return render_template('Error_page/404.html'), 404

    @app.errorhandler(500)
    @limiter.exempt
    def type(error):
        return render_template('Error_page/500.html'), 500


def custom_edit(app):
    from app.models.pro import Admin
    @login_manager.user_loader
    def load_user(user_id):
        user = Admin.query.get(int(user_id))
        return user

    @app.cli.command()
    @app.cli.command()
    def initdb():
        db.create_all()
        click.echo('initdb')


# 创建一个app生成器，使用blueprint来搭建网站域
def create_app(config_name=None):
    # 如果 config_name 为空 那么使用默认配置
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('app')
    app.config.from_object(config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 用于添加 flask 外设
    app.config['SECRET_KEY'] = 'you never guess'
    csrf.init_app(app)

    # 登录模块
    login_manager.init_app(app)
    login_manager.login_view = 'admin_login.login'
    login_manager.login_message_category = 'warning'
    login_manager.login_message = u'请先登录！'

    config[config_name].init_app(app)
    # Set up extensions
    db.init_app(app)

    # 网页前端, 确保 使用的是 Bootstrap-Flask 而不是Flask-Bootstrap
    bootstrap.init_app(app)

    # 限制Ip地址
    limiter.init_app(app)

    # blueprint and custom_edit
    error_page(app)
    custom_edit(app)
    register_blueprint(app)
    return app
