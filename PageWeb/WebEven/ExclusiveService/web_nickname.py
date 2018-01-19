# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: web_nickname.py
@time: 2018/1/19 16:51
"""
import unittest
import inspect
import time
import os

from PageWeb.WebEven import AccountPrivacy as ap
from practical.utils.logger import Log

print("Start getting use cases : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

basename = os.path.splitext(os.path.basename(__file__))[0]
log = Log(basename)
overall_ExcelData = ap._excel_Data(filename="exclusiveServiceFile")

print("Use case acquisition completion : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


class verify_nickname(unittest.TestCase):
    @classmethod
    def setUp(cls):
        log.info("The program begins to execute. Don't stop me when you start.")

        ap.driver = ap._browser()  # 打开浏览器

        ap.user_login(action=True)  # 用户登录

        # 1. 登录完成之后进入个人资料页面
        if ap._visible_css_selectop(".user-head") == False:
            log.info("Log on failed program stopped running")
            os._exit(0)

    @classmethod
    def tearDown(self):
        ap.driver.close()
        log.info("Make it complete and continue to press it next time...")

    def function_overall(self, function):
        self.overall = overall_ExcelData.loc[function]

    def test_look_nickname(self):
        # 实现查看昵称之后，点击昵称元素并点击取消昵称弹窗
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        log.info("%s Function starts to execute " % self.overall["场景"])

        # 2.获取页面上昵称的数据并进行比较
        sidebarMsg = ap._visible_css_selectop(".sidebar-msg")
        ap.function_content_comparison(self.overall["验证条件"], sidebarMsg.text, self.overall["场景"])

        # 3.点击弹窗并获取弹窗中的数据
        uText = ap._visible_css_selectop_attribute(".u-txt.u-txt-l")
        ap.function_content_comparison(self.overall["验证条件"], uText, self.overall["场景"])

        # 4.点击弹窗中的取消按钮
        ap._visible_css_selectop(".am-dialog-footer>button:nth-child(1)")

    def test_modify_nickname(self):
        # 实现修改昵称
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        log.info("%s Function starts to execute " % self.overall["场景"])

        # 2.点击昵称
        ap._visible_css_selectop(".sidebar-msg")

        # 3.获取弹窗中昵称输入框对象，并输入内容
        content_sendKeys = time.strftime('%H:%M:%S', time.localtime(time.time()))
        ap._sendKeys_css_selectop(".u-txt.u-txt-l", content_sendKeys)

        # 4.点击弹窗中的确定按钮
        ap._visible_css_selectop(".am-dialog-footer>button:last-child")

        # 比较页面的最新数据跟输入的内容是否一致
        sidebarMsg = ap._visible_css_selectop_text(".sidebar-msg")

        assert sidebarMsg == content_sendKeys, self.overall["场景"]



