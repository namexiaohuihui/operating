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
@file: commodities.py
@time: 2018/8/20 18:02
@desc:
'''
from tools.excelname.excelBeanName import ExcelTitle


class BundledItems(ExcelTitle):
    def yaml_slot(self):
        return 'slot'

    def yaml_rule(self):
        return 'rule'

    def yaml_water(self):
        return 'water'

    def yaml_platform(self):
        return 'platform'

    def yaml_platformsold(self):
        return 'platformsold'

    def yaml_store(self):
        return 'store'

    def yaml_storesold(self):
        return 'storesold'

    def yaml_watikitype(self):
        return 'watikitype'

    def yaml_formSub(self):
        return 'formSub'

    def yaml_confirm(self):
        return 'confirm'

    def yaml_prompt(self):
        return 'prompt'

    def yaml_ban(self):
        return 'ban'

    def yaml_shielding(self):
        return 'shielding'

    def yaml_remove(self):
        return 'remove'

    def yaml_tabs(self):
        return 'tabs'

    def yaml_source(self):
        return 'source'

    def yaml_iptJ(self):
        return 'iptJ'

    def yaml_paginate(self):
        return 'paginate'
