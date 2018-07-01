# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: RewriteThread.py
@time: 2018/1/15 21:25
@项目名称:operating
"""
import os
import time
from threading import Thread
from multiprocessing import cpu_count, Process, Queue
import requests
from bs4 import BeautifulSoup
from tomorrow import threads


# https://www.cnblogs.com/qualitysong/archive/2011/05/27/2060246.html
class InheritThread(Thread):

    def __init__(self, func, args=()):
        super(InheritThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(self.args)
        print("线程工作者 %s " % self.func)

    def get_result(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
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
            print("是否为最后一个", link_key,link_value)
            self.result = self.func(link_key,link_value)


# 当前脚本所在的目录

cur_path = os.path.dirname(os.path.realpath(__file__))


def single_get_img_urls():
    r = requests.get("http://699pic.com/sousuo-218808-13-1.html")

    fengjing = r.content

    soup = BeautifulSoup(fengjing, "html.parser")

    # 找出所有的标签

    images = soup.find_all(class_="lazy")

    return images


def single_save_img(imgUrl):
    try:

        jpg_rl = imgUrl["data-original"]

        title = imgUrl["title"]

        # print(title)
        # print(jpg_rl)
        # print("")
        # 判断是否有jpg文件夹，不存在创建一个
        save_file = os.path.join(cur_path, "jpg")

        if not os.path.exists(save_file): os.makedirs(save_file)

        with open(os.path.join(save_file, title + '.jpg'), "wb") as f:

            f.write(requests.get(jpg_rl).content)

    except:

        pass


def single_thread():
    t1 = time.time()

    image_ulrs = single_get_img_urls()

    for i in image_ulrs:
        single_save_img(i)

    t2 = time.time()

    print("总耗时：%.2f 秒" % (t2 - t1))


def many_get_img_urls():
    r = requests.get("http://699pic.com/sousuo-218808-13-1.html")

    fengjing = r.content

    soup = BeautifulSoup(fengjing, "html.parser")

    # 找出所有的标签

    images = soup.find_all(class_="lazy")

    return images


@threads(5)
def many_save_img(imgUrl):
    try:

        jpg_rl = imgUrl["data-original"]

        title = imgUrl["title"]

        # print(title)
        # print(jpg_rl)
        # print("")
        # 判断是否有jpg文件夹，不存在创建一个
        save_file = os.path.join(cur_path, "jpgs")

        if not os.path.exists(save_file): os.makedirs(save_file)

        with open(os.path.join(save_file, title + '.jpg'), "wb") as f:

            f.write(requests.get(jpg_rl).content)

    except:

        pass


def many_thread():
    t1 = time.time()

    image_ulrs = many_get_img_urls()

    for i in image_ulrs:
        many_save_img(i)

    t2 = time.time()

    print("总耗时：%.2f 秒" % (t2 - t1))


def xxxx(x):
    return x * 2


def yyyy(y):
    return 3 * y


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
