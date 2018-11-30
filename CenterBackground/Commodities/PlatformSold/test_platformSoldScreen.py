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
@file:      test_platformSoldScreen.py
@time:      2018/8/28 10:10
@Site :     
@desc:
'''
import os
import inspect
import unittest
from CenterBackground import Commodities
from tools.excelname.Center.bundledItems import BundledItems
from CenterBackground.screeningjude import ScreeningJude


class TestPlatformSoldScreen(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + basename
        config = Commodities.add_key(Commodities.platformsold, Commodities.select)
        cls.screen = ScreeningJude(config, cls.basename, BundledItems)

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        self.screen.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        self.screen.openingProgram()
        self.screen._rou_background()
        pass

    def tearDown(self):
        self.screen.driver.quit()
        self.screen.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－类型－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_categorySelect(self):
        self.screen.setFunctionName(inspect.stack()[0][3])
        self.screen.value_options_jude(selectPath=self.screen.overall[self.screen.bi.whole_keys()])
        pass

    def test_categoryDefault(self):
        self.screen.setFunctionName(inspect.stack()[0][3])
        self.screen.value_options_default(selectPath=self.screen.overall[self.screen.bi.whole_keys()])
        pass

    def test_categoryTraverse(self):
        self.screen.setFunctionName(inspect.stack()[0][3])
        self.screen.value_option_traverse(formSub=self.screen.bi.yaml_iptJ(),
                                          selectPath=self.screen.overall[self.screen.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－来源－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_sourceSelect(self):
        self.screen.setFunctionName(inspect.stack()[0][3])
        self.screen.value_options_jude(selectPath=self.screen.overall[self.screen.bi.whole_keys()])
        pass

    def test_sourceDefault(self):
        self.screen.setFunctionName(inspect.stack()[0][3])
        self.screen.value_options_default(selectPath=self.screen.overall[self.screen.bi.whole_keys()])
        pass

    def test_sourceTraverse(self):
        self.screen.setFunctionName(inspect.stack()[0][3])
        self.screen.value_option_traverse(formSub=self.screen.bi.yaml_iptJ(),
                                          selectPath=self.screen.overall[self.screen.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－状态－－－－－－－－－－－－－－－－－－－－－－－－－－

    def test_statusSelect(self):
        self.screen.setFunctionName(inspect.stack()[0][3])
        self.screen.value_options_jude(selectPath=self.screen.overall[self.screen.bi.whole_keys()])
        pass

    def test_statusDefault(self):
        self.screen.setFunctionName(inspect.stack()[0][3])
        self.screen.value_options_default(selectPath=self.screen.overall[self.screen.bi.whole_keys()])
        pass

    def test_statusTraverse(self):
        self.screen.setFunctionName(inspect.stack()[0][3])
        self.screen.value_option_traverse(formSub=self.screen.bi.yaml_iptJ(),
                                          selectPath=self.screen.overall[self.screen.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－标签－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_firstlabelSelect(self):
        self.screen.setFunctionName(inspect.stack()[0][3])
        self.screen.value_options_jude(selectPath=self.screen.overall[self.screen.bi.whole_keys()])
        pass

    def test_firstlabelDefault(self):
        self.screen.setFunctionName(inspect.stack()[0][3])
        self.screen.value_options_default(selectPath=self.screen.overall[self.screen.bi.whole_keys()])
        pass

    def test_firstlabelTraverse(self):
        self.screen.setFunctionName(inspect.stack()[0][3])
        self.screen.value_option_traverse(formSub=self.screen.bi.yaml_iptJ(),
                                          selectPath=self.screen.overall[self.screen.bi.whole_keys()])
        pass

    # －－－－－－－－－－－ －－－－－－－－－－－－－混乱－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_chooseSelect(self):
        self.screen.setFunctionName(inspect.stack()[0][3])
        self.screen.value_options_jude(selectPath=self.screen.overall[self.screen.bi.whole_keys()])
        pass

    def test_chooseDefault(self):
        self.screen.setFunctionName(inspect.stack()[0][3])
        self.screen.value_options_default(selectPath=self.screen.overall[self.screen.bi.whole_keys()])
        pass

    def test_chooseTraverse(self):
        self.screen.setFunctionName(inspect.stack()[0][3])
        self.screen.value_option_traverse(formSub=self.screen.bi.yaml_iptJ(),
                                          selectPath=self.screen.overall[self.screen.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－其他－－－－－－－－－－－－－－－－－－－－－－－－－－

    def test_conditionsInput(self):
        self.screen.setFunctionName(inspect.stack()[0][3])
        self.screen.attribute_value()
        pass

    def test_reservationtime(self):
        self.screen.setFunctionName(inspect.stack()[0][3])
        self.screen.attribute_value()
        pass

    def test_button_search(self):
        self.screen.setFunctionName(inspect.stack()[0][3])
        self.screen.searchExport(formSub=self.screen.bi.yaml_iptJ())
        pass

    def test_button_export(self):
        self.screen.setFunctionName(inspect.stack()[0][3])
        self.screen.searchExport(formSub=self.screen.bi.yaml_iptJ())
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
