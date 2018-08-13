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
@file: shelvesJude.py
@time: 2018/8/13 16:12
@desc:
'''
import time
import operator
from tools import StringCutting
from CenterBackground.GoodsManagement import CityGoods
from CenterBackground.judgmentVerification import JudgmentVerification
from tools.excelname.adminGongsMana import CityGoodsPage


class ShelvesJude(JudgmentVerification):

    def __init__(self, option):
        JudgmentVerification.config_dist = CityGoods.add_key(option)
        JudgmentVerification.__init__(self)
        self.cGoods = CityGoodsPage()
        pass

    def perform_quit_shelves(self):
        self._visible_css_selectop(self.financial[self.cGoods.page_add()])
        title_text = self._visible_css_selectop_text(
            self.financial[self.cGoods.page_shelves()][self.cGoods.page_title()])
        print("shelves----> %s " % title_text)
        self._visible_css_selectop(
            self.financial[self.cGoods.page_shelves()][self.cGoods.page_quit()])
