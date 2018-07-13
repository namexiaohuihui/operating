# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: web_phone.py
@time: 2018/1/19 17:11
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
overall_ExcelData = ap._excel_Data(filename="exclusiveServiceFile",SHEETNAME =1)
lpn = letter_parameter_names()
print("Use case acquisition completion : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

class verify_phone(unittest.TestCase):
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

    def phone_entrance(self):
        log.info("%s Function starts to execute " % self.overall[lpn.whole_scene])

        # 2.点击手机号对象
        ap._visible_css_selectop(".user-sidebar>li:nth-child(4)")

    def verify_phone_sendk(self):

        # 统一路径
        self.phone_entrance()

        # 3.输入验证码不符合条件纯数字的验证码后提交
        ap._sendKeys_css_selectop("input[id='J_code'][class='u-txt-nob']", self.overall["输入"])
        ap._visible_css_selectop(".J_btn.u-btn")
        ap.sleep_Rest()
        content = ap._visible_css_selectop_text(".toast-cont")
        self.assertNotEqual(self.overall["输出"], content, self.overall[lpn.whole_scene])

        # 4.点击返回回到个人资料页面
        ap.driver.back()


    def test_look_phone(self):
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        # 统一路径
        self.phone_entrance()

        # 3.验收修改号码页面倒计时
        content = ap._visible_css_selectop_text(lpn.phone_verify_from)
        self.assertGreaterEqual(self.overall[lpn.whole_output()],int(content),self.overall[lpn.whole_scene])

        # 4.点击返回回到个人资料页面
        ap.driver.back()


    def test_verify_phone(self):
        # 实现进入修改手机页面不输入验证码之后提交
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        self.verify_phone_sendk()  # 统一执行输入和提示信息的验证


    def test_verify_number(self):
        # 实现进入修改手机页面不获取验证码直接输入纯数字作为验证码
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)  # 读取用例

        self.verify_phone_sendk()  # 统一执行输入和提示信息的验证

    def test_verify_english(self):
        # 实现进入修改手机页面输入纯字母作为验证码
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)  # 读取用例

        self.verify_phone_sendk()  # 统一执行输入和提示信息的验证

    def test_verify_string(self):
        # 实现进入修改手机页面输入纯字母作为验证码
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)  # 读取用例

        self.verify_phone_sendk()  # 统一执行输入和提示信息的验证

    def test_code_phone(self):
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        log.info("%s Function starts to execute " % self.overall[lpn.whole_scene])

        # 2.点击手机号对象
        ap._visible_css_selectop(".user-sidebar>li:nth-child(4)")

        # 3.点击获取验证码
        ap._visible_css_selectop("a[id='J_getCode'][class='verify-btn-code']")
        content = ap._visible_css_selectop_text("a[id='J_second'][class='c-ff']")
        assert '120' != content, self.overall[lpn.whole_scene]
        ap.sleep_Rest()

        # 4.点击返回回到个人资料页面
        self.driver.back()
