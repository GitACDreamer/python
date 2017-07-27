# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-07-26 16:06:21
# @title:  authority views

from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from .import auth
from ..import session
from ..models import User
from .forms import LoginForm, RegistrationForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = session.query.filter_by(User.email==form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('用户名或者密码不正确!')
        return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已经退出登录!')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        session.add(user)
        flash('你现在可以登录了!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)