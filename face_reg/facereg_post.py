ngx# -*- coding: utf-8 -*-
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


name = file_name('./pic/')
# name=file_name('./citydo120/')
print(len(name))
print(name[0][:-4])

# url = "http://114.55.242.54:5001/face/register"
url = 'http://114.55.242.54:5001/face/recognition'



n = 0
m = 0
for i in range(len(name)):
    print(i)
    path = './pic/' + name[i]
    # path='./face_photo/20190614_153951.jpg'
    print(path)
    files = {'file': open(path, 'rb')}
    # data = {'uid': name[i][:-4]}
    try:
        # res = requests.post(url,data=data, files=files, verify=False)
        res = requests.post(url, files=files, verify=False)
        print(url, files)
        print("res", res)
        dict = json.loads(res.text)
        print("dict", dict, type(dict["code"]))
        if dict["code"] == "0":
            n += 1
            print('sucuss：', n)
            print(dict["uid"], name[i][:-4])
            if dict["uid"] != " "+name[i][:-4]:
                print(dict["uid"], name[i][:-4])
                m += 1
                print("error times", m)
    except:
        continue
print('成功：' + str(n), '错误：' + str(m))


