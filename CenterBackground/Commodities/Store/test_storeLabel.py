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
@file:      test_storeLable.py
@time:      2018/8/28 18:07
@Site :     
@desc:
'''
import os
import inspect
import unittest
from CenterBackground import Commodities
from CenterBackground.Commodities.Store.storesurface import StoreSurface
from tools.excelname.Center.bundledItems import BundledItems


class TestStoreLable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + basename
        config = Commodities.add_key(Commodities.store, Commodities.page)
        cls.surface = StoreSurface(config, cls.basename, BundledItems)
        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        self.surface.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        self.surface.openingProgram()
        self.surface._rou_background()
        pass

    def tearDown(self):
        self.surface.get_screenshot_image(method_obj=self)

        self.surface.driver.quit()
        self.surface.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_showTitle(self):
        self.surface.setFunctionName(inspect.stack()[0][3])
        self.surface.title_execute()
        pass

    def test_showSurface(self):
        self.surface.setFunctionName(inspect.stack()[0][3])
        self.surface.surface_execute()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
