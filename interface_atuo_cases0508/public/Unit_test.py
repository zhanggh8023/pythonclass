# -*- coding: utf-8 -*-

import unittest
from ddt import ddt,data,unpack
from interface_atuo_cases0508.public.config import config
from interface_atuo_cases0508.public.readExcel import readExcel
from interface_atuo_cases0508.public.writeExcel import writeExcel
from interface_atuo_cases0508.public.get_mysql_info import getMysqlInfo
from interface_atuo_cases0508.public.httpRequest import httpRequest
from interface_atuo_cases0508.conf import Allpath
from interface_atuo_cases0508.public.logger import Log

logger=Log('auto_cases',Allpath.log_path)


#url = config ().read_config (Allpath.http_conf_path, 'HTTP', 'url')
#data1=[{'mobilephone': 17681829064, 'amount': '200'}]
h = readExcel (Allpath.test_data_path, 'rechargetestcases','init')
data2 = h.read_Excel ()
#print(data2)
t=writeExcel(Allpath.test_data_path, 'rechargetestcases')
mode = config ().read_config (Allpath.case_conf_path, 'FLAG', 'mode')
ID = config ().read_config (Allpath.case_conf_path, 'FLAG', 'case_list')
'''
list=[]
for i in data2:
    if i['id'] in ID:
        list.insert(len(data2)-1,i)
        print(list)
'''
@ddt#用ddt装饰我的测试类
class testHttpRequset(unittest.TestCase):
    def setUp(self):
        logger.info("============我要开始测试了===============")

    @data(*data2)#用data 来装饰我的测试用例
    #加一个* 号可以进行区分单个执行
    @unpack
    def test_get(self,id,method,url,data,code,sql):
        logger.info('正在执行第%s条用例'%id)
        result_dict = {}
        result=httpRequest().httpGet(url,method,data)
        sql_result=getMysqlInfo(Allpath.db_conf_path).get_mysql_info(sql['my_sql'],sql['condition'],sql['code'])
        result_dict['code']=result['code']
        result_dict['msg']=result['msg']

        try:
            self.assertEqual(result['code'],str(code))
            result_dict['result']='pass'
            logger.info('用例code比对成功！')
        except Exception as e:
            result_dict['result']='fail'
            logger.info('用例code比对报错：%s'%e+'——原因：%s'%result['msg'])
            #raise e

        try:
            self.assertEqual(sql_result[0],sql['result'])
            result_dict["sql_result"]='pass'
            logger.info('用例sql比对执行成功！')
        except Exception as e:
            result_dict["sql_result"]='fail'
            logger.info('执行用例sql比对报错：%s'%e+'——原因：%s'%result['msg'])
            t.write_Excel(id + 1, result_dict)
            raise e
        #print(result_dict)
        t.write_Excel(id+1,result_dict)

    def tearDown(self):
        logger.info("===============我要结束测试了！==================")


if __name__ == '__main__':
    unittest.main()

