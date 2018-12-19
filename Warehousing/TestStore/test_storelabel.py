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
# @file:      test_storelabel.py
# @time:      2018/12/17 16:23
# @desc:
import unittest
import time
import os
from tools.browser_establish import browser_confirm


class TestStoreLabel(unittest.TestCase):

    def setUp(self):
        print("1")
        br = browser_confirm()
        self.driver = br.url_opens('http://baidu.com')
        time.sleep(1)
    def tearDown(self):
        for k,v in self._outcome.errors:
            if v:
                mn = self._testMethodName
                kk = self._testMethodDoc
                print("-*---",kk )
                print(k,'-*',v,'--')
                print("-*---",mn)
                print(os.getcwd())
                ll_path = os.path.join(os.getcwd(),"qweqw.png")
                self.driver.save_screenshot(ll_path )
        print(2)
    def test_qweqw(self):
        assert True
        time.sleep(1)
        raise Exception


if __name__ == '__main__':
    unittest.main(verbosity=2)
