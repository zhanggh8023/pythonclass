# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : manage.py
# @Software: PyCharm

from public.config import config
import pymysql
from conf import Allpath
from public.logger import Log
import time

logger = Log('get_mysql_info', Allpath.log_path)
data_t = time.strftime('%Y-%m-%d')


class getMysqlInfo:
    def __init__ (self, config_path, conf):
        # 传入参数：路径、便签、对象
        self.config = config().read_config(config_path, 'DBCONFIG', conf)
        logger.info("本次数据库调用配置成功！")

    def get_cnn (self):
        # 出入获取的配置文件，建立游标
        cnn = pymysql.connect(**self.config)
        return cnn

    def auto_insert (self):
        list_1 = {}
        cnn = self.get_cnn()
        cursor = cnn.cursor()
        # 执行SQL语句
        cur = cursor.execute("select * from autotest.jkgl")
        # 查看数据库数据
        data = cursor.description
        data_1 = []
        test = []
        for i in range(len(data)):
            data_1.append(data[i][0])
            # print(data[i][0])
            test.append('%(' + data[i][0] + ')s')  # 生成value数列
            list_1[data[i][0]] = ''
        table_sql = "INSERT INTO jkgl (" + ','.join(data_1) + ")" + " VALUES " + "(" + ','.join(test) + ")"
        logger.info("插入数据库sql拼接成功！%s" % table_sql)
        return table_sql

    def Instert_mysql (self, data):
        sql = getMysqlInfo(Allpath.db_conf_path, 'config1').auto_insert()
        cnn = self.get_cnn()
        cursor = cnn.cursor()
        try:
            # 传入sql语句，对应字段值
            cursor.executemany(sql, data)
            cnn.commit()
            logger.info('sql写入统计测试记录成功！')
        except Exception as e:
            logger.info('sql写入统计测试记录失败！！！%s' % e)
            raise e
        cnn.close()

    def get_mysql_info (self, my_sql, condition, code):
        cnn = self.get_cnn()
        cursor = cnn.cursor()
        # 传入sql语句，对应字段值
        cursor.execute(my_sql, (condition,))
        desc = cursor.description  # 获取字段的描述，默认获取数据库字段名称，重新定义时通过AS关键重新命名即可
        if code == 1:  # 查询所有的
            result = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
        else:
            # 查询一条信息
            result = cursor.fetchone()  # print(result)
        cnn.close()
        logger.info("查询数据库调用成功！{}".format(result))
        return result

    def del_cardid_info (self):
        sql1 = "UPDATE `hospital_user_card` SET isdelete=1 WHERE user_name like '小七%' and `status` != 0 and modify_time <'" + data_t + "'; "
        sql2 = "UPDATE `enterprise_user_card` SET is_deleted=1 WHERE user_name like '小七%' AND begin_time <='" + data_t + "'; "
        sql3 = "delete from msg_content where mobile_no in ('17681829051','15258814180'); "
        sql4 = "UPDATE `hospital_company` SET isdelete=1 WHERE station_id='HL99998' and company_name like '接口测试%' AND create_time <'" + data_t + "'; "
        cnn = self.get_cnn()
        cursor = cnn.cursor()
        # 传入sql语句，对应字段值
        cursor.execute(sql1)
        cursor.execute(sql2)
        cursor.execute(sql3)
        cursor.execute(sql4)
        cnn.commit()
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_mysql_info_test (self, my_sql, code):
        cnn = self.get_cnn()
        cursor = cnn.cursor()
        # 传入sql语句，对应字段值
        cursor.execute(my_sql)
        desc = cursor.description  # 获取字段的描述，默认获取数据库字段名称，重新定义时通过AS关键重新命名即可
        if code == 1:  # 查询所有的
            data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]  # 列表表达式把数据组装起来
        elif code == 0:  # 查询一条信息
            data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchone()]  # 列表表达式把数据组装起来
        cnn.close()
        # print(data_dict)
        result = {'restult': "", 'sum': '', 'ok': '', 'fail': '', 'error': '', 'error_1': ''}
        result['restult'] = data_dict[0]['restult']

        sum = []
        ok = []
        fail = []
        error = []
        error_1 = []
        for i in range(1, len(data_dict) + 1):
            ii = len(data_dict) - i
            sum.append(data_dict[ii]['sum'])
            ok.append(data_dict[ii]['ok'])
            fail.append(data_dict[ii]['fail'])
            error.append(data_dict[ii]['error'])
            error_1.append(data_dict[ii]['error_1'])
        result['sum'] = sum
        result['ok'] = ok
        result['fail'] = fail
        result['error'] = error
        result['error_1'] = error_1
        # print(result)
        logger.info("测试结果数据库调用成功！{}".format(result))
        return result


if __name__ == '__main__':
    sql_result = getMysqlInfo(Allpath.db_conf_path, 'config').del_cardid_info()

    # data = [{
    #     'restult': "{'testname': '质量保障部—章广华', 'time': '2019-11-11 11:55:14', 'sumtime': '0:00:00.125677', 'testresult': '共 1 条接口用例，错误 1 条', 'tonggl': '0.00%'}",
    #     'sum': 1, 'ok': 0, 'fail': 0, 'error': 1, 'error_1': '100.00%', 'date': '2019-11-11_11_55_13'}]
    # sql_result = getMysqlInfo(Allpath.db_conf_path, 'config1').Instert_mysql(data)
    # sql_result=getMysqlInfo(Allpath.db_conf_path,'config1').get_mysql_info_test("select * from znkf ORDER BY date DESC LIMIT 10;",1)
    # sql = getMysqlInfo(Allpath.db_conf_path, 'config1').auto_insert()
    print(sql_result)
