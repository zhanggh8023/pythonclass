# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : manage.py
# @Software: PyCharm

import requests
import urllib, json
import http.cookiejar
from interface_auto_cases_for_ZNKF.conf import Allpath
from interface_auto_cases_for_ZNKF.public.logger import Log
from interface_auto_cases_for_ZNKF.public.get_mysql_info import getMysqlInfo

logger = Log('auto_cases', Allpath.log_path)


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
    def httpGet(self, url, method, data, sql):
        headers = {"Host": "47.97.152.55", "Connection": "keep-alive", "Origin": "http://47.97.152.55",
                   "X-TraceId": "b2486a20-a9d1-11e9-a2b4-5fa2b013c14c",
                   "Referer": "http://47.97.152.55/customerService/SystemManagement/Online", }
        oo = get_login_cookie()
        headers["Cookie"] = 's_authorization=' + oo["s_authorization"]
        headers["Content-Type"] = "application/json"
        # print(oo)
        # headers = {"Content-Type": "application/json",
        #            "Cookie": "s_authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiJzXzgxOWFlZThlZDg1NTRiOWY4MmU4ZDYzMDJjOGQyNDExIiwidGVuYW50SWQiOiJfMU5UTVdMQSIsImV4cCI6MTU2MjkxNzIzMn0.pcJyvYTllNRlHMFdgg9pboRi46PrxQhMurIm5_wgVqM"}
        print(headers)
        if method == 'GET':
            logger.info('现在开始进行get请求')
            request = requests.get(url, data, headers=headers).json()
        elif method == 'POST':
            logger.info('现在开始进行post请求')
            # body格式
            request = requests.post(url, json=data, headers=headers).json()
        elif method == 'POST_file':
            logger.info('现在开始进行post_file请求')
            # body格式
            request = requests.post(url, json=data,file=sql, headers=headers).json()
        elif method == 'POST1':
            logger.info('现在开始进行post1请求')
            # 参数格式
            request = requests.post(url, data, headers).json()
        elif method == 'POST_del':
            logger.info('现在开始进行post_del请求')
            sql_result = getMysqlInfo(Allpath.db_conf_path).get_mysql_info(sql['my_sql'], sql['condition'], sql['code'])
            logger.info('数据库返回:' + str(sql_result))
            print(sql_result)
            data['id'] = sql_result[0]
            # body格式
            request = requests.post(url, json=data, headers=headers).json()
        elif method == 'PUT':
            logger.info('现在开始进行put请求')
            print(data)
            # .encode("UTF-8")对字符串进行`UTF-8`编码格式编码
            # 用dumps转义成json格式
            # json.dump()函数的使用，将json信息写进文件
            # json.dumps()   编码：把一个Python对象编码转换成Json字符串
            # json.load()函数的使用，将读取json信息
            # json.loads()  解码：把Json格式字符串解码转换成Python对象
            # body格式
            request = requests.put(url, data=json.dumps(data), headers=headers).json()
        elif method == 'DELETE':
            logger.info('现在开始进行delete请求')
            sql_result = getMysqlInfo(Allpath.db_conf_path).get_mysql_info(sql['my_sql'], sql['condition'], sql['code'])
            logger.info('数据库返回:' + str(sql_result))
            print(data['1'],sql_result,url)
            #excel的data中指定：1取数据库返回第一个值，2指定数据库返回第二个值
            if data['1'] == 1:
                url_del = url + str(sql_result[0])
            else:
                url_del = url + str(sql_result[1])
            print(url_del)
            request = requests.delete(url_del, headers=headers).json()
        else:
            logger.info('请求方法未知！请核对后在尝试！')
        return request


if __name__ == '__main__':
    data = {"roleIds":["67ed99dc-3645-4215-90df-25945f1da49b","27acc809-03ab-4050-92d5-5f092678b8ed","8ddc45a6-b7b5-477e-9431-eee41fe31b23","1e56829e-83a0-48ec-86ca-6530a0b673bd"]}

    url = 'http://47.97.152.55/v1/tenants/_1NTMWLA/rolesExport'  # http://47.97.152.55//v1/staff/login'
    sql = {"my_sql": "select * from role where role_name=%s", "condition": "测试客服1","result": "1", "code": 0}

    hh = httpRequest().httpGet(url, 'GET', data, sql)
    print(hh)
