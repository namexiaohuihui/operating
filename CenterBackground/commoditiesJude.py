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
@file: commoditiesJude.py
@time: 2018/8/20 16:27
@desc:
'''
from CenterBackground import Commodities
from CenterBackground.judeVerification import JudgmentVerification
from CenterBackground.customTabs import CustomTabs


class CommoditiesJude(JudgmentVerification):
    '''
    二次封装tabs进行判断
    '''
    def __init__(self, config, basename,centerName):
        JudgmentVerification.__init__(self, config, basename)
        self.bi = centerName()
        pass

    def custom_tabs(self):
        try:
            keys = self.overall[self.bi.whole_keys()]
            self.ct = CustomTabs(self.driver, self.financial[keys])
        finally:
            return self.ct

    def active_city(self):
        ov_default = self.overall[self.bi.whole_city()]
        self.custom_tabs().judge_city(ov_default)
        pass

    def active_code(self):
        ov_default = self.overall[self.bi.whole_code()]
        self.custom_tabs().judge_code(ov_default)
        pass

    def already_citys(self, reduce=0):
        self.custom_tabs().judge_citys(reduce=reduce)
        pass

    def already_codes(self, reduce=0):
        self.custom_tabs().judge_codes(reduce=reduce)
        pass

    def switch_city(self, reduce=0):
        self.custom_tabs().judge_source(reduce=reduce)
        pass

    def switch_url(self, reduce=0):
        self.custom_tabs().judge_source_url(reduce=reduce)
        pass

