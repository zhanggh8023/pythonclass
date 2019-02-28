# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : manage.py
# @Software: PyCharm


import os
import configparser

class config:
    def read_config(self,conf_path,section,option):
        rc=configparser.RawConfigParser()
        rc.read(conf_path,encoding='utf-8')
        result=eval(rc.get(section,option))
        return result


class readConfig:
    def get_value(self,filepath,section,option):
        cf=configparser.ConfigParser()
        cf.read(filepath)
        value=cf.get(section,option)
        return value

if __name__ == '__main__':
    print(config ().read_config (os.path.dirname (os.getcwd ()) + '/conf/' + 'case.conf', 'FLAG', 'mode'))