

import unittest
import time
import HTMLTestRunnerNew,HtmlTestrRunner_cn,HtmlTestRunnerzgh,HTMLTestRunner
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
    runner=HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title='python接口自动化测试报告', description='现在应该萌萌哒')
    # 传入测试运行对象
    runner.run(suite)
    # 当前时间，邮件对象
    #massageMail().Message(now,'849080458@qq.com')