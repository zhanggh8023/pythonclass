# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 13:59
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : sco1.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome()
try:
    browser.get("http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
    browser.maximize_window()

    browser.switch_to.frame('iframeResult')

    source = browser.find_element_by_id('draggable')
    target = browser.find_element_by_id('droppable')

    print(source)
    print(target)
    actions = ActionChains(browser)
    actions.drag_and_drop(source, target)
    # 执行动作
    actions.perform()

    # 关闭提示框
    alert = browser.switch_to.alert
    print(alert)
    time.sleep(3)
    alert.dismiss()

    time.sleep(5)
except Exception as e:
    print(e)
finally:
    browser.quit()
    print('OK')