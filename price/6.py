from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
sreach_window=driver.current_window_handle

driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[3]/div[4]/h3/a").click()


time.sleep(1)
driver.close()
driver.quit()