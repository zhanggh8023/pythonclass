# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 14:37
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 1.py
# @Software: PyCharm

import cx_Oracle
import auto_oracle_insert as AOI
# 注：设置环境编码方式，可解决读取数据库乱码问题
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


print(AOI.auto_insert('YJPT_DGHQCKFHZMXJL'))