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
@time:      2018/8/28 10:10
@Site :     
@desc:
'''
import os
import inspect
import unittest
from CenterBackground import MovementUser
from CenterBackground.screeningjude import ScreeningJude
from tools.excelname.Center.bundledItems import BundledItems

BASENAME = os.path.splitext(os.path.basename(__file__))[0]
config = MovementUser.add_key(MovementUser.supporters, MovementUser.select)
sJude = ScreeningJude(config, BASENAME, BundledItems)


class TestStoreScreen(unittest.TestCase):
    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        sJude.openingProgram()
        sJude._rou_background()
        print("%s ---setup: 每个用例开始前后执行" % BASENAME)

    def tearDown(self):
        sJude.driver.quit()
        print("%s ---teardown: 每个用例结束后执行" % BASENAME)
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－状态－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_statusSelect(self):
        sJude.setFunctionName(inspect.stack()[0][3])
        sJude.value_options_jude(selectPath=sJude.overall[sJude.bi.whole_keys()])
        pass

    def test_statusDefault(self):
        sJude.setFunctionName(inspect.stack()[0][3])
        sJude.value_options_default(selectPath=sJude.overall[sJude.bi.whole_keys()])
        pass

    def test_statusTraverse(self):
        sJude.setFunctionName(inspect.stack()[0][3])
        sJude.value_option_traverse(formSub=sJude.bi.yaml_iptJ(), selectPath=sJude.overall[sJude.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－很乱－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_chooseSelect(self):
        sJude.setFunctionName(inspect.stack()[0][3])
        sJude.value_options_jude(selectPath=sJude.overall[sJude.bi.whole_keys()])
        pass

    def test_chooseDefault(self):
        sJude.setFunctionName(inspect.stack()[0][3])
        sJude.value_options_default(selectPath=sJude.overall[sJude.bi.whole_keys()])
        pass

    def test_chooseTraverse(self):
        sJude.setFunctionName(inspect.stack()[0][3])
        sJude.value_option_traverse(formSub=sJude.bi.yaml_iptJ(), selectPath=sJude.overall[sJude.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－其他－－－－－－－－－－－－－－－－－－－－－－－－－－

    def test_conditionsInput(self):
        sJude.setFunctionName(inspect.stack()[0][3])
        sJude.attribute_value()
        pass

    def test_startTime(self):
        sJude.setFunctionName(inspect.stack()[0][3])
        sJude.attribute_value()
        pass

    def test_endTime(self):
        sJude.setFunctionName(inspect.stack()[0][3])
        sJude.attribute_value()
        pass

    def test_button_search(self):
        sJude.setFunctionName(inspect.stack()[0][3])
        sJude.searchExport(formSub=sJude.bi.yaml_iptJ())
        pass

    def test_button_export(self):
        sJude.setFunctionName(inspect.stack()[0][3])
        sJude.searchExport(formSub=sJude.bi.yaml_iptJ())
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
