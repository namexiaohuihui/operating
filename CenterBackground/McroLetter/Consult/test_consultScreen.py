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
@file:      test_consultScreen.py
@time:      2018/9/25 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import McroLetter
from CenterBackground.screeningjude import ScreeningJude
from tools.excelname.Center.mcroletterwechat import McroLetterWechat


class TestConsultScreen(unittest.TestCase):
    """
    条件筛选
    """

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        config = McroLetter.add_key(McroLetter.consult, McroLetter.select)
        cls.c_screen = ScreeningJude(config, cls.basename, McroLetterWechat)

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]
        pass

    def setUp(self):
        # 获取运行文件的类名
        self.c_screen.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.c_screen.openingProgram()
        self.c_screen._rou_background()
        pass

    def tearDown(self):
        self.c_screen.get_screenshot_image(method_obj=self)

        self.c_screen.driver.quit()
        self.c_screen.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－进行中的数据信息－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_statusSelect(self):
        self.c_screen.setFunctionName(inspect.stack()[0][3])
        self.c_screen.value_options_jude(selectPath=self.c_screen.overall[self.c_screen.bi.whole_keys()])
        pass

    def test_statusDefault(self):
        self.c_screen.setFunctionName(inspect.stack()[0][3])
        self.c_screen.value_options_default(selectPath=self.c_screen.overall[self.c_screen.bi.whole_keys()])
        pass

    def test_statusTraverse(self):
        self.c_screen.setFunctionName(inspect.stack()[0][3])
        self.c_screen.value_option_traverse(formSub=self.c_screen.bi.yaml_formSub(),
                                            selectPath=self.c_screen.overall[self.c_screen.bi.whole_keys()])
        pass

    def test_typeSelect(self):
        self.c_screen.setFunctionName(inspect.stack()[0][3])
        self.c_screen.value_options_jude(selectPath=self.c_screen.overall[self.c_screen.bi.whole_keys()])
        pass

    def test_typeDefault(self):
        self.c_screen.setFunctionName(inspect.stack()[0][3])
        self.c_screen.value_options_default(selectPath=self.c_screen.overall[self.c_screen.bi.whole_keys()])
        pass

    def test_typeTraverse(self):
        self.c_screen.setFunctionName(inspect.stack()[0][3])
        self.c_screen.value_option_traverse(formSub=self.c_screen.bi.yaml_formSub(),
                                            selectPath=self.c_screen.overall[self.c_screen.bi.whole_keys()])
        pass

    def test_otherInput(self):
        self.c_screen.setFunctionName(inspect.stack()[0][3])
        self.c_screen.attribute_value()
        pass

    def test_starttime(self):
        self.c_screen.setFunctionName(inspect.stack()[0][3])
        self.c_screen.attribute_value()
        pass

    def test_endtime(self):
        self.c_screen.setFunctionName(inspect.stack()[0][3])
        self.c_screen.attribute_value()
        pass

    def test_button_search(self):
        self.c_screen.setFunctionName(inspect.stack()[0][3])
        self.c_screen.searchExport(formSub=self.c_screen.bi.yaml_formSub())
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
