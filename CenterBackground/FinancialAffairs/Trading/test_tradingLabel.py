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
@file:      test_tradinglabel.py
@time:      2018/9/19 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import FinancialAffairs
from tools.excelname.Center.financial import Financial
from CenterBackground.mutuallyJude import MutuallyJude

# 读取文件所在路径及文件名
basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename

# 读取配置文件
config = FinancialAffairs.add_key(FinancialAffairs.trading, FinancialAffairs.page)

# 实例化用例操作类
tra_sur = MutuallyJude(config, basename, Financial)


class TestTradingLabel(unittest.TestCase):
    """
    页面展示项的标题
    """

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        tra_sur.log.info("%s ---setup: 每个用例开始前后执行" % basename)
        tra_sur.openingProgram()
        tra_sur._rou_background()
        pass

    def tearDown(self):
        tra_sur.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        tra_sur.driver.quit()
        pass

    def test_tradingTitle(self):
        tra_sur.setFunctionName(inspect.stack()[0][3])
        tra_sur.title_execute()
        pass

    def test_tradingSurface(self):
        tra_sur.setFunctionName(inspect.stack()[0][3])
        tra_sur.surface_execute()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
