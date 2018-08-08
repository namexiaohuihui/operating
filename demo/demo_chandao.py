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
@file: demo_chandao.py
@time: 2018/8/8 10:14
@desc:
'''
import os
import time
import pprint
import requests
import threading
from bs4 import BeautifulSoup
from multiprocessing import cpu_count, Process, Queue
from tools.browser_establish import browser_confirm
from tools import StringCutting


def traverseYield(thead_tr, tbody_class):
    for tr in tbody_class:
        tbody_tr = {}
        tr_td = tr.find_all('td')
        for tr_len in range(len(thead_tr)):
            if tr_len == len(thead_tr) - 1:
                td_text = ' '.join([str.strip(a_text.text) for a_text in tr_td[11].find_all('button')])
            else:
                td_text = str.strip(tr_td[tr_len].text)
            tbody_tr[thead_tr[tr_len]] = td_text
        yield tbody_tr


def execute(chandao_text):
    soup = BeautifulSoup(chandao_text, "html.parser")

    thead_th = soup.find('tr', class_='success').find_all('th')
    thead_tr = []
    for th in thead_th:
        text = str.strip(th.text)
        thead_tr.append(text)

    pprint.pprint(thead_tr)

    tbody_class = soup.find('tbody').find_all('tr')

    tr_yield = traverseYield(thead_tr, tbody_class)
    for text in tr_yield:
        tbody_list.append(text)


def main():
    queue = [i for i in range(1, 4)]  # 构造 url 链接 页码。

    for qe in queue:
        url3 = url2 + '{}'.format(qe)
        driver.get(url3)
        chandao_text = driver.page_source
        thread = threading.Thread(target=execute, args=(chandao_text,))
        thread.setDaemon(True)
        thread.start()
        threads.append(thread)


url = '---'
url2 = '{}/**'.format(url)
driver = browser_confirm().url_opens(url)

time.sleep(1)
driver.find_element_by_name('username').send_keys('yangfang')
driver.find_element_by_name('password').send_keys('123456')
driver.find_element_by_id('loginBtn').click()
time.sleep(1)
threads = []
tbody_list = []
main()
for th in threads:
    th.join()

print(len(tbody_list))
pprint.pprint(tbody_list)
