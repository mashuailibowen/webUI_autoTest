import  unittest
from selenium import webdriver
class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome("../tools/chromedriver.exe")
        self.driver.implicitly_wait(5)
        print("开始了")
    def tearDown(self):
        self.driver.quit()
        print("结束")