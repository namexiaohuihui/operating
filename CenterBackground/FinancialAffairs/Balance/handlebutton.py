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
@file:      handlebutton.py
@time:      2018/11/18 16:20
@desc:
"""
import time
import threading
from tools import StringCutting
from CenterBackground.surfacejude import SurfaceJude


class HandleButton(SurfaceJude):
    # 在最后一个tb标签中,a按钮的位置。
    INSERTION_SITE = 1

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
                len_tr = len(tr_td)
                if len_tr > 2:
                    # 需要对数据中空格以及分行符进行过滤操作,并把最后一个查看按钮放置在最前面
                    if tr_len == thead_length - 1:
                        td_text = [td.text.replace(" ", "").replace("\n", "") for td in
                                   tr_td[tr_len].find_all('button')]
                        td_a = tr_td[tr_len].find('a').text.replace(" ", "").replace("\n", "")
                        td_text.insert(self.INSERTION_SITE, td_a)
                        td_text = ' '.join(td_text)

                    else:
                        td_text = tr_td[tr_len].text.replace(" ", "").replace("\n", "")

                    tbody_tr[thead_tr[tr_len]] = td_text
                else:
                    tbody_tr = "没数据"
            yield tbody_tr
        pass
