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
@file: test_fixedpointTabs.py
@time: 2018/8/20 16:08
@desc:
'''
import os

import inspect
import unittest

from CenterBackground import MovementUser
from CenterBackground.MovementUser.Sweating.sweatingTabs import SweatingTabs
from tools.excelname.Center.consumers import Consumers
from CenterBackground import customTabs


class TestFixedpointTabs(unittest.TestCase):
    # 定义头部button中，后面2位不需要
    BUTTON_REDUCE_NUMBER = 0

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        config = MovementUser.add_key(MovementUser.fixedPoint, MovementUser.city)
        cls.cJude = SweatingTabs(config, cls.basename, Consumers)

    def setUp(self):
        # 获取运行文件的类名
        self.cJude.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.cJude.openingProgram()
        self.cJude._rou_background()
        pass

    def tearDown(self):
        self.cJude.driver.quit()
        self.cJude.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_active_city(self):
        self.cJude.setFunctionName(inspect.stack()[0][3])
        self.cJude.active_city(customTabs._class)
        pass

    def test_active_code(self):
        self.cJude.setFunctionName(inspect.stack()[0][3])
        ov_default = self.cJude.overall[self.cJude.bi.whole_code()]
        self.cJude.custom_tabs().judge_box_code(customTabs._class, ov_default)
        pass

    def test_already_citys(self):
        self.cJude.setFunctionName(inspect.stack()[0][3])
        self.cJude.already_citys(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_already_codes(self):
        self.cJude.setFunctionName(inspect.stack()[0][3])
        self.cJude.custom_tabs().judge_box_codes(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_city(self):
        self.cJude.setFunctionName(inspect.stack()[0][3])
        self.cJude.switch_city(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_url(self):
        self.cJude.setFunctionName(inspect.stack()[0][3])
        self.cJude.switch_url(customTabs._class, reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_active_box(self):
        self.cJude.setFunctionName(inspect.stack()[0][3])
        self.cJude.active_city(customTabs._class)
        pass

    def test_active_all(self):
        self.cJude.setFunctionName(inspect.stack()[0][3])
        self.cJude.already_citys()
        pass

    def test_switch_box(self):
        self.cJude.setFunctionName(inspect.stack()[0][3])
        self.cJude.switch_city()
        pass

    def test_switch_href(self):
        self.cJude.setFunctionName(inspect.stack()[0][3])
        self.cJude.switch_url(customTabs._class)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
