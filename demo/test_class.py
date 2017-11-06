# -*- coding: utf-8 -*-
import os
from time import sleep

__author__ = 'Administrator'
"""
@file: test_class.py
@time: 2017/10/26 11:58
"""

from practical.constant.browser.browser_establish import browser_confirm


browser=browser_confirm().firefox_browser()
browser.get("http://baidu.com")
id_ul = browser.find_element_by_id('u1')
id_ul_a = id_ul.find_elements_by_tag_name('a')
for a in id_ul_a:
    print("name %s" % a.text)
    print("href %s" % a.get_attribute('href'))

browser.close()
