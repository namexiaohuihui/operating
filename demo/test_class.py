# -*- coding: utf-8 -*-
import logging
import os
from time import sleep

import re

__author__ = 'Administrator'
"""
@file: test_class.py
@time: 2017/10/26 11:58
"""

from practical.constant.browser.browser_establish import browser_confirm

from practical.operation.selenium_click import element_click

class cc(object):



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

    def zhegnzhe(self):
        line = "Cats are smarter than dogs"
        # s = re.match(r'^[0-9]*$', "没有该123456商品D", re.M|re.I)
        #matchObj = re.match("\d+", '没有该123456商品D', re.M | re.I)
        matchObj = re.sub("\D", "", "没有该商品D")
        print(self.prompt)
        return matchObj;

if __name__ == '__main__':
    c = cc()
    c.prompt = "你好"
    c.zhegnzhe()
