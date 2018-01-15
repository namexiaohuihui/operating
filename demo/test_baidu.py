import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import HTMLTestRunner
from utils.file_reader import ExcelReader

# http://www.cnblogs.com/guanfuchang/p/5970435.html
class TestBaiDu(unittest.TestCase):
    excel = os.getcwd() + '/baidu.xlsx'

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def sub_setUp(self):
        self.browser = webdriver.Chrome("E:\drivers\Drivers\chromedriver59-61.exe")
        self.driver.get('http://www.baidu.com')

    def sub_tearDown(self):
        self.driver.quit()

    def test_search(self):
        datas = ExcelReader(self.excel).data
        print("Datas %s " % datas)
        for d in datas:
            print("d %s " % d)
            with self.subTest(data=d):
                self.sub_setUp()
                self.driver.find_element(*self.locator_kw).send_keys(d['search'])
                self.driver.find_element(*self.locator_su).click()
                time.sleep(2)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()


if __name__ == '__main__':
    report_path = os.path.join(os.getcwd(), "report")
    report_abspath = os.path.join(report_path, "result.html")
    with open(report_abspath, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='qweasd', description='修改html报告')
        runner.run(TestBaiDu('test_search'))
        print(report_abspath)