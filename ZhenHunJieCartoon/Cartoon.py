# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 10:17
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : Cartoon.py
# @Software: PyCharm

import os


def Downloadphoto(url,name,sum):
    os.makedirs('./'+name+'/', exist_ok=True)
    from urllib.request import urlretrieve
    urlretrieve(url, './'+name+'/img'+str(sum)+'.png')


'''
import os

os.makedirs('./image/', exist_ok=True)
IMAGE_URL = "https://img001.yayxcc.com/images/comic/92/183988/1525765333npWESqxsynjgCAVu.jpg"


def urllib_download ():
    from urllib.request import urlretrieve
    urlretrieve(IMAGE_URL, './image/img1.png')


def request_download ():
    import requests
    r = requests.get(IMAGE_URL)
    with open('./image/img2.png', 'wb') as f:
        f.write(r.content)


def chunk_download ():
    import requests
    r = requests.get(IMAGE_URL, stream=True)
    with open('./image/img3.png', 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)


urllib_download()
print('download img1')
#request_download()
#print('download img2')
#chunk_download()
#print('download img3')
'''