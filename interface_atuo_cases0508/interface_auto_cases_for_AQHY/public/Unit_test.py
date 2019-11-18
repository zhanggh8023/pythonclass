# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : manage.py
# @Software: PyCharm

import unittest, time
from ddt import ddt, data, unpack
from public.config import config
from public.readExcel import readExcel
from public.writeExcel import writeExcel
from public.httpRequest import httpRequest
from conf import Allpath
from public.logger import Log

logger = Log('auto_cases', Allpath.log_path)

# url = config().read_config (Allpath.http_conf_path, 'REGISTER', 'recharge')
data1 = [{"id": 1, "url": "https://testdfind.citydo.com.cn/datawindow/os/user/login", "method": "POST", "code": "ok",
          "data": {"username": "emhhbmcwMDE=", "password": "MTIzNDU2", "forceFlag": "true"}}]
h = readExcel(Allpath.test_data_path, 'Sheet1')
data2 = h.read_Excel()
# print(data2)
t = writeExcel(Allpath.test_data_path, 'Sheet1')
mode = config().read_config(Allpath.case_conf_path, 'FLAG', 'mode')
ID = config().read_config(Allpath.case_conf_path, 'FLAG', 'case_list')


@ddt  # 用ddt装饰我的测试类
class testHttpRequset(unittest.TestCase):
    def setUp(self):
        logger.info("============我要开始测试了===============")

    @data(*data2)  # 用data 来装饰我的测试用例
    # 加一个* 号可以进行区分单个执行
    @unpack
    def test_get(self, id, method, url, data, code, case_name, sql):
        logger.info('正在执行第%s条用例' % id)
        result_dict = {}
        logger.info("当前请求内容_URL：{}；method：{}；data：{}；sql：{}".format(url, method, data, sql))
        result = httpRequest().httpGet(url, method, data, sql)
        result_dict['code'] = result['code']
        #判断请求返回内容是否包含key值：data
        if result['data'] is not None:
            # logger.info('接口返回data%s' % result['responseData'])
            result_dict['data'] = str(result['data'])+result['msg']
        else:
            result_dict['data'] = result['msg']

        try:
            # 断言对比(期望值，实际返回值)
            self.assertEqual(code, result['code'])
            result_dict['result'] = 'pass'
            logger.info('用例code比对成功！返回code:%s'% result['code'])
        except Exception as e:
            result_dict['result'] = 'fail'
            logger.info('用例code比对失败！返回：code:{},msg:{}'.format(result['code'],result['msg']))
            t.write_Excel(id + 1, result_dict)
            raise e

        t.write_Excel(id + 1, result_dict)
        logger.info("返回数据写入excel成功！%s" % result_dict)
        time.sleep(0.3)

    def tearDown(self):
        logger.info("===============我要结束测试了！==================")


if __name__ == '__main__':
    unittest.main()
