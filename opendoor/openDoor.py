# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 18:23
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : openDoor.py
# @Software: PyCharm

import requests

url="https://zlxprod.citydo.com.cn/menjin/attendance/openDoor"
data={'phone':17681829051,'wifiName':'Citydo','wifiLevel':5,'wifiMac':'48:bd:3d:d9:c6:40','token':'eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0.HFWtJ9rXvo6BrAwKyEzmWLTxcXfiMIejd55epKAwMjMmkihkPrrvIg.9kVBEDLjt8-VO_1DGxaelA.YBEBfhR1lOe1D9mUQEGvKH69SHFV0qtl0zaDCBNBxRhIslsYCR2uRLyJBSPFiW3wkog1oPeG_pOUePeggL5k2w.J6yIuTKbLI05tfoMBfXC8g'}
files={'file':open('kaimen.wav','rb')}
res=requests.post(url,data=data,files=files)
print(res.text)


# phone	17681829051
# wifiName	Citydo
# wifiLevel	5
# wifiMac	48:bd:3d:d9:c6:40
# token	eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0.HFWtJ9rXvo6BrAwKyEzmWLTxcXfiMIejd55epKAwMjMmkihkPrrvIg.9kVBEDLjt8-VO_1DGxaelA.YBEBfhR1lOe1D9mUQEGvKH69SHFV0qtl0zaDCBNBxRhIslsYCR2uRLyJBSPFiW3wkog1oPeG_pOUePeggL5k2w.J6yIuTKbLI05tfoMBfXC8g

# Content-Disposition: form-data; name="file"; filename="kaimen.wav"
# Content-Type: audio/*
# Content-Length: 359724
