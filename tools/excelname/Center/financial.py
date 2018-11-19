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
@file:      financial.py
@time:      2018/11/15 16:52
@desc:
"""
from tools.excelname.excelBeanName import ExcelTitle


class Financial(ExcelTitle):
    """
    财务元素所在地
    """

    def yaml_start_time(self):
        return 'start_time'

    def yaml_end_time(self):
        return 'end_time'

    def yaml_typeselect(self):
        return 'typeselect'

    def yaml_keyselect(self):
        return 'keyselect'

    def yaml_inputplace(self):
        return 'inputplace'

    def yaml_utypeselect(self):
        return 'utypeselect'

    def yaml_statusselect(self):
        return 'status'

    def yaml_inputtime(self):
        return 'inputtime'

    def yaml_mon_sub(self):
        return 'mon_sub'

    def yaml_mon_search(self):
        return 'mon_search'

    def yaml_mon_export(self):
        return 'mon_export'

    pass
