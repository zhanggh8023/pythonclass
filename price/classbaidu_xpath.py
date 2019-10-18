# -*- coding: utf-8 -*-
# @Time    : 2019/10/9 9:58
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : classbaidu_xpath.py
# @Software: PyCharm

#引入类ActionChains类
from selenium.webdriver.common.action_chains import ActionChains
#AC.方法名1（）.context_click().perform()

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()#打开浏览器
driver.maximize_window()#窗口最大化,要保持良好习惯全屏打开

#打开百度首页
driver.get('http://www.baidu.com')
#设置元素---表达式
setting_xpath='//div[@id="u1"]//a[@name="tj_settingicon"]'
#等待3秒
time.sleep(3)
#设置元素的webelment对象
set_ele=driver.find_element_by_xpath(setting_xpath)
#鼠标悬停操作  先实例化ActionCains类，在调用其方法，最后使用perform（）来执行鼠标操作
ActionChains(driver).move_to_element(set_ele).perform()
#高级搜索的定位路径
mypath='//div[@class="bdpfmenu"]//a[text()="高级搜索"]'
#等待高级搜索元素出现
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,mypath)))
#点击高级搜索进入
driver.find_element_by_xpath(mypath).click()
time.sleep(3)
#高级搜索：包含一下全部的关键内容输入元素路径
mypath_1='//td[@id="adv-setting-1"]//input[@id="adv_keyword"]'
#等待输入元素出现
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,mypath_1)))
#输入输入内容
driver.find_element_by_xpath(mypath_1).send_keys('python元素定位')
time.sleep(3)
#时间元素选择的路径
mypath_2='//td[@id="adv-setting-4"]//select'
mypath_3='//td[@id="adv-setting-4"]//option[text()="最近一年"]'
#等待时间元素出现
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,mypath_2)))
#点击时间进行选择
driver.find_element_by_xpath(mypath_2).click()
time.sleep(3)
#点击时间选择最近一年
driver.find_element_by_xpath(mypath_3).click()
#等待3秒
time.sleep(3)
#文档格式元素路径
mypath_4='//td[@id="adv-setting-5"]//select'
mypath_5='//td[@id="adv-setting-5"]//option[@value="ppt"]'
#点击文档格式进行选择
driver.find_element_by_xpath(mypath_4).click()
time.sleep(3)
#点击文档格式选择ppt
driver.find_element_by_xpath(mypath_5).click()
#等待3秒
time.sleep(3)
#高级搜索按钮元素路径
mypath_6='//td[@id="adv-setting-7"]//input[@class="advanced-search-btn"]'
#点击进行高级搜索
driver.find_element_by_xpath(mypath_6).click()
time.sleep(3)

windows = driver.window_handles
# 切换好指定的窗口
driver.switch_to.window(windows[-1])  # 最新打开的窗口


driver.get('http://sahitest.com/demo/index.htm')
# 切换好指定的窗口
driver.switch_to.window(windows[-1])  # 最新打开的窗口

print(driver.current_window_handle)  # 查看当前window handle
time.sleep(3)

driver.find_element_by_link_text('Window Open Test').click()  # 打开新window1
# 切换好指定的窗口
driver.switch_to.window(windows[-1])  # 最新打开的窗口
time.sleep(3)

driver.find_element_by_link_text('Window Open Test With Title').click()  # 打开新window2
print(driver.window_handles) # 查看当前所有window handle
time.sleep(3)


driver.close()
time.sleep(3)

driver.quit()  # 看到所有window都被关闭

