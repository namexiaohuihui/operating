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
@author:  ln_company
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file:  pre_work.py
@time: 2018/12/23 13:43
@Software: PyCharm
@Site    : 
@desc:
"""
from SimpleProcess.openbrowser import OpenBrowper
from SimpleProcess.Warehouse.communalprocess import CommunalProcess
from tools.screeningdrop import ScreeningDrop


class PreWork(object):
    def __init__(self, muen_i, module_i):
        self.op_br = OpenBrowper()
        self.op_br.open_driver()
        self.comm = CommunalProcess(self.op_br)

        self.comm.warehousing_login()
        self.comm.access_muen_module(muen_i, module_i)
        pass

    def get_object_work(self):
        return self.op_br, self.comm

    def close_quit_driver(self):
        self.op_br.driver.quit()

    def get_option_text(self, label_path):
        screen = ScreeningDrop(self.op_br.driver, label_path, attr='css')
        option_text = screen.getSelectedOptions()
        del screen
        return option_text
        pass
