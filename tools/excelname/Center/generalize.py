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
    # ---------------------foucs-------------------
    def yaml_tabs(self):
        return "tabs"

    def yaml_city(self):
        return "city"

    def yaml_add_assist(self):
        return "add_assist"

    def yaml_preview_assist(self):
        return "preview_assist"

    def yaml_preview_close(self):
        return "preview_close"

    def yaml_rules_assist(self):
        return "rules_assist"

    def yaml_rules_close(self):
        return "rules_close"

    def yaml_modift_assist(self):
        return "modift_assist"

    def yaml_delect_assist(self):
        return "delect_assist"

    def yaml_cancel_assist(self):
        return "cancel_assist"

    def yaml_determine_assist(self):
        return "determine_assist"

    def yaml_operate(self):
        return "operate"

    def yaml_modify(self):
        return "modify"

    def yaml_pupop(self):
        return "pupop"

    # -----------------------img---------------------
    def yaml_box_title(self):
        return "box_title"

    def yaml_img(self):
        return "img"

    def yaml_img_save(self):
        return "img_save"

    pass
