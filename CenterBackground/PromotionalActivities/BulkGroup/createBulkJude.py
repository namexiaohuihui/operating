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
@file: createBulkJude.py
@time: 2018/8/8 17:40
@desc:
'''
from CenterBackground.PromotionalActivities.BulkGroup.bulkGroupJude import BulkGroupJude
from selenium.webdriver.common.action_chains import ActionChains
import time


class CreateBulkJude(BulkGroupJude):
    MODEL_WORKBOOK_CITY = '创建'

    def __init__(self):
        BulkGroupJude.__init__(self)
        pass

    def click_date(self):
        # 点击添加按钮
        self._visible_css_selectop('.btn.btn-default.btn-sm.modal-btn')
        # 点击输入框，并输入内容
        self.vai.css_input_number(self.driver, '.select2-search__field', '水', 0)
        # 点击下拉框，并选择内容
        self.vai.ac_move_to_element(self.driver, ".select2-results__option")

