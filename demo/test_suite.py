# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: test_suite.py
@time: 2017/7/16 16:28
@项目名称:operating
"""
import logging

class sys:
    hello = ''
    world = ''
if __name__ == '__main__':
    sysl = sys()
    print("脚本名：", sysl.argv[0])
    for i in range(1, len(sysl.argv)):
        print("参数", i, sysl.argv[i])
