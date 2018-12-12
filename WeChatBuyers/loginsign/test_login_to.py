# -*- coding: utf-8 -*-
"""
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  -  /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                        `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

               佛祖保佑         永无BUG
@author:  ln_company
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file:  test_login_to.py
@time: 2018/12/12 22:00
@Software: PyCharm
@Site    : 
@desc:
"""
# https://wiki.jenkins.io/display/JENKINS
# https://jenkins.io/
import os

import unittest
import ddt
import time
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions

from WeChatBuyers.loginsign.excel_util import ExcelUtil
from tools.browser_establish import browser_confirm
from tools.Logger import Log
from tools.operation.selenium_click import action_click

ex = ExcelUtil()
ex_data = ex.get_data()

excle_bl = []


@ddt.ddt
class TestUserLogin(unittest.TestCase):
    def mobile_phone_mode(self):
        '''
        谷歌设置手机模式
        Set the Google browser to mobile mode
        :return:
        '''
        from selenium.webdriver.chrome.options import Options
        # 有效的移动设备Galaxy S5.Nexus 5X.Nexus 6P
        # mobile_emulation = {"deviceName": "iPhone 7"}

        mobile_emulation = {
            "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"}

        # mobile_emulation = {"browserName": "IE"}
        options = Options()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        return options

    def chrome_browser(self, url):
        options = self.mobile_phone_mode()
        path_project = os.path.split(os.path.abspath(__file__))[0]
        self.driver = webdriver.Chrome(executable_path=os.path.join(path_project, 'chromedriver.exe'),
                                       options=options)

        self.driver.maximize_window()
        # 输入网址
        self.driver.get(url)
        # 等待网页加载，加载时间为10s，加载完就跳过
        # 隐形等待时间和显性等待时间不同时，默认使用两者之间最大的那个
        self.driver.implicitly_wait(15)

    @classmethod
    def setUpClass(cls):
        # 定义log日志
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.log = Log(executor=cls.basename, classification='buyer')
        # 点击对象
        cls.ele_click = action_click()

    def setUp(self):
        # 打开浏览器
        self.chrome_browser("需要打开的URL")
        # 点击登录按钮
        element = self.ele_click.is_visible_css_selectop(self.driver, "a.head.gotologin")
        TouchActions(self.driver).tap(element).perform()
        self.sleep_rest()

        # 切换到密码输入
        element = self.ele_click.is_visible_css_selectop(self.driver, "div.goto-passbox > a.goto-passlogin")
        TouchActions(self.driver).tap(element).perform()
        self.sleep_rest()

        pass

    def tearDown(self):
        self.driver.quit()
        pass

    @classmethod
    def tearDownClass(cls):
        for row in range(len(excle_bl)):
            ex.write_value(row, excle_bl[row])
            pass
        cls.log.info("数据写入完毕")

    @ddt.data(*ex_data)
    def test_login_me_sign(self, excel_data):
        self.log.info("使用的数据信息为: %s " % excel_data)
        tel, pwd, text_info = excel_data

        # 输入账号
        user_name = self.ele_click.is_visible_id(self.driver, "J_tel")
        user_name.clear()
        user_name.send_keys(tel)
        self.sleep_rest()

        # 输入密码
        user_name = self.ele_click.is_visible_id(self.driver, "J_pwd")
        user_name.clear()
        user_name.send_keys(pwd)
        self.sleep_rest()

        # 点击提交按钮
        element = self.ele_click.is_visible_id(self.driver, "J_login")
        TouchActions(self.driver).tap(element).perform()
        self.sleep_rest()

        # 判断提示信息是否可见,读取text
        user_name = self.ele_click.is_visible_css_selectop(self.driver, ".toast-cont")
        try:
            assert user_name != False, "提示信息没有出现"
            print("有提示语------------------")
            if text_info == user_name.text:
                excle_bl.append("比较成功:%s" % (user_name.text))
                pass
            else:
                excle_bl.append("比较失败:%s-%s" % (text_info, user_name.text))
        except:
            print("没有哟,亲------------------")
            excle_bl.append("没有提示语:%s-%s" % (text_info, "登陆成功"))
        pass

    def sleep_rest(self, rest=1):
        time.sleep(rest)


if __name__ == '__main__':
    unittest.main()
