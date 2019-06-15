# -*- coding: utf-8 -*-
# @Time    : 2019/6/15 8:51
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : Get_newphoto.py
# @Software: PyCharm


import requests
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
requests.packages.urllib3.disable_warnings()
import os


def Downloadphoto(url,name):
    # os.makedirs('./'+name+'/', exist_ok=True)
    from urllib.request import urlretrieve
    urlretrieve(url, './photo_new/'+name+'.jpg')

# 获取目录下语音名称
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print('root_dir:', root)  # 当前目录路径
        print('sub_dirs:', dirs)  # 当前路径下所有子目录
        print('files:', files)  # 当前路径下所有非目录子文件
    return files
name = file_name('./photo/')
print(len(name))

name_list=[]
for i in name:
    ii=i[:-4]
    name_list.append(ii)
print(name_list)


f = open('name.txt', 'r')
sourceInLines = f.readlines()  # 按行读出文件内容
f.close()
new = []  # 定义一个空列表，用来存储结果
for line in sourceInLines:
    temp1 = line.strip('\n',)  # 去掉每行最后的换行符'\n'
    temp2 = temp1.split(',')  # 以','为标志，将每行分割成列表
    new.append(temp2)  # 将上一步得到的列表添加到new中
print(new,len(new))



driver=webdriver.Chrome()
driver.maximize_window()



n=0
for ii in new:
    for i in range(len(ii)):
        if ii[i] not in name_list:
            print(ii[i])
            n += 1
            print(n)
            # 发起一个get请求， 打开一个页面
            url = 'https://baike.baidu.com/item/'+ ii[i]
            driver.get(url)
            try:
                # 等待，未来加载这个元素出来
                hh = '//div[@class="feature-poster-bg"]//div[@class="poster-absolute"]//div[@class="layout"]'
                # hh='/html/body/div[4]/div[1]/div/div[2]/div/style'
                WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_all_elements_located((By.XPATH, hh)))
                photoSrc = driver.find_element_by_xpath(hh).get_attribute("innerHTML")
                # print(photoSrc)
                tt = photoSrc[70:]
                oo = tt[:150]
                print(oo)
                Downloadphoto(oo,ii[i])
            except:
                continue



time.sleep(1)
driver.close()
driver.quit()






