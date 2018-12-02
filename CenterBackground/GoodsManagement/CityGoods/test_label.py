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
@time: 2018/8/10 18:05
@desc:
'''
import os
import inspect
import unittest
from CenterBackground import GoodsManagement
from tools.excelname.Center.gongsMana import CityGoodsPage
from CenterBackground.GoodsManagement.CityGoods.labelJude import LabelJude


class TestGoodsLabel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename

        # 传入子集的key，以及Excel文档中的sheet名字
        config = GoodsManagement.add_key(GoodsManagement.citys, GoodsManagement.label)
        cls.label = LabelJude(config, cls.basename, CityGoodsPage)
        pass

    def setUp(self):
        # 获取运行文件的类名
        self.label.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.label.openingProgram()
        self.label._rou_background()

    def tearDown(self):
        self.label.driver.quit()
        self.label.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_table_hover(self):
        self.label.setFunctionName(inspect.stack()[0][3])
        self.label.get_table_hover()
        pass

    def test_success(self):
        self.label.setFunctionName(inspect.stack()[0][3])
        self.label.get_success_execute()
        pass

    def test_table_bordered(self):
        self.label.setFunctionName(inspect.stack()[0][3])
        self.label.get_execute()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
