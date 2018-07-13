# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: web_nickname.py
@time: 2018/1/19 16:51
"""
import inspect
import os
import time
import unittest

from WeChatBuyers import AccountPrivacy as ap
from utils import Log
from WeChatBuyers.ExclusiveService.namebean import letter_parameter_names

print("Start getting use cases : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

basename = os.path.splitext(os.path.basename(__file__))[0]
log = Log(basename)
overall_ExcelData = ap._excel_Data(filename="exclusiveServiceFile", SHEETNAME=1)
lpn = letter_parameter_names()
print("Use case acquisition completion : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))



class verify_nickname(unittest.TestCase):
    @classmethod
    def setUp(cls):
        log.info("The program begins to execute. Don't stop me when you start.")

        ap.driver = ap._browser()  # 打开浏览器

        ap.user_login(action=True)  # 用户登录

        # 1. 登录完成之后进入个人资料页面
        if ap._visible_css_selectop(lpn.exit_head) == False:
            log.info("Log on failed program stopped running")
            os._exit(0)

    @classmethod
    def tearDown(self):
        log.info("Make it complete and continue to press it next time...")
        # 关闭当前浏览器
        # ap.driver.close()
        # 退出当前driver并且关闭所有的相关窗口
        ap.driver.quit()

    def function_overall(self, function):
        self.overall = overall_ExcelData.loc[function]

    def test_look_nickname(self):
        # 实现查看昵称之后，点击昵称元素并点击取消昵称弹窗
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        log.info("%s Function starts to execute " % self.overall[lpn.whole_scene])

        # 2.获取页面上昵称的数据并进行比较
        sidebarMsg = ap._visible_css_selectop(lpn.nickname_msg)
        self.assertNotEqual(self.overall[lpn.whole_verification], sidebarMsg.text, self.overall[lpn.whole_scene])

        # 3.点击弹窗并获取弹窗中的数据
        uText = ap._visible_css_selectop_attribute(lpn.nickname_txt)
        self.assertNotEqual(self.overall[lpn.whole_verification], uText, self.overall[lpn.whole_scene])

        # 4.点击弹窗中的取消按钮
        ap._visible_css_selectop(lpn.dialog_false)

    def test_modify_nickname(self):
        # 实现修改昵称
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        log.info("%s Function starts to execute " % self.overall[lpn.whole_scene])

        # 2.点击昵称
        ap._visible_css_selectop(lpn.nickname_msg)

        # 3.获取弹窗中昵称输入框对象，并输入内容
        ap._sendKeys_css_selectop(lpn.nickname_txt, lpn.whole_output())

        # 4.点击弹窗中的确定按钮
        ap._visible_css_selectop(lpn.dialog_true)

        # 比较页面的最新数据跟输入的内容是否一致
        sidebarMsg = ap._visible_css_selectop(lpn.nickname_msg)

        assert sidebarMsg == lpn.whole_output(), self.overall[lpn.whole_scene]



