# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: RewriteThread.py
@time: 2018/1/15 21:25
@项目名称:operating
"""
from threading import Thread
class inherit_thread(Thread):

    def __init__(self,func,args=()):
        super(inherit_thread,self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception:
            return None

    def ThreadUse(self):
        x.join() # 在这里统一执行线程等待的方法
        x.start() #线程开始
