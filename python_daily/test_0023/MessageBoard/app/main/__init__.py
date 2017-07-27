# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-07-26 10:57:20
# @title:  main init file

from flask import Blueprint

main = Blueprint('main' , __name__)

from .import views , errors