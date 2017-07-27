# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-07-26 16:21:19
# @title:  error page 

from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500