# -*- coding: utf-8 -*-
'''
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
@file:      test_platformSoldLable.py
@time:      2018/8/28 18:07
@Site :     
@desc:
'''
import os
import inspect
import unittest
from CenterBackground import Commodities
from tools.excelname.Center.bundledItems import BundledItems
from CenterBackground.Commodities.soldLable import SoldLable

BASENAME = os.path.splitext(os.path.basename(__file__))[0]
config = Commodities.add_key(Commodities.platformsold, Commodities.page)
sLabel = SoldLable(config, BASENAME, BundledItems)


class TestPlatformSoldLable(unittest.TestCase):
    def setUp(self):
        # 获取运行文件的类名
        self.basename = os.path.splitext(os.path.basename(__file__))[0]
        print("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        sLabel.openingProgram()
        sLabel._rou_background()

    def tearDown(self):
        sLabel.driver.quit()
        print("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_showTitle(self):
        sLabel.setFunctionName(inspect.stack()[0][3])
        sLabel.title_execute()
        pass

    def test_showSurface(self):
        sLabel.setFunctionName(inspect.stack()[0][3])
        sLabel.surface_execute()
        pass