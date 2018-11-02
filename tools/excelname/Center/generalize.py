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
@file:      generalize.py
@time:      2018/11/2 15:38
@desc:
"""
from tools.excelname.excelBeanName import ExcelTitle


class Generalize(ExcelTitle):
    def yaml_nav_tabs(self):
        return "nav_tabs"

    def yaml_box_city(self):
        return "box_city"

    def yaml_add_modal(self):
        return "add_modal"

    def yaml_preview_modal(self):
        return "preview_modal"

    def yaml_rules_modal(self):
        return "rules_modal"

    pass
