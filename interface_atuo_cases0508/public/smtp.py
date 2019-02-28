# -*- coding: utf-8 -*-
'''
4-19 smtp&logging
1:把发送邮件代码写成一个类，然后把这个类文件作为附件发给华华，邮箱：1255811581@qq.com

2:把你自己写的日志模块写成一个类，要求自己能够随时定义日志收集级别以及日志输出级别，要求同时输出到控制台以及指定文件。
1）级别指定，不管是日志收集还是日志输出，要求做成可配置（用到配置文件）
2）输入格式formatter,要求做成可配置，我想输出什么格式就是什么格式（用到配置文件）
'''

'''
*****邮件会跑到垃圾邮件里面
[STMPMASSAGEMIAL]
config={'mail_host':'smtp.qq.com',
        'mail_user':'*********',
        'mail_pass':'*********',
        'receivers' : '*********',
        'From':'月野*兔',
        'To':'华华老师',
        'subject' : 'Python SMTP 邮件发送代码',
        'MIMEText':'这是Python5,yyt的邮件发送，以及邮件类的代码附件测试……',
        'address':'python5_smtp.txt',
        }
'''

import smtplib
import configparser
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from interface_atuo_cases0508.conf import Allpath

class massageMail:
    def read_config (self,conf_path, section, option):
        tt = configparser.ConfigParser ()
        tt.read (conf_path,encoding='utf-8')
        result = eval (tt.get (section, option,))
        return result

    def Message(self,filename,receivers,):
        data=massageMail().read_config(Allpath.smtp_conf_path,'STMPMASSAGEMIAL','config')

        # Python 发送带附件的邮件
        mail_host = data['mail_host']  # 设置服务器
        mail_user = data['mail_user']  # 用户名
        mail_pass = data['mail_pass']  # 口令
        #receivers = data['receivers']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        #acc = data['acc']
        address=Allpath.html_path

        # 创建一个带附件的实例
        message = MIMEMultipart ()
        message['From'] = Header (data['From'], 'utf-8')  # 邮件名字
        message['To'] = Header (data['To'], 'utf-8')
        subject = data['subject']
        message['Subject'] = Header (subject, 'utf-8')

        # 邮件正文内容
        message.attach (MIMEText (data['MIMEText'], 'plain', 'utf-8'))

        # 构造附件1，传送当前目录下的 python5_smtp.txt 文件
        att1 = MIMEText (open (address+ '/'+filename+'.html', 'rb').read (), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="python5_smtp.html"'
        message.attach (att1)

        try:
            s = smtplib.SMTP_SSL (mail_host, 465)  # 连接上邮箱服务器
            s.login (mail_user, mail_pass)
            s.sendmail (mail_user, receivers.split(','), message.as_string ())
            print ("邮件发送成功")
        except smtplib.SMTPException as e:
            print ("Error: 无法发送邮件")
            raise e


if __name__ == '__main__':
    massageMail().Message()

