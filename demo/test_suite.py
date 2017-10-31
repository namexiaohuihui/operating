# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: test_suite.py
@time: 2017/7/16 16:28
@项目名称:operating
"""
import inspect
import logging

import sys


class sys111:
    hello = ''
    world = ''
    def xxkk(self0):
        print('1', sys._getframe().f_code.co_name)
        print('2', inspect.stack()[0][3])
if __name__ == '__main__':
    lll = sys111()
    lll.xxkk()