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
@file:      test_platformLable.py
@time:      2018/8/28 18:07
@Site :     
@desc:
'''
import os
import inspect
import unittest
from CenterBackground import MovementUser
from CenterBackground.MovementUser.Customer.customersurface import Customersurface
from tools.excelname.Center.bundledItems import BundledItems


class TestPlatformLable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        config = MovementUser.add_key(MovementUser.customer, MovementUser.page)
        cls.cust = Customersurface(config, cls.basename, InteractionController)

    def setUp(self):
        # 获取运行文件的类名
        self.cust.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.cust.openingProgram()
        self.cust._rou_background()
        pass

    def tearDown(self):
        self.cust.driver.quit()
        self.cust.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_showTitle(self):
        self.cust.setFunctionName(inspect.stack()[0][3])
        self.cust.title_execute()
        pass

    def test_showSurface(self):
        self.cust.setFunctionName(inspect.stack()[0][3])
        self.cust.surface_execute()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
