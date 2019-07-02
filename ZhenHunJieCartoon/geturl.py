# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 11:45
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : geturl.py
# @Software: PyCharm


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from ZhenHunJieCartoon.Cartoon import Downloadphoto





#获取生成url地址
for i in range(231271,231274):
    driver = webdriver.Chrome()  # 打开浏览器
    driver.maximize_window()  # 窗口最大化

    driver.get('https://m.36mh.com/manhua/zhenhunjie/')  # 进入链接页面
    mhzjxpath='//div[@class="list"]//a[@href="https://m.36mh.com/manhua/zhenhunjie/'+ str(i) +'.html"]'
    #target = driver.find_element_by_xpath(mhzjxpath)  # 找到这个元素。
    #river.execute_script("arguments[0].scrollIntoView();", target)  # 利用js。拖动到可见的元素去

    #print(mhzjxpath)
    # 获取章节名称
    zjmc = driver.find_element_by_xpath(mhzjxpath).text
    print(zjmc)
    # 点击进入
    driver.find_element_by_xpath(mhzjxpath).click()

    windows = driver.window_handles
    # 切换好指定的窗口
    driver.switch_to.window(windows[-1])  # 最新打开的窗口
    #定位章节页数元素路径
    zjieXpath='//span[@id="k_total"]'
    # 等待元素出现
    WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_all_elements_located((By.XPATH, zjieXpath)))
    # 获取章节页数
    zjys = int(driver.find_element_by_xpath(zjieXpath).text)
    print(zjys)

    #获取图片元素定位路径
    photoXpath='//img[@class="mip-fill-content mip-replaced-content"]'

    for ii in range(zjys):
        # 等待元素出现
        WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_all_elements_located((By.XPATH, photoXpath)))
        # 获得属性值get_attribute("属性名，如name")
        photoSrc = driver.find_element_by_xpath(photoXpath).get_attribute('src')
        print(photoSrc)
        Downloadphoto(photoSrc,zjmc,ii)

        #点击进入下一页
        driver.find_element_by_xpath(photoXpath).click()
        time.sleep(1)
    driver.quit()

