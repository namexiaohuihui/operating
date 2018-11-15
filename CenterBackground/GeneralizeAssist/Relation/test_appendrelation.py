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
@file:      test_appendrelation.py
@time:      2018/11/12 10:51
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

# 传入子集的key，以及Excel文档中的sheet名字
config = GeneralizeAssist.add_key(GeneralizeAssist.relation, GeneralizeAssist.add)
r_append = InviteOperateJude(config, basename, Generalize)


class TestAppendRelation(unittest.TestCase):
    """
       invite页面中默认跳转
       """

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        r_append.openingProgram()
        r_append._rou_background()
        r_append.log.info("%s ---setup: 每个用例开始前后执行" % basename)
        pass

    def tearDown(self):
        r_append.driver.quit()
        r_append.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    def test_ongoingRelation(self):
        r_append.setFunctionName(inspect.stack()[0][3])
        r_append.conditions_screening()
        pass

    def test_ongoingOpenlist(self):
        r_append.setFunctionName(inspect.stack()[0][3])
        r_append.conditions_screening()
        pass

    def test_historyRelation(self):
        r_append.setFunctionName(inspect.stack()[0][3])
        r_append.conditions_screening()
        pass

    def test_historyOpenlist(self):
        r_append.setFunctionName(inspect.stack()[0][3])
        r_append.conditions_screening()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
