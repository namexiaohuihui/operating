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

basename = os.path.splitext(os.path.basename(__file__))[0]
# 传入子集的key，以及Excel文档中的sheet名字
config = MovementUser.add_key(MovementUser.fixedPoint, MovementUser.city)
cJude = SweatingTabs(config, basename, Consumers)


class TestFixedpointTabs(unittest.TestCase):
    # 定义头部button中，后面2位不需要
    BUTTON_REDUCE_NUMBER = 0

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        cJude.openingProgram()
        cJude._rou_background()
        print("%s ---setup: 每个用例开始前后执行" % basename)

    def tearDown(self):
        cJude.driver.quit()
        print("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    def test_active_city(self):
        cJude.setFunctionName(inspect.stack()[0][3])
        cJude.active_city(customTabs._class)
        pass

    def test_active_code(self):
        cJude.setFunctionName(inspect.stack()[0][3])
        ov_default = cJude.overall[cJude.bi.whole_code()]
        cJude.custom_tabs().judge_box_code(customTabs._class, ov_default)
        pass

    def test_already_citys(self):
        cJude.setFunctionName(inspect.stack()[0][3])
        cJude.already_citys(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_already_codes(self):
        cJude.setFunctionName(inspect.stack()[0][3])
        cJude.custom_tabs().judge_box_codes(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_city(self):
        cJude.setFunctionName(inspect.stack()[0][3])
        cJude.switch_city(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_url(self):
        cJude.setFunctionName(inspect.stack()[0][3])
        cJude.switch_url(customTabs._class, reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_active_box(self):
        cJude.setFunctionName(inspect.stack()[0][3])
        cJude.active_city(customTabs._class)
        pass

    def test_active_all(self):
        cJude.setFunctionName(inspect.stack()[0][3])
        cJude.already_citys()
        pass

    def test_switch_box(self):
        cJude.setFunctionName(inspect.stack()[0][3])
        cJude.switch_city()
        pass

    def test_switch_href(self):
        cJude.setFunctionName(inspect.stack()[0][3])
        cJude.switch_url(customTabs._class)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
