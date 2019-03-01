import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
dir = os.path.dirname(__file__)
firefox_driver_path = dir + "\geckodriver.exe"
print(firefox_driver_path)
driver = webdriver.Firefox(executable_path=firefox_driver_path)
driver.get("http://127.0.0.1/forum.php")
usermane=driver.find_element_by_name("username")
password=driver.find_element_by_name("password")
usermane.send_keys("admin")
password.send_keys ("mashuai")
login=driver.find_element_by_css_selector("button")
login.click()
time.sleep(10)
block=driver.find_element_by_link_text("默认版块")
block.click()
time.sleep(10)
posting=driver.find_element_by_id("subject")
content=driver.find_element_by_id("fastpostmessage")
posting.send_keys("000")
content.send_keys("火影")
deliver=driver.find_element_by_id("fastpostsubmit")
deliver.click()
time.sleep(10)
reply=driver.find_element_by_id("fastpostmessage")
reply.send_keys("海贼王")
dianji=driver.find_element_by_id("fastpostsubmit")
dianji.click()
time.sleep(5)
driver.quit()

