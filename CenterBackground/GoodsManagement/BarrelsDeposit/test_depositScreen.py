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
@file:      test_depositScreen.py
@time:      2019/2/23 10:24
@desc:
"""
import unittest
import os
import inspect
from CenterBackground import GoodsManagement
from tools.excelname.Center.googsMana import CityGoodsPage
from CenterBackground.screeningjude import ScreeningJude


class TestDepositScreen(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename

        # 传入子集的key，以及Excel文档中的sheet名字
        config = GoodsManagement.add_key(GoodsManagement.barrelsdeposit, GoodsManagement.select)
        cls.deposit_screen = ScreeningJude(config, cls.basename, CityGoodsPage)

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]
        pass

    def setUp(self):
        self.deposit_screen.screen_set_up(self.basename)
        pass

    def tearDown(self):
        self.deposit_screen.screen_tear_down(self)
        pass

    def jump_tabs_specified(self, path):
        specified = self.deposit_screen.financial[self.deposit_screen.bi.yaml_tabs()]
        specified = '%s:nth-child(%s)' % (specified, path)
        self.deposit_screen.vac.css_click(self.deposit_screen.driver, specified)
        pass

    def select_all_option(self, function, path=0):
        """
        获取select的全部元素信息统一调用地
        :param path:
        :return:
        """
        if path > 0 and path < 4:
            # 判断是否要先进入指定位置的tab
            self.jump_tabs_specified(path)
        self.deposit_screen.setFunctionName(function)
        self.deposit_screen.value_options_jude(
            selectPath=self.deposit_screen.overall[self.deposit_screen.bi.whole_keys()])
        pass

    def select_default(self, function, path=0):
        """
        获取select默认显示的option
        :return:
        """
        if path > 0 and path < 4:
            # 判断是否要先进入指定位置的tab
            self.jump_tabs_specified(path)
        self.deposit_screen.setFunctionName(function)
        self.deposit_screen.value_options_default(
            selectPath=self.deposit_screen.overall[self.deposit_screen.bi.whole_keys()])
        pass

    def select_traverse(self, function, path=0):
        """
        遍历点击select中的option
        :return:
        """
        if path > 0 and path < 4:
            # 判断是否要先进入指定位置的tab
            self.jump_tabs_specified(path)
        self.deposit_screen.setFunctionName(function)
        self.deposit_screen.value_option_traverse(
            formSub=self.deposit_screen.bi.yaml_jiptformsub(),
            selectPath=self.deposit_screen.overall[self.deposit_screen.bi.whole_keys()]
        )
        pass

    def keyInput_timeChooser(self, function, attribute='placeholder', path=0):
        """
        获取输入框或者时间选择器默认显示值的统一调用处
        :return:
        """
        if 0 < path < 4:
            # 判断是否要先进入指定位置的tab
            self.jump_tabs_specified(path)
        self.deposit_screen.setFunctionName(function)
        # 进入库存明细页面
        self.deposit_screen.attribute_value(attribute)
        pass

    def button_search_export(self, function, path=0):
        """用例场景=:="""
        if 0 < path < 4:
            # 判断是否要先进入指定位置的tab
            self.jump_tabs_specified(path)
        self.deposit_screen.setFunctionName(function)
        # 进入库存明细页面
        self.deposit_screen.searchExport(formSub=self.deposit_screen.bi.yaml_jiptformsub())
        pass

    # -----------------------桶押金管理页面:类型下拉校验-----------------------
    def test_depositValSelect(self):
        """用例场景=:="""
        self.select_all_option(inspect.stack()[0][3])
        pass

    def test_depositValDefault(self):
        """用例场景=:="""
        self.select_default(inspect.stack()[0][3])
        pass

    def test_depositValTraverse(self):
        """用例场景=:="""
        self.select_traverse(inspect.stack()[0][3])
        pass

    # -----------------------押金明细页面:状态下拉校验-----------------------
    def test_detailStatusSelect(self):
        """用例场景=:="""
        self.select_all_option(inspect.stack()[0][3], 2)
        pass

    def test_detailStatusDefault(self):
        """用例场景=:="""
        self.select_default(inspect.stack()[0][3], 2)
        pass

    def test_detailStatusTraverse(self):
        """用例场景=:="""
        self.select_traverse(inspect.stack()[0][3], 2)
        pass

    # -----------------------押金明细页面:关键字下拉校验-----------------------
    def test_detailValSelect(self):
        """用例场景=:="""
        self.select_all_option(inspect.stack()[0][3], 2)
        pass

    def test_detailValDefault(self):
        """用例场景=:="""
        self.select_default(inspect.stack()[0][3], 2)
        pass

    def test_detailValTraverse(self):
        """用例场景=:="""
        self.select_traverse(inspect.stack()[0][3], 2)
        pass

    # -----------------------退桶记录页面:退桶方式下拉校验-----------------------
    def test_recordPaymentSelect(self):
        """用例场景=:="""
        self.select_all_option(inspect.stack()[0][3], 3)
        pass

    def test_recordPaymentDefault(self):
        """用例场景=:="""
        self.select_default(inspect.stack()[0][3], 3)
        pass

    def test_recordPaymentTraverse(self):
        """用例场景=:="""
        self.select_traverse(inspect.stack()[0][3], 3)
        pass

    # -----------------------退桶记录页面:关键字下拉校验-----------------------
    def test_recordValSelect(self):
        """用例场景=:="""
        self.select_all_option(inspect.stack()[0][3], 3)
        pass

    def test_recordValDefault(self):
        """用例场景=:="""
        self.select_default(inspect.stack()[0][3], 3)
        pass

    def test_recordValTraverse(self):
        """用例场景=:="""
        self.select_traverse(inspect.stack()[0][3], 3)
        pass

    # ------------------------桶押金页面关键字输入框---------------------------
    def test_depositInput(self):
        """用例场景=:="""
        self.keyInput_timeChooser(inspect.stack()[0][3])
        pass

    # -----------------------桶押金明细页面关键字输入框及时间选择器--------------
    def test_detailInput(self):
        """用例场景=:="""
        self.keyInput_timeChooser(inspect.stack()[0][3], path=2)
        pass

    def test_detailTime(self):
        """用例场景=:="""
        self.keyInput_timeChooser(inspect.stack()[0][3], path=2, attribute='value')
        pass

    # -----------------------桶押金明细页面关键字输入框及时间选择器--------------
    def test_recordInput(self):
        """用例场景=:="""
        self.keyInput_timeChooser(inspect.stack()[0][3], path=3)
        pass

    def test_recordTime(self):
        """用例场景=:="""
        self.keyInput_timeChooser(inspect.stack()[0][3], path=3, attribute='value')
        pass

    # -----------------------三个页面的搜索以及导出按钮-----------------------
    def test_depositSearch(self):
        self.button_search_export(inspect.stack()[0][3])
        pass

    def test_depositExport(self):
        self.button_search_export(inspect.stack()[0][3])
        pass

    def test_detailSearch(self):
        self.button_search_export(inspect.stack()[0][3], 2)
        pass

    def test_detailExport(self):
        self.button_search_export(inspect.stack()[0][3], 2)
        pass

    def test_recordSearch(self):
        self.button_search_export(inspect.stack()[0][3], 3)
        pass

    def test_recordExport(self):
        self.button_search_export(inspect.stack()[0][3], 3)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
