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
@file:      test_recordorder.py
@time:      2018/10/18 11:34
@desc:
"""
import os
import inspect
import unittest
from CenterBackground.InteractionActions.operationViewJude import OperationViewJude
from CenterBackground import InteractionActions
from tools.excelname.Center.Interaction import InteractionController

basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename
# 传入子集的key，以及Excel文档中的sheet名字
config = InteractionActions.add_key(InteractionActions.collective, InteractionActions.record)
record_o = OperationViewJude(config, basename, InteractionController)
print("--------------")
print(config)
print(record_o)
print("--------------")


class TestRecordOrder(unittest.TestCase):
    """
    记录
    """

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        record_o.openingProgram()
        record_o._rou_background()
        print("%s ---setup: 每个用例开始前后执行" % basename)

    def tearDown(self):
        record_o.driver.close()
        print("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    def test_dayrecord(self):
        """
        查看下单时间为当天的订单
        :return:
        """
        record_o.setFunctionName(inspect.stack()[0][3])
        record_o.release_success()
        # 找到td通过子元素的text来找到信息
        record_o.record_order_types()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)