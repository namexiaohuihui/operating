# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: app_buyer_sign.py
@time: 2018/1/15 17:35
"""

import unittest

from appium import webdriver


class buyer_sign(unittest.TestCase):
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
    @classmethod
    def setUp(cls):
        cls.start_server(cls)
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

    @classmethod
    def tearDown(self):
        print(self.strr + "qwe")

    def test_one(self):
        print("qw")
        # 	com.android.packageinstaller:id/permission_allow_button
        # com.lianni.delivery:id/edt_account
        # com.lianni.delivery:id/edt_password
        # android.widget.Button
        # driver.sendKeyEvent(66)
        # 权限弹窗的处理
        self.driver.switchTo().alert().accept();

    def start_server(self):
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desired_caps)
        sleep(5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
