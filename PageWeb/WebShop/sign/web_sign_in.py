# -*- coding: utf-8 -*-

"""
@__author__ :70486 
@file: web_sh_sign_in.py
@time: 2017/7/16 16:05
@项目名称:operating
"""
import os
import unittest
from time import sleep

from practical.constant.browser.browser_establish import browser_confirm
from practical.constant.parameter.parameter_data import parameter_content
from practical.operation import selenium_input, selenium_click
from practical.utils.DefinitionError import definition_error

'''
笔记：
unittest.TestCase的使用：
    使用setUpClass时，调用class函数需要传入self：比如：self.url_op(self)
    使用setUp时，则相反不需要传入self
'''


class sign_input(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.basename = os.path.splitext(os.path.basename(__file__))[0]
        self.url_op(self)

    @classmethod
    def tearDownClass(self):
        print(" :The program has completed the use case.")
        # self.browser.close()#关闭浏览器

    def url_op(self):
        bc = browser_confirm.__new__(browser_confirm)

        # 创建浏览器对象
        self.browser = bc.url_opens()

        # 创建参数对象
        self.parame = parameter_content()

    # 密码输入错误的提示
    def test_case01(self):

        try:
            # 定义函数名，供于数据打印
            str = 'test_case01'

            # 错误提示对象
            ele_css_load = '.login-box-msg'

            # 定义需要输入的参数
            account = "***"
            password = "---"

            # 调用公共函数进行数据执行
            self.case_browesr(account, password)

            sleep(5)

            # 这一块先不判断，制作程序是否可以运行的结果
            log_msg = self.browser.find_element_by_css_selector(ele_css_load).text

            assert log_msg == '登陆失败，账号或密码错误', str + 'Login judgment'

            print(str + "执行成功")
        except Exception as msg:
            self.writelog()
            print(str + "错误信息:%s" % msg)

    # 账号输入错误的提示
    def test_case02(self):
        try:
            # 定义函数名，供于数据打印
            str = 'test_case02'

            # 错误提示对象
            ele_css_load = '.login-box-msg'

            # 定义需要输入的参数
            account = "***"
            password = "---"

            # 调用公共函数进行数据执行
            self.case_browesr(account, password)

            sleep(5)

            # 这一块先不判断，制作程序是否可以运行的结果
            log_msg = self.browser.find_element_by_css_selector(ele_css_load).text
            assert log_msg == '登陆失败， 用户不存在', str + 'Login judgment'

            print(str + "执行成功")

        except Exception as  msg:
            self.writelog()
            print(str + "错误信息:%s" % msg)

    # 成功登陆的提示
    def test_case03(self):
        try:
            # 定义函数名，供于数据打印
            str = 'test_case03'

            # 错误提示对象
            ele_css_load = '.content'

            # 定义需要输入的参数
            account = self.parame.return_account()
            password = self.parame.return_password()

            # 调用公共函数进行数据执行
            self.case_browesr(account, password)

            sleep(5)

            # 这一块先不判断，制作程序是否可以运行的结果
            log_msg = self.browser.find_element_by_css_selector(ele_css_load).text.strip()

            #python在字符串中进行拼接只需要一个加号
            assert log_msg == "欢迎您: " + account + " ,登录连你生活管理系统", str + 'Login judgment'

            print(str + "执行成功")

        except Exception as msg:
            self.writelog()
            print(str + "错误信息:%s" % msg)

    def case_browesr(self, account, password):
        try:
            # 往元素中输入
            # 调用公共函数，输入元素名称和需要输入的内容。进行输入
            # 调用公共函数目的：是为了以后更好的排查问题
            # self.browser为浏览器对象
            # username为元素名称对象
            # account为输入框要输入的内容对象
            selenium_input.name_input(self.browser,'username', account)
            selenium_input.name_input(self.browser,'password', password)

            # 点击某个元素
            # 调用公共函数，对元素进行点击
            # 调用公共函数目的：是为了以后更好的排查问题
            # self.browser为浏览器对象
            # #loginBtn为元素的id对象，井号代表id的意思
            selenium_click.css_click(self.browser,'#loginBtn')

        except Exception as msg:
            self.writelog()
            print("错误信息:%s" % msg)

    # 出现错误之后截图以及写入文档中
    def writelog(self):
        # 调用错误类吗，进行错误打印
        de_error = definition_error()
        de_error.erroe_get(self.basename, self.browser)


if __name__ == '__main__':
    unittest.main()
