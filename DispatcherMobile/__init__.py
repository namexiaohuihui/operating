# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: __init__.py.py
@time: 2018/1/15 17:35
"""
import unittest

from appium import webdriver


strr = "qweads11"
# 设置可支持中文输入unicodeKeyboard
# 设置输入法为系统默认resetKeyboard
desired_caps = {
"platformName": "Android",
"platformVersion": "7.1.1",
"deviceName": "Android Emulator",
"appPackage": "com.lianni.delivery",
"appActivity": ".StartActivity",
"noReset": 'True',
"unicodeKeyboard": 'True',
"resetKeyboard": 'True'
}
# desired_caps = {
#   "platformName": "Android",
#   "platformVersion": "7.1.1",
#   "deviceName": "64535188",
#   "appPackage": "com.lianni.delivery",
#   "appActivity": ".StartActivity",
#   "noSign": True,
#   "unicodeKeyboard": True,
#   "resetKeyboard": True
# }
# self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# sleep(5)




if __name__ == '__main__':
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)