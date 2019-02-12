# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 15:45
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : __init__.py.py
# @Software: PyCharm


from flask import Flask

app=Flask(__name__)
app.debug=True

from Flask_study.app.home import home as home_blueprint
# 导入前后端模块
from Flask_study.app.admin import admin as admin_blueprint


# 注册蓝图 (添加前后端模块，将蓝图中的url映射关系加载到项目中)
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint,url_prefix="/admin")