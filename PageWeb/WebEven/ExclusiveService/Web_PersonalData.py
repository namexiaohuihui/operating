# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: Web_PersonalData.py
@time: 2018/1/4 22:03
@项目名称:operating
"""
import unittest
from PageWeb.WebEven.ExclusiveService import AccountPrivacy as ap
import os
from practical.utils.logger import Log
from threading import Thread
import time
import inspect

print("你好。我开始获取数据了 %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
overall_ExcelData = ap._excel_Data()  # 获取用例数据


class personal_Privacy(unittest.TestCase):
    @classmethod
    def setUp(cls):
        basename = os.path.splitext(os.path.basename(__file__))[0]

        cls.log = Log(basename)
        cls.log.info("The program begins to execute. Don't stop me when you start.")

        cls.driver = ap._browser()  # 打开浏览器

        cls.excelData = overall_ExcelData  # 获取数据

        ap._user_login(cls.driver)  # 用户登录

        cls.log.info("open driver time")

        # 1. 登录完成之后进入个人资料页面
        ap._visible_css_selectop(cls.driver, ".user-head")

    @classmethod
    def tearDown(self):
        self.log.info("Make it complete and continue to press it next time...")
        self.driver.close()

    def qwetest_look_nickname(self):
        # 实现查看昵称之后，点击昵称元素并点击取消昵称弹窗
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.log.info("%s Function starts to execute " % function)

        # 2.获取页面上昵称的数据并进行比较
        sidebarMsg = ap._visible_css_selectop(self.driver, ".sidebar-msg")
        assert "。。" != sidebarMsg.text, function

        # 3.点击弹窗并获取弹窗中的数据
        uText = ap._visible_css_selectop_attribute(self.driver, ".u-txt.u-txt-l")
        assert "..." != uText, function

        # 4.点击弹窗中的取消按钮
        ap._visible_css_selectop(self.driver, ".am-dialog-footer>button:nth-child(1)")

        self.log.info("%s Complete function execution " % function)

    def qwetest_modify_nickname(self):
        # 实现修改昵称
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.log.info("%s Function starts to execute " % function)

        # 2.点击昵称
        ap._visible_css_selectop(self.driver, ".sidebar-msg")

        # 3.获取弹窗中昵称输入框对象，并输入内容
        content_sendKeys = time.strftime('%H:%M:%S', time.localtime(time.time()))
        ap._sendKeys_css_selectop(self.driver, ".u-txt.u-txt-l", content_sendKeys)

        # 4.点击弹窗中的确定按钮
        ap._visible_css_selectop(self.driver, ".am-dialog-footer>button:last-child")

        # 比较页面的最新数据跟输入的内容是否一致
        sidebarMsg = ap._visible_css_selectop_text(self.driver, ".sidebar-msg")

        assert sidebarMsg == content_sendKeys, function

        self.log.info("%s Complete function execution " % function)

    def qwetest_look_phone(self):
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.log.info("%s Function starts to execute " % function)

        # 2.点击昵称对象
        phone = ap._visible_css_selectop(self.driver, ".user-sidebar>li:nth-child(4)>a>span")

        # 3.验收修改号码页面的数据
        content = ap._visible_css_selectop_text(self.driver, ".verify-form-itme>span:nth-child(2)")

        assert phone.text == content, function

        # 4.点击返回回到个人资料页面
        self.driver.back()

        self.log.info("%s Complete function execution " % function)

    def qwetest_cancel_exit(self):
        # 实现点击退出之后点击取消弹窗
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.log.info("%s Function starts to execute " % function)

        # 2.点击退出按钮
        ap._visible_css_selectop(self.driver, ".user-sidebar>li:last-child")

        # 3.获取退出提示语
        ap._visible_css_selectop_text(self.driver, ".am-dialog-body")

        # 4.点取消退出
        ap._visible_css_selectop(self.driver, ".am-dialog-footer>button:nth-child(1)")

        self.log.info("%s Complete function execution " % function)

    def qwetest_decide_exit(self):
        # 实现点击退出之后，确定提出
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.log.info("%s Function starts to execute " % function)

        # 2.点击退出按钮
        ap._visible_css_selectop(self.driver, ".user-sidebar>li:last-child")

        # 3.获取退出提示语
        ap._visible_css_selectop_text(self.driver, ".am-dialog-body")

        # 4.点确定退出
        ap._visible_css_selectop(self.driver, ".am-dialog-footer>button:last-child")

        # 获取退出之后的判断
        ap._visible_css_selectop_text(self.driver, ".u-btn.u-btn-morange")

        self.log.info("%s Complete function execution " % function)

    def qwetest_enter_same_password(self):
        # 实现修改密码时，输入相同的密码，提示框的提示
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.log.info("%s Function starts to execute " % function)

        # 2.点击修改密码
        ap._visible_css_selectop(self.driver, ".user-sidebar>li:nth-child(6)")

        # 3.获取输入密码
        ap._sendKeys_css_selectop(self.driver, "#J_oldpwd", '十一个一')
        ap._sendKeys_css_selectop(self.driver, "#J_newpwd", '十一个一')
        ap._sendKeys_css_selectop(self.driver, "#J_repeatPwd", '十一个一')

        # 4.点击提交
        ap._visible_css_selectop(self.driver, ".u-btn.u-btn-morange")

        # 5.获取提示信息
        ap._visible_css_selectop_text(self.driver, ".error-msg")

        self.log.info("%s Complete function execution " % function)

    def test_password_page(self):
        # 实现从修改密码页面返回到个人资料页面

        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.log.info("%s Function starts to execute " % function)

        # 2.点击修改密码
        ap._visible_css_selectop(self.driver, ".user-sidebar>li:nth-child(6)")

        # 3.点击返回
        self.driver.back()

        # 4.获取验证信息
        ap._visible_css_selectop_text(self.driver, ".user-sidebar>li:nth-child(6)")

        self.log.info("%s Complete function execution " % function)


if __name__ == '__main__':
    unittest.main()
