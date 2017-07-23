# -*- coding: utf-8 -*-

"""
@__author__ :70486 
@file: web_sh_sign_in.py
@time: 2017/7/16 16:05
@项目名称:operating
"""
import datetime
import logging
import os
import traceback
import unittest

from selenium.common.exceptions import NoSuchElementException

from practical.constant.parameter.parameter_data import parameter_content
from practical.operation import selenium_input,selenium_click
from practical.constant.browser.browser_establish import browser_confirm


class sign_input(unittest.TestCase):

    def url_op(self):
        global _browser_  # 定义全局变量

        bc = browser_confirm.__new__(browser_confirm)

        # 创建浏览器对象
        _browser_ = bc.url_opens()

    @classmethod
    def setUpClass(cls):
        cls.url_op(cls)

    @classmethod
    def tearDownClass(cls):
        print("do something after test.Clean up.")
        # _browser_.close()#关闭浏览器

    def test_browesr(seft):
        global parame
        # 创建参数对象
        parame = parameter_content.__new__(parameter_content)
        try:
            # 获取参数
            account = parame.return_account()

            # 往元素中输入
            selenium_input.id_input('phone', account)
            selenium_input.id_input('password', parame.return_password())

            # 点击某个元素
            selenium_click.id_click('loginBtn')

            #获取登录成功之后的账号
            title = seft.get_test()

            # 断言判断text是否正确
            assert title == account, 'Logon execution failed'

        except Exception as msg:
            seft.writelog(seft)
            print("错误信息:%s" % msg)

    #获取某个元素的text值，然后返回
    def get_test(self):
        try:
            # 获取某个元素将其转成对象,获取该元素的text
            tt = _browser_.find_element_by_css_selector('span.user-info').text
            return tt;
        except NoSuchElementException:
            return 'null';

    #出现错误之后截图以及写入文档中
    def writelog(self):
        # 组合日志文件名（当前文件名+当前时间）.比如：case_login_success_20150817192533
        basename = os.path.splitext(os.path.basename(__file__))[0]
        logFile = basename + "-" + datetime.datetime.now().strftime("%Y%m%d %H%M%S") + ".log"

        # 创建文件
        logging.basicConfig(filename=logFile)

        # 获取错误日志并打印
        s = traceback.format_exc()

        # 指定输出类型。。
        logging.error(s)

        # 截图
        _browser_.get_screenshot_as_file("./" + logFile + "-screenshot_error.png")

if __name__ == '__main__':
    unittest.main()
