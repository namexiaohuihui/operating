# -*- coding: utf-8 -*-
'''
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  -  /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                        `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

               佛祖保佑         永无BUG
@author:  ln_company
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file: demo_image.py
@time: 2018/8/8 9:29
@desc:
'''

# 当前脚本所在的目录
import os
import time
import sys
import pprint
from threading import Thread
from multiprocessing import cpu_count, Process, Queue
import requests
from bs4 import BeautifulSoup

if sys.version_info <= (3, 6):
    from tomorrow import threads
else:
    from tomorrow3 import threads

# 读取当前文件所在的目录
cur_path = os.path.dirname(os.path.realpath(__file__))
# 判断是否有jpg文件夹，不存在创建一个
save_file = os.path.join(cur_path, "jpg")

if not os.path.exists(save_file): os.makedirs(save_file)

# 判断是否有jpgs文件夹，不存在创建一个
save_files = os.path.join(cur_path, "jpgs")

if not os.path.exists(save_files): os.makedirs(save_files)

# ------------------------------------------不使用线程来爬去数据
def single_get_img_urls():
    r = requests.get("http://699pic.com/sousuo-218808-13-1.html")

    # fengjing = r.text
    fengjing = r.content

    soup = BeautifulSoup(fengjing, "html.parser")

    # 找出所有的标签
    images = soup.find_all(class_="lazy")
    titles = soup.find_all(class_="fl filter-title")
    pprint.pprint(titles)
    for title in titles:
        print(title.text)
    return images


def single_save_img(imgUrl):
    try:
        # 获取标签元素上面的URL
        jpg_rl = imgUrl["data-original"]
        # 获取标签元素上面的title
        title = imgUrl["title"]

        with open(os.path.join(save_file, title + '.jpg'), "wb") as f:
            r = requests.get(jpg_rl)  # 下载图片，之后保存到文件
            print(r)
            print(r.content)
            print('-------------')
            f.write(r.content)

    except:

        pass


def single_thread():
    t1 = time.time()

    image_ulrs = single_get_img_urls()

    # for i in image_ulrs:
    #     single_save_img(i)
    for i in range(5):
        single_save_img(image_ulrs[i])

    t2 = time.time()

    print("总耗时：%.2f 秒" % (t2 - t1))


# ---------------------------------------------使用线程来爬取数据
def many_get_img_urls():
    r = requests.get("http://699pic.com/sousuo-218808-13-1.html")

    fengjing = r.content

    soup = BeautifulSoup(fengjing, "html.parser")

    # 找出所有的标签

    images = soup.find_all(class_="lazy")

    return images


@threads(cpu_count())
def many_save_img(imgUrl):
    try:

        jpg_rl = imgUrl["data-original"]

        title = imgUrl["title"]

        with open(os.path.join(save_files, title + '.jpg'), "wb") as f:

            f.write(requests.get(jpg_rl).content)
    except:

        pass


def many_thread():
    t1 = time.time()

    image_ulrs = many_get_img_urls()

    # for i in image_ulrs:
    #     many_save_img(i)
    for i in range(5):
        many_save_img(image_ulrs[i])

    t2 = time.time()

    print("总耗时：%.2f 秒" % (t2 - t1))


if __name__ == '__main__':
    many_thread()
    # single_thread()
