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
@file:      test_redpacketScreen.py
@time:      2018/9/25 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import GeneralizeAssist
from tools.excelname.Center.generalize import Generalize
from CenterBackground.screeningjude import ScreeningJude


class TestRedPacketScreen(unittest.TestCase):
    """
    条件筛选
    """
    INVITE_DESIGNATED_CODE = "兑换码"
    INVITE_DESIGNATED_RACORD = "红包发放记录"

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename

        # 传入子集的key，以及Excel文档中的sheet名字
        config = GeneralizeAssist.add_key(GeneralizeAssist.redpacket, GeneralizeAssist.select)
        cls.rp_screen = ScreeningJude(config, cls.basename, Generalize)

        cls.INVITE_DESIGNATED_TABS = cls.rp_screen.bi.yaml_tabs()

    def setUp(self):
        # 获取运行文件的类名
        self.rp_screen.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.rp_screen.openingProgram()
        self.rp_screen._rou_background()

    def tearDown(self):
        self.rp_screen.driver.quit()
        self.rp_screen.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－红包设置页面－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_typeSelect(self):
        self.rp_screen.setFunctionName(inspect.stack()[0][3])
        self.rp_screen.value_options_jude(selectPath=self.rp_screen.overall[self.rp_screen.bi.whole_keys()])
        pass

    def test_typeDefault(self):
        self.rp_screen.setFunctionName(inspect.stack()[0][3])
        self.rp_screen.value_options_default(selectPath=self.rp_screen.overall[self.rp_screen.bi.whole_keys()])
        pass

    def test_typeTraverse(self):
        self.rp_screen.setFunctionName(inspect.stack()[0][3])
        self.rp_screen.value_option_traverse(formSub=self.rp_screen.bi.yaml_formSub(),
                                             selectPath=self.rp_screen.overall[self.rp_screen.bi.whole_keys()])
        pass

    def test_button_search(self):
        self.rp_screen.setFunctionName(inspect.stack()[0][3])
        self.rp_screen.searchExport(formSub=self.rp_screen.bi.yaml_formSub())
        pass

    def test_otherInput(self):
        self.rp_screen.setFunctionName(inspect.stack()[0][3])
        self.rp_screen.attribute_value()
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－兑换码页面－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_typesSelect(self):
        self.rp_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.rp_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_CODE)
        self.rp_screen.value_options_jude(selectPath=self.rp_screen.overall[self.rp_screen.bi.whole_keys()])
        pass

    def test_typesDefault(self):
        self.rp_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.rp_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_CODE)
        self.rp_screen.value_options_default(selectPath=self.rp_screen.overall[self.rp_screen.bi.whole_keys()])
        pass

    def test_typesTraverse(self):
        self.rp_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.rp_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_CODE)
        self.rp_screen.value_option_traverse(formSub=self.rp_screen.bi.yaml_formSub(),
                                             selectPath=self.rp_screen.overall[self.rp_screen.bi.whole_keys()])
        pass

    def test_code_search(self):
        self.rp_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.rp_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_CODE)
        self.rp_screen.searchExport(formSub=self.rp_screen.bi.yaml_formSub())
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－红包发放记录－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_statusSelect(self):
        self.rp_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.rp_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_RACORD)
        self.rp_screen.value_options_jude(selectPath=self.rp_screen.overall[self.rp_screen.bi.whole_keys()])
        pass

    def test_statusDefault(self):
        self.rp_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.rp_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_RACORD)
        self.rp_screen.value_options_default(selectPath=self.rp_screen.overall[self.rp_screen.bi.whole_keys()])
        pass

    def test_statusTraverse(self):
        self.rp_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.rp_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_RACORD)
        self.rp_screen.value_option_traverse(formSub=self.rp_screen.bi.yaml_formSub(),
                                             selectPath=self.rp_screen.overall[self.rp_screen.bi.whole_keys()])
        pass

    def test_typetSelect(self):
        self.rp_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.rp_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_RACORD)
        self.rp_screen.value_options_jude(selectPath=self.rp_screen.overall[self.rp_screen.bi.whole_keys()])
        pass

    def test_typetDefault(self):
        self.rp_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.rp_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_RACORD)
        self.rp_screen.value_options_default(selectPath=self.rp_screen.overall[self.rp_screen.bi.whole_keys()])
        pass

    def test_typetTraverse(self):
        self.rp_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.rp_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_RACORD)
        self.rp_screen.value_option_traverse(formSub=self.rp_screen.bi.yaml_formSub(),
                                             selectPath=self.rp_screen.overall[self.rp_screen.bi.whole_keys()])
        pass

    def test_racord_search(self):
        self.rp_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.rp_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_RACORD)
        self.rp_screen.searchExport(formSub=self.rp_screen.bi.yaml_formSub())
        pass

    def test_racord_export(self):
        self.rp_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.rp_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_RACORD)
        self.rp_screen.searchExport(formSub=self.rp_screen.bi.yaml_formSub())
        pass

    def test_racordInput(self):
        self.rp_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.rp_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_RACORD)
        self.rp_screen.attribute_value()
        pass

    def test_starttime(self):
        self.rp_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.rp_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_RACORD)
        self.rp_screen.attribute_value()
        pass

    def test_endtime(self):
        self.rp_screen.setFunctionName(inspect.stack()[0][3])
        # 先进入指定的box
        self.rp_screen.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_RACORD)
        self.rp_screen.attribute_value()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
