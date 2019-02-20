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
@file:      test_emptyScreen.py
@time:      2019/2/20 10:27
@desc:
"""
import unittest
import os
import inspect
from CenterBackground import GoodsManagement
from tools.excelname.Center.googsMana import CityGoodsPage
from CenterBackground.screeningjude import ScreeningJude


class TestSalesScreen(unittest.TestCase):

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
        config = GoodsManagement.add_key(GoodsManagement.emptybarrel, GoodsManagement.select)
        cls.empty_screen = ScreeningJude(config, cls.basename, CityGoodsPage)

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]
        pass

    def setUp(self):
        self.empty_screen.screen_set_up(self.basename)
        pass

    def tearDown(self):
        self.empty_screen.screen_tear_down(self)
        pass

    def barrel_empty_to(self, way):
        """
        统一编写跳转页面
        :return:
        """
        fun_attr = "yaml_barrel_%s" % way
        fun_attr = getattr(self.empty_screen.bi, fun_attr, False)
        self.empty_screen.vac.css_click(self.empty_screen.driver,
                                        self.empty_screen.financial[fun_attr()])
        pass

    # -----------------------空桶管理页面:类型下拉框的校验-----------------------
    def test_emptyValSelect(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.empty_screen.value_options_jude(selectPath=self.empty_screen.overall[self.empty_screen.bi.whole_keys()])
        pass

    def test_emptyValDefault(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.empty_screen.value_options_default(selectPath=self.empty_screen.overall[self.empty_screen.bi.whole_keys()])
        pass

    def test_emptyValTraverse(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.empty_screen.value_option_traverse(formSub=self.empty_screen.bi.yaml_formSub(),
                                                selectPath=self.empty_screen.overall[self.empty_screen.bi.whole_keys()])
        pass

    # -----------------------空桶明细页面:账户类型下拉框的校验-----------------------
    def test_emptyTypeSelect(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_detail)
        self.empty_screen.value_options_jude(selectPath=self.empty_screen.overall[self.empty_screen.bi.whole_keys()])
        pass

    def test_emptyTypeDefault(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_detail)
        self.empty_screen.value_options_default(selectPath=self.empty_screen.overall[self.empty_screen.bi.whole_keys()])
        pass

    def test_emptyTypeTraverse(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_detail)
        self.empty_screen.value_option_traverse(formSub=self.empty_screen.bi.yaml_formSub(),
                                                selectPath=self.empty_screen.overall[self.empty_screen.bi.whole_keys()])
        pass

    # -----------------------空桶明细页面:用户类型下拉框的校验-----------------------
    def test_valUserSelect(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_detail)
        self.empty_screen.value_options_jude(selectPath=self.empty_screen.overall[self.empty_screen.bi.whole_keys()])
        pass

    def test_valUserDefault(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_detail)
        self.empty_screen.value_options_default(selectPath=self.empty_screen.overall[self.empty_screen.bi.whole_keys()])
        pass

    def test_valUserTraverse(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_detail)
        self.empty_screen.value_option_traverse(formSub=self.empty_screen.bi.yaml_formSub(),
                                                selectPath=self.empty_screen.overall[self.empty_screen.bi.whole_keys()])
        pass

    # -----------------------空桶明细页面:商品类型下拉框的校验-----------------------
    def test_valGoodsSelect(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_detail)
        self.empty_screen.value_options_jude(selectPath=self.empty_screen.overall[self.empty_screen.bi.whole_keys()])
        pass

    def test_valGoodsDefault(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_detail)
        self.empty_screen.value_options_default(selectPath=self.empty_screen.overall[self.empty_screen.bi.whole_keys()])
        pass

    def test_valGoodsTraverse(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_detail)
        self.empty_screen.value_option_traverse(formSub=self.empty_screen.bi.yaml_formSub(),
                                                selectPath=self.empty_screen.overall[self.empty_screen.bi.whole_keys()])
        pass

    # -----------------------空桶日志页面:变更类型下拉框的校验-----------------------
    def test_logTypeSelect(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_logs)
        self.empty_screen.value_options_jude(selectPath=self.empty_screen.overall[self.empty_screen.bi.whole_keys()])
        pass

    def test_logTypeDefault(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_logs)
        self.empty_screen.value_options_default(selectPath=self.empty_screen.overall[self.empty_screen.bi.whole_keys()])
        pass

    def test_logTypeTraverse(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_logs)
        self.empty_screen.value_option_traverse(formSub=self.empty_screen.bi.yaml_formSub(),
                                                selectPath=self.empty_screen.overall[self.empty_screen.bi.whole_keys()])
        pass

    # -----------------------空桶日志页面:用户下拉框的校验-----------------------
    def test_logUserSelect(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_logs)
        self.empty_screen.value_options_jude(selectPath=self.empty_screen.overall[self.empty_screen.bi.whole_keys()])
        pass

    def test_logUserDefault(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_logs)
        self.empty_screen.value_options_default(selectPath=self.empty_screen.overall[self.empty_screen.bi.whole_keys()])
        pass

    def test_logUserTraverse(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_logs)
        self.empty_screen.value_option_traverse(formSub=self.empty_screen.bi.yaml_formSub(),
                                                selectPath=self.empty_screen.overall[self.empty_screen.bi.whole_keys()])
        pass

    # -----------------------空桶日志页面:关键字下拉框的校验-----------------------
    def test_logKeySelect(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_logs)
        self.empty_screen.value_options_jude(selectPath=self.empty_screen.overall[self.empty_screen.bi.whole_keys()])
        pass

    def test_logKeyDefault(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_logs)
        self.empty_screen.value_options_default(selectPath=self.empty_screen.overall[self.empty_screen.bi.whole_keys()])
        pass

    def test_logKeyTraverse(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_logs)
        self.empty_screen.value_option_traverse(formSub=self.empty_screen.bi.yaml_formSub(),
                                                selectPath=self.empty_screen.overall[self.empty_screen.bi.whole_keys()])
        pass

    # -----------------------空桶管理:关键字输入框的校验-----------------------
    def test_emptyInput(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        # 进入库存明细页面
        self.empty_screen.attribute_value()
        pass

    # -----------------------空桶明细页面:用户类型输入框的校验-----------------------
    def test_detailUser(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_detail)
        # 进入库存明细页面
        self.empty_screen.attribute_value()
        pass

    # -----------------------空桶明细页面:商品类型输入框的校验-----------------------
    def test_detailGoods(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_detail)
        # 进入库存明细页面
        self.empty_screen.attribute_value()
        pass

    # -----------------------库存变更:用户类型输入框默认值的校验-----------------------
    def test_logUser(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_logs)
        # 进入库存明细页面
        self.empty_screen.attribute_value()
        pass

    # -----------------------库存变更:关键字输入框默认值的校验-----------------------
    def test_logKeys(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_logs)
        # 进入库存明细页面
        self.empty_screen.attribute_value()
        pass

    # -----------------------库存变更:时间选择框框默认值的校验-----------------------
    def test_logtimeChoose(self):
        """用例场景=:="""
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_logs)
        # 进入库存明细页面
        self.empty_screen.attribute_value('value')
        pass

    # -----------------------三个页面的搜索以及导出按钮-----------------------
    def test_empty_search(self):
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.empty_screen.searchExport(formSub=self.empty_screen.bi.yaml_formSub())
        pass

    def test_empty_export(self):
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.empty_screen.searchExport(formSub=self.empty_screen.bi.yaml_formSub())
        pass

    def test_detail_search(self):
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_detail)
        self.empty_screen.searchExport(formSub=self.empty_screen.bi.yaml_formSub())
        pass

    def test_detail_export(self):
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_detail)
        self.empty_screen.searchExport(formSub=self.empty_screen.bi.yaml_formSub())
        pass

    def test_log_search(self):
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_logs)
        self.empty_screen.searchExport(formSub=self.empty_screen.bi.yaml_formSub())
        pass

    def test_log_export(self):
        self.empty_screen.setFunctionName(inspect.stack()[0][3])
        self.barrel_empty_to(self.jump_logs)
        self.empty_screen.searchExport(formSub=self.empty_screen.bi.yaml_formSub())
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
