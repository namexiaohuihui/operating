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
@author:    ln_company
@license:   (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@Software:  PyCharm
@file:      soldLable.py
@time:      2018/9/3 14:38
@desc:
'''
from CenterBackground.surfacejude import SurfaceJude


class SoldLable(SurfaceJude):
    def __init__(self, module, sheet, basename, centerName):
        '''
        定义模块数据信息
        :param module:   元素模块
        :param sheet:   用例标签名
        :param basename:  执行程序的文件名
        :param centerName:  元素所在的类
        '''
        SurfaceJude.__init__(self, module, sheet, basename, centerName)
        pass

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
                if tr_len == thead_length - 1:
                    td_text = [str.strip(a_text.text) for a_text in tr_td[tr_len].find_all('button')]
                    td_a = tr_td[tr_len].find('a').text
                    td_text.insert(0, td_a)
                    td_text = ' '.join(td_text)
                else:
                    td_text = str.strip(tr_td[tr_len].text)
                tbody_tr[thead_tr[tr_len]] = td_text
            yield tbody_tr
        pass
