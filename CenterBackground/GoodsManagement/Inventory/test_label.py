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
@file: test_label.py
@time: 2018/8/14 14:08
@desc:
'''
import os
import inspect
import unittest
from CenterBackground.GoodsManagement import Inventory
from CenterBackground.GoodsManagement.Inventory.inventoryLabelJude import InventoryLabelJude

# 给ArgumentAdmin.yaml进行使用
label = InventoryLabelJude(Inventory.label)


class TestLabel(unittest.TestCase):
    def setUp(self):
        # 获取运行文件的类名
        self.basename = os.path.splitext(os.path.basename(__file__))[0]
        print("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        label.openingProgram(self.basename)
        label._rou_background()

    def tearDown(self):
        # label.driver.quit()
        print("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass


    def test_success(self):
        label.setFunctionName(inspect.stack()[0][3])
        label.get_success_execute()
        pass

    def test_table_bordered(self):
        label.setFunctionName(inspect.stack()[0][3])
        label.get_execute()
        pass
