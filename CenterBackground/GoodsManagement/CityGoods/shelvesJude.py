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
@file: shelvesJude.py
@time: 2018/8/13 16:12
@desc:
'''
from CenterBackground.GoodsManagement import CityGoods
from CenterBackground.judeVerification import JudgmentVerification
from tools.excelname.Center.gongsMana import CityGoodsPage


class ShelvesJude(JudgmentVerification):

    def __init__(self, config, basename, centerName):
        '''
        :param config: 头文件所在位置
        :param basename: 执行用例的文件名
        :param centerName: 参数定义的类对象
        '''
        JudgmentVerification.__init__(self, config, basename)
        self.bi = centerName()
        pass

    def perform_quit_shelves(self):
        self._visible_css_selectop(self.financial[self.bi.page_add()])
        title_text = self._visible_css_selectop_text(
            # self.financial[self.bi.page_shelves()][self.bi.page_title()])
            self.financial[self.bi.page_title()])
        print("shelves----> %s " % title_text)
        self._visible_css_selectop(
            # self.financial[self.bi.page_shelves()][self.bi.page_quit()])
            self.financial[self.bi.page_quit()])
