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
@file:      test_completeView.py
@time:      2018/9/27 17:25
@desc:
"""
import os
import inspect
import unittest
from CenterBackground.InteractionActions.operationViewJude import OperationViewJude
from CenterBackground import InteractionActions
from tools.excelname.Center.Interaction import InteractionController


class TestCompleteView(unittest.TestCase):
    """
    通过筛选查看页面数据
    """

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        config = InteractionActions.add_key(InteractionActions.complete, InteractionActions.views)
        cls.tive_v = OperationViewJude(config, cls.basename, InteractionController)

    def setUp(self):
        # 获取运行文件的类名
        self.tive_v.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.tive_v.openingProgram()
        self.tive_v._rou_background()
        pass

    def tearDown(self):
        self.tive_v.driver.quit()
        self.tive_v.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_showtimetoday(self):
        """
        查看下单时间为当天的订单
        :return:
        """
        self.tive_v.setFunctionName(inspect.stack()[0][3])
        self.tive_v.release_success()
        pass

    def test_yesterdayorder(self):
        """
        查看下单时间为昨天的订单
        :return:
        """
        self.tive_v.setFunctionName(inspect.stack()[0][3])
        self.tive_v.release_success()
        pass

    def test_sevendayorder(self):
        """
        查看下单时间为七天的订单
        :return:
        """
        self.tive_v.setFunctionName(inspect.stack()[0][3])
        self.tive_v.release_success()
        pass

    def test_thirtydayorder(self):
        """
        查看下单时间为30的订单
        :return:
        """
        self.tive_v.setFunctionName(inspect.stack()[0][3])
        self.tive_v.release_success()
        pass

    def test_yeardayorder(self):
        """
        查看下单时间为全部的订单
        :return:
        """
        self.tive_v.setFunctionName(inspect.stack()[0][3])
        self.tive_v.release_success()
        pass

    def test_customtoday(self):
        """
        查看下单时间为自定义的订单
        :return:
        """
        self.tive_v.setFunctionName(inspect.stack()[0][3])
        self.tive_v.release_success()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
