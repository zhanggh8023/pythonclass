# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : manage.py
# @Software: PyCharm

import requests
import json, time
# import http.cookiejar
from conf import Allpath
from public.logger import Log
from public.get_mysql_info import getMysqlInfo

logger = Log('auto_cases', Allpath.log_path)


# 登录获取cookie
def get_login_cookie():
    url1 = "http://47.97.152.55/v1/staff/login"
    data1 = {"username": "emhhbmcwMDE=", "password": "MTIzNDU2", "forceFlag": "true"}
    session = requests.Session()
    request = requests.post(url1, data1).json()
    logger.info("登录请求返回：%s" % request)
    cookie_jar = session.post(url1, data1).cookies
    # print(cookie_jar)
    cookie = requests.utils.dict_from_cookiejar(cookie_jar)
    logger.info("返回cookie：%s" % cookie)
    return cookie


# 退出登录
def get_logout(url, data, headers):
    # body格式
    request = requests.post(url, json=data, headers=headers).json()
    logger.info('调用退出请求成功%s' % request)
    return request


class httpRequest:
    def httpGet(self, url, method, data, sql):
        headers = {"Host": "47.97.152.55", "Connection": "keep-alive", "Origin": "http://47.97.152.55",
                   "X-TraceId": "b2486a20-a9d1-11e9-a2b4-5fa2b013c14c",
                   "Referer": "http://47.97.152.55/customerService/SystemManagement/Online", }
        oo = get_login_cookie()
        headers["Cookie"] = 's_authorization=' + oo["s_authorization"]
        # headers["Content-Type"] = "application/json"
        logger.info("当前headers配置：%s" % headers)
        if method == 'GET':
            logger.info('现在开始进行get请求')
            request = requests.get(url, data, headers=headers).json()
        elif method == 'POST':
            logger.info('现在开始进行post请求')
            # body格式
            request = requests.post(url, json=data, headers=headers).json()
        elif method == 'POST_file':
            logger.info('现在开始进行post_file请求')
            path = Allpath.project_path + "/request_file/" + sql['filename']
            print(sql['name'], headers, path)
            files = {sql['name']: (sql['filename'], open(path, 'rb'))}
            # body格式
            request = requests.post(url, data=data, files=files, headers=headers).json()
        elif method == 'POST1':
            logger.info('现在开始进行post1请求')
            # 参数格式
            request = requests.post(url, data, headers).json()
        elif method == 'POST2':
            logger.info('现在开始进行post2请求')
            # 参数格式
            request = requests.post(url, headers).json()
        elif method == 'POST_word':
            logger.info('现在开始进行post_word请求')
            request = {}
            # 参数格式,返回的是字符串格式
            text = requests.post(url, data, headers).text
            request['code'] = text
        elif method == 'POST_del':
            logger.info('现在开始进行post_del请求')
            sql_result = getMysqlInfo(Allpath.db_conf_path).get_mysql_info(sql['my_sql'], sql['condition'], sql['code'])
            logger.info('post删除数据库返回：' + str(sql_result))
            data['id'] = sql_result[0]
            # body格式
            request = requests.post(url, json=data, headers=headers).json()
        elif method == 'PUT':
            logger.info('现在开始进行put请求')
            headers["Content-Type"] = "application/json"
            # 2019年7月23日 16:17:38新增cookie不变循环处理方法
            if sql['1'] == 0:
                # 新增cookie中o_authorization状态保存
                headers["Cookie"] = 's_authorization=' + oo["s_authorization"] + ';o_authorization=' + oo[
                    "o_authorization"]
                request = requests.put(url, data=json.dumps(data), headers=headers).json()
                time.sleep(0.3)
                # 退出
                get_logout('http://47.97.152.55/v1/tenants/_1NTMWLA/logout', '', headers)
            else:
                # print(data)
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
            logger.info("excel取值获取数据库返回第%s位：" % data['1'])
            # excel的data中指定：0表示正常请求，1取数据库返回第一个值，2指定数据库返回第二个值
            if data['1'] == 1:
                url_del = url + str(sql_result[0])
                logger.info("请求URL：%s" % url_del)
                request = requests.delete(url_del, headers=headers).json()
            elif data['1'] == 2:
                url_del = url + str(sql_result[1])
                logger.info("请求URL：%s" % url_del)
                request = requests.delete(url_del, headers=headers).json()
            else:
                request = requests.delete(url, headers=headers).json()

        else:
            logger.info('请求方法未知！请核对后在尝试！')
        return request


if __name__ == '__main__':
    data = {"0": {"status": "online"}, "1": {"status": "rest"}, "2": {"status": "offline"}}

    url = 'http://47.97.152.55/v1/tenants/_1NTMWLA/staffs/s_819aee8ed8554b9f82e8d6302c8d2411/online'  # http://47.97.152.55//v1/staff/login'
    sql = {"1": 1}

    # DELETE,PUT,POST_del,POST_word,POST2,POST1,POST,POST_file,GET
    hh = httpRequest().httpGet(url, 'PUT', data, sql)
    print(hh)
