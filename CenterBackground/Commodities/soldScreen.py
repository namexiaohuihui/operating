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
@author:    ln_company
@license:   (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@Software:  PyCharm
@file:      soldScreen.py
@time:      2018/9/3 11:27
@desc:
'''
from CenterBackground.screeningjude import ScreeningJude


class SoldScreen(ScreeningJude):

    def __init__(self, module, sheet, basename, centerName):
        '''
        定义模块数据信息
        :param module:   元素模块
        :param sheet:   用例标签名
        :param basename:  执行程序的文件名
        '''
        ScreeningJude.__init__(self, module, sheet, basename, centerName)
        pass

    def button_formSub(self, att: str):
        '''
        根据按钮位置来进行点击
        :param att:  按钮所在位置的key值
        :return:
        '''
        attribute = self._visible_returns_selectop(self.financial[self.bi.yaml_iptJ()])
        attribute = attribute[int(self.financial[att]) - 1]
        return attribute
