# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 15:48
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : views.py
# @Software: PyCharm


from . import home
from flask import Flask, render_template, request, redirect, url_for, flash, session, request
from Flask_study.app.home.forms import RegistForm, LoginForm, UserdatailForm, PwdForm
from Flask_study.app.models import User, Userlog
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from Flask_study.app import db, app
from functools import wraps
import os
import datetime
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


# 修改文件名称
def change_filename(filename):
    fileinfo = os.path.split(filename)
    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + str(uuid.uuid4().hex) + fileinfo[-1]
    return filename


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


# 会员修改资料
@home.route("/user/", methods=["GET", "POST"])
@user_login_req
def user():
    form = UserdatailForm()
    user = User.query.get(int(session["user_id"]))
    form.face.validators = []
    if request.method == "GET":
        form.name.data = user.name
        form.email.data = user.email
        form.phone.data = user.phone
        form.info.data = user.info
    if form.validate_on_submit():
        data = form.data
        file_face = secure_filename(form.face.data.filename)
        if not os.path.exists(app.config["FC_DIR"]):
            os.makedirs(app.config["FC_DIR"])
            os.chmod(app.config("FC_DIR"), "rw")
        user.face = change_filename(file_face)
        form.face.data.save(app.config["FC_DIR"] + user.face)

        name_count = User.query.filter_by(name=data["name"])
        if data["name"] != user.name and name_count == 1:
            flash('昵称已经存在！', "err")
            return redirect(url_for("home.user"))

        email_count = User.query.filter_by(email=data["email"])
        if data["email"] != user.name and email_count == 1:
            flash('邮箱已经存在！', "err")
            return redirect(url_for("home.user"))

        phone_count = User.query.filter_by(phone=data["phone"])
        if data["phone"] != user.name and phone_count == 1:
            flash('手机号码已经存在！', "err")
            return redirect(url_for("home.user"))

        user.name = data["name"]
        user.email = data["email"]
        user.phone = data["phone"]
        user.info = data["info"]
        db.session.add(user)
        db.session.commit()
        flash("修改资料成功!!", 'ok')
        return redirect(url_for("home.user"))
    return render_template("home/user.html", form=form, user=user)


# 密码
@home.route("/pwd/", methods=["GET", "POST"])
@user_login_req
def pwd():
    form = PwdForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(name=session['user']).first()
        if not user.check_pwd(data['old_pwd']):
            flash("旧密码错误!!", "err")
            return redirect(url_for('home.pwd'))
        user.pwd = generate_password_hash(data['new_pwd'])
        db.session.add(user)
        db.session.commit()  # 提交新密码保存，然后跳转到登录界面
        flash('密码修改成功，请重新登录！', category='ok')
        return redirect(url_for('home.logout'))
    return render_template("home/pwd.html", form=form)


# 评论
@home.route("/comments/")
@user_login_req
def comments():
    return render_template("home/comments.html")


# 登录日志
@home.route("/loginlog/<int:page>/", methods=['GET'])
@user_login_req
def loginlog(page=None):
    if page is None:
        page = 1
    page_data = Userlog.query.filter_by(
        user_id=int(session["user_id"])
    ).order_by(
        Userlog.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template("home/loginlog.html", page_data=page_data)


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
