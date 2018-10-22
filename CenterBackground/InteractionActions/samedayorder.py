# -*- coding: utf-8 -*-
"""
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
@author:    ln_company
@license:   (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@Software:  PyCharm
@file:      orderButoon.py
@time:      2018/9/25 11:49
@desc:
"""
import time
import threading
from tools import StringCutting
from CenterBackground.surfacejude import SurfaceJude


class SameDayOrder(SurfaceJude):
    INSERTION_SITE = 0

    def __init__(self, config, basename, centerName):
        '''
        定义模块数据信息
        :param module:   元素模块
        :param sheet:   用例标签名
        :param basename:  执行程序的文件名
        :param centerName:  元素所在的类
        '''
        SurfaceJude.__init__(self, config, basename, centerName)
        pass

    def traverseYield(self, thead_tr, tbody_class):
        '''
        页面操作按钮的统计，每个页面的都不一样需要单独尽心编写
        :param thead_tr:  页面内容标题
        :param tbody_class:  页面内容展示项
        :return:
        '''
        for tr in tbody_class:
            tbody_tr = {}
            thead_length = len(thead_tr)
            for tr_len in range(thead_length):
                tr_td = tr.find_all('td')
                # 需要对数据中空格以及分行符进行过滤操作,并把最后一个查看按钮放置在最前面
                if tr_len == thead_length - 1:
                    td_text = [td.text.replace(" ", "").replace("\n", "") for td in tr_td[tr_len].find_all('button')]
                    td_a = tr_td[tr_len].find('a').text.replace(" ", "").replace("\n", "")
                    td_text.insert(self.INSERTION_SITE, td_a)
                    td_text = ' '.join(td_text)

                else:
                    td_text = tr_td[tr_len].text.replace(" ", "").replace("\n", "")

                tbody_tr[thead_tr[tr_len]] = td_text
            yield tbody_tr
        pass

    def surface_execute(self):
        pages = self.info_number()  # 获取into的总数据信息
        if pages:
            self.log.info('There is data that needs to be paged: %s' % pages)

            self.tbody_list = []
            self.threads = []
            thead_tr = self.success_execute()

            queue = [i for i in range(1, pages + 1)]  # 构造 url 链接 页码。
            # 对当前url进行切割
            current = self.driver.current_url
            # current = str.split(current, '?', 1)
            # together = current[1].split('&', 1)

            for qe in range(1, 3):
                # url = current[0] + '?page={}&'.format(qe) + together[1]
                url = current + '?page={}&'.format(qe)
                thread = threading.Thread(target=self.success_tbody, args=(url, thead_tr,))
                thread.setDaemon(True)
                thread.start()
                self.threads.append(thread)
                time.sleep(1)

            for th in self.threads:
                th.join()
                pass
        else:
            self.log.info("label no data !.....")
        pass
