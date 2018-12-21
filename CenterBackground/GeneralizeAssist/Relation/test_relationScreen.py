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



class TestRelationScreen(unittest.TestCase):
    """
    条件筛选
    """
    INVITE_DESIGNATED_BOX = "历史数据"

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename

        # 传入子集的key，以及Excel文档中的sheet名字
        config = GeneralizeAssist.add_key(GeneralizeAssist.relation, GeneralizeAssist.select)

        cls.r_screen = ScreeningJude(config, cls.basename, Generalize)
        cls.INVITE_DESIGNATED_TABS = cls.r_screen.bi.yaml_tabs()

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]
        pass

    def setUp(self):
        # 获取运行文件的类名
        self.r_screen.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.r_screen.openingProgram()
        self.r_screen._rou_background()

    def tearDown(self):
        self.r_screen.get_screenshot_image(method_obj=self)

        self.r_screen.driver.quit()
        self.r_screen.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－进行中的数据信息－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_ostatusSelect(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        self.r_screen.value_options_jude(selectPath=self.r_screen.overall[self.r_screen.bi.whole_keys()])
        pass

    def test_ostatusDefault(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        self.r_screen.value_options_default(selectPath=self.r_screen.overall[self.r_screen.bi.whole_keys()])
        pass

    def test_ostatusTraverse(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        self.r_screen.value_option_traverse(formSub=self.r_screen.bi.yaml_formSub(),
                                       selectPath=self.r_screen.overall[self.r_screen.bi.whole_keys()])
        pass

    def test_otypeSelect(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        self.r_screen.value_options_jude(selectPath=self.r_screen.overall[self.r_screen.bi.whole_keys()])
        pass

    def test_otypeDefault(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        self.r_screen.value_options_default(selectPath=self.r_screen.overall[self.r_screen.bi.whole_keys()])
        pass

    def test_otypeTraverse(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        self.r_screen.value_option_traverse(formSub=self.r_screen.bi.yaml_formSub(),
                                       selectPath=self.r_screen.overall[self.r_screen.bi.whole_keys()])
        pass

    def test_obutton_search(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        self.r_screen.searchExport(formSub=self.r_screen.bi.yaml_formSub())
        pass

    def test_obutton_export(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        self.r_screen.searchExport(formSub=self.r_screen.bi.yaml_formSub())
        pass

    def test_ootherInput(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        self.r_screen.attribute_value()
        pass

    def test_ostarttime(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        self.r_screen.attribute_value()
        pass

    def test_oendtime(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        self.r_screen.attribute_value()
        pass

    # ---------------------------------历史数据信息----------------------------
    def test_hstatusSelect(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        self.r_screen.value_options_jude(selectPath=self.r_screen.overall[self.r_screen.bi.whole_keys()])
        pass

    def test_hstatusDefault(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        self.r_screen.value_options_default(selectPath=self.r_screen.overall[self.r_screen.bi.whole_keys()])
        pass

    def test_hstatusTraverse(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        self.r_screen.value_option_traverse(formSub=self.r_screen.bi.yaml_formSub(),
                                       selectPath=self.r_screen.overall[self.r_screen.bi.whole_keys()])
        pass

    def test_htypeSelect(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        self.r_screen.value_options_jude(selectPath=self.r_screen.overall[self.r_screen.bi.whole_keys()])
        pass

    def test_htypeDefault(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        self.r_screen.value_options_default(selectPath=self.r_screen.overall[self.r_screen.bi.whole_keys()])
        pass

    def test_htypeTraverse(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        self.r_screen.value_option_traverse(formSub=self.r_screen.bi.yaml_formSub(),
                                       selectPath=self.r_screen.overall[self.r_screen.bi.whole_keys()])
        pass

    def test_hbutton_search(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        self.r_screen.searchExport(formSub=self.r_screen.bi.yaml_formSub())
        pass

    def test_hbutton_export(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        self.r_screen.searchExport(formSub=self.r_screen.bi.yaml_formSub())
        pass

    def test_hotherInput(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        self.r_screen.attribute_value()
        pass

    def test_hstarttime(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        self.r_screen.attribute_value()
        pass

    def test_hendtime(self):
        self.r_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.r_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        self.r_screen.attribute_value()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
