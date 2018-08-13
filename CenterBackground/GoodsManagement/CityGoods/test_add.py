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
@file: test_add.py
@time: 2018/8/13 16:02
@desc:
'''
import os
import inspect
import unittest
from CenterBackground.GoodsManagement import CityGoods
from CenterBackground.GoodsManagement.CityGoods.shelvesJude import ShelvesJude

# 给ArgumentAdmin.yaml进行使用
shelves = ShelvesJude(CityGoods.shelves)

class TestShelvesGood(unittest.TestCase):
    def setUp(self):
        # 获取运行文件的类名
        self.basename = os.path.splitext(os.path.basename(__file__))[0]
        print("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        shelves.openingProgram(self.basename)
        shelves._rou_background()

    def tearDown(self):
        # shelves.driver.quit()
        print("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_quit_shelves(self):
        shelves.setFunctionName(inspect.stack()[0][3])
        shelves.perform_quit_shelves()
        pass

