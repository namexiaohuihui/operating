# -*- coding: utf-8 -*-
import os
from time import sleep

import sys

__author__ = 'Administrator'
"""
@file: browser_into.py
@time: 2017/11/1 15:21
"""

from practical.operation import selenium_input, selenium_click

class browser_get_info(object):


    #　公告登陆类
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


    # 进入的执行路径
    def system_parameter_discount(self):
        self.browser.find_element_by_link_text('系统设置').click()
        sleep(1)
        self.browser.find_element_by_link_text('参数设置').click()
        sleep(1)
        self.browser.find_element_by_link_text('新用户优惠设置').click()


    def writeLog(self):
        basename = os.path.splitext(os.path.basename(__file__))[0]
        print("自己定义的_文件出现错误,名为名=%s" % basename, )
        sleep(2)
        #退出程序
        sys.exit(0)
        #发生异常之后，raise之后的都不执行
        raise