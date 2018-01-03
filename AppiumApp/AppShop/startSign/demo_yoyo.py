# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: demo_yoyo.py
@time: 2017/11/29 10:14
"""
from appium import webdriver

desired_caps = {
  "platformName": "Android",
  "platformVersion": "7.1.1",
  "deviceName": "64535188",
  "appPackage": "com.lianni.delivery",
  "appActivity": ".StartActivity",
  "noReset": 'True'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
