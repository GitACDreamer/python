# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-07-26 16:22:24
# @title:  main forms

from flask_wtf import Form
from wtforms import TextAreaField, SubmitField
from wtforms.validators import Required


class PostForm(Form):
    body = TextAreaField("说点什么吧!", validators=[Required()])
    submit = SubmitField('提交')
