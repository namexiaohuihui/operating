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
@file:      test_operaterelation.py
@time:      2018/11/9 11:20
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import GeneralizeAssist
from tools.excelname.Center.generalize import Generalize
from CenterBackground.GeneralizeAssist.Invite.inviteoperatejude import InviteOperateJude


class TestOperateRelation(unittest.TestCase):
    """
    invite页面中tbody内容的跳转
    """

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename

        # 传入子集的key，以及Excel文档中的sheet名字
        config = GeneralizeAssist.add_key(GeneralizeAssist.relation, GeneralizeAssist.operate)
        cls.m_operate = InviteOperateJude(config, cls.basename, Generalize)

    def setUp(self):
        # 获取运行文件的类名
        self.m_operate.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.m_operate.openingProgram()
        self.m_operate._rou_background()

    def tearDown(self):
        self.m_operate.driver.quit()
        self.m_operate.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    @unittest.skip("test_ongoingUser-未注册没有点击按钮:需要通过数据进行检验,先跳过该用例")
    def test_ongoingUser(self):
        """
        点击用户
        :return:
        """
        self.m_operate.setFunctionName(inspect.stack()[0][3])
        self.m_operate.conditions_screening()
        pass

    @unittest.skip("test_ongoingOrder-未注册没有点击按钮:需要通过数据进行检验,先跳过该用例")
    def test_ongoingOrder(self):
        """
        点击点击
        :return:
        """
        self.m_operate.setFunctionName(inspect.stack()[0][3])
        self.m_operate.conditions_screening()
        pass

    @unittest.skip("test_ongoingWatiki-未注册没有点击按钮:需要通过数据进行检验,先跳过该用例")
    def test_ongoingWatiki(self):
        """
        点击水票
        :return:
        """
        self.m_operate.setFunctionName(inspect.stack()[0][3])
        self.m_operate.conditions_screening()
        pass

    def test_ongoingAlter(self):
        """
        点击修改
        """
        self.m_operate.setFunctionName(inspect.stack()[0][3])
        self.m_operate.conditions_screening()
        pass

    def test_ongoingHandle(self):
        """
        点击操作
        :return:
        """
        self.m_operate.setFunctionName(inspect.stack()[0][3])
        self.m_operate.conditions_screening()
        pass

    @unittest.skip("test_historyUser-未注册没有点击按钮:需要通过数据进行检验,先跳过该用例")
    def test_historyUser(self):
        """
        点击用户
        :return:
        """
        self.m_operate.setFunctionName(inspect.stack()[0][3])
        self.m_operate.conditions_screening()
        pass

    @unittest.skip("test_historyOrder-未注册没有点击按钮:需要通过数据进行检验,先跳过该用例")
    def test_historyOrder(self):
        """
        点击订单
        :return:
        """
        self.m_operate.setFunctionName(inspect.stack()[0][3])
        self.m_operate.conditions_screening()
        pass

    @unittest.skip("test_historyWatiki-未注册没有点击按钮:需要通过数据进行检验,先跳过该用例")
    def test_historyWatiki(self):
        """
        点击水票
        :return:
        """
        self.m_operate.setFunctionName(inspect.stack()[0][3])
        self.m_operate.conditions_screening()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
