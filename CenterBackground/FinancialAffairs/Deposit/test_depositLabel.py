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
@file:      test_depositlabel.py
@time:      2018/9/19 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import FinancialAffairs
from tools.excelname.Center.financial import Financial
from CenterBackground.mutuallyJude import MutuallyJude


class TestDepositLabel(unittest.TestCase):
    """
    页面展示项的标题
    """

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename

        # 传入子集的key，以及Excel文档中的sheet名字
        config = FinancialAffairs.add_key(FinancialAffairs.deposit, FinancialAffairs.page)
        cls.d_sur = MutuallyJude(config, cls.basename, Financial)

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        self.d_sur.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        self.d_sur.openingProgram()
        self.d_sur._rou_background()
        pass

    def tearDown(self):
        self.d_sur.driver.quit()
        self.d_sur.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_balanceTitle(self):
        self.d_sur.setFunctionName(inspect.stack()[0][3])
        self.d_sur.title_execute()
        pass

    def test_balanceSurface(self):
        self.d_sur.setFunctionName(inspect.stack()[0][3])
        self.d_sur.surface_execute()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
