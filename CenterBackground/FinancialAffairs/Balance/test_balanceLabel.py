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
@file:      test_balancelabel.py
@time:      2018/9/19 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import FinancialAffairs
from tools.excelname.Center.financial import Financial
from CenterBackground.FinancialAffairs.Balance.handlebutton import HandleButton


class TestBalanceLabel(unittest.TestCase):
    """
    页面展示项的标题
    """

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        # 读取配置文件
        config = FinancialAffairs.add_key(FinancialAffairs.balance, FinancialAffairs.page)

        # 实例化用例操作类
        cls.bala_sur = HandleButton(config, cls.basename, Financial)

    def setUp(self):
        # 获取运行文件的类名
        self.bala_sur.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.bala_sur.openingProgram()
        self.bala_sur._rou_background()

    def tearDown(self):
        self.bala_sur.driver.quit()
        self.bala_sur.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_balanceTitle(self):
        self.bala_sur.setFunctionName(inspect.stack()[0][3])
        self.bala_sur.title_execute()
        pass

    def test_balanceSurface(self):
        self.bala_sur.setFunctionName(inspect.stack()[0][3])
        self.bala_sur.bala_sur_execute()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
