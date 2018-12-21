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
@file:      test_feedbackLabel.py
@time:      2018/9/19 16:43
@desc:
"""
import os
import inspect
import unittest

from CenterBackground import GeneralizeAssist
from CenterBackground.mutuallyJude import MutuallyJude
from tools.excelname.Center.generalize import Generalize


class TestFeedbackLabel(unittest.TestCase):
    """
    页面展示项的标题
    """

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        # I pass in the key of the subset, and the sheet name in the Excel document
        config = GeneralizeAssist.add_key(GeneralizeAssist.feedback, GeneralizeAssist.page)
        cls.f_label = MutuallyJude(config, cls.basename, Generalize)
        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]

    def setUp(self):
        # 获取运行文件的类名
        self.f_label.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.f_label.openingProgram()
        self.f_label._rou_background()

    def tearDown(self):
        self.f_label.get_screenshot_image(method_obj=self)
        self.f_label.driver.quit()
        self.f_label.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_showTitle(self):
        self.f_label.setFunctionName(inspect.stack()[0][3])
        self.f_label.title_execute()
        pass

    def test_showSurface(self):
        self.f_label.setFunctionName(inspect.stack()[0][3])
        self.f_label.surface_execute()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
