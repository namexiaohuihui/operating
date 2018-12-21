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
@file:      test_entranceScreen.py
@time:      2018/9/25 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import GeneralizeAssist
from tools.excelname.Center.generalize import Generalize
from CenterBackground.screeningjude import ScreeningJude


class TestEntranceScreen(unittest.TestCase):
    """
    条件筛选
    """

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        # I pass in the key of the subset, and the sheet name in the Excel document
        config = GeneralizeAssist.add_key(GeneralizeAssist.entrance, GeneralizeAssist.select)

        cls.e_screen = ScreeningJude(config, cls.basename, Generalize)

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]

    def setUp(self):
        # 获取运行文件的类名
        self.e_screen.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.e_screen.openingProgram()
        self.e_screen._rou_background()

    def tearDown(self):
        self.e_screen.get_screenshot_image(method_obj=self)

        self.e_screen.driver.quit()
        self.e_screen.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－其他页面的状态－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_statusSelect(self):
        self.e_screen.setFunctionName(inspect.stack()[0][3])
        self.e_screen.value_options_jude(selectPath=self.e_screen.overall[self.e_screen.bi.whole_keys()])
        pass

    def test_statusDefault(self):
        self.e_screen.setFunctionName(inspect.stack()[0][3])
        self.e_screen.value_options_default(selectPath=self.e_screen.overall[self.e_screen.bi.whole_keys()])
        pass

    def test_statusTraverse(self):
        self.e_screen.setFunctionName(inspect.stack()[0][3])
        self.e_screen.value_option_traverse(formSub=self.e_screen.bi.yaml_formSub(),
                                            selectPath=self.e_screen.overall[self.e_screen.bi.whole_keys()])
        pass

    # -----------------------------------------其他页面的输入框和按钮-------------------------------------------------
    def test_otherInput(self):
        self.e_screen.setFunctionName(inspect.stack()[0][3])
        self.e_screen.attribute_value()
        pass

    def test_button_search(self):
        self.e_screen.setFunctionName(inspect.stack()[0][3])
        self.e_screen.searchExport(formSub=self.e_screen.bi.yaml_formSub())
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
