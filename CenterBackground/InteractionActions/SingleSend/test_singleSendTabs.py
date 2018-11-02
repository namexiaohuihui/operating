# -*- coding: utf-8 -*-
"""
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
@author:    ln_company
@license:   (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@Software:  PyCharm
@file:      test_singleSendTabs.py
@time:      2018/9/19 16:44
@desc:
"""
import time

import os
import inspect
import unittest
from CenterBackground import InteractionActions
from CenterBackground.commoditiesJude import CommoditiesJude
from tools.excelname.Center.Interaction import InteractionController

basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename

# 传入子集的key，以及Excel文档中的sheet名字
config = InteractionActions.add_key(InteractionActions.single, InteractionActions.city)
sw_tab = CommoditiesJude(config, basename, InteractionController)


class TestSingleSendTabs(unittest.TestCase):
    """
    城市tab切换用例所在地
    """
    # 定义头部button中，后面N位不需要
    BUTTON_REDUCE_NUMBER = 0

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        sw_tab.openingProgram()
        sw_tab._rou_background()
        sw_tab.log.info("%s ---setup: 每个用例开始前后执行" % basename)
        pass

    def tearDown(self):
        sw_tab.driver.quit()
        sw_tab.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    def test_active_tab(self):
        sw_tab.setFunctionName(inspect.stack()[0][3])
        sw_tab.active_city('class')
        pass

    def test_already_tabs(self):
        sw_tab.setFunctionName(inspect.stack()[0][3])
        sw_tab.already_citys(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_tab(self):
        sw_tab.setFunctionName(inspect.stack()[0][3])
        sw_tab.switch_city(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_url(self):
        sw_tab.setFunctionName(inspect.stack()[0][3])
        sw_tab.switch_url('class', reduce=self.BUTTON_REDUCE_NUMBER)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
