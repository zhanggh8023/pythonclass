# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 15:48
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : views.py
# @Software: PyCharm


from . import home
from flask import Flask, render_template, request, redirect, url_for

# 2. 创建蓝图的视图函数 (通过蓝图装饰路由)
# @home.route("/")
# def index():
#     return render_template("home/index.html")


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

#会员
@home.route("/user/")
def user():
    return render_template("home/user.html")

#密码
@home.route("/pwd/")
def pwd():
    return render_template("home/pwd.html")

#评论
@home.route("/comments/")
def comments():
    return render_template("home/comments.html")

#登录日志
@home.route("/loginlog/")
def loginlog():
    return render_template("home/loginlog.html")

#电影收藏
@home.route("/moviecol/")
def moviecol():
    return render_template("home/moviecol.html")

#电影列表
@home.route("/")
def index():
    return render_template("home/index.html")

#电影收藏
@home.route("/animation/")
def animation():
    return render_template("home/animation.html")

#搜索
@home.route("/search/")
def search():
    return render_template("home/search.html")

#详情
@home.route("/play/")
def play():
    return render_template("home/play.html")





