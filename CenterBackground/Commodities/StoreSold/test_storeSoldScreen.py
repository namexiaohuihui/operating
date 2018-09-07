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
@author:    ln_company
@license:   (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@Software:  PyCharm
@file:      test_storeScreen.py
@time:      2018/8/31 15:35
@desc:
'''
import os
import inspect
import unittest
from CenterBackground import Commodities
from CenterBackground.Commodities.soldScreen import SoldScreen
from tools.excelname.Center.bundledItems import BundledItems

BASENAME = os.path.splitext(os.path.basename(__file__))[0]
config = Commodities.add_key(Commodities.storesold, Commodities.select)
screen = SoldScreen(config, BASENAME, BundledItems)


class TestStoreScreen(unittest.TestCase):
    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        screen.openingProgram()
        screen._rou_background()
        print("%s ---setup: 每个用例开始前后执行" % BASENAME)

    def tearDown(self):
        screen.driver.quit()
        print("%s ---teardown: 每个用例结束后执行" % BASENAME)
        pass

        # －－－－－－－－－－－－－－－－－－－－－－－－状态－－－－－－－－－－－－－－－－－－－－－－－－－－

    def test_statusSelect(self):
        screen.setFunctionName(inspect.stack()[0][3])
        screen.value_options_jude(selectPath=screen.overall[screen.bi.whole_keys()])
        pass

    def test_statusDefault(self):
        screen.setFunctionName(inspect.stack()[0][3])
        screen.value_options_default(selectPath=screen.overall[screen.bi.whole_keys()])
        pass

    def test_statusTraverse(self):
        screen.setFunctionName(inspect.stack()[0][3])
        screen.value_option_traverse(formSub=screen.bi.yaml_formSub(), selectPath=screen.overall[screen.bi.whole_keys()])
        pass

        # －－－－－－－－－－－－－－－－－－－－－－－－状态－－－－－－－－－－－－－－－－－－－－－－－－－－

    def test_chooseSelect(self):
        screen.setFunctionName(inspect.stack()[0][3])
        screen.value_options_jude(selectPath=screen.overall[screen.bi.whole_keys()])
        pass

    def test_chooseDefault(self):
        screen.setFunctionName(inspect.stack()[0][3])
        screen.value_options_default(selectPath=screen.overall[screen.bi.whole_keys()])
        pass

    def test_chooseTraverse(self):
        screen.setFunctionName(inspect.stack()[0][3])
        screen.value_option_traverse(formSub=screen.bi.yaml_formSub(), selectPath=screen.overall[screen.bi.whole_keys()])
        pass

        # －－－－－－－－－－－－－－－－－－－－－－－－其他－－－－－－－－－－－－－－－－－－－－－－－－－－

    def test_conditionsInput(self):
        screen.setFunctionName(inspect.stack()[0][3])
        screen.attribute_value()
        pass

    def test_startTime(self):
        screen.setFunctionName(inspect.stack()[0][3])
        screen.attribute_value()
        pass

    def test_endTime(self):
        screen.setFunctionName(inspect.stack()[0][3])
        screen.attribute_value()
        pass

    def test_button_search(self):
        screen.setFunctionName(inspect.stack()[0][3])
        screen.searchExport(formSub=screen.bi.yaml_formSub())
        pass

    def test_button_export(self):
        screen.setFunctionName(inspect.stack()[0][3])
        screen.searchExport(formSub=screen.bi.yaml_formSub())
        pass
