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
@file:      test_depositTabel.py
@time:      2019/2/22 15:36
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import GoodsManagement
from tools.excelname.Center.googsMana import CityGoodsPage
from CenterBackground.commoditiesJude import CommoditiesJude


class TestBarrelsDeposit(unittest.TestCase):
    """
    城市商品tab
    """
    BUTTON_REDUCE_NUMBER = 0

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename

        # 传入子集的key，以及Excel文档中的sheet名字
        config = GoodsManagement.add_key(GoodsManagement.barrelsdeposit, GoodsManagement.city)
        cls.deposit_city = CommoditiesJude(config, cls.basename, CityGoodsPage)

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]
        pass

    def setUp(self):
        self.deposit_city.screen_set_up(self.basename)
        pass

    def tearDown(self):
        self.deposit_city.screen_tear_down(self)
        pass

    def jump_tabs_specified(self, path):
        specified = self.deposit_city.financial[self.deposit_city.bi.yaml_tabs()]
        specified = '%s:nth-child(%s)' % (specified, path)
        self.deposit_city.vac.css_click(self.deposit_city.driver, specified)
        pass

    def active_tab(self, function):
        """获取默认tab/city的统一调用处"""
        self.deposit_city.setFunctionName(function)
        self.deposit_city.active_city('class')
        pass

    def already_tabs(self, function):
        """获取全部tab/city的统一调用处"""
        self.deposit_city.setFunctionName(function)
        self.deposit_city.already_citys(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def switch_tab(self, function):
        """点击tab/click的统一调用处"""
        self.deposit_city.setFunctionName(function)
        self.deposit_city.switch_city(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def switch_url(self, function):
        """通过tab/city的url进行切换的统一调用处"""
        self.deposit_city.setFunctionName(function)
        self.deposit_city.switch_url('class', reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    # ---------------------点击菜单之后,默认数据校验---------------------------
    def test_active_tab(self):
        """
        寻找默认值
        :return:
        """
        self.active_tab(inspect.stack()[0][3])
        pass

    def test_already_tabs(self):
        """
        比较tabs中的全部信息
        :return:
        """
        self.already_tabs(inspect.stack()[0][3])
        pass

    def test_switch_tab(self):
        """
        遍历点击tab
        :return:
        """
        self.switch_tab(inspect.stack()[0][3])
        pass

    def test_switch_url(self):
        """
        通过tabs的url进行切换
        :return:
        """
        self.switch_url(inspect.stack()[0][3])
        pass

    # ----------------------------点击tab切换之后,页面city校验---------------
    def test_detail_default_city(self):
        """用例场景=:="""
        # 进入明细页面
        self.jump_tabs_specified(2)
        self.active_tab(inspect.stack()[0][3])
        pass

    def test_detail_citys(self):
        """用例场景=:="""
        # 进入明细页面
        self.jump_tabs_specified(2)
        self.already_tabs(inspect.stack()[0][3])

    def test_detail_click_city(self):
        self.jump_tabs_specified(2)
        self.switch_tab(inspect.stack()[0][3])

    def test_detail_switch_url(self):
        self.jump_tabs_specified(2)
        self.switch_url(inspect.stack()[0][3])

    # ----------------------------点击tab切换之后,页面city校验---------------
    def test_record_default_city(self):
        """用例场景=:="""
        # 进入记录页面
        self.jump_tabs_specified(3)
        self.active_tab(inspect.stack()[0][3])
        pass

    def test_record_citys(self):
        """用例场景=:="""
        # 进入记录页面
        self.jump_tabs_specified(3)
        self.already_tabs(inspect.stack()[0][3])

    def test_record_click_city(self):
        """用例场景=:="""
        # 进入记录页面
        self.jump_tabs_specified(3)
        self.switch_tab(inspect.stack()[0][3])

    def test_record_switch_url(self):
        """用例场景=:="""
        self.jump_tabs_specified(3)
        # 进入记录页面
        self.switch_url(inspect.stack()[0][3])


if __name__ == '__main__':
    unittest.main(verbosity=2)
