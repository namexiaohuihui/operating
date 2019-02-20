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
@file:      test_emptyLabel.py
@time:      2019/2/20 11:10
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import GoodsManagement
from tools.excelname.Center.googsMana import CityGoodsPage
from CenterBackground.surfacejude import SurfaceJude


class TestEmptyLabel(unittest.TestCase):
    # 跳转到明细页面关键字定义
    jump_detail = "detail"
    # 跳转到日志页面关键字定义
    jump_logs = "logs"

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename

        # 传入子集的key，以及Excel文档中的sheet名字
        config = GoodsManagement.add_key(GoodsManagement.emptybarrel, GoodsManagement.label)
        cls.empty_label = SurfaceJude(config, cls.basename, CityGoodsPage)

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]
        pass

    def setUp(self):
        self.empty_label.screen_set_up(self.basename)
        pass

    def tearDown(self):
        self.empty_label.screen_tear_down(self)
        pass

    def barrel_empty_to(self, way):
        """
        统一编写跳转页面
        :return:
        """
        fun_attr = "yaml_barrel_%s" % way
        fun_attr = getattr(self.empty_label.bi, fun_attr, False)
        self.empty_label.vac.css_click(self.empty_label.driver,
                                        self.empty_label.financial[fun_attr()])
        pass

    # -------------------------------进销库顶部success用例-----------------------------
    def test_empty_success(self):
        self.empty_label.setFunctionName(inspect.stack()[0][3])
        self.empty_label.title_execute()
        pass

    def test_empty_datas(self):
        self.empty_label.setFunctionName(inspect.stack()[0][3])
        self.empty_label.surface_execute()
        pass

    # -------------------------------库存明细顶部success用例-----------------------------
    def test_detail_success(self):
        self.empty_label.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_detail)
        self.empty_label.title_execute()
        pass

    def test_detail_datas(self):
        self.empty_label.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_detail)
        self.empty_label.surface_execute()
        pass

    # -------------------------------库存变更顶部success用例-----------------------------
    def test_log_success(self):
        self.empty_label.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_logs)
        self.empty_label.title_execute()
        pass

    def test_log_datas(self):
        self.empty_label.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_logs)
        self.empty_label.surface_execute()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
