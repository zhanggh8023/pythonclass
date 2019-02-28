# -*- coding: utf-8 -*-

import requests
from interface_atuo_cases0508.conf import Allpath
from interface_atuo_cases0508.public.logger import Log

logger=Log('auto_cases',Allpath.log_path)
class httpRequest:
    def httpGet(self,url,method,data_1):
        if method=='get':
            logger.info('现在开始进行get请求')
            request=requests.get(url,data_1).json()
        elif method=='post':
            logger.info('现在开始进行post请求')
            request=requests.post(url,data_1).json()
        else:
            logger.info('请求方法未知！请核对后在尝试！')
        return request