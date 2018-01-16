# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: Web_PersonalData.py
@time: 2018/1/4 22:03
@项目名称:operating
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


class personal_Privacy(unittest.TestCase):
    @classmethod
    def setUp(cls):
        log.info("The program begins to execute. Don't stop me when you start.")

        ap.driver = ap._browser()  # 打开浏览器

        ap.user_login()  # 用户登录

        # 1. 登录完成之后进入个人资料页面
        if ap._visible_css_selectop(".user-head") == False:
            log.info("的呢过了啊哈私房钱微博")
            os._exit(0)

    @classmethod
    def tearDown(self):
        log.info("Make it complete and continue to press it next time...")
        ap.driver.close()

    def qwetest_look_nickname(self):
        # 实现查看昵称之后，点击昵称元素并点击取消昵称弹窗
        function = inspect.stack()[0][3]  # 执行函数的函数名
        overall = overall_ExcelData.loc[function]
        overall["场景"]
        log.info("%s Function starts to execute " % function)

        # 2.获取页面上昵称的数据并进行比较
        sidebarMsg = ap._visible_css_selectop(self.driver, ".sidebar-msg")
        ap.function_content_comparison(overall["验证条件"], sidebarMsg.text, function)

        # 3.点击弹窗并获取弹窗中的数据
        uText = ap._visible_css_selectop_attribute(self.driver, ".u-txt.u-txt-l")
        ap.function_content_comparison(overall["验证条件"], uText, function)

        # 4.点击弹窗中的取消按钮
        ap._visible_css_selectop(self.driver, ".am-dialog-footer>button:nth-child(1)")

        log.info("%s Complete function execution " % function)

    def qwetest_modify_nickname(self):
        # 实现修改昵称
        function = inspect.stack()[0][3]  # 执行函数的函数名
        log.info("%s Function starts to execute " % function)

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

        log.info("%s Complete function execution " % function)

    def qwetest_look_phone(self):
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        log.info("%s Function starts to execute " % function)

        # 2.点击昵称对象
        phone = ap._visible_css_selectop(self.driver, ".user-sidebar>li:nth-child(4)>a>span")

        # 3.验收修改号码页面的数据
        content = ap._visible_css_selectop_text(self.driver, ".verify-form-itme>span:nth-child(2)")

        assert phone.text == content, function

        # 4.点击返回回到个人资料页面
        self.driver.back()

        log.info("%s Complete function execution " % function)

    def qwetest_cancel_exit(self):
        # 实现点击退出之后点击取消弹窗
        function = inspect.stack()[0][3]  # 执行函数的函数名
        log.info("%s Function starts to execute " % function)

        # 2.点击退出按钮
        ap._visible_css_selectop(self.driver, ".user-sidebar>li:last-child")

        # 3.获取退出提示语
        ap._visible_css_selectop_text(self.driver, ".am-dialog-body")

        # 4.点取消退出
        ap._visible_css_selectop(self.driver, ".am-dialog-footer>button:nth-child(1)")

        log.info("%s Complete function execution " % function)

    def qwetest_decide_exit(self):
        # 实现点击退出之后，确定提出
        function = inspect.stack()[0][3]  # 执行函数的函数名
        log.info("%s Function starts to execute " % function)

        # 2.点击退出按钮
        ap._visible_css_selectop(self.driver, ".user-sidebar>li:last-child")

        # 3.获取退出提示语
        ap._visible_css_selectop_text(self.driver, ".am-dialog-body")

        # 4.点确定退出
        ap._visible_css_selectop(self.driver, ".am-dialog-footer>button:last-child")

        # 获取退出之后的判断
        ap._visible_css_selectop_text(self.driver, ".u-btn.u-btn-morange")

        log.info("%s Complete function execution " % function)

    def qwetest_enter_same_password(self):
        # 实现修改密码时，输入相同的密码，提示框的提示
        function = inspect.stack()[0][3]  # 执行函数的函数名
        log.info("%s Function starts to execute " % function)

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

        log.info("%s Complete function execution " % function)

    def test_password_page(self):
        # 实现从修改密码页面返回到个人资料页面

        function = inspect.stack()[0][3]  # 执行函数的函数名
        log.info("%s Function starts to execute " % function)

        # 2.点击修改密码
        ap._visible_css_selectop(".user-sidebar>li:nth-child(6)")

        # 3.点击返回
        ap.driver.back()

        # 4.获取验证信息
        ap._visible_css_selectop_text(".user-sidebar>li:nth-child(6)")

        log.info("%s Complete function execution " % function)


if __name__ == '__main__':
    unittest.main()
