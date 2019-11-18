# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : manage.py
# @Software: PyCharm

import requests
import json, time
from conf import Allpath
from public.logger import Log
from public.get_mysql_info import getMysqlInfo

logger = Log('auto_cases', Allpath.log_path)




class httpRequest:
    def httpGet(self, url, method, data, sql):
        headers = {"Host": "aiapplet.citydo.com.cn", "Connection": "keep-alive", "Origin": "https://aiapplet.citydo.com.cn",
                   "Referer": "https://aiapplet.citydo.com.cn/","openid":"helloworld" }
        # headers['Cookie']="SESSION="+oo['SESSION']+';JSESSIONID='+oo['JSESSIONID']
        # headers["Content-Type"] = "multipart/form-data"
        logger.info("当前headers配置：%s" % headers)

        if method == 'GET':
            logger.info('现在开始进行get请求')
            request = requests.get(url, data, headers=headers).json()
        elif method == 'GET_cube':
            requests.post('https://testdfind.citydo.com.cn/datawindow/os/user/changeRole',{'windowUserAccount':'zhanggh@citydo.com.cn'}, headers=headers).json()
            logger.info('现在开始进行GET_cube请求')
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
            request = requests.post(url, data=data, files=files, headers=headers).json()
        elif method == 'POST1':
            logger.info('现在开始进行post1请求')
            # 参数格式
            request = requests.post(url, data, headers=headers).json()
        elif method == 'POST2':
            logger.info('现在开始进行post2请求')
            # 参数格式
            request = requests.post(url, headers).json()
        elif method == 'POST3':
            logger.info('现在开始进行post3请求')
            # 参数格式
            request = requests.post(url, data=json.dumps(data), headers=headers).json()
        elif method == 'POST_word':
            logger.info('现在开始进行post_word请求')
            request = {}
            # 参数格式,返回的是字符串格式
            text = requests.post(url, data, headers).text
            request['code'] = text
        elif method == 'POST_del':
            logger.info('现在开始进行post_del请求')
            sql_result = getMysqlInfo(Allpath.db_conf_path,'config').get_mysql_info(sql['my_sql'], sql['condition'], sql['code'])
            logger.info('post删除数据库返回：' + str(sql_result))
            data['id'] = sql_result[0]
            # body格式
            request = requests.post(url, json=data, headers=headers).json()

        elif method == 'PUT':
            logger.info('现在开始进行put请求')
            request = requests.put(url, data=json.dumps(data), headers=headers).json()


        elif method == 'DELETE':
            logger.info('现在开始进行delete请求')
            request = requests.delete(url, headers=headers).json()

        else:
            logger.info('请求方法未知！请核对后在尝试！')
        return request


if __name__ == '__main__':
    data ={"number":"245719360"}


    url = "https://aiapplet.citydo.com.cn/exploreHall/voice/livecheck"  # http://47.97.152.55//v1/staff/login'
    sql = {"name":"file","filename":"yy1.m4a"}

    # DELETE,PUT,POST_del,POST_word,POST2,POST1,POST,POST_file,GET,GET_kh
    hh = httpRequest().httpGet(url, 'POST_file', data, sql)
    print(hh)
