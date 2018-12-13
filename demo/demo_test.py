# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: demo_test.py
@time: 2018/1/15 18:07
"""
import time
from threading import Thread


class MyThread(Thread):

    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception:
            return None


def foo(a, b, c):
    time.sleep(1)
    return a * 2, b * 2, c * 2


def fii():
    print("qqq")


def ding():
    return "qawe"


def dong():
    return "asd"


def dingdong():
    aa = abdq + 3
    return aa


def get_basename():
    from utils import Log
    import os
    basename = os.path.splitext(os.path.basename(__file__))[0]
    log = Log(basename)
    return log


def homepage(a, b):
    return a + b + 3


if __name__ == '__main__':
    import os

    cur_path = os.path.dirname(os.path.realpath(__file__))

    log_path = os.path.join(os.path.dirname(cur_path), 'logs')
    path = os.path.join(log_path, "qweassdd" + "-screenshot_error.png")
    print(path)
    # st = time.time()
    # from WeChatBuyers.ExclusiveService import AccountPrivacy as ap
    # from practical.utils.RewriteThread import inherit_thread as th
    # funktion = [ap._excel_Data, get_basename]  # 该列表存放需要执行的函数
    #
    # faden = []  # 该列表存放已经开启的线程
    #
    # inhalt = []  # 该列表存放线程中所执行的函数返回值内容
    #
    # for para in funktion:  # 遍历函数开启线程
    #     threads = th(para)
    #     faden.append(threads)
    #     threads.start()
    #
    # for argu in faden:  # 开启的线程中，进行阻塞，当子线程完成之后才继续下一步
    #     argu.join()
    #     inhalt.append(argu.get_result())
    #
    # overall_ExcelData = inhalt[0]  # df转换的数据，方便对excel进行操作
    # et = time.time() - st
    # print(et)
    # print("**************")
    # st = time.time()
    # get_basename()
    # neir = ap._excel_Data()
    # print(neir)
    # et = time.time() - st
    # print(et)
