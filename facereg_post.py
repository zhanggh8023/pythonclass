# -*- coding: utf-8 -*-
# @Time    : 2019/6/14 15:53
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : face_post.py
# @Software: PyCharm


import requests
import json

requests.packages.urllib3.disable_warnings()
import os



# 获取目录下语音名称
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print('root_dir:', root)  # 当前目录路径
        print('sub_dirs:', dirs)  # 当前路径下所有子目录
        print('files:', files)  # 当前路径下所有非目录子文件
    return files
name = file_name('./face_photo/')
# name=file_name('./citydo120/')
print(len(name))
print(name[0][:-4])

# url = "http://114.55.242.54:5001/face/register"
url='http://114.55.242.54:5001/face/recognition'
for i in range(len(name)):
    print(i)
    path = './face_photo/' + name[i]
    # path='./face_photo/20190614_153951.jpg'
    print(path)
    files = {'file': open(path, 'rb')}
    # data = {'uid': name[i][:-4]}
    try:
        res = requests.post(url, files=files, verify=False)
        print(url,files)
        print(res)
        dict = json.loads(res.text)
        print(dict)
    except:
        continue
