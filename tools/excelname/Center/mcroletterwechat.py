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
@file:      mcroletterwechat.py
@time:      2018/11/19 10:45
@desc:
"""
from tools.excelname.excelBeanName import ExcelTitle


class McroLetterWechat(ExcelTitle):
    def yaml_wt_check(self):
        return "wt_check"

    def yaml_amstart(self):
        return "amstart"

    def yaml_amsend(self):
        return "amsend"

    def yaml_pmstart(self):
        return "pmstart"

    def yaml_pmsend(self):
        return "pmsend"

    pass
