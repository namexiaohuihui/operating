# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: demo_yoyo.py
@time: 2017/11/29 10:14
"""
from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': '64535188',
    'platformVersion': '7.1.1',
    # apk包名
    'appPackage': 'com.tencent.mm',
    # apk的launcherActivity
    'appActivity': 'com.tencent.mm.ui.LauncherUI'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
