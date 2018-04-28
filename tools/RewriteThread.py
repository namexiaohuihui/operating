# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: RewriteThread.py
@time: 2018/1/15 21:25
@项目名称:operating
"""
from threading import Thread

from bs4 import BeautifulSoup

import requests

import os

import time

from tomorrow import threads

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



        with open(os.path.join(save_file, title+'.jpg'), "wb") as f:

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

        with open(os.path.join(save_file, title+'.jpg'), "wb") as f:

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
if __name__ == '__main__':
    many_thread()