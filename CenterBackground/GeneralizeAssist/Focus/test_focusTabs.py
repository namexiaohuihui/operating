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
@file: test_focusTabs.py
@time: 2018/8/20 16:08
@desc:
'''
import os
import inspect

import unittest

from CenterBackground import customTabs
from CenterBackground import GeneralizeAssist
from tools.excelname.Center.generalize import Generalize
from CenterBackground.commoditiesJude import CommoditiesJude


class TestFocusTabs(unittest.TestCase):
    # 定义头部button中，后面2位不需要
    BUTTON_REDUCE_NUMBER = 0

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename

        # 传入子集的key，以及Excel文档中的sheet名字
        config = GeneralizeAssist.add_key(GeneralizeAssist.focus, GeneralizeAssist.city)

        cls.fJude = CommoditiesJude(config, cls.basename, Generalize)

    def setUp(self):
        # 获取运行文件的类名
        self.fJude.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.fJude.openingProgram()
        self.fJude._rou_background()

    def tearDown(self):
        self.fJude.driver.quit()
        self.fJude.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_active_city(self):
        self.fJude.setFunctionName(inspect.stack()[0][3])
        self.fJude.active_city(customTabs._class)
        pass

    def test_active_code(self):
        self.fJude.setFunctionName(inspect.stack()[0][3])
        self.fJude.div_a_city_code(customTabs._class)
        pass

    def test_already_citys(self):
        self.fJude.setFunctionName(inspect.stack()[0][3])
        self.fJude.already_citys(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_already_codes(self):
        self.fJude.setFunctionName(inspect.stack()[0][3])
        self.fJude.div_a_city_codes(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_city(self):
        self.fJude.setFunctionName(inspect.stack()[0][3])
        self.fJude.switch_city(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_url(self):
        self.fJude.setFunctionName(inspect.stack()[0][3])
        self.fJude.switch_url(customTabs._class, reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_active_box(self):
        self.fJude.setFunctionName(inspect.stack()[0][3])
        self.fJude.active_city(customTabs._class)
        pass

    def test_active_all(self):
        self.fJude.setFunctionName(inspect.stack()[0][3])
        self.fJude.already_citys()
        pass

    def test_switch_box(self):
        self.fJude.setFunctionName(inspect.stack()[0][3])
        self.fJude.switch_city()
        pass

    def test_switch_href(self):
        self.fJude.setFunctionName(inspect.stack()[0][3])
        self.fJude.switch_url(customTabs._class)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
