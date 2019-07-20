# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : manage.py
# @Software: PyCharm

import unittest
from ddt import ddt,data,unpack
from interface_auto_cases_for_ZNKF.public.config import config
from interface_auto_cases_for_ZNKF.public.readExcel import readExcel
from interface_auto_cases_for_ZNKF.public.writeExcel import writeExcel
from interface_auto_cases_for_ZNKF.public.get_mysql_info import getMysqlInfo
from interface_auto_cases_for_ZNKF.public.httpRequest import httpRequest
from interface_auto_cases_for_ZNKF.conf import Allpath
from interface_auto_cases_for_ZNKF.public.logger import Log

logger=Log('auto_cases',Allpath.log_path)


# url = config().read_config (Allpath.http_conf_path, 'REGISTER', 'recharge')
data1=[{"id":1,"url":"http://47.97.152.55//v1/staff/login","method":"POST","code":"ok","data":{"username":"emhhbmcwMDE=","password":"MTIzNDU2","forceFlag":"true"}}]
h = readExcel (Allpath.test_data_path, 'Sheet1')
data2 = h.read_Excel ()
print(data2)
t=writeExcel(Allpath.test_data_path, 'Sheet1')
mode = config ().read_config (Allpath.case_conf_path, 'FLAG', 'mode')
ID = config ().read_config (Allpath.case_conf_path, 'FLAG', 'case_list')



@ddt#用ddt装饰我的测试类
class testHttpRequset(unittest.TestCase):
    def setUp(self):
        logger.info("============我要开始测试了===============")

    @data(*data2)#用data 来装饰我的测试用例
    #加一个* 号可以进行区分单个执行
    @unpack
    def test_get(self,id,method,url,data,code,case_name,sql):
        logger.info('正在执行第%s条用例'%id)
        result_dict = {}
        print(url,method,data,sql)
        result=httpRequest().httpGet(url,method,data,sql)
        result_dict['code']=result['code']
        if 'data' in result.keys():
            print(result['data'])
            result_dict['data']=result['data']
        try:
            self.assertEqual(result['code'],str(code))
            result_dict['result']='pass'
            logger.info('用例code比对成功！')
        except Exception as e:
            result_dict['result']='fail'
            logger.info('用例code比对失败！')
            raise e

        print(result_dict)
        t.write_Excel(id+1,result_dict)

    def tearDown(self):
        logger.info("===============我要结束测试了！==================")


if __name__ == '__main__':
    unittest.main()


