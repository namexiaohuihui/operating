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
@file:      test_depositLabel.py
@time:      2019/2/23 11:03
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import GoodsManagement
from tools.excelname.Center.googsMana import CityGoodsPage
from CenterBackground.surfacejude import SurfaceJude


class TestDepositLabel(unittest.TestCase):
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
        config = GoodsManagement.add_key(GoodsManagement.barrelsdeposit, GoodsManagement.label)
        cls.deposit_label = SurfaceJude(config, cls.basename, CityGoodsPage)

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]
        pass

    def setUp(self):
        self.deposit_label.screen_set_up(self.basename)
        pass

    def tearDown(self):
        self.deposit_label.screen_tear_down(self)
        pass

    def jump_tabs_specified(self, path):
        specified = self.deposit_label.financial[self.deposit_label.bi.yaml_tabs()]
        specified = '%s:nth-child(%s)' % (specified, path)
        self.deposit_label.vac.css_click(self.deposit_label.driver, specified)
        pass

    def deposit_title_execute(self, function, path=0) -> "获取列表头部标题的统一调用处":
        """用例场景=:="""
        if path > 0 and path < 4:
            # 判断是否要先进入指定位置的tab
            self.jump_tabs_specified(path)
        self.deposit_label.setFunctionName(function)
        self.deposit_label.title_execute()
        pass

    def deposit_surface_execute(self, function, path=0) -> "获取列表信息的统一调用处":
        """用例场景=:="""
        if path > 0 and path < 4:
            # 判断是否要先进入指定位置的tab
            self.jump_tabs_specified(path)
        self.deposit_label.setFunctionName(function)
        self.deposit_label.surface_execute()
        pass

    # -------------------------------桶押金顶部success用例-----------------------------
    def test_deposit_success(self):
        self.deposit_title_execute(inspect.stack()[0][3])
        pass

    def test_deposit_datas(self):
        self.deposit_surface_execute(inspect.stack()[0][3])
        pass

    # -------------------------------押金明细顶部success用例-----------------------------
    def test_detail_success(self):
        self.deposit_title_execute(inspect.stack()[0][3], 2)
        pass

    def test_detail_datas(self):
        self.deposit_surface_execute(inspect.stack()[0][3], 2)
        pass

    # -------------------------------退桶记录顶部success用例-----------------------------
    def test_record_success(self):
        self.deposit_title_execute(inspect.stack()[0][3], 3)
        pass

    def test_record_datas(self):
        self.deposit_surface_execute(inspect.stack()[0][3], 3)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
