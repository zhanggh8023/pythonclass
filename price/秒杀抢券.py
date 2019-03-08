# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 14:51
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 秒杀抢券.py
# @Software: PyCharm


from selenium import webdriver
import pymouse
from selenium.webdriver import ActionChains
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import requests
import json


driver=webdriver.Chrome()
driver.maximize_window()

driver.get('https://cuxiao.suning.com/307haierpc.html?adtype=3')

Login_x='//div[@id="reg-bar-node"]/a'
Login_xx='//*[text()="账户登录"]'
namber_x='//*[@id="userName"]'
namber_xx='//*[@id="password"]'
button_x='//*[@id="submit"]'

#等待账号输入框元素出现
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,Login_x)))
driver.find_element_by_xpath(Login_x).click()
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,Login_xx)))
driver.find_element_by_xpath(Login_xx).click()
#输入手机号
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,namber_x)))
driver.find_element_by_xpath(namber_x).send_keys('13611535363')
sleep(1)
#输入密码
driver.find_element_by_xpath(namber_xx).send_keys('sunbin945')
#等待登录按钮元素出现
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,button_x)))
#点击登录
driver.find_element_by_xpath(button_x).click()

sleep(1)

