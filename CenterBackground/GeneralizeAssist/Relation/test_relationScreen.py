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
@file:      test_relationScreen.py
@time:      2018/9/25 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import GeneralizeAssist
from tools.excelname.Center.generalize import Generalize
from CenterBackground.screeningjude import ScreeningJude

basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename

# 传入子集的key，以及Excel文档中的sheet名字
config = GeneralizeAssist.add_key(GeneralizeAssist.relation, GeneralizeAssist.select)

r_screen = ScreeningJude(config, basename, Generalize)


class TestRelationScreen(unittest.TestCase):
    """
    条件筛选
    """
    INVITE_DESIGNATED_BOX = "历史数据"
    INVITE_DESIGNATED_TABS = r_screen.bi.yaml_tabs()

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        r_screen.openingProgram()
        r_screen._rou_background()
        r_screen.log.info("%s ---setup: 每个用例开始前后执行" % basename)
        pass

    def tearDown(self):
        r_screen.driver.quit()
        r_screen.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－进行中的数据信息－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_ostatusSelect(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        r_screen.value_options_jude(selectPath=r_screen.overall[r_screen.bi.whole_keys()])
        pass

    def test_ostatusDefault(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        r_screen.value_options_default(selectPath=r_screen.overall[r_screen.bi.whole_keys()])
        pass

    def test_ostatusTraverse(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        r_screen.value_option_traverse(formSub=r_screen.bi.yaml_formSub(),
                                       selectPath=r_screen.overall[r_screen.bi.whole_keys()])
        pass

    def test_otypeSelect(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        r_screen.value_options_jude(selectPath=r_screen.overall[r_screen.bi.whole_keys()])
        pass

    def test_otypeDefault(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        r_screen.value_options_default(selectPath=r_screen.overall[r_screen.bi.whole_keys()])
        pass

    def test_otypeTraverse(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        r_screen.value_option_traverse(formSub=r_screen.bi.yaml_formSub(),
                                       selectPath=r_screen.overall[r_screen.bi.whole_keys()])
        pass

    def test_obutton_search(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        r_screen.searchExport(formSub=r_screen.bi.yaml_formSub())
        pass

    def test_obutton_export(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        r_screen.searchExport(formSub=r_screen.bi.yaml_formSub())
        pass

    def test_ootherInput(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        r_screen.attribute_value()
        pass

    def test_ostarttime(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        r_screen.attribute_value()
        pass

    def test_oendtime(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        r_screen.attribute_value()
        pass

    # ---------------------------------历史数据信息----------------------------
    def test_hstatusSelect(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        r_screen.value_options_jude(selectPath=r_screen.overall[r_screen.bi.whole_keys()])
        pass

    def test_hstatusDefault(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        r_screen.value_options_default(selectPath=r_screen.overall[r_screen.bi.whole_keys()])
        pass

    def test_hstatusTraverse(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        r_screen.value_option_traverse(formSub=r_screen.bi.yaml_formSub(),
                                       selectPath=r_screen.overall[r_screen.bi.whole_keys()])
        pass

    def test_htypeSelect(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        r_screen.value_options_jude(selectPath=r_screen.overall[r_screen.bi.whole_keys()])
        pass

    def test_htypeDefault(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        r_screen.value_options_default(selectPath=r_screen.overall[r_screen.bi.whole_keys()])
        pass

    def test_htypeTraverse(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        r_screen.value_option_traverse(formSub=r_screen.bi.yaml_formSub(),
                                       selectPath=r_screen.overall[r_screen.bi.whole_keys()])
        pass

    def test_hbutton_search(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        r_screen.searchExport(formSub=r_screen.bi.yaml_formSub())
        pass

    def test_hbutton_export(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        r_screen.searchExport(formSub=r_screen.bi.yaml_formSub())
        pass

    def test_hotherInput(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        r_screen.attribute_value()
        pass

    def test_hstarttime(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        r_screen.attribute_value()
        pass

    def test_hendtime(self):
        r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        r_screen.attribute_value()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
