# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: wx_sign_start.py
@time: 2017/8/21 21:03
@项目名称:operating
"""
from time import sleep

from appium import webdriver

desired_caps={
    'platformName':'Android',
    'deviceName':'72836533:5555',
    'platfrormVersion':'5.1.1',
    #包名
    'appPackage':'com.tencent.mm',
    #启动页
    'appActivity':'com.tencent.mm.ui.LauncherUI',
    #com.tencent.mm:id/adj
    'unicodeKeyboard':'True',
    #将键盘隐藏起来
    'resetKeyboard':'True'
}
deriver_app=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(5)

el = deriver_app.find_element_by_id("com.tencent.mm:id/cjk")
el.click()

textfields1 = deriver_app.find_element_by_id("com.tencent.mm:id/h2")
textfields1.send_keys("13654789512")

textfields2 = deriver_app.find_element_by_id("com.tencent.mm:id/bhf")
textfields2.click()

textfields3 = deriver_app.find_element_by_id("com.tencent.mm:id/h2")
#textfields3.send_keys("13654789512")
textfields3.set_text("13654789512");

deriver_app.find_element_by_id("com.tencent.mm:id/adj").click()