# -*- coding: utf-8 -*-

import re

import selenium.webdriver.support.expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui

__author__ = 'Administrator'
"""
@file: test_class.py
@time: 2017/10/26 11:58
"""

from practical.constant.browser_establish import browser_confirm

class cc():

    def __init__(self):
        print("你才是大佬....我是定义这个类是默认调用的。。。")



from time import ctime
from time import sleep

def ftfunc(func):
    def timef(*s,**gs):
        print ("[%s] %s() called" % (ctime(),func.__name__))
        return func(*s,**gs)
    return timef

@ftfunc
def foo(*s,**gs):
    print(s)
    print(gs)
    foo()
    foo(1)
    foo(1, 2)
    foo(1, 2, 3)
    stu = {'name': 'alam', 'age': 12}
    foo(1, 2,)
from threading import Thread
import time
class Sayhi(Thread):
    # 为线程定义一个函数
    def __init__(self,threadName,delay):
        super().__init__()
        self.threadName = threadName
        self.delay = delay


    def run(self):
        time.sleep(self.delay)
        print("%s: %s" % (self.threadName, time.ctime(time.time())))

if __name__ == '__main__':
    # 创建两个线程
    # https://www.cnblogs.com/smallmars/p/7149507.html
    try:
        t1 = Sayhi("Thread-1", 2,)
        t2 = Sayhi("Thread-2", 1,)
        t1.start()
        t2.start()
        print("zhu")
    except:
        print("Error: unable to start thread")


