# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 15:48
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : views.py
# @Software: PyCharm


from . import home
from flask import Flask, render_template, request, redirect, url_for, flash, session, request
from Flask_study.app.home.forms import RegistForm, LoginForm
from Flask_study.app.models import User, Userlog
from werkzeug.security import generate_password_hash
from Flask_study.app import db
from functools import wraps
import uuid


# 2. 创建蓝图的视图函数 (通过蓝图装饰路由)
# @home.route("/")
# def index():
#     return render_template("home/index.html")

# 登录装饰器
def user_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("home.login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


# 登录
@home.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        if User.query.filter_by(name=data['name']).count() != 1:
            flash('账号不存在，请重新输入！', category='err')
            return redirect(url_for("home.login"))
        user = User.query.filter_by(name=data["name"]).first()
        if not user.check_pwd(data["pwd"]):
            flash("密码错误！", "err")
            return redirect(url_for("home.login"))
        session["user"] = user.name
        session["user_id"] = user.id
        userlog = Userlog(
            user_id=user.id,
            ip=request.remote_addr
        )
        db.session.add(userlog)
        db.session.commit()
        flash("登录成功！", "ok")
        return redirect(url_for("home.user"))
    return render_template("home/login.html", form=form)


# 退出
@home.route("/logout/")
def logout():
    session.pop("user", None)
    session.pop("user_id", None)
    return redirect(url_for("home.login"))


# 注册
@home.route("/regist/", methods=["GET", "POST"])
def regist():
    form = RegistForm()
    if form.validate_on_submit():
        data = form.data
        user = User(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            pwd=generate_password_hash(data['pwd']),
            uuid=uuid.uuid4().hex
        )
        db.session.add(user)
        db.session.commit()
        flash("注册成功！！", "ok")
    return render_template("home/regist.html", form=form)


# 会员
@home.route("/user/")
@user_login_req
def user():
    return render_template("home/user.html")


# 密码
@home.route("/pwd/")
@user_login_req
def pwd():
    return render_template("home/pwd.html")


# 评论
@home.route("/comments/")
@user_login_req
def comments():
    return render_template("home/comments.html")


# 登录日志
@home.route("/loginlog/")
@user_login_req
def loginlog():
    return render_template("home/loginlog.html")


# 电影收藏
@home.route("/moviecol/")
@user_login_req
def moviecol():
    return render_template("home/moviecol.html")


# 电影列表
@home.route("/")
@user_login_req
def index():
    return render_template("home/index.html")


# 电影收藏
@home.route("/animation/")
def animation():
    return render_template("home/animation.html")


# 搜索
@home.route("/search/")
def search():
    return render_template("home/search.html")


# 详情
@home.route("/play/")
def play():
    return render_template("home/play.html")
