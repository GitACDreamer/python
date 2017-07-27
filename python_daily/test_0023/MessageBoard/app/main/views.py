# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-07-26 16:23:52
# @title:  main views

from flask import render_template, url_for, redirect
from flask_login import current_user
from .forms import PostForm
from ..models import Post
from .. import session
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data,
                    author=current_user._get_current_object())
        session.session.add(post)
        return redirect(url_for('.index'))
    posts = session.query(Post).order_by(Post.timestamp.desc()).all()
    return render_template('index.html', form=form, posts=posts)
