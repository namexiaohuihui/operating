# -*- coding: utf-8 -*-

"""
@__author__ :70486 
@file: sign_in.py
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
from practical.constant.url_website.url_data import url_content
from practical.operation import selenium_input
from practical.operation import selenium_click
from practical.CuttingOperation import stringCutting
from practical.Program_exit import exit_os_sys
from practical.constant.browser import browser_establish


class sign_input(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global _browser_  # 定义全局变量
        print("do something before test.Prepare environment.")

        # 创建浏览器所在类的对象
        bc = browser_establish.browser_confirm.__new__(browser_establish.browser_confirm)

        # 创建网址对象
        url = url_content.__new__(url_content)

        # 创建浏览器对象
        _browser_ = bc.chrome_browser()

        # 输入网址
        _browser_.get(url.return_landing())

        # 等待网页加载，加载时间为10s，加载完就跳过
        _browser_.implicitly_wait(10)

        # 验证网址是否正确，如果错误就直接退出程序
        cls.verification(url.return_landing())

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

            print("错误信息:%s" % msg)

    def verification(whole, local='ler', mssg='Web page open failed'):
        number = stringCutting.string_lookup_index(whole, local)
        if number == -1:
            exit_os_sys.sys_information(mssg)

    def get_test(self):
        try:
            # 获取某个元素将其转成对象,获取该元素的text
            tt = _browser_.find_element_by_css_selector('span.user-info').text
            return tt;
        except NoSuchElementException:
            return 'null';


if __name__ == '__main__':
    unittest.main()
