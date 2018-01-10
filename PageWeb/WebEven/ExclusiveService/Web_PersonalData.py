# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: Web_PersonalData.py
@time: 2018/1/4 22:03
@项目名称:operating
"""
import unittest
from PageWeb.WebEven.ExclusiveService import AccountPrivacy
import os
from practical.utils.logger import Log
from threading import Thread
import time
import inspect

print("你好。我开始获取数据了 %s" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
overall_ExcelData = AccountPrivacy.accountPrivacy_excel_Data() # 获取用例数据

class personal_Privacy(unittest.TestCase):

    @classmethod
    def setUp(cls):
        basename = os.path.splitext(os.path.basename(__file__))[0]

        cls.log = Log(basename)
        cls.log.info("The program begins to execute. Don't stop me when you start.")

        cls.driver = AccountPrivacy.accountPrivacy_browser() # 打开浏览器

        cls.excelData = overall_ExcelData # 获取数据

        AccountPrivacy.accountPrivacy_user_login(cls.driver) # 用户登录

        cls.log.info("open driver time")




    @classmethod
    def tearDown(self):
        self.log.info("Make it complete and continue to press it next time...")
        self.driver.close()


    def qwetest_personal_nickname_one(self):
        # 实现查看昵称之后，点击昵称元素并点击取消昵称弹窗
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.log.info("%s Function starts to execute " % function)
        # 1.进入个人资料页面
        AccountPrivacy.accountPrivacy_visible_css_selectop(self.driver, ".user-head")

        # 2.获取页面上昵称的数据并进行比较
        sidebarMsg = AccountPrivacy.accountPrivacy_visible_css_selectop(self.driver, ".sidebar-msg")
        assert "。。" != sidebarMsg.text, "test_personal_nickname_one"

        # 3.点击弹窗并获取弹窗中的数据
        uText = AccountPrivacy.accountPrivacy_visible_css_selectop_attribute(self.driver, ".u-txt.u-txt-l")
        assert "..." != uText, "test_personal_nickname_one"

        # 4.点击弹窗中的取消按钮
        AccountPrivacy.accountPrivacy_visible_css_selectop(self.driver,".am-dialog-footer>button:nth-child(1)")

        self.log.info("%s Complete function execution " % function)

    def qwetest_personal_nickname_two(self):
        # 实现修改昵称
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.log.info("%s Function starts to execute " % function)

        # 1.进入个人资料页面
        AccountPrivacy.accountPrivacy_visible_css_selectop(self.driver, ".user-head")

        # 2.获取页面上昵称对象
        AccountPrivacy.accountPrivacy_visible_css_selectop(self.driver, ".sidebar-msg")

        # 3.获取弹窗中昵称输入框对象，并输入内容
        content_sendKeys  = time.strftime('%H:%M:%S', time.localtime(time.time()))
        AccountPrivacy.accountPrivacy_sendKeys_css_selectop(self.driver, ".u-txt.u-txt-l",content_sendKeys)

        # 4.点击弹窗中的确定按钮
        AccountPrivacy.accountPrivacy_visible_css_selectop(self.driver, ".am-dialog-footer>button:last-child")

        # 比较页面的最新数据跟输入的内容是否一致
        sidebarMsg = AccountPrivacy.accountPrivacy_visible_css_selectop_text(self.driver, ".sidebar-msg")

        assert sidebarMsg == content_sendKeys, "test_personal_nickname_one"

        self.log.info("%s Complete function execution " % function)

    def qwetest_personal_nickname_there(self):
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.log.info("%s Function starts to execute " % function)

        # 1.进入个人资料页面
        AccountPrivacy.accountPrivacy_visible_css_selectop(self.driver, ".user-head")

        # 2.获取页面上昵称对象
        AccountPrivacy.accountPrivacy_visible_css_selectop(self.driver, ".user-sidebar>li:nth-child(4)>a>span")

        # 3.验收修改号码页面的数据
        _text = AccountPrivacy.accountPrivacy_visible_css_selectop_text(self.driver,
                                                                        ".verify-form-itme>span:nth-child(2)")
        print(_text + " shouji ")
        AccountPrivacy.sleep_Rest(3)

        # 4.点击返回回到个人资料页面
        self.driver.back()

        AccountPrivacy.sleep_Rest(3)

        self.log.info("%s Complete function execution " % function)

    def qwetest_personal_nickname_four(self):
        # 实现点击退出之后点击取消弹窗
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.log.info("%s Function starts to execute " % function)

        # 1.进入个人资料页面
        AccountPrivacy.accountPrivacy_visible_css_selectop(self.driver, ".user-head")

        # 2.点击退出按钮
        AccountPrivacy.accountPrivacy_visible_css_selectop(self.driver, ".user-sidebar>li:last-child")

        # 3.获取退出提示语
        _text = AccountPrivacy.accountPrivacy_visible_css_selectop_text(self.driver, ".am-dialog-body")

        print(_text + " tuichu ")

        AccountPrivacy.sleep_Rest(3)

        # 4.点取消退出
        AccountPrivacy.accountPrivacy_visible_css_selectop(self.driver, ".am-dialog-footer>button:nth-child(1)")

        AccountPrivacy.sleep_Rest(3)

        self.log.info("%s Complete function execution " % function)

    def qwetest_personal_nickname_five(self):
        # 实现点击退出之后，确定提出
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.log.info("%s Function starts to execute " % function)

        # 1.进入个人资料页面
        AccountPrivacy.accountPrivacy_visible_css_selectop(self.driver, ".user-head")

        # 2.点击退出按钮
        AccountPrivacy.accountPrivacy_visible_css_selectop(self.driver, ".user-sidebar>li:last-child")

        # 3.获取退出提示语
        _text = AccountPrivacy.accountPrivacy_visible_css_selectop_text(self.driver, ".am-dialog-body")

        print(_text + " tuichu ")

        AccountPrivacy.sleep_Rest(3)

        # 4.点确定退出
        AccountPrivacy.accountPrivacy_visible_css_selectop(self.driver, ".am-dialog-footer>button:last-child")

        # 获取退出之后的判断
        _text = AccountPrivacy.accountPrivacy_visible_css_selectop_text(self.driver, ".u-btn.u-btn-morange")
        print(_text + " yanzhegnma ")

        AccountPrivacy.sleep_Rest(3)

        self.log.info("%s Complete function execution " % function)

    def qwetest_personal_nickname_five(self):
        # 实现修改密码时，输入相同的密码，提示框的提示
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.log.info("%s Function starts to execute " % function)

        # 1.进入个人资料页面
        AccountPrivacy.accountPrivacy_visible_css_selectop(self.driver, ".user-head")

        # 2.点击修改密码
        AccountPrivacy.accountPrivacy_visible_css_selectop(self.driver, ".user-sidebar>li:nth-child(6)")

        # 3.获取输入密码
        AccountPrivacy.accountPrivacy_sendKeys_css_selectop(self.driver, "#J_oldpwd",'十一个一')
        AccountPrivacy.accountPrivacy_sendKeys_css_selectop(self.driver, "#J_newpwd",'十一个一')
        AccountPrivacy.accountPrivacy_sendKeys_css_selectop(self.driver, "#J_repeatPwd",'十一个一')

        # 4.点击提交
        AccountPrivacy.accountPrivacy_visible_css_selectop(self.driver, ".u-btn.u-btn-morange")

        # 5.获取提示信息
        _text = AccountPrivacy.accountPrivacy_visible_css_selectop_text(self.driver, ".error-msg")
        print(_text + " tuichu ")

        AccountPrivacy.sleep_Rest(3)

        self.log.info("%s Complete function execution " % function)


    def test_personal_nickname_seven(self):
        # 实现从修改密码页面返回到个人资料页面

        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.log.info("%s Function starts to execute " % function)

        # 1.进入个人资料页面
        AccountPrivacy.accountPrivacy_visible_css_selectop(self.driver, ".user-head")

        # 2.点击修改密码
        AccountPrivacy.accountPrivacy_visible_css_selectop(self.driver, ".user-sidebar>li:nth-child(6)")

        # 3.点击返回
        self.driver.back()

        # 4.获取验证信息
        _text = AccountPrivacy.accountPrivacy_visible_css_selectop_text(self.driver, ".user-sidebar>li:nth-child(6)")
        print(_text + " tuichu ")

        AccountPrivacy.sleep_Rest(3)

        self.log.info("%s Complete function execution " % function)

if __name__ == '__main__':
    unittest.main()