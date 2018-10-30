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
@file:      test_releaseOffline.py
@time:      2018/10/23 17:33
@desc:
"""
import os
import inspect
import unittest
from .offlineGenerate import OfflineGenerate
from CenterBackground.InteractionActions.operationViewJude import OperationViewJude
from CenterBackground import InteractionActions
from tools.excelname.Center.Interaction import InteractionController

basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename

# 传入子集的key，以及Excel文档中的sheet名字
config = InteractionActions.add_key(InteractionActions.offline, InteractionActions.release)
generate = OfflineGenerate(config, basename, InteractionController)


class TestReleaseOffline(unittest.TestCase):
    """
    发布内容
    """

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        generate.openingProgram()
        generate._rou_background()
        generate.log.info("%s : The use case begins execution" % basename)
        pass

    def tearDown(self):
        # generate.driver.quit()
        generate.log.info("%s : The use case is done" % basename)
        pass

    def test_defaultSingleGood(self):
        """
        默认流程发布单个商品
        :return:
        """
        generate.setFunctionName(inspect.stack()[0][3])
        generate.operating_environment()

    def test_ungenerate(self):
        generate.setFunctionName(inspect.stack()[0][3])
        generate.operating_environment()
if __name__ == '__main__':
    unittest.main(verbosity=2)
