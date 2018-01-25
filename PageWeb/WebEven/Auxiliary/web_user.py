# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: web_user.py
@time: 2018/1/21 17:26
@Entry Name:operating
"""
import inspect
import os
import time
import unittest

from PageWeb.WebEven import AccountPrivacy as ap
from utils import Log
from PageWeb.WebEven.Auxiliary.namebean import letter_parameter_names
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

class verify_user(unittest.TestCase):
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

        # 切割字符并获取第二份的内容，将数据里面的空格清空
        account = self.overall[lpn.even_account()]

        # 切割字符并获取第二份的内容，将数据里面的空格清空
        password = self.overall[lpn.even_password()]

        return account, password

    def route_path(self,content,message):
        ap._visible_css_selectop(lpn.user_user)
        ap._visible_css_selectop(message)

        ap.sign_switching_logon(content[0], content[1])

    def test_user_sign(self, account=None, password=None):  # 用户sgin
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        funs = self.function_overall(function)
        self.route_path(funs,lpn.registered_head)


    def test_pending_payment(self, account=None, password=None):  # 待付款跳转
        function = inspect.stack()[0][3]  # 执行函数的函数名
        funs = self.function_overall(function)
        self.route_path(funs, lpn.user_payment)


    def test_pending_delivery(self, account=None, password=None):  # 待发货跳转
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        funs = self.function_overall(function)
        self.route_path(funs, lpn.user_delivery)

    def test_distribution(self, account=None, password=None):  # 配送中跳转
        function = inspect.stack()[0][3]  # 执行函数的函数名
        funs = self.function_overall(function)
        self.route_path(funs, lpn.user_distribution)

    def test_be_evaluated(self, account=None, password=None):  # 待评价跳转
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        funs = self.function_overall(user_evaluated)
        self.route_path(funs, lpn.user_distribution)


    def test_red_envelopes(self, account=None, password=None):  # 红包跳转
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        funs = self.function_overall(function)
        self.route_path(funs, lpn.user_envelopes)

    def test_card_coupons(self, account=None, password=None):  # 卡券跳转
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        funs = self.function_overall(function)
        self.route_path(funs, lpn.user_coupons)

    def test_water_ticket(self, account=None, password=None):  # 水票跳转
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        funs = self.function_overall(function)
        self.route_path(funs, lpn.user_ticket)

    def test_address(self, account=None, password=None):  # 地址跳转
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        funs = self.function_overall(function)
        self.route_path(funs, lpn.user_address)
