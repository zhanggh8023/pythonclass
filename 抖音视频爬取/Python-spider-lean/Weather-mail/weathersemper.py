#!/usr/bin/env python3
# coding: utf-8

from json import *
import pickle
import urllib.request
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

useraccount = 'wya@oneyian.com'    # 账号
password = '略略略'    # 授权码
#合肥天气
link = 'http://t.weather.sojson.com/api/weather/city/101220101'

html=urllib.request.urlopen(link) #就可以访问了，不会报异常
weatherHTML = html.read().decode('utf-8')#读入打开的url
weatherJSON = JSONDecoder().decode(weatherHTML)#创建json
if weatherJSON['status'] == 200:
    weatherInfo = weatherJSON['data']
    weatherToday = weatherInfo['forecast'][0]
    weather24 = weatherInfo['forecast'][1]
    # 今日
    todayWeather = weatherToday['type']+' '+weatherToday['fx']
    todayWenDu= weatherToday['low']+' ~ '+weatherToday['high']
    # 明日
    tomorrowWeather = weather24['type']+' '+weather24['fx']
    tomorrowWenDu= weather24['low']+' ~ '+weather24['high']
    
    mailContent = '<html><body style="background-color:AntiqueWhite;"><h2 align="center" style="color: #0497ff">今日天气：%s</h2><p align="center" style="color: green;font-size:18px">天气：%s</p><p align="center" style="color: green;font-size:18px">风级：%s</p><p align="center" style="color: green;font-size:18px">温度：%s</p><p align="center" style="color: green;font-size:18px">空气质量：%s</p><p align="center" style="color: green;font-size:18px">温馨提示：%s</p><hr/><h2 align="center" style="color: #0497ff">明日天气：%s</h2><p align="center" style="color: green;font-size:18px">天气：%s</p><p align="center" style="color: green;font-size:18px">风级：%s</p><p align="center" style="color: green;font-size:18px">温度：%s</p><p align="center" style="color: green;font-size:18px">温馨提示：%s</p></body></html>' % (weatherToday['date'],todayWeather,weatherToday['fl'],todayWenDu,weatherInfo['quality'],weatherToday['notice'],weather24['date'],tomorrowWeather,weather24['fl'],tomorrowWenDu,weather24['notice'])
    
    if '雨' in mailContent or '雪' in mailContent :
        host_server = 'smtp.qq.com'
        sender_qq = useraccount # 登录账号
        pwd = password # 登录qq邮箱的授权码
        sender_qq_mail = useraccount # 邮件发送方
        receiver = useraccount #邮件接收方
        #邮件标题
        mail_title = '【南昌】今日天气提醒❤️'
        #ssl登录
        smtp = SMTP_SSL(host_server)
        smtp.set_debuglevel(1)
        smtp.ehlo(host_server)
        smtp.login(sender_qq, pwd)
        
        msg = MIMEText(mailContent, "html", 'utf-8')
        msg["Subject"] = Header(mail_title, 'utf-8')
        msg["From"] = sender_qq_mail
        msg["To"] = receiver
        smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
        smtp.quit()
    else:
        print ('今日【%s】天气：%s\n明日【%s】天气：%s' % (weatherToday['date'],todayWeather,weather24['date'],tomorrowWeather))
else:
    print(weatherJSON['message'])
