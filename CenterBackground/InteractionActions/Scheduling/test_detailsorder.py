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
from CenterBackground.InteractionActions.operationViewJude import OperationViewJude
from CenterBackground import InteractionActions
from tools.excelname.Center.Interaction import InteractionController

basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename

# 传入子集的key，以及Excel文档中的sheet名字
config = InteractionActions.add_key(InteractionActions.dispatch, InteractionActions.details)
details_o = OperationViewJude(config, basename, InteractionController)


class TestDetailsOrder(unittest.TestCase):
    """
    订单详情
    """
    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        details_o.openingProgram()
        details_o._rou_background()
        details_o.log.info("%s : The use case begins execution" % basename)
        pass

    def tearDown(self):
        details_o.driver.quit()
        details_o.log.info("%s : The use case is done" % basename)
        pass

    def test_daydetails(self):
        """
        查看下单时间为当天的订单
        :return:
        """
        details_o.setFunctionName(inspect.stack()[0][3])
        details_o.release_success()
        # 找到td通过子元素的text来找到信息
        details_o.details_order_types()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
