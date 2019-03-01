from selenium import webdriver
from framwork.logger import Logger
import unittest
import logging
import time
import os
from selenium.webdriver.support import expected_conditions as  EC
from selenium.webdriver.support.wait import WebDriverWait
logger=Logger(logger="Basepage").getlog()
class BaseCase(object):

    def __init__(self,driver):
        self.driver=driver
    def open_url(self,url):
        self.driver.get(url)
    def quit_browser(self):
        self.driver.quit()
    def close(self):
        self.driver.close()
    def click(self,*loc):
        self.find_element(*loc).click()
    def find_element(self,*loc):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
        return self.driver.find_element(*loc)
    def sendkeys(self,text,*loc):
        el=self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("输入搜索内容%s" % text)
        except:
            logger.error("没找到")

        def get_windows_img(self):
            file_path = os.path.dirname(os.path.abspath(".")) + '/screenshorts/'
            rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
            screen_name = file_path + rq + '.png'
            try:
                self.driver.get_screenshot_as_file(screen_name)
                logger.info("get_windows_img")
            except:
                self.get_windows_img()
                logger.error("not get_windows_img")
