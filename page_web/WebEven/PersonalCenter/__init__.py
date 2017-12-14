# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: __init__.py.py
@time: 2017/12/4 22:14
@项目名称:operating

https://www.cnblogs.com/yoyoketang/p/7942275.html


"""

from practical.constant.browser.browser_establish import browser_confirm


def url_op():
    # 1.创建浏览器所在函数的对象
    bc = browser_confirm.__new__(browser_confirm)

    options = bc.mobile_phone_mode()

    # 2.调用已经规划好的浏览器函数
    driver = bc.url_opens('http', options)
    driver.implicitly_wait(10)
    tt = driver.find_element_by_css_selector('.am-dialog-button')

    import time
    time.sleep(1)

    from selenium.webdriver.common.touch_actions import TouchActions
    TouchActions(driver).tap(tt).perform()

    screen = get_size(driver)
    time.sleep(5)
    print(screen)
    x1 = screen[0]*0.5
    y1 = screen[1]*0.75
    y2 = screen[1]*0.25
    #driver.swipe(driver,x1,y1,x1, y2,100)

    qq = driver.find_element_by_css_selector('.m-cart-cont')
    ww = driver.find_element_by_css_selector('.filter-recommend.cur')
    print(x1,y1)
    TouchActions(driver).scroll_from_element(qq,x1,y1).perform()


def get_size(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x,y)

url_op()
