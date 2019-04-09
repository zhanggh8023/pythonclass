#!/usr/bin/env weathersemper
# coding=utf-8
# author: zengyuetian
# 新房楼盘的数据结构

import sys
from lib.utility.version import PYTHON_3
if not PYTHON_3:   # 如果小于Python3
    reload(sys)
    sys.setdefaultencoding("utf-8")


class LouPan(object):
    def __init__(self, xiaoqu, price, total, url):
        # self.district = district
        # self.area = area
        self.xiaoqu = xiaoqu
        # self.address = address
        # self.size = size
        self.price = price
        self.total = total
        self.url = url

    def text(self):
        return self.xiaoqu + "," + \
                self.price + "," + \
                self.total + "," + \
                self.url
