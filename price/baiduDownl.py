from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


def Downloadphoto(url,name,sum):
    os.makedirs('./'+name+'/', exist_ok=True)
    from urllib.request import urlretrieve
    urlretrieve(url, './'+name+'/img'+str(sum)+'.jpg')



driver=webdriver.Chrome()
driver.maximize_window()

driver.get('https://wenku.baidu.com/view/40863ca7db38376baf1ffc4ffe4733687f21fc03.html?rec_flag=default&sxts=1543224017108')
hh='//div[@class="banner-more-btn"]//span[text()="继续阅读"]'
dd='//div[text()="下载文档到电脑，使用更方便"]'
zjmc='最新语音识别技术与声纹鉴定原理'
#等待登录按钮元素出现
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,hh)))
target = driver.find_element_by_xpath(dd)#找到这个元素。
driver.execute_script("arguments[0].scrollIntoView();", target) #利用js。拖动到可见的元素去
time.sleep(1)
driver.find_element_by_xpath(hh).click()#点击进入
time.sleep(2)

#前三张取地址
for j in range(1,4):
    ii = '//div[@class="ppt-page-item ppt-bd reader-pageNo-'+ str(j)+'"]//img'

    # 等待元素出现
    # ii='//div[@class="ppt-page-item reader-pageNo-4 ppt-bd hide"]//div[@class="ppt-image-wrap"]//img'
    print(ii)
    # WebDriverWait(driver, 10, 1).until(EC.visibility_of_all_elements_located((By.XPATH,ii)))
    # target = driver.find_element_by_xpath(ii)  # 找到这个元素。
    # driver.execute_script("arguments[0].scrollIntoView();", target)  # 利用js。拖动到可见的元素去
    # photoSrc1 = driver.find_element_by_xpath(ii).text()
    # print(photoSrc1)
    photoSrc = driver.find_element_by_xpath(ii).get_attribute('src')
    print(photoSrc)
    Downloadphoto(photoSrc,zjmc,j)

#中间取地址
for i in range(4,189):
    ii = '//div[@class="ppt-page-item reader-pageNo-'+ str(i) +' ppt-bd hide hidden-doc-banner"]//img'

    # 等待元素出现
    # ii='//div[@class="ppt-page-item reader-pageNo-4 ppt-bd hide"]//div[@class="ppt-image-wrap"]//img'
    print(ii)
    # WebDriverWait(driver, 10, 1).until(EC.visibility_of_all_elements_located((By.XPATH,ii)))
    # target = driver.find_element_by_xpath(ii)  # 找到这个元素。
    # driver.execute_script("arguments[0].scrollIntoView();", target)  # 利用js。拖动到可见的元素去
    # photoSrc1 = driver.find_element_by_xpath(ii).text()
    # print(photoSrc1)
    photoSrc = driver.find_element_by_xpath(ii).get_attribute('data-src')
    print(photoSrc)
    Downloadphoto(photoSrc,zjmc,i)

#最后一张
photoSrc = driver.find_element_by_xpath('//div[@class="ppt-page-item reader-pageNo-189 ppt-bd hide hidden-doc-banner"]//img').get_attribute('src')
Downloadphoto(photoSrc,zjmc,189)


time.sleep(1)
driver.close()
driver.quit()
