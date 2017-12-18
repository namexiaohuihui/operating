# -*- coding: utf-8 -*-
import os
from time import sleep

import sys

__author__ = 'Administrator'
"""
@file: browser_into.py
@time: 2017/11/1 15:21
"""

from practical.operation.selenium_input import element_input


class browser_get_info(object):
    # 　公告登陆类
    def case_browesr(self, account, password):
        try:
            # 往元素中输入
            # 调用公共函数，输入元素名称和需要输入的内容。进行输入
            # 调用公共函数目的：是为了以后更好的排查问题
            # self.browser为浏览器对象
            # username为元素名称对象
            # account为输入框要输入的内容对象
            ele_in = element_input()
            ele_in.name_input(self.browser, 'username', account)
            ele_in.name_input(self.browser, 'password', password)

            # 点击某个元素
            # 调用公共函数，对元素进行点击
            # 调用公共函数目的：是为了以后更好的排查问题
            # self.browser为浏览器对象
            # #loginBtn为元素的id对象，井号代表id的意思
            self.browser.execute_script("document.getElementById('loginBtn').click();")

        except Exception as msg:
            self.writelog()
            print("错误信息:%s" % msg)

    def writeLog(self):
        basename = os.path.splitext(os.path.basename(__file__))[0]
        print("自己定义的_文件出现错误,名为名=%s" % basename, )
        sleep(2)
        # 退出程序
        sys.exit(0)
        # 发生异常之后，raise之后的都不执行
        raise
