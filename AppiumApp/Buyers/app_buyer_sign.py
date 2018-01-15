# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: app_buyer_sign.py
@time: 2018/1/15 17:35
"""

import unittest
class buyer_sign(unittest.TestCase):
    strr = "qweads11"

    @classmethod
    def setUp(self):
        self.start_server(self)

    @classmethod
    def tearDown(self):
        print(self.strr + "qwe")

    def test_one(self):
        print("qw")

    def start_server(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "7.1.1",
            "deviceName": "Android Emulator",
            "appPackage": "com.lianni.delivery.test",
            "appActivity": "com.lianni.delivery.StartActivity",
            "noReset": 'True',
            "unicodeKeyboard": 'True',  # 设置可支持中文输入
            "resetKeyboard": 'True'  # 设置输入法为系统默认
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(5)


if __name__ == '__main__':
    unittest.main()
