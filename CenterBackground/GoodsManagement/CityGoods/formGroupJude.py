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
@file: formGroupJude.py
@time: 2018/8/6 14:34
@desc:
'''
import operator
from tools import StringCutting
from tools.operationSelector import OperationSelector
from CenterBackground.GoodsManagement.CityGoods.conditionsJude import ConditionsJude


class FormGroupJude(ConditionsJude):
    MODEL_WORKBOOK_CITY = '筛选'

    def __init__(self):
        ConditionsJude.__init__(self)

    def get_statusSelect(self):
        OperationSelector(self.driver,self.financial_path)

