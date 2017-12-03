# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: backups.py
@time: 2017/12/2 21:10
@项目名称:operating
"""

def mobilePhoneMode():
    url = "https://login.m.taobao.com/msg_login.htm?spm=0.0.0.0"
    paths = "E:\drivers\Drivers\chromedriver60-62.exe"
    # 设置成手机模式
    mobile_emulation = {"deviceName": "iPhone 6"}
    options = Options()  # 下拉框的选择
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(executable_path=paths, chrome_options=options)
    driver.get(url)

    driver.find_element_by_id("username").send_keys("yoyoketang")

    # 触摸事件
    el = driver.find_element_by_id('getCheckcode')
    from selenium.webdriver.common.touch_actions import TouchActions
    TouchActions(driver).tap(el).perform()
