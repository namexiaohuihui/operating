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
@file:      test_collectiveTabs.py
@time:      2018/9/19 16:44
@desc:
"""
import time

start = time.time()
print('1', start)
import os
import inspect
import unittest
from CenterBackground import InteractionActions
from CenterBackground.commoditiesJude import CommoditiesJude
from tools.excelname.Center.Interaction import InteractionController

print('2', time.time() - start)
basename = os.path.splitext(os.path.basename(__file__))[0]
# 传入子集的key，以及Excel文档中的sheet名字
config = InteractionActions.add_key(InteractionActions.collective, InteractionActions.city)
cust = CommoditiesJude(config, basename, InteractionController)

print('3', time.time() - start)
print("--------------")
print(config)
print(cust)
print("--------------")


class TestCollectiveTabs(unittest.TestCase):
    # 定义头部button中，后面2位不需要
    BUTTON_REDUCE_NUMBER = 0

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        cust.openingProgram()
        cust._rou_background()
        print('4', time.time() - start)
        print("%s ---setup: 每个用例开始前后执行" % basename)

    def tearDown(self):
        cust.driver.quit()
        print("%s ---teardown: 每个用例结束后执行" % basename)
        print('6', time.time() - start)
        pass

    def test_active_tab(self):
        cust.setFunctionName(inspect.stack()[0][3])
        cust.active_city('class')
        print('5', time.time() - start)
        pass

    def test_already_tabs(self):
        cust.setFunctionName(inspect.stack()[0][3])
        cust.already_citys(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_tab(self):
        cust.setFunctionName(inspect.stack()[0][3])
        cust.switch_city(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_url(self):
        cust.setFunctionName(inspect.stack()[0][3])
        cust.switch_url('class', reduce=self.BUTTON_REDUCE_NUMBER)
        pass
