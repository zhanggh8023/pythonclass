# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 15:45
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Flask, render_template, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy

import pymysql

# 定义数据库连接
app = Flask(__name__)  # 创建实例化app对象
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@172.16.20.130:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True  # 配置，如果设置True,将会追踪对象修改并且发送信号
app.config["SECRET_KEY"] = "7c9d7c8e53614affba09ddc9947e4329"
app.debug = True
db = SQLAlchemy(app)  # 定义db，传入app对象

from Flask_study.app.home import home as home_blueprint
# 导入前后端模块
from Flask_study.app.admin import admin as admin_blueprint

# 注册蓝图 (添加前后端模块，将蓝图中的url映射关系加载到项目中)
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")


# 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404
