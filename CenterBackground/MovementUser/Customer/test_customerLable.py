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
# import os
# import inspect
# import unittest
# from CenterBackground import MovementUser
# from CenterBackground.MovementUser.Customer.customersurface import Customersurface
# from tools.excelname.Center.bundledItems import BundledItems
#
# BASENAME = os.path.splitext(os.path.basename(__file__))[0]
# config = MovementUser.add_key(MovementUser.customer, MovementUser.page)
# ps = Customersurface(config, BASENAME, BundledItems)
#
#
# class TestPlatformLable(unittest.TestCase):
#     def setUp(self):
#         # 获取运行文件的类名
#         self.basename = os.path.splitext(os.path.basename(__file__))[0]
#         print("%s ---setup: 每个用例开始前后执行" % self.basename)
#         # 打开浏览器，定义log日志。读取excle文档数据
#         ps.openingProgram()
#         ps._rou_background()
#
#     def tearDown(self):
#         ps.driver.quit()
#         print("%s ---teardown: 每个用例结束后执行" % self.basename)
#         pass
#
#     def test_showTitle(self):
#         ps.setFunctionName(inspect.stack()[0][3])
#         ps.title_execute()
#         pass
#
#     def test_showSurface(self):
#         ps.setFunctionName(inspect.stack()[0][3])
#         ps.surface_execute()
#         pass
import time

start = time.time()
print('1', start)

import os
import inspect
import unittest
from CenterBackground import MovementUser
from CenterBackground.MovementUser.Customer.releaseCustomer import ReleaseCustomer
from tools.excelname.Center.consumers import Consumers

print('2', time.time() - start)

basename = os.path.splitext(os.path.basename(__file__))[0]
# 传入子集的key，以及Excel文档中的sheet名字
config = MovementUser.add_key(MovementUser.customer, MovementUser.release)
release = ReleaseCustomer(config, basename, Consumers)

print('3', time.time() - start)


class TestReleaseBuyer(unittest.TestCase):
    def setUp(self):
        # 获取运行文件的类名
        # 打开浏览器，定义log日志。读取excle文档数据
        print('4.0', time.time() - start)
        release.openingProgram()
        print('4.1', time.time() - start)
        release._rou_background()
        print('4.2', time.time() - start)
        release.log.info("%s ---setup: 每个用例开始前后执行" % basename)

    def tearDown(self):
        release.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        release.driver.quit()
        print('6', time.time() - start)
        pass

    @unittest.skip('test_popupclosed')
    def test_popupclosed(self):
        release.setFunctionName(inspect.stack()[0][3])
        release.close_popup()

        pass

    @unittest.skip('test_buttoncancel')
    def test_buttoncancel(self):
        release.setFunctionName(inspect.stack()[0][3])
        release.close_popup()
        print('5', time.time() - start)
        pass

    # @unittest.skip('test_releaseSuccess')
    def test_releaseSuccess(self):
        release.setFunctionName(inspect.stack()[0][3])
        release.releaseSuccess()
        pass

