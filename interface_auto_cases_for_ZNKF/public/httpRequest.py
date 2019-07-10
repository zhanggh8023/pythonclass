# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : manage.py
# @Software: PyCharm

import requests
import urllib
import http.cookiejar
from interface_auto_cases_for_ZNKF.conf import Allpath
from interface_auto_cases_for_ZNKF.public.logger import Log


logger=Log('auto_cases',Allpath.log_path)

# 登录获取cookie
def get_login_cookie():
    url1 = "http://47.97.152.55/v1/staff/login"
    data1 = {"username": "emhhbmcwMDE=", "password": "MTIzNDU2", "forceFlag": "true"}
    session = requests.Session()
    request = requests.post(url1, data1).json()
    print(request)
    cookie_jar = session.post(url1, data1).cookies
    cookie = requests.utils.dict_from_cookiejar(cookie_jar)
    print(cookie)
    return cookie


class httpRequest:
    def httpGet(self,url,method,data):
        headers={}
        oo = get_login_cookie()
        headers["Cookie"]='s_authorization='+oo["s_authorization"]
        headers["Content-Type"]="application/json"
        # print(oo)
        # headers = {"Content-Type": "application/json",
        #            "Cookie": "s_authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiJzXzgxOWFlZThlZDg1NTRiOWY4MmU4ZDYzMDJjOGQyNDExIiwidGVuYW50SWQiOiJfMU5UTVdMQSIsImV4cCI6MTU2MjkxNzIzMn0.pcJyvYTllNRlHMFdgg9pboRi46PrxQhMurIm5_wgVqM"}
        print(headers)
        if method=='GET':
            logger.info('现在开始进行get请求')
            request=requests.get(url,data).json()
        elif method=='POST':
            logger.info('现在开始进行post请求')
            # print(headers)
            request=requests.post(url,json=data,headers=headers).json()
        elif method=='POST1':
            logger.info('现在开始进行post请求')
            # print(headers)
            request=requests.post(url,data,headers).json()
        else:
            logger.info('请求方法未知！请核对后在尝试！')
        return request

if __name__ == '__main__':

    data={'staffId': 's_819aee8ed8554b9f82e8d6302c8d2411', 'keywords': '111', 'afterEvent': '1'}

    url='http://47.97.152.55/v1/tenants/_1NTMWLA/addStaffSummaryAfterwards'#http://47.97.152.55//v1/staff/login'

    hh=httpRequest().httpGet(url,'POST',data)
    print(hh)













