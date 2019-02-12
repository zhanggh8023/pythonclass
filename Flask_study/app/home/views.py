# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 15:48
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : views.py
# @Software: PyCharm


from . import home


# 2. 创建蓝图的视图函数 (通过蓝图装饰路由)
@home.route("/")
def index():
    return "<h1 style='color:green'>this is home!</h1>"
