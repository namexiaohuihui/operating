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
@file:      test_addtrademark.py
@time:      2018/11/6 11:03
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import Website
from tools.excelname.Center.officialwebsite import OfficialWebsite
from CenterBackground.GeneralizeAssist.Invite.inviteoperatejude import InviteOperateJude


class TestAddTrademark(unittest.TestCase):
    """
    点击某个按钮,获取弹窗的标题
    """

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        config = Website.add_key(Website.trademark, Website.add)
        cls.j_operate = InviteOperateJude(config, cls.basename, InteractionController)

    def setUp(self):
        # 获取运行文件的类名
        self.j_operate.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.j_operate.openingProgram()
        self.j_operate._rou_background()
        pass

    def tearDown(self):
        self.j_operate.driver.quit()
        self.j_operate.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_addbrand(self):
        self.j_operate.setFunctionName(inspect.stack()[0][3])
        ov_para = os.path.split(os.path.dirname(__file__))[0]
        self.j_operate.conditions_screening(ov_para)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
