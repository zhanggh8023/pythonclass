

import unittest
import time,shutil
import HTMLTestRunner_zgh
from public import Unit_test
from conf import Allpath
from public.get_mysql_info import getMysqlInfo
from public.writeExcel import writeExcel
from public.readExcel import readexcel
from public.smtp import massageMail
from public.logger import Log
import requests
import random

gmi=getMysqlInfo(Allpath.db_conf_path,'config1')
logger=Log('auto_cases',Allpath.log_path)
#去随机数赋值图片名称
name=str(random.randint(0,18))


# 2019年7月22日 10:40:51新增执行前清理原始用例结果记录
writeExcel(Allpath.test_data_path, 'Sheet1').Excel_dellog()

suite = unittest.TestSuite()  # 实例
loader = unittest.TestLoader()
# 测试模块
suite.addTest(loader.loadTestsFromModule(Unit_test))


now = time.strftime('%Y-%m-%d_%H_%M_%S')
file_path=Allpath.html_path+'/'+now+'.html'

with open(file_path, 'wb+') as file:
    # 实例化测试报告运行
    runner=HTMLTestRunner_zgh.HTMLTestRunner(stream=file, verbosity=2, tester='质量保障部—章广华',title='安全核验接口自动化测试报告【Python】',
                                             description='该测试报告仅体现某接口请求以及参数值验证情况。')
    # 传入测试运行对象
    runner.run(suite)

text=eval(gmi.get_mysql_info("select * from aqhy ORDER BY date DESC LIMIT 10;",1)['restult'])
logger.info('获取数据库测试结果内容成功：%s' % text)
#钉钉智能消息机器人智能客服
# url='https://oapi.dingtalk.com/robot/send?access_token=171c03789a58465e92cb4108a366de083cda389841f59d40d84980fb'
#测试地址
# url='https://oapi.dingtalk.com/robot/send?access_token=9abe322cb85c9a877bb026b0b9029378890c5f14fcc106be9ab5725e'
headers={"Content-Type":"application/json"}
data={
     "msgtype": "markdown",
     "markdown": {
         "title": "安全核验接口自动化测试报告",
         "text": "#### 安全核验接口自动化测试报告【V1.0.0】\n" +
                 "> 【测试人员】:"+str(text['testname']) + "\n" +
                 "\n> 【开始时间】:"+str(text['time']) + "\n" +
                 "\n> 【合计耗时】:"+str(text['sumtime']) + "\n" +
                 "\n> 【本次结果】:"+str(text['testresult']) + "\n" +
                 "\n> 【通过率】:"+str(text['tonggl']) + "\n" +
                 "> ![screenshot](http://47.111.14.23:8503/" + name + ".jpg)\n" +
                 "> ###### " + now[0:10] + " 发布 [在线查看报告详情](http://47.111.14.23:8503/) \n"
     },
    "at": {
        "atMobiles": [
            "18267199586",
            "13111595333"
        ],
        "isAtAll": "false"
    }
 }
# request = requests.post(url, json=data, headers=headers).json()
# logger.info("钉钉机器人消息请求内容%s" % data)
# logger.info('钉钉机器人消息请求成功%s' % request)

shutil.copyfile(Allpath.html_path+'/'+now+'.html',Allpath.html_path+'/report/index.html')
# 当前时间，邮件对象
# name=['zhanggh@citydo.com.cn','sunb@citydo.com.cn','liyj@citydo.com.cn','zhanghx@citydo.com.cn','liyang@citydo.com.cn','wangm@citydo.com.cn','liuhq@citydo.com.cn','panyw@citydo.com.cn','liuml@citydo.com.cn','gaoq0132@citydo.com.cn','zhuyx@citydo.com.cn','luojl@citydo.com.cn','liulb@citydo.com.cn','zhourc@citydo.com.cn','jinjl@citydo.com.cn','liufy@citydo.com.cn','liufy@citydo.com.cn','lib@citydo.com.cn','rongz@citydo.com.cn']
# name=['zhanggh@citydo.com.cn',]
# for i in range(len(name)):
#     try:
#         logger.info('发送邮箱为：%s' % name[i])
#         massageMail().Message(now,name[i])
#     except:
#         continue
logger.info('本次Python接口自动化框架执行完毕！%s' % time.strftime('%Y-%m-%d %H:%M:%S'))