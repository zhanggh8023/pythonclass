# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : manage.py
# @Software: PyCharm

from interface_auto_cases_for_ZNKF.public.config import config
import mysql.connector
from interface_auto_cases_for_ZNKF.conf import Allpath

class getMysqlInfo:
    def __init__(self,config_path):
        # 传入参数：路径、便签、对象
        self.config=config().read_config(config_path,'DBCONFIG','config')
        print(self.config)

    def get_cnn(self):
        # 出入获取的配置文件，建立游标
        cnn=mysql.connector.connect(**self.config)
        return cnn

    def get_mysql_info(self,my_sql,condition,code):
        cnn=self.get_cnn()
        cursor=cnn.cursor()
        # 传入sql语句，对应字段值
        cursor.execute(my_sql,(condition,))
        if code==1:#查询所有的
            result=cursor.fetchall()
        elif code==0:#查询一条信息
            result=cursor.fetchone()
        cursor.close()
        cnn.close()
        return result


if __name__ == '__main__':
    sql_result=getMysqlInfo(Allpath.db_conf_path).get_mysql_info("select * from staff_summary_afterwards where keywords=%s","你好",0)
    print(sql_result)