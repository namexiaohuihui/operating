# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: test_suite.py
@time: 2017/7/16 16:28
@项目名称:operating
"""
import inspect
import sys

import time
from selenium import  webdriver
from selenium.webdriver import ActionChains


class sys111:
    hello = ''
    world = ''
    def xxkk(self0):
        print('1', sys._getframe().f_code.co_name)
        print('2', inspect.stack()[0][3])
if __name__ == '__main__':
    browser = webdriver.Chrome("E:\drivers\Drivers\chromedriver59-61.exe")
    browser.get("https://www.baidu.com/")
    br_ele = browser.find_element_by_id('kw')
    print(br_ele)
    br_ele.send_keys('6666')
    ActionChains(browser).move_to_element(br_ele).perform()
    time.sleep(2)