# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : manage.py
# @Software: PyCharm

from interface_atuo_cases0508.public.config import config
import mysql.connector

class getMysqlInfo:
    def __init__(self,config_path):
        self.config=config().read_config(config_path,'DBCONFIG','config')

    def get_cnn(self):
        cnn=mysql.connector.connect(**self.config)
        return cnn

    def get_mysql_info(self,my_sql,condition,code):
        cnn=self.get_cnn()
        cursor=cnn.cursor()
        cursor.execute(my_sql,(condition,))
        if code==1:#查询所有的
            result=cursor.fetchall()
        elif code==0:#查询一条信息
            result=cursor.fetchone()
        cursor.close()
        cnn.close()
        return result
