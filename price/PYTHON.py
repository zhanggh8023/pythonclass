# -*- coding: utf-8 -*-
# @Time    : 2018/8/9 14:54
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : PYTHON.py
# @Software: PyCharm

# import re
# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

import requests
import re
import reload
import time
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import sys




def changepage(url, total):
    urls = []
    nowpage = int(re.search('(\d+)', url, re.S).group(1))
    for i in range(nowpage, total + 1):
        link = re.sub('page_index=(\d+)', 'page_index=%s' % i, url, re.S)
        urls.append(link)
    return urls


def spider(url):
    html = requests.get(url)
    content = html.text

    selector = etree.HTML(content)
    title = []
    title = selector.xpath('//*[@id="component_0__0__6612"]/li/a/@title')

    detail = []
    detail = selector.xpath('//*[@id="component_0__0__6612"]/li/p[3]/span[1]/text()')
    saveinfo(title, detail)


def saveinfo(title, detail):
    length1 = len(title)
    for i in range(0, length1 - 1):
        f.writelines(title[i] + '\n')
        f.writelines(detail[i] + '\n\n')


if __name__ == '__main__':
    pool = ThreadPool(4)
    f = open('info.txt', 'a')
    url = 'http://search.dangdang.com/?key=Java&act=input&page_index=1'
    urls = changepage(url, 80)

    time1 = time.time()
    pool.map(spider, urls)
    pool.close()
    pool.join()

    f.close()
    print('爬取成功！')
    time2 = time.time()
    print('多线程耗时 : ' + str(time2 - time1) + 's')
