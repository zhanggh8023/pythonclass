# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 15:09
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : pymongo.py
# @Software: PyCharm

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Flask!'


if __name__ == '__main__':
    app.run()