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
@file: commoditiesJude.py
@time: 2018/8/20 16:27
@desc:
'''
from CenterBackground import Commodities
from CenterBackground.judeVerification import JudgmentVerification
from tools.excelname.Center.bundledItems import BundledItems


class CommoditiesJude(JudgmentVerification):
    def __init__(self, module, sheet):
        JudgmentVerification.__init__(self, Commodities.add_key(module, sheet))
        self.bi = BundledItems()
        self.driver.find_element_by_tag_name()
