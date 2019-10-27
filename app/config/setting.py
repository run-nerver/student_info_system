# -*- coding: UTF-8 –*-
import os

class Config(object):
    # 获取本地的 APP 名字： Flask(__name__)
    APP_NAME = os.environ.get('APP_NAME') or 'Flask-Base'

    if os.environ.get('SECRET_KEY'):
        SECRET_KEY = os.environ.get('SECRET_KEY')
    else:
        SECRET_KEY = 'you never guess'

    # 静态回调, 引入APP
    @staticmethod
    def init_app(app):
        return

# 继承Config，来设定下面的内容：MySQL
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Qwer123456@127.0.0.1:3306/xueji'

    @classmethod
    def init_app(cls, app):
        print('>>>>>Two: This app has update')



config = {
    'development' : DevelopmentConfig,
    'default' : DevelopmentConfig
}