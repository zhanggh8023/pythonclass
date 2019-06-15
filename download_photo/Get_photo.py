# -*- coding: utf-8 -*-
# @Time    : 2019/6/14 11:18
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : Get_photo.py
# @Software: PyCharm


from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os,json


def Downloadphoto(url,name):
    # os.makedirs('./'+name+'/', exist_ok=True)
    from urllib.request import urlretrieve
    urlretrieve(url, './photo/'+name+'.jpg')




driver=webdriver.Chrome()
driver.maximize_window()


f = open('name_list.txt', 'r')
sourceInLines = f.readlines()  # 按行读出文件内容
f.close()
new = []  # 定义一个空列表，用来存储结果
for line in sourceInLines:
    temp1 = line.strip('\n',)  # 去掉每行最后的换行符'\n'
    temp2 = temp1.split(',')  # 以','为标志，将每行分割成列表
    new.append(temp2)  # 将上一步得到的列表添加到new中
print(new,len(new))


n=0
for ii in range(len(new)):
    for i in range(len(new[ii])):
        print(new[ii][i])
        n += 1
        print(n)
        # 发起一个get请求， 打开一个页面
        url = 'https://baike.baidu.com/item/'+ new[ii][i]
        driver.get(url)
        try:
            # 等待，未来加载这个元素出来
            hh='//div[@class="summary-pic"]/a/img'
            WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,hh)))

            photoSrc = driver.find_element_by_xpath(hh).get_attribute('src')
            print(photoSrc)
            Downloadphoto(photoSrc,new[ii][i])
        except:
            continue



time.sleep(1)
driver.close()
driver.quit()








