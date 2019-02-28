# -*- coding: utf-8 -*-
import requests
import os
import unittest
import time
import HTMLTestRunnerNew
from interface_atuo_cases0508.public.config import config
from interface_atuo_cases0508.public.readExcel import readExcel
import interface_atuo_cases0508.public.writeExcel
from interface_atuo_cases0508.public import Unit_test
from interface_atuo_cases0508.public.logger import Log
from interface_atuo_cases0508.public.smtp import massageMail

url = config().read_config(os.path.dirname(os.getcwd()) + '/conf/' + 'http.conf', 'REGISTER', 'recharge')
# print (url)
h = readExcel(os.path.dirname(os.getcwd()) + '/test_data/' + 'rechargetestcases.xlsx', 'rechargetestcases', 'init')

t = interface_atuo_cases0508.public.writeExcel.writeExcel(
    os.path.dirname(os.getcwd()) + '/test_data/' + 'rechargetestcases.xlsx', 'rechargetestcases')
# print (data)
mode = config().read_config(os.path.dirname(os.getcwd()) + '/conf/' + 'case.conf', 'FLAG', 'mode')
# print(mode)
list = []

data = h.read_Excel()
try:
    if mode == 0:
        ID = config().read_config(os.path.dirname(os.getcwd()) + '/conf/' + 'case.conf', 'FLAG', 'case_list')
        for i in data:
            if i['id'] in ID:
                data = list.insert(len(data) - 1, i)
                data = list
    for i in range(len(data)):
        request = requests.get(url, data[i]['data'])
        result = request.json()
        # print (data[i]['id'])

        # 写入excel数据
        t.write_Excel(data[i]['id'] + 1, 4, result['code'])
        # result
        if int(result['code']) == data[i]['code']:
            t.write_Excel(data[i]['id'] + 1, 5, 'pass')
        else:
            t.write_Excel(data[i]['id'] + 1, 5, 'fail')
        # result
        t.write_Excel(data[i]['id'] + 1, 6, result['msg'])


except Exception as e:
    print('出错了')
    raise e

suite = unittest.TestSuite()  # 实例
loader = unittest.TestLoader()

suite.addTest(loader.loadTestsFromModule(Unit_test))
runner = unittest.TextTestRunner()
runner.run(suite)

now = time.strftime('%Y-%m-%d_%H_%M_%S')
file = open('python5_' + now +'.html', "wb+")
runner1 = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title='python TextReport', description='现在应该萌萌哒')
runner.run(suite)


logger = Log("summer's log", os.path.dirname(os.getcwd()) + '/Result/test_result_data/')
logger.info("test_p")

massageMail().Message()


