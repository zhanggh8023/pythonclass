# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 22:28
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : photo_aout_dow.py
# @Software: PyCharm


from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os



driver=webdriver.Chrome()
driver.maximize_window()

#发起一个get请求， 打开一个页面
driver.get("http://www.baidu.com")
#等待，未来加载这个元素出来
time.sleep(2)
#driver.quit()


#完成搜索功能
#id class name  type  基础的
#xpath

#完成一个搜索功能

#1、输入搜索的内容
#driver.find_element_by_id()#id 肯定是唯一的 首选项
#driver.find_element_by_name()#除了id我们可以用name来定位  确保不会重复、没有冲突
#driver.find_element_by_class_name()#建议用这个么？你能确定她是唯一的，且有没有id


#页面操作  点击click  输入send_keys  清空 clear
driver.find_element_by_id('kw').send_keys('明星')
driver.find_element_by_id('su').click()
time.sleep(2)

name_list=[]

def GetName():
    for i in range(1,13):
        hh='//div[@class="op_exactqa_itemsArea c-row "]//div['+ str(i) +']/p/a'
    #等待登录按钮元素出现
        WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,hh)))
        #target = driver.find_element_by_xpath(hh)#找到这个元素。
        #driver.execute_script("arguments[0].scrollIntoView();", target) #利用js。拖动到可见的元素去
        print(hh)
        ii=driver.find_element_by_xpath(hh).get_attribute('title')
        print(ii)
        name_list.append(ii)

for o in range(1000):
    tt='//span[text()="下一页"]'
    driver.find_element_by_id(tt).click()








time.sleep(1)
driver.close()
driver.quit()


