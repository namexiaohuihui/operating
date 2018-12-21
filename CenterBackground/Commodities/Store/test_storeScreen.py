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
@file:      test_storeScreen.py
@time:      2018/8/31 15:35
@desc:
'''
import os
import inspect
import unittest
from CenterBackground import Commodities
from CenterBackground.screeningjude import ScreeningJude
from tools.excelname.Center.bundledItems import BundledItems


class TestStoreScreen(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 读取包名
        basedir = os.path.split(os.path.dirname(__file__))[1]
        # 读取文件名
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basedir + "-" + cls.basename

        # 读取配置所在文件
        config = Commodities.add_key(Commodities.store, Commodities.select)
        cls.sJude = ScreeningJude(config, cls.basename, BundledItems)

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]
        pass

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        self.sJude.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        self.sJude.openingProgram()
        self.sJude._rou_background()
        # 定义后面使用的参数,到时候会进行回收
        pass

    def tearDown(self):
        self.sJude.get_screenshot_image(method_obj=self)

        self.sJude.driver.quit()
        self.sJude.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－状态－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_statusSelect(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])

        # 定义后面使用的参数,到时候会进行回收
        select_path = self.sJude.overall[self.sJude.bi.whole_keys()]
        self.sJude.value_options_jude(selectPath=select_path)
        pass

    def test_statusDefault(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        select_path = self.sJude.overall[self.sJude.bi.whole_keys()]
        self.sJude.value_options_default(selectPath=select_path)
        pass

    def test_statusTraverse(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        select_path = self.sJude.overall[self.sJude.bi.whole_keys()]
        form_sub = self.sJude.bi.yaml_formSub()
        self.sJude.value_option_traverse(formSub=form_sub, selectPath=select_path)
        pass

        # －－－－－－－－－－－－－－－－－－－－－－－－其他－－－－－－－－－－－－－－－－－－－－－－－－－－

    def test_chooseSelect(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        select_path = self.sJude.overall[self.sJude.bi.whole_keys()]
        self.sJude.value_options_jude(selectPath=select_path)
        pass

    def test_chooseDefault(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        select_path = self.sJude.overall[self.sJude.bi.whole_keys()]
        self.sJude.value_options_default(selectPath=select_path)
        pass

    def test_chooseTraverse(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        select_path = self.sJude.overall[self.sJude.bi.whole_keys()]
        form_sub = self.sJude.bi.yaml_formSub()
        self.sJude.value_option_traverse(formSub=form_sub, selectPath=select_path)
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
        form_sub = self.sJude.bi.yaml_formSub()
        self.sJude.searchExport(formSub=form_sub)
        pass

    def test_button_export(self):
        self.sJude.setFunctionName(inspect.stack()[0][3])
        form_sub = self.sJude.bi.yaml_formSub()
        self.sJude.searchExport(formSub=form_sub)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
