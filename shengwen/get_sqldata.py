# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 21:57
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : get_sqldata.py
# @Software: PyCharm


import mysql.connector

# 连接数据库
# 1、数据库连接信息
config = {'host': '47.97.253.39',
          'user': 'root',
          'password': 'cityDo@123',
          'port': 3306,
          'database': 'aqhy',
          }


def get_data():
    # 2、登录数据库
    connector = mysql.connector.connect(**config)  # **后面加上配置文件名

    # 建游标
    cursor = connector.cursor(buffered=True)

    list_1 = {}

    cur = cursor.execute("select name,phone from aqhy.access_user")

    # 查看数据库数据
    desc = cursor.description  # 获取字段的描述，默认获取数据库字段名称，重新定义时通过AS关键重新命名即可
    data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]  # 列表表达式把数据组装起来

    print(data_dict)
    return data_dict

    # 切记一定要执行
    cursor.execute('commit')

    # 关闭游标
    cursor.close()

    # 关闭连接
    connector.close()
