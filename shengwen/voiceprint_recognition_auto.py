# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 18:23
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : openDoor.py
# @Software: PyCharm

import requests
import json

requests.packages.urllib3.disable_warnings()
import os
from shengwen.RWexcel import readexcel, write_Excel, write_sqldata
from shengwen.get_sqldata import get_data

# 获取数据库姓名手机号，写入excel
write_sqldata('voicedata.xlsx', 'Sheet1', len(get_data()), get_data())


# 获取目录下语音名称
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print('root_dir:', root)  # 当前目录路径
        print('sub_dirs:', dirs)  # 当前路径下所有子目录
        print('files:', files)  # 当前路径下所有非目录子文件
    return files


name = file_name('./yuying/')
print(len(name))

datas = readexcel('Sheet1')
url = "http://47.96.120.226:8180/menjin/voice/voiceLogin"
n = 0
m = 0
k = 0
for ii in range(len(datas)):
    sorce = []
    for i in range(len(datas)):
        path = './yuying/' + str(datas[i]['phone']) + '6.wav'
        filename = datas[i]['phone'] + '6.wav'
        print(filename)
        print(datas[ii]['name'], '→', datas[ii]['phone'], '→', path)
        if os.path.exists('./yuying/' + datas[i]['phone'] + '6.wav') == False:
            sorce.append('语音不存在')
            print('语音不存在')
            continue
        files = {'voice': open(path, 'rb')}
        data = {'phone': datas[ii]['phone'],
                'token': 'eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0.HFWtJ9rXvo6BrAwKyEzmWLTxcXfiMIejd55epKAwMjMmkihkPrrvIg.9kVBEDLjt8-VO_1DGxaelA.YBEBfhR1lOe1D9mUQEGvKH69SHFV0qtl0zaDCBNBxRhIslsYCR2uRLyJBSPFiW3wkog1oPeG_pOUePeggL5k2w.J6yIuTKbLI05tfoMBfXC8g'}
        res = requests.post(url, data=data, files=files, verify=False)
        dict = json.loads(res.text)
        print(dict)
        if dict['code'] == 0:
            print('成功')
            sorce.append('成功：' + dict['msg'])
            m += 1
        else:
            sorce.append(dict['data'])
            print('加入分数：', dict['data'])
            k += 1
        n += 1
        print('对比次数：' + n, '通过次数：' + m, '未通过次数：' + k)

    write_Excel('voicedata.xlsx', 'Sheet1', ii + 2, sorce, len(datas))


