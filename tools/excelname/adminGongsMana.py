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
    def excle_name(self):
        return '城市'

    def excle_code(self):
        return '编码'

    def excle_including(self):
        return '全部'

    def excle_default(self):
        return '默认'

    def yaml_obj(self):
        return 'obj'

    def yaml_city_tab(self):
        return 'citytab'

    def yaml_label(self):
        return 'label'

    def yaml_active(self):
        return 'active'

    def yaml_formGroup(self):
        return 'formGroup'

    def yaml_statusV(self):
        return 'statusV'

    def yaml_categoryV(self):
        return 'categoryV'

    def yaml_preferencesV(self):
        return 'preferencesV'

    def yaml_conditionsV(self):
        return 'conditionsV'

    def yaml_searchB(self):
        return 'searchB'

    def yaml_exportB(self):
        return 'exportB'
