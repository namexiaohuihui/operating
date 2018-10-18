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
from CenterBackground.InteractionActions.operationViewJude import OperationViewJude
from CenterBackground import InteractionActions
from tools.excelname.Center.Interaction import InteractionController

basename = os.path.splitext(os.path.basename(__file__))[0]
# 传入子集的key，以及Excel文档中的sheet名字
config = InteractionActions.add_key(InteractionActions.collective, InteractionActions.close)

ovj = OperationViewJude(config, basename, InteractionController)


class TestCloseOrder(unittest.TestCase):
    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        ovj.openingProgram()
        ovj._rou_background()
        print("%s ---setup: 每个用例开始前后执行" % basename)

    def tearDown(self):
        ovj.driver.close()
        print("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    def test_dayWaiting(self):
        """
        查看下单时间为当天的订单
        :return:
        """
        ovj.setFunctionName(inspect.stack()[0][3])
        ovj.release_success()
        ovj.close_order_types()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
