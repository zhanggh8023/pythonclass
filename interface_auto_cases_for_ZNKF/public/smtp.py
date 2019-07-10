# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : smtp.py
# @Software: PyCharm


import smtplib
import configparser
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from interface_auto_cases_for_ZNKF.conf import Allpath


class massageMail:
    def read_config (self,conf_path, section, option):
        tt = configparser.ConfigParser ()
        tt.read (conf_path,encoding='utf-8')
        result = eval (tt.get (section, option,))
        return result

    def Message(self,filename,receivers,):
        data=massageMail().read_config(Allpath.smtp_conf_path,'STMPMASSAGEMIAL','config')
        print(data)

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

        # 构造附件1，传送当前目录下的 smtp.txt 文件
        att1 = MIMEText (open (address+ '/'+filename+'.html', 'rb').read (), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="znkf_interface_smtp.html"'
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
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    massageMail().Message(now,'[1441548753@qq.com,849080458@qq.com]')

