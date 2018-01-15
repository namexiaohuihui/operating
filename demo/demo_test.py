# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: demo_test.py
@time: 2018/1/15 18:07
"""
from threading import Thread
import time
class MyThread(Thread):

    def __init__(self,func,args=()):
        super(MyThread,self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception:
            return None
def foo(a,b,c):
    time.sleep(1)
    return a*2,b*2,c*2

def ding():
    return "qawe"

def dong():
    return "asd"

if __name__ == '__main__':
    # 创建两个线程
    # https://www.cnblogs.com/smallmars/p/7149507.html
    st = time.time()
    li = []
    for i in range(4):
        t = MyThread(foo, args=(i, i + 1, i + 2))
        li.append(t)
        t.start()

    for t in li:
        t.join()  # 一定要join，不然主线程比子线程跑的快，会拿不到结果
        print(t.get_result())

    et = time.time()
    print(et - st)
    ding = MyThread(func=ding)
    dong = MyThread(dong)
    ding.start()
    dong.start()
    ding.join()
    dong.join()
    print(ding.get_result())
    print(dong.get_result())