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
@file:      test_salesDetail.py
@time:      2019/2/16 15:57
@desc:
"""

import os
import inspect
import unittest
import ddt
from CenterBackground import GoodsManagement
from tools.excelname.Center.googsMana import CityGoodsPage
from CenterBackground.surfacejude import SurfaceJude
from CenterBackground.judeVerification import JudgmentVerification
from Warehousing.TestStore import StoreDefault
from CenterBackground.GoodsManagement.EnterSales.handle_action_ddt import HandleActionDdt


def read_excle_data():
    GoodsManagement.add_key(GoodsManagement.entersales, GoodsManagement.modetail)
    excle_data = GoodsManagement._excel_Data('序号')
    return excle_data


@ddt.ddt
class TestSalesDetail(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        #
        cls.sales_detail = HandleActionDdt(cls.basename, GoodsManagement.INVENTORY['yaml'])

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]
        cls.sales_detail.screen_set_up('admin_url', 'admin_account', 'admin_password')

        cls.sales_detail.a_click.css_click(cls.sales_detail.driver,
                                     cls.sales_detail.financial['default_to'])

        pass

    @classmethod
    def tearDownClass(cls):
        cls.sales_detail.screen_tear_down(cls)
        pass

    @ddt.data(*read_excle_data())
    def test_modify_operation(self, case):
        """用例场景=:="""
        self.sales_detail.log.fun_name = inspect.stack()[0][3]
        self.sales_detail.log.info("注释开头%s注释结尾" % case['场景'])
        print(case)
        if 'y' in case['执行'] or 'Y' in case['执行']:
            method_way = case.loc['执行方法']
            locator = case.loc['元素']
            way = case.loc['信息']
            method_way = self.function_getattr(method_way)
            method_way(locator, way)
            pass
        else:
            self.sales_detail.log.info("该场景不执行:%s" % case["场景"])

        pass

    def function_getattr(self, fun_attr):
        fun_attr = getattr(self.sales_detail, fun_attr, False)
        return fun_attr
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
