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
@file:      test_storeSoldLable.py
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


class TestStoreSoldLable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + basename
        config = Commodities.add_key(Commodities.platform, Commodities.page)
        cls.sLabel = SoldLable(config, cls.basename, BundledItems)

    def setUp(self):
        # 获取运行文件的类名
        print("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.sLabel.openingProgram()
        self.sLabel._rou_background()

    def tearDown(self):
        self.sLabel.driver.quit()
        print("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_showTitle(self):
        self.sLabel.setFunctionName(inspect.stack()[0][3])
        self.sLabel.title_execute()
        pass

    def test_showSurface(self):
        self.sLabel.setFunctionName(inspect.stack()[0][3])
        self.sLabel.surface_execute()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
