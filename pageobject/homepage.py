from pageobject.basecase import BaseCase
from selenium.webdriver.common.by import By
class HomePage(BaseCase):

    homepage_input_search_loc=(By.NAME,'wd')
    homepage_btn_search_loc=(By.ID,'su')

    def search(self,content):
        self.sendkeys(content,*self.homepage_input_search_loc)
        self.click(*self.homepage_btn_search_loc)