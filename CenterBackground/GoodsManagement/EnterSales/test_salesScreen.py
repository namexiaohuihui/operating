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
@file:      test_salesScreen.py
@time:      2019/2/14 11:39
@desc:
"""
import unittest
import os
import inspect
from CenterBackground import GoodsManagement
from tools.excelname.Center.googsMana import CityGoodsPage
from CenterBackground.screeningjude import ScreeningJude


class TestSalesScreen(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename

        # 传入子集的key，以及Excel文档中的sheet名字
        config = GoodsManagement.add_key(GoodsManagement.entersales, GoodsManagement.select)
        cls.sales_screen = ScreeningJude(config, cls.basename, CityGoodsPage)

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]
        pass

    def setUp(self):
        self.sales_screen.screen_set_up(self.basename)
        pass

    def tearDown(self):
        self.sales_screen.screen_tear_down(self)
        pass

    def detail_jump_to(self):
        """
        统一编写跳转进入库存明细页面
        :return:
        """
        self.sales_screen.vac.css_click(self.sales_screen.driver,
                                        self.sales_screen.financial[self.sales_screen.bi.yaml_default_to()])
        pass

    def log_jump_to(self):
        """
        统一编写跳转进入库存变更日志页面
        :return:
        """
        self.sales_screen.vac.css_click(self.sales_screen.driver,
                                        self.sales_screen.financial[self.sales_screen.bi.yaml_log_to()])
        pass

    # -----------------------库存明细页面:类型下拉框的校验-----------------------
    def test_detailUserTypeSelect(self):
        """用例场景=:="""
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        # 打印场景,便于文档显示
        # 进入库存明细页面
        self.detail_jump_to()
        self.sales_screen.value_options_jude(selectPath=self.sales_screen.overall[self.sales_screen.bi.whole_keys()])
        pass

    def test_detailUserTypeDefault(self):
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        # 进入库存明细页面
        self.detail_jump_to()
        self.sales_screen.value_options_default(selectPath=self.sales_screen.overall[self.sales_screen.bi.whole_keys()])
        pass

    def test_detailUserTypeTraverse(self):
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        # 进入库存明细页面
        self.detail_jump_to()
        self.sales_screen.value_option_traverse(formSub=self.sales_screen.bi.yaml_formSub(),
                                                selectPath=self.sales_screen.overall[self.sales_screen.bi.whole_keys()])
        pass

    # -----------------------库存变更页面:变更方式框的校验-----------------------
    def test_logChangeSelect(self):
        """用例场景=:="""
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        # 打印场景,便于文档显示
        # 进入库存明细页面
        self.log_jump_to()
        self.sales_screen.value_options_jude(selectPath=self.sales_screen.overall[self.sales_screen.bi.whole_keys()])
        pass

    def test_logChangeDefault(self):
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        # 进入库存明细页面
        self.log_jump_to()
        self.sales_screen.value_options_default(selectPath=self.sales_screen.overall[self.sales_screen.bi.whole_keys()])
        pass

    def test_logChangeTraverse(self):
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        # 进入库存明细页面
        self.log_jump_to()
        self.sales_screen.value_option_traverse(formSub=self.sales_screen.bi.yaml_formSub(),
                                                selectPath=self.sales_screen.overall[self.sales_screen.bi.whole_keys()])
        pass

    # -----------------------库存变更页面: 变更类型框的校验-----------------------
    def test_logTypeSelect(self):
        """用例场景=:="""
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        # 打印场景,便于文档显示
        # 进入库存明细页面
        self.log_jump_to()
        self.sales_screen.value_options_jude(selectPath=self.sales_screen.overall[self.sales_screen.bi.whole_keys()])
        pass

    def test_logTypeDefault(self):
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        # 进入库存明细页面
        self.log_jump_to()
        self.sales_screen.value_options_default(selectPath=self.sales_screen.overall[self.sales_screen.bi.whole_keys()])
        pass

    def test_logTypeTraverse(self):
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        # 进入库存明细页面
        self.log_jump_to()
        self.sales_screen.value_option_traverse(formSub=self.sales_screen.bi.yaml_formSub(),
                                                selectPath=self.sales_screen.overall[self.sales_screen.bi.whole_keys()])
        pass

    # -----------------------进销库页面:时间输入框的校验-----------------------
    def test_othertimeInput(self):
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        self.sales_screen.time_value_jump('ym')
        pass

    # -----------------------进销库页面:关键字输入框的校验-----------------------
    def test_conditionsInput(self):
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        self.sales_screen.attribute_value()
        pass

    # -----------------------库存明细页面:用户输入的校验-----------------------
    def test_detail_user(self):
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        # 进入库存明细页面
        self.detail_jump_to()
        self.sales_screen.attribute_value()
        pass

    # -----------------------库存明细页面:商品输入框的校验-----------------------
    def test_detail_goods(self):
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        # 进入库存明细页面
        self.detail_jump_to()
        self.sales_screen.attribute_value()
        pass

    # -----------------------库存变更:时间输入框的校验-----------------------
    def test_logtimeValue(self):
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        # 进入库存明细页面
        self.log_jump_to()
        self.sales_screen.attribute_value('value')
        pass

    # -----------------------库存变更:用户输入框的校验-----------------------
    def test_log_user(self):
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        # 进入库存明细页面
        self.log_jump_to()
        self.sales_screen.attribute_value()
        pass

    # -----------------------库存变更:商品输入框的校验-----------------------
    def test_log_goods(self):
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        # 进入库存明细页面
        self.log_jump_to()
        self.sales_screen.attribute_value()
        pass

    # -----------------------三个页面的搜索以及导出按钮-----------------------
    def test_button_search(self):
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        self.sales_screen.searchExport(formSub=self.sales_screen.bi.yaml_formSub())
        pass

    def test_button_export(self):
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        self.sales_screen.searchExport(formSub=self.sales_screen.bi.yaml_formSub())
        pass

    def test_detail_search(self):
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        self.detail_jump_to()
        self.sales_screen.searchExport(formSub=self.sales_screen.bi.yaml_formSub())
        pass

    def test_detail_export(self):
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        self.detail_jump_to()
        self.sales_screen.searchExport(formSub=self.sales_screen.bi.yaml_formSub())
        pass

    def test_log_search(self):
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        self.log_jump_to()
        self.sales_screen.searchExport(formSub=self.sales_screen.bi.yaml_formSub())
        pass

    def test_log_export(self):
        self.sales_screen.setFunctionName(inspect.stack()[0][3])
        self.log_jump_to()
        self.sales_screen.searchExport(formSub=self.sales_screen.bi.yaml_formSub())
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
