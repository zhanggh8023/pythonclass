# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 15:48
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : views.py
# @Software: PyCharm


from . import home
from flask import Flask, render_template, request, redirect, url_for

# 2. 创建蓝图的视图函数 (通过蓝图装饰路由)
@home.route("/")
def index():
    return render_template("home/index.html")


# 登录
@home.route("/login/")
def login():
    return render_template("home/login.html")


#退出
@home.route("/logout/")
def logout():
    return redirect(url_for("home.login"))


# 注册
@home.route("/regist/")
def regist():
    return render_template("home/regist.html")
