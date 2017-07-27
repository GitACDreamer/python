# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-07-26 10:41:34
# @title:  flask demo

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello,World'

if __name__ == '__main__':
    app.run()