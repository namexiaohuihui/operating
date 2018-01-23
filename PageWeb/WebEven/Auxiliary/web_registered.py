# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: web_registered.py
@time: 2018/1/21 17:35
@Entry Name:operating
"""

import unittest
import inspect
import time
import os

from PageWeb.WebEven.ConversionStorage import conversionstorage
from PageWeb.WebEven import AccountPrivacy as ap
from practical.utils.logger import Log


"""
#--------------------读取excel表格数据部分-----------------------------------------
"""
print("Start getting use cases : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

basename = os.path.splitext(os.path.basename(__file__))[0]
log = Log(basename)
overall_ExcelData = ap._excel_Data(filename="auxiliaryFile",SHEETNAME=6)

print("Use case acquisition completion : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

class verify_registered(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # 该类运行时优先调用的函数
        log.info("The program begins to execute. Don't stop me when you start.")

        ap.driver = ap._browser()  # 打开浏览器

    @classmethod
    def tearDownClass(self):
        # 该类结束时最后调用的函数
        log.info("Make it complete and continue to press it next time...")
        ap.driver.close()

    def function_overall(self, function):
        self.overall = overall_ExcelData.loc[function]

    def test_protocol(self):  # 注册页面点击内容
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        ap._visible_css_selectop(".nav-user")
        ap._visible_css_selectop(".user-head")
        ap._visible_css_selectop('.login-type>a:nth-child(2)')  # 切换注册
        ap._visible_json_click('J_protocol')

        message = ap._visible_css_selectop_text(".over-box")
        # 储存登陆之后的提示
        conversionstorage().set_remarks(message)

        ap._visible_css_selectop('.close')

    def test_privacy(self):  # 注册页面点击内容
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        ap._visible_css_selectop(".nav-user")
        ap._visible_css_selectop(".user-head")
        ap._visible_css_selectop('.login-type>a:nth-child(2)')  # 切换注册
        ap.driver.execute_script("document.getElementById('J_privacy').click();")
        ap._visible_json_click('J_privacy')

        message = ap._visible_css_selectop_text(".over-box")
        # 储存登陆之后的提示
        conversionstorage().set_remarks(message)

        ap._visible_css_selectop('.close')

    def test_message_tip(self):  # 注册页面点击内容
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        ap._visible_css_selectop(".nav-user")
        ap._visible_css_selectop(".user-head")
        ap._visible_css_selectop('.login-type>a:nth-child(2)')  # 切换注册

        message = ap._visible_css_selectop_text(".message-tip")
        # 储存登陆之后的提示
        conversionstorage().set_remarks(message)