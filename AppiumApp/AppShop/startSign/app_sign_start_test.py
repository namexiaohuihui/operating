# -*- coding: utf-8 -*-
from time import sleep

__author__ = 'Administrator'
"""
@file: app_sign_start_test.py
@time: 2017/8/30 5:39

http://blog.csdn.net/zhenzhendexiaoer/article/details/77162513
"""

from appium import webdriver

desired_caps={
    'platformName':'Android',
    'deviceName':'64535188:5555',
    'browserVersion':'7.1.1',
    'platfrormVersion':'23',
    'app':'E:\\drivers\\mobileqq_android.apk',
    #包名
    'appPackage':'com.tencent.mobileqq',
    #启动页
    'appActivity':'com.tencent.mobileqq.activity.SplashActivity',
    #com.tencent.mm:id/adj
    'unicodeKeyboard':'True',
    #将键盘隐藏起来
    'resetKeyboard':'True'
}
deriver_app=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(5)

print(deriver_app)