# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: web_password.py
@time: 2018/1/19 17:21
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



class verify_password(unittest.TestCase):
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

    def password_entrance(self):
        log.info("%s Function starts to execute " % self.overall[lpn.whole_scene])

        # 2.点击修改密码
        ap._visible_css_selectop(lpn.password_sidebar)

    def password_after(self):
        # 4.获取提示信息
        msg_text = ap._visible_css_selectop_text(lpn.password_error_msg)
        self.assertNotEqual(self.overall[lpn.whole_output()], msg_text, self.overall[lpn.whole_scene])
        ap.sleep_Rest()


        # 5.获取返回上一页之后的验证信息
        ap.driver.back()

    def verify_password_sendkey(self, *content):
        """
        修改密码页面判断是否要输入密码，以及不输入时的情况
        :param action:  验证是否要输入信息
        :param content: 存储需要输入的信息
        :return:
        """
        self.password_entrance()

        # 3.获取输入信息
        ap._visible_json_input(lpn.password_oldpwd, content[0])
        ap._visible_json_input(lpn.password_newpwd, content[1])
        ap._visible_json_input(lpn.password_repeatPwd, content[2])
        self.password_after()

    def password_sendkey(self):
        oldpwd = sself.overall[lpn.password_past()]  # 切割字符并获取第二份的内容，将数据里面的空格清空
        newpwd = self.overall[lpn.password_establish()]  # 切割字符并获取第二份的内容，将数据里面的空格清空
        repeatPwd = self.overall[lpn.password_confirm()]  # 切割字符并获取第二份的内容，将数据里面的空格清空

        inString = [oldpwd, newpwd, repeatPwd]
        self.verify_password_sendkey(content=inString)

    def verify_password_none(self):
        self.password_entrance()
        # 3.点击提交
        ap._visible_css_selectop(lpn.password_morange)
        self.password_after()

    def test_none_password(self):
        # 实现修改密码时，不输入密码
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)
        self.verify_password_sendkey(content=None)

    def test_verify_password_len(self):
        # 实现修改密码时，新密码长度不符合
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)
        self.password_sendkey()

    def test_enter_same_password(self):
        # 实现修改密码时，输入相同的密码，提示框的提示
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)
        self.password_sendkey()
