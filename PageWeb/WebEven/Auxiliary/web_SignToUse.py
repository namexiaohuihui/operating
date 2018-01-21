# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: web_SignToUse.py
@time: 2018/1/2 17:40
https://foofish.net/python-decorator.html 装饰器的使用
"""

import unittest
import inspect
import time
import os

from PageWeb.WebEven.ConversionStorage import conversionstorage
from PageWeb.WebEven import AccountPrivacy as ap
from practical.utils.logger import Log

"""
#--------------------读取excel表格数据部分-----------------------------------------
"""
print("Start getting use cases : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

basename = os.path.splitext(os.path.basename(__file__))[0]
log = Log(basename)
overall_ExcelData = ap._excel_Data(filename="auxiliaryFile")
# print(overall_ExcelData)

print("Use case acquisition completion : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

"""
#-----------------函数指定运行的头文件-------------
"""


def modifier_Interface_sliding(func): # 装饰器中调用浏览器和界面滚动
    # Interface_sliding()

    def modifier(*s, **gs):
        print("自动滚动的开始执行 %s() called" % (ctime(), func.__name__))
        # 将线程中的内容进行读取
        ap.driver = ap._browser()
        ap.Interface_sliding()
        return func(*s, **gs)

    return modifier

def modifier_Browser_usage(func): # 装饰器中只调用浏览器对象
    # Interface_sliding()

    def modifier(*s, **gs):
        print("自动滚动的开始执行 %s() called" % (ctime(), func.__name__))
        # 将线程中的内容进行读取
        ap.driver = ap._browser()
        return func(*s, **gs)

    return modifier

class singn_to_use(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # 该类运行时优先调用的函数
        log.info("The program begins to execute. Don't stop me when you start.")

    @classmethod
    def tearDownClass(self):
        # 该类结束时最后调用的函数
        log.info("Make it complete and continue to press it next time...")
        # self.driver.close()
