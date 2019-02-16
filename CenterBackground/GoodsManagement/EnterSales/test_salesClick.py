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
@file:      test_salesClick.py
@time:      2019/2/15 11:04
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
    GoodsManagement.add_key(GoodsManagement.entersales, GoodsManagement.jump)
    excle_data = GoodsManagement._excel_Data('序号')
    return excle_data


@ddt.ddt
class TestDataClick(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        #
        cls.handle = HandleActionDdt(cls.basename, GoodsManagement.INVENTORY['yaml'])

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]

        pass

    def setUp(self):
        self.handle.screen_set_up('admin_url', 'admin_account', 'admin_password')
        pass

    def tearDown(self):
        self.handle.screen_tear_down(self)
        pass

    @ddt.data(*read_excle_data())
    def test_click_jump(self, case):
        """用例场景=:="""
        self.handle.log.info("注释开头%s注释结尾" % case['场景'])
        self.handle.log.fun_name = inspect.stack()[0][3]
        if 'y' in case['进入'] or 'Y' in case['进入']:
            self.handle.element_click_jump(case['位置'])
            pass
        self.handle.element_click_jump(case['元素'])
        text_title = case['标题']
        title_key = str.split(text_title, ':')[0]
        title_value = str.split(text_title, ':')[-1]
        self.handle.element_text(title_key, title_value)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
