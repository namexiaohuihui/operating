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
@file: platformSoldTabs.py
@time: 2018/8/20 16:08
@desc:
'''
import os
import inspect
import unittest
from CenterBackground import Commodities
from tools.excelname.Center.bundledItems import BundledItems
from CenterBackground.commoditiesJude import CommoditiesJude


class TestStoreSoldTabs(unittest.TestCase):
    # 定义头部button中，后面不需要button的数量
    BUTTON_REDUCE_NUMBER = 0

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + basename
        config = Commodities.add_key(Commodities.storesold, Commodities.city)
        cls.group = CommoditiesJude(config, basename, BundledItems)

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        self.group.log.debug("%s ---setup: 每个用例开始前后执行" % self.basename)
        self.group.openingProgram()
        self.group._rou_background()
        pass

    def tearDown(self):
        self.group.driver.quit()
        self.group.log.debug("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_active_city(self):
        self.group.setFunctionName(inspect.stack()[0][3])
        self.group.active_city('class')
        pass

    def test_active_code(self):
        self.group.setFunctionName(inspect.stack()[0][3])
        self.group.active_code('class')
        pass

    def test_already_citys(self):
        self.group.setFunctionName(inspect.stack()[0][3])
        self.group.already_citys(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_already_codes(self):
        self.group.setFunctionName(inspect.stack()[0][3])
        self.group.already_codes(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_city(self):
        self.group.setFunctionName(inspect.stack()[0][3])
        self.group.switch_city(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_url(self):
        self.group.setFunctionName(inspect.stack()[0][3])
        self.group.switch_url('class', reduce=self.BUTTON_REDUCE_NUMBER)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
