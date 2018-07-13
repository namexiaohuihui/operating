# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: app_youdu.py
@time: 2018/5/11 10:56
"""
import unittest
from appium import webdriver
class buy_app(unittest.TestCase):
    strr = "qweads11"

    @classmethod
    def setUp(self):
        self.start_server(self)

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
        # self.driver.switchTo().alert().accept();
    def start_server(self):
        print("nihao")
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "7.1.1"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4726/wd/hub',desired_caps)

if __name__ == '__main__':
    unittest.main(verbosity=2)