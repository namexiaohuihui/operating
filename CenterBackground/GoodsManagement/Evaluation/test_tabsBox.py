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
@file: test_tabsBox.py
@time: 2018/8/14 17:40
@desc:
'''
import os
import inspect
import unittest
from CenterBackground.GoodsManagement import Evaluation
from CenterBackground.GoodsManagement.Evaluation.tabsJude import TabsJude

box = TabsJude(Evaluation.tap)


class TestTabsBox(unittest.TestCase):
    def setUp(self):
        # 获取运行文件的类名
        self.basename = os.path.splitext(os.path.basename(__file__))[0]
        print("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        box.openingProgram(self.basename)
        box._rou_background()

    def tearDown(self):
        box.driver.quit()
        print("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    # -------------------------------顶部tabs用例-----------------------------
    def test_tabs_active(self):
        box.setFunctionName(inspect.stack()[0][3])
        box.get_tabs_active()
        pass

    def test_tabs_text(self):
        box.setFunctionName(inspect.stack()[0][3])
        box.get_tabs_text()
        pass

    def test_tabs_switch(self):
        box.setFunctionName(inspect.stack()[0][3])
        box.get_tabs_switch()
        pass

    # -------------------------------顶部box用例-----------------------------
    def test_box_active(self):
        box.setFunctionName(inspect.stack()[0][3])
        box.get_box_active()
        pass

    def test_box_text(self):
        box.setFunctionName(inspect.stack()[0][3])
        box.get_box_text()
        pass

    def test_box_switch(self):
        box.setFunctionName(inspect.stack()[0][3])
        box.get_box_switch()
        pass
