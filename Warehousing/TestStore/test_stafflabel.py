# -*- coding: utf-8 -*-
#                        _oo0oo_
#                       o8888888o
#                       88" . "88
#                       (| -_- |)
#                       0\  =  /0
#                     ___/`---'\___
#                   .' \\|     |// '.
#                  / \\|||  :  |||// \
#                 / _||||| -:- |||||- \
#                |   | \\\  -  /// |   |
#                | \_|  ''\---/''  |_/ |
#                \  .-\__  '-'  ___/-. /
#              ___'. .'  /--.--\  `. .'___
#           ."" '<  `.___\_<|>_/___.' >' "".
#          | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#          \  \ `_.   \_ __\ /__ _/   .-` /  /
#      =====`-.____`.___ \_____/___.-`___.-'=====
#                         `=---='
#
#
#      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                佛祖保佑         永无BUG
# @author:    ln_company
# @license:   (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
# @Software:  PyCharm
# @file:      test_stafflabel.py
# @time:      2018/12/17 16:23
# @desc:
import unittest
import time
import os
from tools.browser_establish import browser_confirm
import ddt
from Warehousing.TestStore import StoreDefault
from Warehousing.handle_action import HandleAction

basepath = os.path.split(os.path.dirname(__file__))[1]
basename = basepath + "-" + os.path.splitext(os.path.basename(__file__))[0]


def read_excle_data():
    store_label = StoreDefault()
    store_label.add_key(store_label.staff, store_label.page)
    excle_data = store_label._excel_Data('序号')
    return excle_data


@ddt.ddt
class TestStaffLabel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ac_handle = HandleAction(basename)
        import time

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(*read_excle_data())
    def test_simple_keyword(self, case):
        self.ac_handle.log.log_ppriny(case)
        if str(case.loc['是否执行']) == 'yes':
            self.ac_handle.execution_method(case)
        time.sleep(1)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
