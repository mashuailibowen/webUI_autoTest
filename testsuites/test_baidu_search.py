import unittest
from testsuites.basetest import BaseTest
from pageobject.homepage import HomePage
class TestBaiduSearch(BaseTest):
    def test_baidusearch(self):
        url="https://www.baidu.com"
        home = HomePage(self.driver)
        home.open_url(url)
        home.search("TFBOYS")

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run()
