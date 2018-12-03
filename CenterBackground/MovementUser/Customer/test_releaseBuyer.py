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
@file:      test_releaseBuyer.py
@time:      2018/9/5 17:26
@desc:
'''
import os
import inspect
import unittest
from CenterBackground import MovementUser
from CenterBackground.MovementUser.Customer.releaseCustomer import ReleaseCustomer
from tools.excelname.Center.consumers import Consumers


class TestReleaseBuyer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        config = MovementUser.add_key(MovementUser.customer, MovementUser.release)
        cls.release = ReleaseCustomer(config, cls.basename, InteractionController)

    def setUp(self):
        # 获取运行文件的类名
        self.release.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.release.openingProgram()
        self.release._rou_background()
        pass

    def tearDown(self):
        self.release.driver.quit()
        self.release.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_popupclosed(self):
        self.release.setFunctionName(inspect.stack()[0][3])
        self.release.close_popup()
        pass

    def test_buttoncancel(self):
        self.release.setFunctionName(inspect.stack()[0][3])
        self.release.close_popup()
        pass

    def test_releaseSuccess(self):
        self.release.setFunctionName(inspect.stack()[0][3])
        self.release.releaseSuccess()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
