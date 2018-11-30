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
@file:      test_moneyScreen.py
@time:      2018/9/25 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import FinancialAffairs
from tools.excelname.Center.financial import Financial
from CenterBackground.screeningjude import ScreeningJude


class TestMoneyScreen(unittest.TestCase):
    """
    条件筛选
    """

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename

        # 传入子集的key，以及Excel文档中的sheet名字
        config = FinancialAffairs.add_key(FinancialAffairs.money, FinancialAffairs.select)

        cls.mon_screen = ScreeningJude(config, cls.basename, Financial)

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        self.mon_screen.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        self.mon_screen.openingProgram()
        self.mon_screen._rou_background()
        pass

    def tearDown(self):
        self.mon_screen.driver.quit()
        self.mon_screen.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_typeSelect(self):
        self.mon_screen.setFunctionName(inspect.stack()[0][3])
        self.mon_screen.value_options_jude(selectPath=self.mon_screen.overall[self.mon_screen.bi.whole_keys()])
        pass

    def test_typeDefault(self):
        self.mon_screen.setFunctionName(inspect.stack()[0][3])
        self.mon_screen.value_options_default(selectPath=self.mon_screen.overall[self.mon_screen.bi.whole_keys()])
        pass

    def test_typeTraverse(self):
        self.mon_screen.setFunctionName(inspect.stack()[0][3])
        self.mon_screen.value_option_traverse(formSub=self.mon_screen.bi.yaml_mon_sub(),
                                              selectPath=self.mon_screen.overall[self.mon_screen.bi.whole_keys()])
        pass

    def test_statusSelect(self):
        self.mon_screen.setFunctionName(inspect.stack()[0][3])
        self.mon_screen.value_options_jude(selectPath=self.mon_screen.overall[self.mon_screen.bi.whole_keys()])
        pass

    def test_statusDefault(self):
        self.mon_screen.setFunctionName(inspect.stack()[0][3])
        self.mon_screen.value_options_default(selectPath=self.mon_screen.overall[self.mon_screen.bi.whole_keys()])
        pass

    def test_statusTraverse(self):
        self.mon_screen.setFunctionName(inspect.stack()[0][3])
        self.mon_screen.value_option_traverse(formSub=self.mon_screen.bi.yaml_mon_sub(),
                                              selectPath=self.mon_screen.overall[self.mon_screen.bi.whole_keys()])
        pass

    # -----------------------------------------其他页面的输入框和按钮-------------------------------------------------
    def test_otherInput(self):
        self.mon_screen.setFunctionName(inspect.stack()[0][3])
        self.mon_screen.attribute_value()
        pass

    def test_button_search(self):
        self.mon_screen.setFunctionName(inspect.stack()[0][3])
        self.mon_screen.searchExport(formSub=self.mon_screen.bi.yaml_mon_sub())
        pass

    def test_button_export(self):
        self.mon_screen.setFunctionName(inspect.stack()[0][3])
        self.mon_screen.searchExport(formSub=self.mon_screen.bi.yaml_mon_sub())
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
