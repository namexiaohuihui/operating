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
@file:      test_detailsorder.py
@time:      2018/10/18 10:50
@desc:
"""
import os

import inspect
import unittest

from CenterBackground import InteractionActions
from CenterBackground.InteractionActions.operationViewJude import OperationViewJude
from tools.excelname.Center.Interaction import InteractionController


class TestDetailsOrder(unittest.TestCase):
    """
    订单详情
    """

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename

        config = InteractionActions.add_key(InteractionActions.carriage, InteractionActions.details)
        cls.details_o = OperationViewJude(config, cls.basename, InteractionController)

    def setUp(self):
        # 获取运行文件的类名
        self.details_o.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.details_o.openingProgram()
        self.details_o._rou_background()

    def tearDown(self):
        self.details_o.driver.quit()
        self.details_o.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_daydetails(self):
        """
        查看下单时间为当天的订单
        :return:
        """
        self.details_o.setFunctionName(inspect.stack()[0][3])
        self.details_o.release_success()
        # 找到td通过子元素的text来找到信息
        self.details_o.details_order_types()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
