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
@file:      test_customerScreen.py
@time:      2018/8/28 10:10
@Site :     
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import MovementUser
from CenterBackground.screeningjude import ScreeningJude
from tools.excelname.Center.consumers import Consumers


class TestCustomerScreen(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        config = MovementUser.add_key(MovementUser.customer, MovementUser.select)
        cls.sJude = ScreeningJude(config, cls.basename, Consumers)

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]
        pass

    def setUp(self):
        # 获取运行文件的类名
        self.sJude.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.sJude.openingProgram()
        self.sJude._rou_background()
        pass

    def tearDown(self):
        self.sJude.get_screenshot_image(method_obj=self)

        self.sJude.driver.quit()
        self.sJude.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－状态－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_interestSelect(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.value_options_jude(selectPath=self.sJude.overall[self.sJude.bi.whole_keys()])
        pass

    def test_interestDefault(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.value_options_default(selectPath=self.sJude.overall[self.sJude.bi.whole_keys()])
        pass

    def test_interestTraverse(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.value_option_traverse(formSub=self.sJude.bi.yaml_iptJ(),
                                         selectPath=self.sJude.overall[self.sJude.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－认证－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_approveSelect(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.value_options_jude(selectPath=self.sJude.overall[self.sJude.bi.whole_keys()])
        pass

    def test_approveDefault(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.value_options_default(selectPath=self.sJude.overall[self.sJude.bi.whole_keys()])
        pass

    def test_approveTraverse(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.value_option_traverse(formSub=self.sJude.bi.yaml_iptJ(),
                                         selectPath=self.sJude.overall[self.sJude.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－状态－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_statusSelect(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.value_options_jude(selectPath=self.sJude.overall[self.sJude.bi.whole_keys()])
        pass

    def test_statusDefault(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.value_options_default(selectPath=self.sJude.overall[self.sJude.bi.whole_keys()])
        pass

    def test_statusTraverse(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.value_option_traverse(formSub=self.sJude.bi.yaml_iptJ(),
                                         selectPath=self.sJude.overall[self.sJude.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－类型－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_sourceSelect(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.value_options_jude(selectPath=self.sJude.overall[self.sJude.bi.whole_keys()])
        pass

    def test_sourceDefault(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.value_options_default(selectPath=self.sJude.overall[self.sJude.bi.whole_keys()])
        pass

    def test_sourceTraverse(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.value_option_traverse(formSub=self.sJude.bi.yaml_iptJ(),
                                         selectPath=self.sJude.overall[self.sJude.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－城市－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_citySelect(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.value_options_jude(selectPath=self.sJude.overall[self.sJude.bi.whole_keys()])
        pass

    def test_cityDefault(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.value_options_default(selectPath=self.sJude.overall[self.sJude.bi.whole_keys()])
        pass

    def test_cityTraverse(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.value_option_traverse(formSub=self.sJude.bi.yaml_iptJ(),
                                         selectPath=self.sJude.overall[self.sJude.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－很乱－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_chooseSelect(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.value_options_jude(selectPath=self.sJude.overall[self.sJude.bi.whole_keys()])
        pass

    def test_chooseDefault(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.value_options_default(selectPath=self.sJude.overall[self.sJude.bi.whole_keys()])
        pass

    def test_chooseTraverse(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.value_option_traverse(formSub=self.sJude.bi.yaml_iptJ(),
                                         selectPath=self.sJude.overall[self.sJude.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－其他－－－－－－－－－－－－－－－－－－－－－－－－－－

    def test_conditionsInput(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.attribute_value()
        pass

    def test_startTime(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.attribute_value()
        pass

    def test_endTime(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.attribute_value()
        pass

    def test_button_search(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.searchExport(formSub=self.sJude.bi.yaml_iptJ())
        pass

    def test_button_export(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        self.sJude.searchExport(formSub=self.sJude.bi.yaml_iptJ())
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
