# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: web_registered.py
@time: 2018/1/21 17:35
@Entry Name:operating
"""

import inspect
import os
import time
import unittest

from WeChatBuyers import AccountPrivacy as ap
from WeChatBuyers.ConversionStorage import conversionstorage
from utils import Log
from WeChatBuyers.Auxiliary.namebean import letter_parameter_names
"""
#--------------------读取excel表格数据部分-----------------------------------------
"""
print("Start getting use cases : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

basename = os.path.splitext(os.path.basename(__file__))[0]
log = Log(basename)
overall_ExcelData = ap._excel_Data(filename="auxiliaryFile", SHEETNAME=4)
# print(overall_ExcelData)
lpn = letter_parameter_names()
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
        # 关闭当前浏览器
        # ap.driver.close()
        # 退出当前driver并且关闭所有的相关窗口
        ap.driver.quit()

    def function_overall(self, function):
        self.overall = overall_ExcelData.loc[function]

    def route_path(self):
        ap._visible_css_selectop(lpn.registered_user)
        ap._visible_css_selectop(lpn.registered_head)
        ap._visible_css_selectop(lpn.registered_login_type)  # 切换注册

    def message_content(self,remarks):
        message = ap._visible_css_selectop_text(remarks)
        # 储存登陆之后的提示
        conversionstorage().set_remarks(message)

    def close_content(self):
        ap._visible_css_selectop(lpn.registered_close)

    def test_protocol(self):  # 注册页面点击内容
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        self.route_path()

        ap._visible_json_click(lpn.registered_protocol) # 协议
        self.message_content(lpn.registered_over_box)
        self.close_content()

    def test_privacy(self):  # 注册页面点击隐私
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        self.route_path()

        ap._visible_json_click(lpn.registered_privacy)  # 协议

        self.message_content(lpn.registered_over_box)

        self.close_content()

    def test_message_tip(self):  # 注册页面页面的优惠
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        self.route_path()

        self.message_content(lpn.registered_message_tip)