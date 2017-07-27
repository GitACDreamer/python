# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-07-26 10:53:27
# @title:  authority init file

from flask import Blueprint

auth = Blueprint('auth' , __name__)

from .import views