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

    def excle_time_zone(self):
        return '时区'
