

import unittest
import time
import HTMLTestRunnerNew
from interface_atuo_cases0508.public import Unit_test
from interface_atuo_cases0508.conf import Allpath
from interface_atuo_cases0508.public.smtp import massageMail


suite = unittest.TestSuite()  # 实例
loader = unittest.TestLoader()

suite.addTest(loader.loadTestsFromModule(Unit_test))
#runner = unittest.TextTestRunner()
#runner.run(suite)

now = time.strftime('%Y-%m-%d_%H_%M_%S')
file_path=Allpath.html_path+'/'+now+'.html'
with open(file_path, 'wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title='python TextReport', description='现在应该萌萌哒')
    runner.run(suite)
    #massageMail().Message(now,'849080458@qq.com')