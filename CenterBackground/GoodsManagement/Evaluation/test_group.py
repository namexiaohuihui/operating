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
@file: test_group.py
@time: 2018/8/14 15:54
@desc:
'''
import unittest
import os
import inspect
from CenterBackground import GoodsManagement
from tools.excelname.Center.gongsMana import CityGoodsPage
from CenterBackground.GoodsManagement.Evaluation.groupJude import GroupJude


class TestGroup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename

        # 传入子集的key，以及Excel文档中的sheet名字
        config = GoodsManagement.add_key(GoodsManagement.evaluation, GoodsManagement.select)
        cls.group = GroupJude(config,cls.basename, CityGoodsPage)

    def setUp(self):
        # 获取运行文件的类名
        self.group.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.group.openingProgram()
        self.group._rou_background()

    def tearDown(self):
        self.group.driver.quit()
        self.group.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    # ------------------quality所对应的用例所在地------------------
    def test_quality(self):
        self.group.setFunctionName(inspect.stack()[0][3])
        self.group.get_quality()
        pass

    def test_qualityDefault(self):
        self.group.setFunctionName(inspect.stack()[0][3])
        self.group.get_qualityDefault()
        pass

    def test_qualityTraversey(self):
        self.group.setFunctionName(inspect.stack()[0][3])
        self.group.get_qualityTraverse()
        pass

    # -------------------conditions所对应的用例所在地------------------
    def test_conditions(self):
        self.group.setFunctionName(inspect.stack()[0][3])
        self.group.get_conditions()
        pass

    def test_condDefault(self):
        self.group.setFunctionName(inspect.stack()[0][3])
        self.group.get_conndDefault()
        pass

    def test_condTraverse(self):
        self.group.setFunctionName(inspect.stack()[0][3])
        self.group.get_conndTraverse()
        pass

    # ---------------------timetype所对应的用例所在地----------------
    def test_timeOrder(self):
        self.group.setFunctionName(inspect.stack()[0][3])
        self.group.get_timeOrder()
        pass

    def test_timeDefault(self):
        self.group.setFunctionName(inspect.stack()[0][3])
        self.group.get_timeDefault()
        pass

    def test_timeTraverse(self):
        self.group.setFunctionName(inspect.stack()[0][3])
        self.group.get_timeTraverse()
        pass

    # ----------------------关键字及按钮的位置----------------------
    def test_conditionsInput(self):
        self.group.setFunctionName(inspect.stack()[0][3])
        self.group.get_conditionsInput()
        pass

    def test_timename(self):
        self.group.setFunctionName(inspect.stack()[0][3])
        self.group.get_timename()
        pass

    def test_button_search(self):
        self.group.setFunctionName(inspect.stack()[0][3])
        self.group.jude_button_search()
        pass

    def test_button_export(self):
        self.group.setFunctionName(inspect.stack()[0][3])
        self.group.jude_button_export()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
