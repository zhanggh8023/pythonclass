# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 15:29
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : fist_flask.py
# @Software: PyCharm

from flask import Flask



app= Flask(__name__)

@app.route('/')
def index():
    return "<h1 style='color:red'>hello world!</h1>"



if __name__=="__main__":
    app.run()























