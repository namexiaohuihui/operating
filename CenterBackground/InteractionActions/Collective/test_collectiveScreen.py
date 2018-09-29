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
@file:      test_collectiveScreen.py
@time:      2018/9/25 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground.InteractionActions.selectlableverify import SelectLableVerify
from CenterBackground import InteractionActions
from tools.excelname.Center.Interaction import InteractionController

basename = os.path.splitext(os.path.basename(__file__))[0]
# 传入子集的key，以及Excel文档中的sheet名字
config = InteractionActions.add_key(InteractionActions.collective, InteractionActions.select)

slVerity = SelectLableVerify(config, basename, InteractionController)


class TestCollectiveScreen(unittest.TestCase):
    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        slVerity.openingProgram()
        slVerity._rou_background()
        print("%s ---setup: 每个用例开始前后执行" % basename)

    def tearDown(self):
        # slVerity.driver.quit()
        slVerity.driver.close()
        print("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－时间－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_timetypeSelect(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.value_options_jude(selectPath=slVerity.overall[slVerity.bi.whole_keys()])
        pass

    def test_timetypeDefault(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.value_options_default(selectPath=slVerity.overall[slVerity.bi.whole_keys()])
        pass

    def test_timetypeTraverse(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.value_option_traverse(formSub=slVerity.bi.yaml_formSub(),
                                       selectPath=slVerity.overall[slVerity.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－其他－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_chooseSelect(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.value_options_jude(selectPath=slVerity.overall[slVerity.bi.whole_keys()])
        pass

    def test_chooseDefault(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.value_options_default(selectPath=slVerity.overall[slVerity.bi.whole_keys()])
        pass

    def test_chooseTraverse(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.value_option_traverse(formSub=slVerity.bi.yaml_formSub(),
                                       selectPath=slVerity.overall[slVerity.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－状态－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_statusSelect(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.value_options_jude(selectPath=slVerity.overall[slVerity.bi.whole_keys()])
        pass

    def test_statusDefault(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.value_options_default(selectPath=slVerity.overall[slVerity.bi.whole_keys()])
        pass

    def test_statusTraverse(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.value_option_traverse(formSub=slVerity.bi.yaml_formSub(),
                                       selectPath=slVerity.overall[slVerity.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－编号－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_orderkeySelect(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.value_options_jude(selectPath=slVerity.overall[slVerity.bi.whole_keys()])
        pass

    def test_orderkeyDefault(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.value_options_default(selectPath=slVerity.overall[slVerity.bi.whole_keys()])
        pass

    def test_orderkeyTraverse(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.value_option_traverse(formSub=slVerity.bi.yaml_formSub(),
                                       selectPath=slVerity.overall[slVerity.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－用户－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_buyerkeySelect(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.value_options_jude(selectPath=slVerity.overall[slVerity.bi.whole_keys()])
        pass

    def test_buyerkeyDefault(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.value_options_default(selectPath=slVerity.overall[slVerity.bi.whole_keys()])
        pass

    def test_buyerkeyTraverse(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.value_option_traverse(formSub=slVerity.bi.yaml_formSub(),
                                       selectPath=slVerity.overall[slVerity.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－键值－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_otherkeySelect(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.value_options_jude(selectPath=slVerity.overall[slVerity.bi.whole_keys()])
        pass

    def test_otherkeyDefault(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.value_options_default(selectPath=slVerity.overall[slVerity.bi.whole_keys()])
        pass

    def test_otherkeyTraverse(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.value_option_traverse(formSub=slVerity.bi.yaml_formSub(),
                                       selectPath=slVerity.overall[slVerity.bi.whole_keys()])
        pass

    # -----------------------------------------三个没做校验的对象------------------------------------------
    def test_managerDefault(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.value_options_default(selectPath=slVerity.overall[slVerity.bi.whole_keys()])
        pass

    def test_directorDefault(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.value_options_default(selectPath=slVerity.overall[slVerity.bi.whole_keys()])
        pass

    def test_areaDefault(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.value_options_default(selectPath=slVerity.overall[slVerity.bi.whole_keys()])
        pass

    # -----------------------------------------多选框对象-------------------------------------------------
    def test_labelInput(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.get_lable_text()
        pass

    # -----------------------------------------三个输入框以及按钮------------------------------------------
    def test_orderInput(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.attribute_value()
        pass

    def test_buyerInput(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.attribute_value()
        pass

    def test_otherInput(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.attribute_value()
        pass

    def test_button_search(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.searchExport(formSub=slVerity.bi.yaml_formSub())
        pass

    def test_button_export(self):
        slVerity.setFunctionName(inspect.stack()[0][3])
        slVerity.searchExport(formSub=slVerity.bi.yaml_formSub())
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
