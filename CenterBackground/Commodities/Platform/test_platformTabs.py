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
@file: platformTabs.py
@time: 2018/8/20 16:08
@desc:
'''
import os
import inspect
import unittest
from CenterBackground import Commodities
from CenterBackground.commoditiecJude import CommoditiecJude
from tools.excelname.Center.bundledItems import BundledItems

class TestPlatformTabs(unittest.TestCase):
    # 定义头部button中，后面2位不需要
    BUTTON_REDUCE_NUMBER = 2

    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + basename
        config = Commodities.add_key(Commodities.platform, Commodities.city)
        cls.cJude = CommoditiecJude(config, cls.basename, BundledItems)

    def setUp(self):
        # 获取运行文件的类名
        self.cJude.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.cJude.openingProgram()
        self.cJude._rou_background()

    def tearDown(self):
        self.cJude.driver.quit()
        self.cJude.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_active_city(self):
        self.cJude.setFunctionName(inspect.stack()[0][3])
        self.cJude.active_city('class')
        pass

    def test_active_code(self):
        self.cJude.setFunctionName(inspect.stack()[0][3])
        self.cJude.active_code('class')
        pass

    def test_already_citys(self):
        self.cJude.setFunctionName(inspect.stack()[0][3])
        self.cJude.already_citys(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_already_codes(self):
        self.cJude.setFunctionName(inspect.stack()[0][3])
        self.cJude.already_codes(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_city(self):
        self.cJude.setFunctionName(inspect.stack()[0][3])
        self.cJude.switch_city(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_url(self):
        self.cJude.setFunctionName(inspect.stack()[0][3])
        self.cJude.switch_url('class', reduce=self.BUTTON_REDUCE_NUMBER)
        pass


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = TestLoader()
    loader.testMethodPrefix = 'ab'
    test_cases = unittest.TestLoader().loadTestsFromTestCase(TestPlatformTabs)
    suite.addTests(test_cases)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)