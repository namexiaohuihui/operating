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
@file:      sweatingTabs.py
@time:      2018/9/6 18:07
@desc:
"""
from CenterBackground.commoditiesJude import CommoditiesJude


class SweatingTabs(CommoditiesJude):
    def __init__(self, config, basename, centerName):
        CommoditiesJude.__init__(self, config, basename, centerName)
        pass

    def activeBox(self):
        '''
        比较默认的box
        :return:
        '''
        ov_default = self.overall[self.bi.whole_city()]
        self.custom_tabs().judge_city(ov_default)
        pass
