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
@file:      test_relationLabel.py
@time:      2018/9/19 16:43
@desc:
"""
import os
import inspect
import unittest

from CenterBackground import GeneralizeAssist
from CenterBackground.surfacejude import SurfaceJude
from tools.excelname.Center.generalize import Generalize


class TestRelationLabel(unittest.TestCase):
    """
    页面展示项的标题
    """
    INVITE_DESIGNATED_HISTORY = "历史数据"

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename

        # 传入子集的key，以及Excel文档中的sheet名字
        config = GeneralizeAssist.add_key(GeneralizeAssist.relation, GeneralizeAssist.page)
        cls.rt_label = SurfaceJude(config, cls.basename, Generalize)
        cls.INVITE_DESIGNATED_TABS = cls.rt_label.bi.yaml_tabs()

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]
        pass

    def setUp(self):
        # 获取运行文件的类名
        self.rt_label.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.rt_label.openingProgram()
        self.rt_label._rou_background()

    def tearDown(self):
        self.rt_label.get_screenshot_image(method_obj=self)
        self.rt_label.driver.quit()
        self.rt_label.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_ongoingTitle(self):
        self.rt_label.setFunctionName(inspect.stack()[0][3])
        self.rt_label.title_execute()
        pass

    def test_ongoingSurface(self):
        self.rt_label.setFunctionName(inspect.stack()[0][3])
        self.rt_label.surface_execute()
        pass

    def test_historyTitle(self):
        self.rt_label.setFunctionName(inspect.stack()[0][3])
        self.rt_label.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_HISTORY)
        self.rt_label.title_execute()
        pass

    def test_historySurface(self):
        self.rt_label.setFunctionName(inspect.stack()[0][3])
        self.rt_label.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_HISTORY)
        self.rt_label.surface_execute()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
