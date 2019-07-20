

import unittest
import time
import HTMLTestRunner_zgh
from interface_auto_cases_for_ZNKF.public import Unit_test
from interface_auto_cases_for_ZNKF.conf import Allpath
from interface_auto_cases_for_ZNKF.public.smtp import massageMail


suite = unittest.TestSuite()  # 实例
loader = unittest.TestLoader()
# 测试模块
suite.addTest(loader.loadTestsFromModule(Unit_test))
#runner = unittest.TextTestRunner()
#runner.run(suite)

now = time.strftime('%Y-%m-%d_%H_%M_%S')
file_path=Allpath.html_path+'/'+now+'.html'
with open(file_path, 'wb+') as file:
    # 实例化测试报告运行
    runner=HTMLTestRunner_zgh.HTMLTestRunner(stream=file, verbosity=2, tester='质量保障部—章广华',title='智能客服接口自动化测试报告【Python】',
                                             description='该测试报告仅体现某接口请求以及参数值验证情况。')
    # 传入测试运行对象
    runner.run(suite)
    # 当前时间，邮件对象
    #massageMail().Message(now,'849080458@qq.com')