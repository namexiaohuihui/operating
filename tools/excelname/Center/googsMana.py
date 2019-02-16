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
@file: adminGoongdManagement.py
@time: 2018/8/1 11:31
@desc:
'''
from tools.excelname.excelBeanName import ExcelTitle


class CityGoodsPage(ExcelTitle):
    """
    商品
    """

    def yaml_shelves(self):
        return 'shelves'

    def yaml_title(self):
        return 'title'

    def yaml_quit(self):
        return 'quit'

    def yaml_add(self):
        return 'add'

    def yaml_evaluation(self):
        return 'evaluation'

    def yaml_formSub(self):
        return "formSub"

    def yaml_cityformSub(self):
        return "cityformSub"

    def yaml_quality(self):
        return 'quality'

    def yaml_timeType(self):
        return 'timeType'

    def yaml_timename(self):
        return 'timename'

    def yaml_tabs(self):
        return 'tabs'

    def yaml_box(self):
        return 'box'

    def yaml_through(self):
        return 'through'

    def yaml_ranges(self):
        return 'ranges'

    def yaml_default_to(self):
        return "default_to"

    def yaml_default_name(self):
        return "default_name"

    def yaml_default_repertory(self):
        return "default_repertory"

    def yaml_default_modify(self):
        return "default_modify"

    def yaml_log_to(self):
        return "log_to"

    def yaml_log_name(self):
        return "log_name"

    def yaml_log_remark(self):
        return "log_remark"

    def excle_time_zone(self):
        return '时区'

    def yaml_h1_title(self):
        return 'h1_title'

    def yaml_h2_title(self):
        return 'h2_title'

    def yaml_h3_title(self):
        return 'h3_title'

    def yaml_h4_title(self):
        return 'h4_title'
