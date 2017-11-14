# -*- coding: utf-8 -*-

import re
import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
import selenium.webdriver.support.expected_conditions as EC
__author__ = 'Administrator'
"""
@file: test_class.py
@time: 2017/10/26 11:58
"""

from practical.constant.browser.browser_establish import browser_confirm

from practical.operation.selenium_click import element_click

class cc(unittest.TestCase):



    def error(self):

        e = element_click()

        self.prompt = ""

        try:

            self.browser = browser_confirm().chrome_browser()
            self.browser.get("http://baidu.com")
            self.browser.implicitly_wait(30)
            id_ul = self.browser.find_element_by_id("u1")
            id_ul_a = id_ul.find_elements_by_tag_name('a')
            for a in id_ul_a:
                print("name %s" % a.text)
                print("href %s" % a.get_attribute('href'))

            e.css_click('.qrcode-img1')
        except Exception:

            e.writeLog(self.browser)

    # 将s中的字符和数字筛选出
    def OnlyCharNum(self,s):
        s2 = s.lower();
        fomart = '0123456789'
        for c in s2:
            if not c in fomart:
                s = s.replace(c, '');
        return s;

    def test_zhegnzhe(self):
        """这是一个按时开放你看我"""
        '''qwedfsdfgsd'''
        line = "Cats are smarter than dogs"
        # s = re.match(r'^[0-9]*$', "没有该123456商品D", re.M|re.I)
        #matchObj = re.match("\d+", '没有该123456商品D', re.M | re.I)
        matchObj = re.sub("\D", "", "没有12345+698该商品D")
        print("daye %s" %matchObj)
        #return matchObj;

    def is_visible_css_selectop(self, driver, locator, timeout=10):
        try:
            ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except TimeoutException:
            return False
        except Exception:
            return False

    def liulanqi(self):
        # 实现全局变量的引用
        browser = webdriver.Chrome("E:\drivers\Drivers\chromedriver59-61.exe")
        browser.get("http://baidu.com")
        size = browser.get_window_size()
        print(size)
        if c.is_visible_css_selectop(browser, "#kw"):
            print("chuxian")
        else:
            print("meiyou")

import time
if __name__ == '__main__':

    unittest.main

