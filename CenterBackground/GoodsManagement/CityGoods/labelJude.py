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
@file: labelJude.py
@time: 2018/8/10 18:06
@desc:
'''

import operator
from tools import StringCutting
from CenterBackground.GoodsManagement import CityGoods
from CenterBackground.judgmentVerification import JudgmentVerification
from tools.excelname.adminGongsMana import CityGoodsPage


class LabelJude(JudgmentVerification):

    def __init__(self, option):
        JudgmentVerification.config_dist = CityGoods.add_key(option)
        JudgmentVerification.__init__(self)
        self.cGoods = CityGoodsPage()
        pass