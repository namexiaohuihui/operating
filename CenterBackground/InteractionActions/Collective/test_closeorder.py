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
@file:      test_closeorder.py
@time:      2018/10/16 17:18
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import InteractionActions
from CenterBackground.InteractionActions.operationViewJude import OperationViewJude
from tools.excelname.Center.Interaction import InteractionController


class TestCloseOrder(unittest.TestCase):
    """
    关闭
    """

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        config = InteractionActions.add_key(InteractionActions.collective, InteractionActions.close)
        cls.close_o = OperationViewJude(config, cls.basename, InteractionController)

    def setUp(self):
        # 获取运行文件的类名
        self.close_o.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.close_o.openingProgram()
        self.close_o._rou_background()

    def tearDown(self):
        self.close_o.driver.quit()
        self.close_o.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_dayWaiting(self):
        """
        查看下单时间为当天的订单
        :return:
        """
        self.close_o.setFunctionName(inspect.stack()[0][3])
        self.close_o.release_success()
        self.close_o.close_order_types()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
