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


class TestParticulars(unittest.TestCase):
    """
    详情页进行操作
    """

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        config = InteractionActions.add_key(InteractionActions.complete, InteractionActions.particulars)
        cls.parti_c = OperationViewJude(config, cls.basename, InteractionController)

    def setUp(self):
        # 获取运行文件的类名
        self.parti_c.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.parti_c.openingProgram()
        self.parti_c._rou_background()
        pass

    def tearDown(self):
        self.parti_c.driver.quit()
        self.parti_c.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_closecancel(self):
        """
        详情页面点击关闭
        :return:
        """
        self.parti_c.setFunctionName(inspect.stack()[0][3])
        self.parti_c.release_success()
        self.parti_c.parti_crder_types()
        self.parti_c.close_cancel()
        pass

    def test_appointmentcancel(self):
        """
        详情页面点击转预约
        :return:
        """
        self.parti_c.setFunctionName(inspect.stack()[0][3])
        self.parti_c.release_success()
        self.parti_c.parti_crder_types()
        self.parti_c.appointmen_cancel()
        pass

    def test_replacecancel(self):
        """
        详情页面点击更换
        :return:
        """
        self.parti_c.setFunctionName(inspect.stack()[0][3])
        self.parti_c.release_success()
        self.parti_c.parti_crder_types()
        self.parti_c.replace_cancel()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
