# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: web_exit.py
@time: 2018/1/19 17:19
"""
import inspect
import os
import time
import unittest

from PageWeb.WebEven import AccountPrivacy as ap
from utils import Log
from PageWeb.WebEven.ExclusiveService.namebean import letter_parameter_names

print("Start getting use cases : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

basename = os.path.splitext(os.path.basename(__file__))[0]
log = Log(basename)
overall_ExcelData = ap._excel_Data(filename="exclusiveServiceFile", SHEETNAME=1)
lpn = letter_parameter_names()
print("Use case acquisition completion : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


class verify_exit(unittest.TestCase):
    @classmethod
    def setUp(cls):
        log.info("The program begins to execute. Don't stop me when you start.")

        ap.driver = ap._browser()  # 打开浏览器

        ap.user_login()  # 用户登录

        # 1. 登录完成之后进入个人资料页面
        if ap._visible_css_selectop(lpn.exit_head) == False:
            log.info("Log on failed program stopped running")
            os._exit(0)

    @classmethod
    def tearDown(self):
        # 关闭当前浏览器
        # ap.driver.close()
        # 退出当前driver并且关闭所有的相关窗口
        ap.driver.quit()

    def function_overall(self, function):
        self.overall = overall_ExcelData.loc[function]

    def exit_entrance(self):
        log.info("%s Function starts to execute " % self.overall[lpn.whole_scene])

        # 2.点击退出按钮
        ap._visible_css_selectop(lpn.exit_sidebar)

    def test_cancel_exit(self):
        # 实现点击退出之后点击取消弹窗
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        self.exit_entrance()

        # 3.获取退出提示语
        ap._visible_css_selectop_text(lpn.exit_dialog_body)

        # 4.点取消退出
        ap._visible_css_selectop(lpn.dialog_false)

    def test_decide_exit(self):
        # 实现点击退出之后，确定提出
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        self.exit_entrance()

        # 3.获取退出提示语
        ap._visible_css_selectop_text(lpn.exit_dialog_body)

        # 4.点确定退出
        ap._visible_css_selectop(lpn.dialog_true)

        # 获取退出之后的判断
        ap._visible_css_selectop_text(lpn.exit_dialog_morange)
