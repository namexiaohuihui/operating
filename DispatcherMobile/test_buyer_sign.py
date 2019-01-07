# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: app_buyer_sign.py
@time: 2018/1/15 17:35
"""

import time
import unittest

from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tools.operation.selenium_input import action_input
from tools.operation.selenium_click import action_click


class test_buyer_sign(unittest.TestCase):
    strr = "qweads11"
    app_package = "com.lianni.delivery.develop"
    # 设置可支持中文输入unicodeKeyboard，有你就会出现code：1的错误
    r"""
    	[error] [MJSONWP] Encountered internal error running command: 
    	Error: Error executing adbExec. Original 
    	error: 'Command 'E\:\\sdk\\platform-tools\\adb.exe -P 5037 -s 192.168.10.148\:5555 
    	install C\:\\Users\\Administrator\\AppData\\Local\\Programs\\appium-desktop\\resources\\app\\node_modules\\appium\\node_modules\\appium-android-ime\\bin\\UnicodeIME-debug.apk' 
    	exited with code 1'; 
    	Stderr: 'adb: failed to install C:\Users\Administrator\AppData\Local\Programs\appium-desktop\resources\app\node_modules\appium\node_modules\appium-android-ime\bin\UnicodeIME-debug.apk: 
    	Failure [INSTALL_FAILED_UPDATE_INCOMPATIBLE: Package io.appium.android.ime signatures do not match the previously installed version; ignoring!]';
    	 Code: '1'
    """
    # 设置输入法为系统默认resetKeyboard
    # desired_caps = {
    #     "platformName": "Android",
    #     "platformVersion": "7.1.1",
    #     "deviceName": "64535188",
    #     "appPackage": app_package,
    #     "appActivity": "com.lianni.delivery.StartActivity",
    #     # "automationName": 'uiautomator2',
    #     "noReset": 'True',
    #     "resetKeyboard": 'True',
    #     "unicodeKeyboard": 'True',
    # }
    # desired_caps = {
    #     "platformName": "Android",
    #     "platformVersion": "8.1.0",
    #     "deviceName": "bba2100",
    #     "appPackage": app_package,
    #     "appActivity": "com.lianni.delivery.StartActivity",
    #     "noReset": True,
    # }
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "6.0.1",
        "deviceName": "be3dd43e",
        "appPackage": app_package,
        "appActivity": "com.lianni.delivery.StartActivity",
        "noReset": True,
    }

    @classmethod
    def setUp(cls):
        cls.a_input = action_input()
        cls.a_click = action_click()

        cls.start_server(cls)
        # desired_caps = {
        #   "platformName": "Android",
        #   "platformVersion": "7.1.1",
        #   "deviceName": "64535188",
        #   "appPackage": "com.lianni.delivery",
        #   "appActivity": ".StartActivity",
        #   "noSign": True,
        #   "resetKeyboard": True
        # }
        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # sleep(5)

    @classmethod
    def tearDown(self):
        print(self.strr + "qwe")

    def test_one(self):
        print("test_one")

    def start_server(self):
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_caps)
        self.driver.implicitly_wait(10)
        time.sleep(5)
        cu_ac = self.driver.current_activity
        if 'LoginActivity' in cu_ac:
            print("进入登录页面")
            self.a_input.id_input(self.driver, self.app_package + ':id/edt_account', '19968049483')
            self.a_input.id_input(self.driver, self.app_package + ':id/edt_password', 'a123456')
            self.driver.press_keycode(66)
            login_button = self.driver.find_element_by_class_name('android.widget.Button')
            self.a_click.touchActions_tap(self.driver, login_button)

        elif 'MainActivity' in cu_ac:
            print("进入菜单页面")
        else:
            print("什么页面都没有进入:%s" % cu_ac)

        login_load = self.a_click.is_visible_id(self.driver, 'com.lianni.delivery.develop:id/txt_weex_hint')
        if login_load:
            print(login_load.text)
            self.driver.tap([(10, 50), (30, 100), (50, 150)])
            pass
        else:
            print("更新提示没有出现跳过滑动")

    def always_allow(self, number=5):
        '''
        权限弹窗--始终允许
        :param number:弹窗判断次数，默认给5次
        :return:
        '''
        for i in range(number):
            loc = ("xpath", "//*[@text='始终允许']")
            try:
                e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except Exception as ex:
                print("权限弹窗处查找出现错误 ---------> {}".format(ex))
                # 出现权限错误时说明找不到弹窗或者找不到相应的路径，故跳出循环节约时间
                break
        else:
            print("权限判断循环没有进入好好看看自己传入的是啥玩意...........")


if __name__ == '__main__':
    unittest.main(verbosity=2)
