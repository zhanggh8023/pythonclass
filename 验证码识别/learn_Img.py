# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 14:46
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : learn_Img.py
# @Software: PyCharm

import time
#杭州市小客车登录验证码获取
import os
from fnmatch import fnmatch
import pytesseract
import pycapt
from PIL import Image
from 验证码识别.two_value_image import baidu_discern


def Downloadphoto(url,sum):
    os.makedirs('./image/', exist_ok=True)
    from urllib.request import urlretrieve
    urlretrieve(url, './image/img'+str(sum)+'.jpg')

# for i in range(18596,40500):
#     url='https://apply.hzxkctk.cn/apply/app/validCodeImage?ee='+str(i)
#     Downloadphoto(url,i)
#     print("下载成功："+url)


i = 0
for file in os.listdir('./image/'):
    # src1=file.replace('.jpg', '')
    src1 = baidu_discern('./image/'+ file)
    print(file,src1)

    # if fnmatch(file, '*.jpg'):
    #     img_name = file
    #     print(img_name)
    #     src = os.path.join(os.path.abspath('./image/'), img_name)  # 原先的图片名字
    #     dst = os.path.join(os.path.abspath('./image/'), src1) #根据自己的需要重新命名,可以把'E_' + img改成你想要的名字
    #     os.rename(src, dst) #重命名,覆盖原先的名字
    #     i += 1
        # time.sleep(0.05)






