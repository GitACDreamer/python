# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-07-26 15:43:43
# @title:  authrity forms include login and register

from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, EqualTo
from wtforms import ValidationError
from ..models import User
from .. import session


class LoginForm(Form):
    email = StringField(
        'Email', validators=[Required(), Length(1, 40), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')


class RegistrationForm(Form):
    email = StringField(
        'Email', validators=[Required(), Length(1, 64), Email()])
    username = StringField('Username', validators=[Required(), Length(1, 40)])
    password = PasswordField('Password', validators=[Required(), EqualTo(
        'password2', message='Passwords must match...')])
    password2 = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('注册')

    def validate_email(self, email):
        if session.query.filter_by(User.email == email).first():
            raise ValidationError('邮箱已经被注册！')

    def validate_username(self, user):
        if session.query.filter_by(User.username == user).first():
            raise ValidationError('用户名已存在！')
