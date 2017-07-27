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