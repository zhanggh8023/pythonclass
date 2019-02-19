from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


driver=webdriver.Chrome()
driver.maximize_window()

driver.get('http://testjghg.citydo.com.cn')
#driver.implicitly_wait(30)#设置全局大范围智能等待最多30秒

name='//*[@id="root"]//input[@placeholder="账户名"]'
pwd='//div[@id="root"]//input[@id="password"]'
button='//div[@class="landing_form_button"]//span'

button_1='//div[@id="modelManage"]//button[@class="ant-btn addModel"]'#新建模型

button_2='//div[@class="diagram-operation-wrap"]//div[@data-id="1"]/img'#过滤
button_3='//div[@id="model-svg-wrapper"]/*'#画布
#等待账号输入框元素出现
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,name)))
#输入手机号
driver.find_element_by_xpath(name).send_keys('admin')
time.sleep(1)
#输入密码
driver.find_element_by_xpath(pwd).send_keys('123456')
#等待登录按钮元素出现
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,button)))
#点击登录
driver.find_element_by_xpath(button).click()

time.sleep(5)
#等待登录按钮元素出现
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,button_1)))
#点击新建模型
driver.find_element_by_xpath(button_1).click()

#等待登录按钮元素出现
# WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,button_2)))
# driver.find_element_by_xpath(button_2).click()
# # move_to  移动
# # 定位到元素的源位置
# ele = driver.find_element_by_link_text(button_2)
# # 将鼠标移动到定位的元素上面
# ActionChains(driver).move_to_element(ele).perform()
#
# #拖拽组件
# # 起点
# start = driver.find_element_by_id(button_2)
# # 终点
# end = driver.find_element_by_id(button_3)
#
# actions = ActionChains(driver)
# actions.drag_and_drop(start, end)
# # 执行
# actions.perform()

#获取模型ID
model_name_xpath='//div[@id="model-svg-wrapper"]//div[@class="model-name"]'
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,model_name_xpath)))
edddd=driver.find_element_by_xpath(model_name_xpath).text()
print(edddd)







time.sleep(1)
driver.close()
driver.quit()