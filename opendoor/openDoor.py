# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 18:23
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : openDoor.py
# @Software: PyCharm

import requests
requests.packages.urllib3.disable_warnings()
headers={'Host': '121.40.16.175:8180','accessToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiJsdW9qaW5sb25nIiwiZXhwIjoxNTc3Njk3MDA3fQ.NiZCZFg47LmHYNaWMF_ft1P0PONVyq0FDx904KINoSo',
         'apiKey': 'cityDo_test','deviceid': '50b53908652543b0a6e99415bc94fd1c','deviceModel': 'polaris'}
url="http://121.40.16.175:8180/gateway/menjin/attendance/openDoor"
data={'phone':17681829051,'wifiName':'Citydo','wifiLevel':5,'wifiMac':'48:bd:3d:d9:c6:40',
      'token':'eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0.0T_WE1btyR9hMtCN7Ta8ZC7zjm36d9Rb8bzyehoXXLP3ngOGmPj9iQ.qaAVrsr34jxeHlXpkOJ7mA.I2QvgJlbTCuTu4HmvUTAlt71nBcq5WZwJ-gLnRdCV8hMeZwgjAnt9DxHnDGvMWqJ0hFkpsmIrMeH7Q1Z3rOq0A.J48RwiTosxlRfmtmXgXKOw&longitude'}
files={'file':open('kaimen.wav','rb')}
res=requests.post(url,params=data,headers=headers,files=files,verify=False)
print(res.text)


# phone	17681829051
# wifiName	Citydo
# wifiLevel	5
# wifiMac	48:bd:3d:d9:c6:40
# token	eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0.HFWtJ9rXvo6BrAwKyEzmWLTxcXfiMIejd55epKAwMjMmkihkPrrvIg.9kVBEDLjt8-VO_1DGxaelA.YBEBfhR1lOe1D9mUQEGvKH69SHFV0qtl0zaDCBNBxRhIslsYCR2uRLyJBSPFiW3wkog1oPeG_pOUePeggL5k2w.J6yIuTKbLI05tfoMBfXC8g

# Content-Disposition: form-data; name="file"; filename="kaimen.wav"
# Content-Type: audio/*
# Content-Length: 359724
