# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: RewriteThread.py
@time: 2018/1/15 21:25
@项目名称:operating
"""
import os
import time
import sys
from threading import Thread
from multiprocessing import cpu_count, Process, Queue
import requests
from bs4 import BeautifulSoup

if sys.version_info <= (3, 6):
    from tomorrow import threads
else:
    from tomorrow3 import threads


# https://www.cnblogs.com/qualitysong/archive/2011/05/27/2060246.html
class InheritThread(Thread):

    def __init__(self, func, args=()):
        super(InheritThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        if self.args:
            self.result = self.func(self.args)
        else:  # 参数为空时，不传入内容值
            self.result = self.func()
        print("线程工作者 %s " % self.func)

    def get_result(self):
        try:
            # 如果子线程不使用join方法，此处可能会报没有self.result的错误
            return self.result
        except Exception:
            return None

    def ThreadUse(self):
        x.join()  # 在这里统一执行线程等待的方法
        x.start()  # 线程开始


class InheritProcess(Process):
    # 通过并发异步形式执行
    def __init__(self, fun, args=()):
        Process.__init__(self)
        self.func = fun
        self.args = args

    def run(self):
        for link_key, link_value in self.args[0].items():
            print("是否为最后一个", link_key, link_value)
            self.result = self.func(link_key, link_value)


if __name__ == '__main__':
    funktion = [{"func": xxxx, "args": 2}, {"func": yyyy, "args": 3}]
    faden = []  # 该列表存放已经开启的线程
    inhalt = []  # 该列表存放线程中所执行的函数返回值内容

    for para in funktion:  # 遍历函数开启线程
        # th是内置的函数
        th = InheritThread(para['func'], [para['args']])
        th.start()
        faden.append(th)

    for argu in faden:  # 开启的线程中，进行阻塞，当子线程完成之后才继续下一步
        argu.join()
        inhalt.append(argu.get_result())
    print(inhalt)