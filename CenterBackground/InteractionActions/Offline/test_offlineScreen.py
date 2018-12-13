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
@file:      test_offlineScreen.py
@time:      2018/9/25 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import InteractionActions
from tools.excelname.Center.Interaction import InteractionController
from CenterBackground.InteractionActions.selectlableverify import SelectLableVerify


class TestOfflineScreen(unittest.TestCase):
    """
    条件筛选
    """

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        config = InteractionActions.add_key(InteractionActions.offline, InteractionActions.select)

        cls.slVerity = SelectLableVerify(config, cls.basename, InteractionController)

    def setUp(self):
        # 获取运行文件的类名
        self.slVerity.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.slVerity.openingProgram()
        self.slVerity._rou_background()
        pass

    def tearDown(self):
        self.slVerity.driver.quit()
        self.slVerity.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－时间－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_timetypeSelect(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.value_options_jude(selectPath=self.slVerity.overall[self.slVerity.bi.whole_keys()])
        pass

    def test_timetypeDefault(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.value_options_default(selectPath=self.slVerity.overall[self.slVerity.bi.whole_keys()])
        pass

    def test_timetypeTraverse(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.value_option_traverse(formSub=self.slVerity.bi.yaml_formSub(),
                                            selectPath=self.slVerity.overall[self.slVerity.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－编号－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_orderkeySelect(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.value_options_jude(selectPath=self.slVerity.overall[self.slVerity.bi.whole_keys()])
        pass

    def test_orderkeyDefault(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.value_options_default(selectPath=self.slVerity.overall[self.slVerity.bi.whole_keys()])
        pass

    def test_orderkeyTraverse(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.value_option_traverse(formSub=self.slVerity.bi.yaml_formSub(),
                                            selectPath=self.slVerity.overall[self.slVerity.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－用户－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_buyerkeySelect(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.value_options_jude(selectPath=self.slVerity.overall[self.slVerity.bi.whole_keys()])
        pass

    def test_buyerkeyDefault(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.value_options_default(selectPath=self.slVerity.overall[self.slVerity.bi.whole_keys()])
        pass

    def test_buyerkeyTraverse(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.value_option_traverse(formSub=self.slVerity.bi.yaml_formSub(),
                                            selectPath=self.slVerity.overall[self.slVerity.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－配送－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_deliverySelect(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.value_options_jude(selectPath=self.slVerity.overall[self.slVerity.bi.whole_keys()])
        pass

    def test_deliveryDefault(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.value_options_default(selectPath=self.slVerity.overall[self.slVerity.bi.whole_keys()])
        pass

    def test_deliveryTraverse(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.value_option_traverse(formSub=self.slVerity.bi.yaml_formSub(),
                                            selectPath=self.slVerity.overall[self.slVerity.bi.whole_keys()])
        pass

    # -----------------------------------------三个没做校验的对象------------------------------------------
    def test_managerDefault(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.value_options_default(selectPath=self.slVerity.overall[self.slVerity.bi.whole_keys()])
        pass

    def test_directorDefault(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.value_options_default(selectPath=self.slVerity.overall[self.slVerity.bi.whole_keys()])
        pass

    def test_areaDefault(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.value_options_default(selectPath=self.slVerity.overall[self.slVerity.bi.whole_keys()])
        pass

    # -----------------------------------------多选框对象-------------------------------------------------
    def test_labelInput(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.get_lable_text()
        pass

    # -----------------------------------------三个输入框以及按钮------------------------------------------
    def test_orderInput(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.attribute_value()
        pass

    def test_buyerInput(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.attribute_value()
        pass

    def test_otherInput(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.attribute_value()
        pass

    def test_deliveryInput(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.attribute_value()
        pass

    def test_singleInput(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.attribute_value()
        pass

    def test_button_search(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.searchExport(formSub=self.slVerity.bi.yaml_formSub())
        pass

    def test_button_export(self):
        self.slVerity.setFunctionName(inspect.stack()[0][3])
        self.slVerity.searchExport(formSub=self.slVerity.bi.yaml_formSub())
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
