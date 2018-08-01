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
@author: 70486
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file: test_cityTab.py
@time: 2018/7/31 14:03
@desc:
'''
import os
import inspect
import unittest
from CenterBackground.GoodsManagement.CityGoods.conditionsJude import ConditionsJude

cond = ConditionsJude()


class TestCityTab(unittest.TestCase):

    def setUp(self):
        print("setup: 每个用例开始前后执行")
        # 获取运行文件的类名
        basename = os.path.splitext(os.path.basename(__file__))[0]
        # 打开浏览器，定义log日志。读取excle文档数据
        cond.openingProgram(basename, cond.MODEL_WORKBOOK_CITY)
        cond._rou_interaction()

    def tearDown(self):
        cond.driver.quit()
        print("teardown: 每个用例结束后执行")

    def test_active_city(self):
        cond.get_active_city()
        pass

    def test_switch(self):
        print("------------")
        print(os.path.basename(__file__))
        print(os.path.splitext(os.path.basename(__class__.__name__))[0])
        print(os.path.splitext(os.path.basename(__file__))[0])
        print(inspect.stack()[0][3])
        print("------------")
