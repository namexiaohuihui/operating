# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: web_exit.py
@time: 2018/1/19 17:19
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
overall_ExcelData = ap._excel_Data(filename="exclusiveServiceFile", SHEETNAME=1)

print("Use case acquisition completion : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


class verify_exit(unittest.TestCase):
    @classmethod
    def setUp(cls):
        log.info("The program begins to execute. Don't stop me when you start.")

        ap.driver = ap._browser()  # 打开浏览器

        ap.user_login()  # 用户登录

        # 1. 登录完成之后进入个人资料页面
        if ap._visible_css_selectop(".user-head") == False:
            log.info("Log on failed program stopped running")
            os._exit(0)

    @classmethod
    def tearDown(self):
        ap.driver.close()

    def function_overall(self, function):
        self.overall = overall_ExcelData.loc[function]

    def exit_entrance(self):
        log.info("%s Function starts to execute " % self.overall["场景"])

        # 2.点击退出按钮
        ap._visible_css_selectop(".user-sidebar>li:last-child")

    def test_cancel_exit(self):
        # 实现点击退出之后点击取消弹窗
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        self.exit_entrance()

        # 3.获取退出提示语
        ap._visible_css_selectop_text(".am-dialog-body")

        # 4.点取消退出
        ap._visible_css_selectop(".am-dialog-footer>button:nth-child(1)")

    def test_decide_exit(self):
        # 实现点击退出之后，确定提出
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        self.exit_entrance()

        # 3.获取退出提示语
        ap._visible_css_selectop_text(".am-dialog-body")

        # 4.点确定退出
        ap._visible_css_selectop(".am-dialog-footer>button:last-child")

        # 获取退出之后的判断
        ap._visible_css_selectop_text(".u-btn.u-btn-morange")
