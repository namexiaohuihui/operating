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
@file:      test_salesLabel.py
@time:      2019/2/14 16:55
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import GoodsManagement
from tools.excelname.Center.googsMana import CityGoodsPage
from CenterBackground.surfacejude import SurfaceJude


class TestLabel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename

        # 传入子集的key，以及Excel文档中的sheet名字
        config = GoodsManagement.add_key(GoodsManagement.entersales, GoodsManagement.label)
        cls.sales_label = SurfaceJude(config, cls.basename, CityGoodsPage)

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]
        pass

    def setUp(self):
        """
        # # 获取运行文件的类名
        # self.sales_label.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # # 打开浏览器，定义log日志。读取excle文档数据
        # self.sales_label.openingProgram()
        # self.sales_label._rou_background()
        """
        # 将上面注释的内容统一写在一个地方,方便日后统一调用
        self.sales_label.screen_set_up(self.basename)

    def tearDown(self):
        """
        self.sales_label.get_screenshot_image(method_obj=self)
        self.sales_label.driver.quit()
        self.sales_label.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        """

        # 将上面注释的内容统一写在一个地方,方便日后统一调用
        self.sales_label.screen_tear_down(self)
        pass

    def detail_jump_to(self):
        """
        统一编写跳转进入库存明细页面
        :return:
        """
        self.sales_label.vac.css_click(self.sales_label.driver,
                                       self.sales_label.financial[self.sales_label.bi.yaml_default_to()])
        pass

    def log_jump_to(self):
        """
        统一编写跳转进入库存明细页面
        :return:
        """
        self.sales_label.vac.css_click(self.sales_label.driver,
                                       self.sales_label.financial[self.sales_label.bi.yaml_log_to()])
        pass

    # -------------------------------进销库顶部uccess用例-----------------------------
    def test_repertory_success(self):
        self.sales_label.setFunctionName(inspect.stack()[0][3])
        self.sales_label.title_execute()
        pass

    def test_repertory_datas(self):
        self.sales_label.setFunctionName(inspect.stack()[0][3])
        self.sales_label.surface_execute()
        pass

    # -------------------------------库存明细顶部uccess用例-----------------------------
    def test_detail_success(self):
        self.sales_label.setFunctionName(inspect.stack()[0][3])
        self.detail_jump_to()
        self.sales_label.title_execute()
        pass

    def test_detail_datas(self):
        self.sales_label.setFunctionName(inspect.stack()[0][3])
        self.detail_jump_to()
        self.sales_label.surface_execute()
        pass

    # -------------------------------库存变更顶部uccess用例-----------------------------
    def test_log_success(self):
        self.sales_label.setFunctionName(inspect.stack()[0][3])
        self.log_jump_to()
        self.sales_label.title_execute()
        pass

    def test_log_datas(self):
        self.sales_label.setFunctionName(inspect.stack()[0][3])
        self.log_jump_to()
        self.sales_label.surface_execute()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
