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
from CenterBackground import GoodsManagement
from tools.excelname.Center.gongsMana import CityGoodsPage
from CenterBackground.GoodsManagement.CityGoods.shelvesJude import ShelvesJude


class TestShelvesGood(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename

        # 传入子集的key，以及Excel文档中的sheet名字
        config = GoodsManagement.add_key(GoodsManagement.citys, GoodsManagement.shelves)
        cls.shelves = ShelvesJude(config, cls.basename, CityGoodsPage)

    def setUp(self):
        # 获取运行文件的类名
        self.shelves.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.shelves.openingProgram()
        self.shelves._rou_background()

    def tearDown(self):
        self.shelves.driver.quit()
        self.shelves.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_quit_shelves(self):
        self.shelves.setFunctionName(inspect.stack()[0][3])
        self.shelves.perform_quit_shelves()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
