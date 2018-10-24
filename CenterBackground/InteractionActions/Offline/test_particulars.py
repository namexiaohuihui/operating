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
@file:      test_particulars.py
@time:      2018/10/19 11:40
@desc:
"""
import os
import inspect
import unittest
from CenterBackground.InteractionActions.operationViewJude import OperationViewJude
from CenterBackground import InteractionActions
from tools.excelname.Center.Interaction import InteractionController

basePath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basePath + "-" + basename

# 传入子集的key，以及Excel文档中的sheet名字
config = InteractionActions.add_key(InteractionActions.offline, InteractionActions.particulars)
parti_c = OperationViewJude(config, basename, InteractionController)


class TestParticulars(unittest.TestCase):
    """
    详情页进行操作
    """

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        parti_c.openingProgram()
        parti_c._rou_background()
        parti_c.log.info("%s : The use case begins execution" % basename)
        pass

    def tearDown(self):
        parti_c.driver.quit()
        parti_c.log.info("%s : The use case is done" % basename)
        pass

    def test_closecancel(self):
        """
        详情页面点击关闭
        :return:
        """
        parti_c.setFunctionName(inspect.stack()[0][3])
        parti_c.release_success()
        parti_c.details_order_types()
        parti_c.close_cancel()
        pass

    def test_appointmentcancel(self):
        """
        详情页面点击转预约
        :return:
        """
        parti_c.setFunctionName(inspect.stack()[0][3])
        parti_c.release_success()
        parti_c.details_order_types()
        parti_c.appointmen_cancel()
        pass

    def test_replacecancel(self):
        """
        详情页面点击更换
        :return:
        """
        parti_c.setFunctionName(inspect.stack()[0][3])
        parti_c.release_success()
        parti_c.details_order_types()
        parti_c.replace_cancel()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
