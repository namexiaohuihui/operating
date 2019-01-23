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
@file:      test_nihaoone.py
@time:      2018/11/29 10:35
@desc:
"""
import unittest
from tools.browser_establish import browser_confirm
import os
import inspect


class TestShaLeBaOne(unittest.TestCase):
    def setUp(self):
        # 1.创建浏览器所在函数的对象
        bc = browser_confirm.__new__(browser_confirm)
        self.driver = bc.url_opens("http://baidu.com")
        pass

    def tearDown(self):
        self.driver.quit()
        pass

    def test_shaleba_one(self):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        basename = os.path.splitext(os.path.basename(__file__))[0]
        basename = basepath + "-" + basename
        fun_name = inspect.stack()[0][3]
        print(basename + "--" + fun_name)
        pass

    def test_shaleba_two(self):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        basename = os.path.splitext(os.path.basename(__file__))[0]
        basename = basepath + "-" + basename
        fun_name = inspect.stack()[0][3]
        print(basename + "--" + fun_name)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
