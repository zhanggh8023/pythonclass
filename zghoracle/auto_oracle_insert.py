# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 15:43
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : auto_oracle_insert.py
# @Software: PyCharm



import cx_Oracle


# 注：设置环境编码方式，可解决读取数据库乱码问题
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# scott是数据用户名，tiger是登录密码（默认用户名和密码）
connection = cx_Oracle.connect("hg", "123456", '122.112.248.182:1521/CITYDO')

# 操作游标
cursor = connection.cursor()

def JGHG_insert_data(table):
    sql = auto_insert(table)
    #print(sql)

    #批量生成数据进行插入
    for i in range(50000,60000):
        ii=1000+i

        #插入数据格式（修改内容）
        table_data =  [('88T646' + str(ii), '987465004' + str(ii), '648665004' + str(i), 'DKFH0992' + str(ii),'DKeeeFH0992' + str(ii), '抵押','313340' + str(ii), 20180506, 20180506, '解除' ,  '科目1' + str(i), 20180504)]


        cursor.prepare(sql)#sql语句，需要与数据库字段相对应，value值长度与字段对应
        cursor.execute(None,table_data[0])#插入数据集
        print('执行sql:', sql)
        print('插入内容：', table_data[0])

        # 切记一定要执行
        cursor.execute('commit')


    # 关闭连接，释放资源
    cursor.close()
    connection.close()


def auto_insert(table):
    #执行SQL语句
    curs = cursor.execute("select column_name from all_tab_columns where  TABLE_NAME = '" + table + "'order by column_id")
    #查看数据库数据
    data = curs.fetchall()
    data_1=[]
    test=[]
    for i in range(len(data)):
        data_1.append(data[i][0])
        print(data[i][0])
        test.append(':'+str(i+1))#生成value数列

    table_sql="INSERT INTO "+ table + "("+ ','.join(data_1) + ")" + " VALUES " + "("+ ','.join(test) + ")"

    # data_2=[i for i in reversed(data_1)]#反序排列
    # print(','.join(data_1))  # 转为元组
    # print(','.join(test))#转为元组
    # print(data)
    # print(len(data))
    return table_sql



JGHG_insert_data('YJPT_DBGX')





