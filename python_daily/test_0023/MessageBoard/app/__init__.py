# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-07-26 11:18:57
# @title:  app init file

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()

# 初始化数据库连接
engine = create_engine(
    'mysql+pymysql://root:123456@localhost:3306/messageboard?charset=utf8', max_overflow=5, encoding='utf-8')
# 创建DBSession
DBSesssion = sessionmaker(bind=engine)

# 创建session
session = DBSesssion()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-07-26 11:33:41
# @title:  Mesage board config file

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # 配置类
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guss string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    # 开发所用的数据库
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URL') or 'mysql://' + os.path.join(basedir, 'messageboard.db')


class TestingConfig(Config):
    # 测试所用的数据库
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URL') or 'mysql://' + os.path.join(basedir, 'messageboard-test.db')


class ProductionConfig(Config):
    # 生产所用的数据库
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URL') or 'mysql://' + os.path.join(basedir, 'messageboard-data.db')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

def create_app(config_name):
    # app工厂函数
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
