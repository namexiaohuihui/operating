# -*- coding: utf-8 -*-

# @author:  dingdong
# @license: (C) Copyright 2016-2019, Ding dong online.
# @software: PyCharm
# @file:  yongwu_yisheng.py
# @time: 2019/5/8 10:48
# @Software: PyCharm
# @Site    : 
# @desc:


import os
import time
import sys
import pprint

from threading import Thread
from multiprocessing import cpu_count, Process, Queue
import requests
import pandas as pd
from bs4 import BeautifulSoup

if sys.version_info <= (3, 6):
    from tomorrow import threads
else:
    from tomorrow3 import threads

# 读取当前文件所在的目录
cur_path = os.path.dirname(os.path.realpath(__file__))
save_image = os.path.join(cur_path, "yongwu_image")
save_file = os.path.join(cur_path, "yongwu_file")

# 如果不存在该文件目录就进行创建
if not os.path.exists(save_image): os.mkdir(save_image)
if not os.path.exists(save_file): os.mkdir(save_file)


class YongwuInfo(object):
    def __init__(self):
        self.url = 'http://www.gxhospital.com'
        self.df = pd.DataFrame()
        pass

    def many_get_ul_urls(self, num):
        r = requests.get("%s/depart_zuowuyiyuana0_zhuanjiaj/%s/" % (self.url, num))

        info = r.content

        soup = BeautifulSoup(info, "html.parser")

        adress = soup.select("ul.expert-lists.clearfix")

        ul_li = adress[0].find_all('li')
        return ul_li

    def many_save_info(self, ys_name, ys_info):
        # 程序运行过快,加个时间休息一下
        time.sleep(2)
        r = requests.get("%s/%s" % (self.url, ys_info))

        info = r.content

        info = BeautifulSoup(info, "html.parser")

        info_content = info.find('div', class_="content")

        # 将医生详细信息写入txt文件
        with open(os.path.join(save_file, ys_name + '.txt'), "w+", encoding='utf8') as f:
            f.write(info_content.text)

        return info_content.text

    def many_save_content(self, img_url):
        try:
            # 医生logo
            ys_logo = img_url.find('a').find('img')['src']

            # 医生名字标签
            ys_h2 = img_url.find('h2').find('a')
            ys_name = ys_h2.text

            # 医生科室
            ys_title = img_url.find('h2').find('span').text.strip()

            # 将医生logo保存在本地
            with open(os.path.join(save_image, ys_name + '.jpg'), "wb") as f:
                f.write(requests.get(ys_logo).content)

            # 存储医生info
            ys_info = self.many_save_info(ys_name, ys_h2['href'])

            # 记录医生关键字
            dict_yongwu = {"logo": ys_name + '.jpg', "name": ys_name, "title": ys_title, 'info': ys_info}

            self.df.append(dict_yongwu, ignore_index=True)

            print("(%s)医生写入成功\n" % ys_name)

        except Exception as  e:
            print("(%s)医生写入失败,详细页为(%s),失败原有为(%s)\n" % (ys_name, ys_h2['href'], e))
            pass

    def many_thread(self):

        t1 = time.time()

        for i in range(1, 4):
            ul_urls = self.many_get_ul_urls(i)
            for ul_url in ul_urls:
                self.many_save_content(ul_url)

        t2 = time.time()

        print("总耗时：%.2f 秒" % (t2 - t1))

        self.df.to_csv("yongwu.csv", index=False, encoding="gbk")


if __name__ == '__main__':
    yw_info = YongwuInfo()
    yw_info.many_thread()
