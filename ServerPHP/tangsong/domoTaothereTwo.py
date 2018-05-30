# -*- coding: utf-8 -*-
"""
@__author__ :DingDong
@file: domoTaothereTwo.py
@time: 2018/5/13 21:24
@Entry Name:operating
"""

import os
import sys

from selenium import webdriver


# 调用函数，实现打开火狐浏览器的步骤
def firefox_browser():
    # 实现全局变量的引用
    firefoxBin = os.path.abspath(r"E:\Program Files\Mozilla Firefox\firefox.exe")
    os.environ["webdriver.firefox.bin"] = firefoxBin
    # 代码加载火狐驱动
    firefoxgeckobdriver = os.path.abspath(r"E:\drivers\Drivers\geckodriver64.exe")

    browser = webdriver.Firefox(executable_path=firefoxgeckobdriver)
    return browser


def kaishijixu(browser, shuliang, number):
    try:
        css_selector = "#pageNo-%s > div > div > div > div.reader-txt-layer > div" % (str(shuliang))
        page_dic = browser.find_element_by_css_selector(css_selector)
        page_dict[shuliang] = page_dic.text.strip()
        print(page_dic.text.strip())
        print("----------------------------------------------------------------->以上是第 %s 页的内容" % shuliang)
    except:
        scrollto = "window.scrollTo(0,%s)" % (500 * int(number))
        browser.execute_script(scrollto)
        kaishijixu(browser, shuliang, number + 1)
        if number >= 50:
            sys.exit(-1)


link = "https://wenku.baidu.com/view/db0103316fdb6f1aff00bed5b9f3f90f76c64d07.html"
browser = firefox_browser()
browser.maximize_window()
browser.get(link)
browser.implicitly_wait(5)
page_dict = {}
for shuliang in range(1, 22):
    kaishijixu(browser, shuliang, 1)
