# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: __init__.py.py
@time: 2017/12/4 22:14
@项目名称:operating
"""

from practical.constant.browser.browser_establish import browser_confirm

def url_op():
    TitleAttention();

    # 1.创建浏览器所在函数的对象
    bc = browser_confirm.__new__(browser_confirm)

    # 2.调用已经规划好的浏览器函数
    browser = bc.url_opens()
    browser.implicitly_wait(10)
    slide = browser.find_element_by_css_selector(".sysMsg.slide")
    slide.click()
    print(slide.text)


    even = browser.find_element_by_css_selector(".m-attention>a[0]")
    print(even.text)
    link = browser.find_element_by_css_selector(".m-attention>a[1]")
    print(link.text)

def TitleAttention():
    print("Verify the existence of 'm-attention' and determine whether the content of the display is accurate.")

url_op()