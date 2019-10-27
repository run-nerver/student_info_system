import os, click
import subprocess

from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app.models import pro


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, pro=pro)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


# 创建数据库
@manager.option('-u', dest='username')
@manager.option('-p', dest='password')
def recreate_db(username, password):
    """
    重新生成数据库
    """
    db.drop_all()
    db.create_all()
    db.session.commit()



if __name__ == '__main__':
    manager.run()