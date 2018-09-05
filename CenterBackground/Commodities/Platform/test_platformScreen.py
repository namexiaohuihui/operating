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
@file:      test_platformScreen.py
@time:      2018/8/28 10:10
@Site :     
@desc:
'''
import os
import inspect
import unittest
from CenterBackground import Commodities
from CenterBackground.screeningjude import ScreeningJude
from tools.excelname.Center.bundledItems import BundledItems

BASENAME = os.path.splitext(os.path.basename(__file__))[0]
config = Commodities.add_key(Commodities.platform, Commodities.select)
sj = ScreeningJude(config, BASENAME, BundledItems)


class TestPlatformScreen(unittest.TestCase):
    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        sj.openingProgram()
        sj._rou_background()
        print("%s ---setup: 每个用例开始前后执行" % BASENAME)

    def tearDown(self):
        sj.driver.quit()
        print("%s ---teardown: 每个用例结束后执行" % BASENAME)
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－状态－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_statusSelect(self):
        sj.setFunctionName(inspect.stack()[0][3])
        sj.value_options_jude(selectPath=sj.overall[sj.bi.whole_keys()])
        pass

    def test_statusDefault(self):
        sj.setFunctionName(inspect.stack()[0][3])
        sj.value_options_default(selectPath=sj.overall[sj.bi.whole_keys()])
        pass

    def test_statusTraverse(self):
        sj.setFunctionName(inspect.stack()[0][3])
        sj.value_option_traverse(formSub = sj.bi.yaml_formSub(),selectPath=sj.overall[sj.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－类型－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_watikiSelect(self):
        sj.setFunctionName(inspect.stack()[0][3])
        sj.value_options_jude(selectPath=sj.overall[sj.bi.whole_keys()])
        pass

    def test_watikiDefault(self):
        sj.setFunctionName(inspect.stack()[0][3])
        sj.value_options_default(selectPath=sj.overall[sj.bi.whole_keys()])
        pass

    def test_watikiTraverse(self):
        sj.setFunctionName(inspect.stack()[0][3])
        sj.value_option_traverse(formSub = sj.bi.yaml_formSub(),selectPath=sj.overall[sj.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－优惠－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_preferencesSelect(self):
        sj.setFunctionName(inspect.stack()[0][3])
        sj.value_options_jude(selectPath=sj.overall[sj.bi.whole_keys()])
        pass

    def test_preferencesDefault(self):
        sj.setFunctionName(inspect.stack()[0][3])
        sj.value_options_default(selectPath=sj.overall[sj.bi.whole_keys()])
        pass

    def test_preferencesTraverse(self):
        sj.setFunctionName(inspect.stack()[0][3])
        sj.value_option_traverse(formSub = sj.bi.yaml_formSub(),selectPath=sj.overall[sj.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－状态－－－－－－－－－－－－－－－－－－－－－－－－－－

    def test_chooseSelect(self):
        sj.setFunctionName(inspect.stack()[0][3])
        sj.value_options_jude(selectPath=sj.overall[sj.bi.whole_keys()])
        pass

    def test_chooseDefault(self):
        sj.setFunctionName(inspect.stack()[0][3])
        sj.value_options_default(selectPath=sj.overall[sj.bi.whole_keys()])
        pass

    def test_chooseTraverse(self):
        sj.setFunctionName(inspect.stack()[0][3])
        sj.value_option_traverse(formSub = sj.bi.yaml_formSub(),selectPath=sj.overall[sj.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－其他－－－－－－－－－－－－－－－－－－－－－－－－－－

    def test_conditionsInput(self):
        sj.setFunctionName(inspect.stack()[0][3])
        sj.attribute_value()
        pass

    def test_startTime(self):
        sj.setFunctionName(inspect.stack()[0][3])
        sj.attribute_value()
        pass

    def test_endTime(self):
        sj.setFunctionName(inspect.stack()[0][3])
        sj.attribute_value()
        pass

    def test_button_search(self):
        sj.setFunctionName(inspect.stack()[0][3])
        sj.searchExport(formSub = sj.bi.yaml_formSub())
        pass

    def test_button_export(self):
        sj.setFunctionName(inspect.stack()[0][3])
        sj.searchExport(formSub = sj.bi.yaml_formSub())
        pass
