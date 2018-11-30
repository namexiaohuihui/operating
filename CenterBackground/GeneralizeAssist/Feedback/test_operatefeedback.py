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
@file:      test_operatefeedback.py
@time:      2018/11/9 11:20
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import GeneralizeAssist
from tools.excelname.Center.generalize import Generalize
from CenterBackground.GeneralizeAssist.Invite.inviteoperatejude import InviteOperateJude

basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename


class TestOperateFeedback(unittest.TestCase):
    """
    invite页面中tbody内容的跳转
    """

    @classmethod
    def setUpClass(cls):
        # I pass in the key of the subset, and the sheet name in the Excel document
        config = GeneralizeAssist.add_key(GeneralizeAssist.feedback, GeneralizeAssist.operate)
        cls.f_operate = InviteOperateJude(config, basename, Generalize)

    def setUp(self):
        # 获取运行文件的类名
        self.f_operate.log.info("%s ---setup: 每个用例开始前后执行" % basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.f_operate.openingProgram()
        self.f_operate._rou_background()

    def tearDown(self):
        self.f_operate.driver.quit()
        self.f_operate.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    def test_watikiAccess(self):
        self.f_operate.setFunctionName(inspect.stack()[0][3])
        ov_para = os.path.split(os.path.dirname(__file__))[0]
        self.f_operate.conditions_screening(ov_para)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
