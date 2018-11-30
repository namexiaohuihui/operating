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
@file:      selectlableverify.py
@time:      2018/9/25 16:52
@desc:
"""
from CenterBackground.screeningjude import ScreeningJude


class SelectLableVerify(ScreeningJude):

    def get_lable_text(self):
        '''
        读取单选框/多选框对象的text
        self.overall存的是用例数据
        self.financial存的是元素对象路径数据
        :return:
        '''
        # 找到页面数据
        obj_lable = self.overall[self.bi.whole_keys()]
        obj_lable = self.financial[obj_lable]
        obj_lable = [la.text.replace(" ", "") for la in self.vac.is_visibles_css_selectop(self.driver, obj_lable)]

        # 读取用户数据
        ov_str = self.overall[self.bi.whole_including()]
        ov_str = ov_str.split(',')

        # 比较两者之间的数据准确性
        msg = 'Obtain all options values incorrectly get_lable_text'
        self.debugging_log(obj_lable, ov_str, msg)
