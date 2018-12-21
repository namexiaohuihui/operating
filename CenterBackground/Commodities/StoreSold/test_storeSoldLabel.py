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
        config = Commodities.add_key(Commodities.storesold, Commodities.page)
        cls.sLabel = SoldLable(config, cls.basename, BundledItems)

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]
        pass

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        self.sLabel.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        self.sLabel.openingProgram()
        self.sLabel._rou_background()
        # 定义后面使用的参数,到时候会进行回收
        pass

    def tearDown(self):
        self.sLabel.get_screenshot_image(method_obj=self)

        self.sLabel.driver.quit()
        self.sLabel.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
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
