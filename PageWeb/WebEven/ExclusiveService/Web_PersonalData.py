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
    self.overall = ''
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
        log.info("Make it complete and continue to press it next time... %s" % self.overall["场景"])
        ap.driver.close()

    def function_overall(self,function):
        self.overall = overall_ExcelData.loc[function]

    def verify_phone_sendk(self):
        log.info("%s Function starts to execute " % self.overall["场景"])

        # 2.点击手机号对象
        ap._visible_css_selectop(".user-sidebar>li:nth-child(4)")

        # 3.输入验证码不符合条件纯数字的验证码后提交
        ap._sendKeys_css_selectop("input[id='J_code'][class='u-txt-nob']", self.overall["输入"])
        ap._visible_css_selectop(".J_btn.u-btn")
        ap.sleep_Rest()
        content = ap._visible_css_selectop_text(".toast-cont")
        assert self.overall["输出"] >= content, self.overall["场景"]

        # 4.点击返回回到个人资料页面
        ap.driver.back()

    def verify_password_sendk(self,action =False,*content):
        """
        修改密码页面判断是否要输入密码，以及不输入时的情况
        :param action:  验证是否要输入信息
        :param content: 存储需要输入的信息
        :return:
        """
        log.info("%s Function starts to execute " % self.overall["场景"])

        # 2.点击修改密码
        ap._visible_css_selectop(".user-sidebar>li:nth-child(6)")

        # 3.判断是不是要执行输入程序
        if action:
            if len(content) == 3:
                # 3.获取输入信息
                ap._sendKeys_css_selectop("#J_oldpwd", content[0])
                ap._sendKeys_css_selectop("#J_newpwd", content[1])
                ap._sendKeys_css_selectop("#J_repeatPwd", content[2])

            # 3.点击提交
            ap._visible_css_selectop(".u-btn.u-btn-morange")


        # 4.获取提示信息
        msg_text = ap._visible_css_selectop_text(".error-msg")
        ap.function_content_comparison(self.overall["输出"], msg_text, self.overall["场景"])
        ap.sleep_Rest()

        # 5.获取返回上一页之后的验证信息
        ap.driver.back()
        ap._visible_css_selectop_text(".user-sidebar>li:nth-child(6)")

    def test_look_nickname(self):
        # 实现查看昵称之后，点击昵称元素并点击取消昵称弹窗
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        log.info("%s Function starts to execute " % overall["场景"])

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


    def test_look_phone(self):
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        log.info("%s Function starts to execute " % self.overall["场景"])

        # 2.点击昵称对象
        phone = ap._visible_css_selectop(".user-sidebar>li:nth-child(4)>a>span")

        # 3.验收修改号码页面的数据
        content = ap._visible_css_selectop_text(".verify-form-itme>span:nth-child(2)")

        assert phone.text == content, self.overall["场景"]

        # 4.点击返回回到个人资料页面
        self.driver.back()


    def test_cancel_exit(self):
        # 实现点击退出之后点击取消弹窗
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        log.info("%s Function starts to execute " % self.overall["场景"])

        # 2.点击退出按钮
        ap._visible_css_selectop(".user-sidebar>li:last-child")

        # 3.获取退出提示语
        ap._visible_css_selectop_text(".am-dialog-body")

        # 4.点取消退出
        ap._visible_css_selectop(".am-dialog-footer>button:nth-child(1)")


    def test_decide_exit(self):
        # 实现点击退出之后，确定提出
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        log.info("%s Function starts to execute " % self.overall["场景"])

        # 2.点击退出按钮
        ap._visible_css_selectop(".user-sidebar>li:last-child")

        # 3.获取退出提示语
        ap._visible_css_selectop_text(".am-dialog-body")

        # 4.点确定退出
        ap._visible_css_selectop(".am-dialog-footer>button:last-child")

        # 获取退出之后的判断
        ap._visible_css_selectop_text(".u-btn.u-btn-morange")


    def test_enter_same_password(self):
        # 实现修改密码时，输入相同的密码，提示框的提示
        # 实现修改密码时，输入相同的密码，提示框的提示
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        string = STR_ILOC["输入"].split(',')  # 获取登录账号密码
        oldpwd = string[0].split(':')[1].strip()  # 切割字符并获取第二份的内容，将数据里面的空格清空
        newpwd = string[1].split(':')[1].strip()  # 切割字符并获取第二份的内容，将数据里面的空格清空
        repeatPwd = string[2].split(':')[1].strip()  # 切割字符并获取第二份的内容，将数据里面的空格清空

        inString = [oldpwd, newpwd, repeatPwd]
        self.verify_password_sendk(action=True, content=inString)

    def test_password_page(self):
        # 实现从修改密码页面返回到个人资料页面

        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        self.verify_password_sendk(content=None)



    def test_code_phone(self):
        # 实现进入修改手机页面获取验证码
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        log.info("%s Function starts to execute " % self.overall["场景"])

        # 2.点击手机号对象
        ap._visible_css_selectop(".user-sidebar>li:nth-child(4)")

        # 3.点击获取验证码
        ap._visible_css_selectop("a[id='J_getCode'][class='verify-btn-code']")
        content = ap._visible_css_selectop_text("a[id='J_second'][class='c-ff']")
        assert '120' >= content, self.overall["场景"]
        ap.sleep_Rest()


        # 4.点击返回回到个人资料页面
        self.driver.back()


    def test_verify_phone(self):
        # 实现进入修改手机页面不输入验证码之后提交
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        self.verify_phone_sendk()  # 统一执行输入和提示信息的验证


    def test_verify_number(self):
        # 实现进入修改手机页面不获取验证码直接输入纯数字作为验证码
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function) # 读取用例

        self.verify_phone_sendk() # 统一执行输入和提示信息的验证


    def test_verify_english(self):
        # 实现进入修改手机页面输入纯字母作为验证码
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function) # 读取用例

        self.verify_phone_sendk() # 统一执行输入和提示信息的验证

    def test_verify_string(self):
        # 实现进入修改手机页面输入纯字母作为验证码
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)  # 读取用例

        self.verify_phone_sendk()  # 统一执行输入和提示信息的验证

    def test_none_password(self):
        # 实现修改密码时，不输入密码
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        self.verify_password_sendk(action=True, content=None)


    def test_verify_password_len(self):
        # 实现修改密码时，新密码长度不符合
        function = inspect.stack()[0][3]  # 执行函数的函数名
        self.function_overall(function)

        string = STR_ILOC["输入"].split(',')  # 获取登录账号密码
        oldpwd = string[0].split(':')[1].strip()  # 切割字符并获取第二份的内容，将数据里面的空格清空
        newpwd = string[1].split(':')[1].strip()  # 切割字符并获取第二份的内容，将数据里面的空格清空
        repeatPwd = string[2].split(':')[1].strip()  # 切割字符并获取第二份的内容，将数据里面的空格清空

        inString = [oldpwd,newpwd,repeatPwd]
        self.verify_password_sendk(action=True, content=inString)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(personal_Privacy("test_password_page"))
    # suite.addTest(demounit("testTwo"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # unittest.main()
