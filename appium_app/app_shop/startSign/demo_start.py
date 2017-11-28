# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: demo_start.py
@time: 2017/11/28 20:57
@项目名称:operating
"""

import os, time, unittest
from selenium import webdriver


PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 设备系统
desired_caps['platformVersion'] = '7.1.1'  # 设备系统版本
desired_caps['deviceName'] = '192.168.1.100:5555'  #  设备名称

desired_caps['app'] = PATH(r"E:\drivers\mobileqq_android.apk")
desired_caps['appPackage'] = 'com.tencent.mobileqq'
desired_caps['appActivity'] = 'com.tencent.mobileqq.activity.LoginActivity'

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
time.sleep(5)