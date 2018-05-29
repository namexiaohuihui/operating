# -*- coding: utf-8 -*-
"""
@__author__ :DingDong
@file: domoTaothereTwo.py
@time: 2018/5/13 21:24
@Entry Name:operating
"""

import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
import time
import sys
# 调用函数，实现打开火狐浏览器的步骤
def firefox_browser():
    # 实现全局变量的引用
    firefoxBin = os.path.abspath(r"E:\Program Files\Mozilla Firefox\firefox.exe")
    os.environ["webdriver.firefox.bin"] = firefoxBin
    # 代码加载火狐驱动
    firefoxgeckobdriver = os.path.abspath(r"E:\drivers\Drivers\geckodriver64.exe")
    # os.environ["webdriver.path"] = firefoxgeckobdriver

    browser = webdriver.Firefox(executable_path=firefoxgeckobdriver)
    return browser
gundong = [0]
def kaishijixu(browser,shuliang,number):
    try:
        css_selector = "#pageNo-%s > div > div > div > div.reader-txt-layer > div" % (str(shuliang))
        page_dic = browser.find_element_by_css_selector(css_selector)
        page_dict[shuliang] = page_dic.text.strip()
        print(page_dic.text.strip())
        print("---------------------------->以上是第 %s 页的内容" % shuliang)

        return gundong[0]
    except:
        # print(1000 * int(number))
        gundong[0] = gundong[0] + 500 * int(number)
        scrollto = "window.scrollTo(0,%s)" % (gundong)
        browser.execute_script(scrollto)
        kaishijixu(browser,shuliang,number + 1)
        if number >= 50:
            sys.exit(-1)
link = "https://wenku.baidu.com/view/ba04345bf56527d3240c844769eae009591ba246.html"
browser = firefox_browser()
browser.get(link)
browser.maximize_window()
browser.implicitly_wait(5)
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)
browser.find_element_by_css_selector("#html-reader-go-more > div.banner-more-btn > span").click()
time.sleep(1)
browser.execute_script("window.scrollTo(0,0)")
time.sleep(1)
page_dict = {}
for shuliang in range(1,26):
    kaishijixu(browser,shuliang,1)
# page_dic1 = browser.find_element_by_css_selector("#pageNo-1 > div > div > div > div.reader-txt-layer > div")
# page_dic2 = browser.find_element_by_css_selector("#pageNo-1 > div > div > div > div.reader-txt-layer > div")
import pprint
pprint.pprint(page_dict)


