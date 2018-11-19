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
@file:      mutuallyJude.py
@time:      2018/11/12 18:07
@desc:
"""
from CenterBackground.surfacejude import SurfaceJude


class MutuallyJude(SurfaceJude):
    """
    td项中最后一个值可以直接获取,不需要进行数据判断
    """

    def traverseYield(self, thead_tr, tbody_class):
        '''
        :param thead_tr:  页面内容标题
        :param tbody_class:  页面内容展示项
        :return:
        '''
        for tr in tbody_class:
            tbody_tr = {}
            thead_length = len(thead_tr)
            for tr_len in range(thead_length):
                tr_td = tr.find_all('td')
                td_text = tr_td[tr_len].text.replace(" ", "").replace("\n", "").replace("\t", "")
                tbody_tr[thead_tr[tr_len]] = td_text
            yield tbody_tr
        pass
