# -*- coding: utf-8 -*-
import os
import sys

__author__ = 'Administrator'
"""
@file: exit_os_sys.py
@time: 2017/7/17 11:18
"""

#退出时来个提示,一般主程序中使用此退出.
def sys_information(msg):
    sys.exit(msg)

#sys.exit(n) 退出程序引发SystemExit异常
def sys_direct():
    sys.exit(0)

# os._exit(n), 直接退出, 不抛异常, 不执行相关清理工作. 常用在子进程的退出.
def os_direct():
    os._exit(0)


