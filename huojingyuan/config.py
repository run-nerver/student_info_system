import os


SECRET_KEY = os.getenv('SECRET_KEY', '11111111')
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 自己变更
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/huojingyuan'  # win
POST_PER_PAGE = 5
DEBUG = True
