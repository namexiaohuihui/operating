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
@file:      test_noticeScreen.py
@time:      2018/9/25 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import SystemSetting
from CenterBackground.screeningjude import ScreeningJude
from tools.excelname.Center.systemparameter import SystemParameter


class TestNoticeScreen(unittest.TestCase):
    """
    条件筛选
    """

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        config = SystemSetting.add_key(SystemSetting.notice, SystemSetting.select)

        cls.n_Verity = ScreeningJude(config, cls.basename, SystemParameter)

    def setUp(self):
        # 获取运行文件的类名
        self.n_Verity.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.n_Verity.openingProgram()
        self.n_Verity._rou_background()
        pass

    def tearDown(self):
        self.n_Verity.driver.quit()
        self.n_Verity.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_cityDefault(self):
        self.n_Verity.setFunctionName(inspect.stack()[0][3])
        self.n_Verity.value_options_default(selectPath=self.n_Verity.overall[self.n_Verity.bi.whole_keys()])
        pass

    def test_cityTraverse(self):
        self.n_Verity.setFunctionName(inspect.stack()[0][3])
        self.n_Verity.value_option_traverse(formSub=self.n_Verity.bi.yaml_formSub(),
                                            selectPath=self.n_Verity.overall[self.n_Verity.bi.whole_keys()])
        pass

    def test_statusSelect(self):
        self.n_Verity.setFunctionName(inspect.stack()[0][3])
        self.n_Verity.value_options_jude(selectPath=self.n_Verity.overall[self.n_Verity.bi.whole_keys()])
        pass

    def test_statusDefault(self):
        self.n_Verity.setFunctionName(inspect.stack()[0][3])
        self.n_Verity.value_options_default(selectPath=self.n_Verity.overall[self.n_Verity.bi.whole_keys()])
        pass

    def test_statusTraverse(self):
        self.n_Verity.setFunctionName(inspect.stack()[0][3])
        self.n_Verity.value_option_traverse(formSub=self.n_Verity.bi.yaml_formSub(),
                                            selectPath=self.n_Verity.overall[self.n_Verity.bi.whole_keys()])
        pass

    def test_button_search(self):
        self.n_Verity.setFunctionName(inspect.stack()[0][3])
        self.n_Verity.searchExport(formSub=self.n_Verity.bi.yaml_formSub())
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
