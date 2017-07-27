# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-07-26 14:54:49
# @title:  文件管理

import os
import importlib
from app import create_app, session
from app.models import User
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """运行单元测试"""
    import unittest
    test = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(test)


if __name__ == '__main__':
    manager.run()
