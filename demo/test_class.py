# -*- coding: utf-8 -*-

__author__ = 'Administrator'
"""
@file: test_class.py
@time: 2017/10/26 11:58
"""
class cc():

    def __init__(self):
        print("你才是大佬....我是定义这个类是默认调用的。。。")


def ftfunc(func):
    def timef(*s, **gs):
        from time import ctime
        from time import sleep
        print("[%s] %s() called" % (ctime(),func.__name__))
        return func(*s, **gs)

    return timef

@ftfunc
def foo(*s, **gs):
    print(s)
    print(gs)



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

def doWaiting():
    print('start waiting:', time.strftime('%H:%M:%S'))
    time.sleep(3)
    print('stop waiting', time.strftime('%H:%M:%S'))


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

if __name__ == '__main__':
    # 创建两个线程
    # https://www.cnblogs.com/smallmars/p/7149507.html
    st = time.time()
    li = []
    for i in xrange(4):
        t = MyThread(foo(), args=(i, i + 1, i + 2))
        li.append(t)
        t.start()

    for t in li:
        t.join()  # 一定要join，不然主线程比子线程跑的快，会拿不到结果
        print(t.get_result())

    et = time.time()
    print(et - st)



