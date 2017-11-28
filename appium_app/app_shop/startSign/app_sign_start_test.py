# -*- coding: utf-8 -*-
from time import sleep

__author__ = 'Administrator'
"""
@file: app_sign_start_test.py
@time: 2017/8/30 5:39
"""

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

print(deriver_app)