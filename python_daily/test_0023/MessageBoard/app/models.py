# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-07-26 16:16:37
# @title:  models

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from . import session, login_manager

Base = declarative_base()


class User(UserMixin, Base):
    # 用户数据库表
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(64), unique=True, index=True)
    username = Column(String(40), unique=True, index=True)
    password_hash = Column(String(256))
    posts = relationship('Post', backref="author", lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username


@login_manager.user_loader
def load_user(user_id):
    return session.query(User).filter(User.id == user_id)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    body = Column(Text)
    timestamp = Column(DateTime, index=True, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id'))
