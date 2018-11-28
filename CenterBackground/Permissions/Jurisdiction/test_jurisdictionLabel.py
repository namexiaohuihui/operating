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
@file:      test_jurisdictionlabel.py
@time:      2018/9/19 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import Permissions
from CenterBackground.surfacejude import SurfaceJude
from tools.excelname.Center.management import RightOfManagement

basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename

config = Permissions.add_key(Permissions.jurisdiction, Permissions.page)

p_mana = SurfaceJude(config, basename, RightOfManagement)


class TestJurisdictionLabel(unittest.TestCase):
    """
    页面展示项的标题
    """
    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        p_mana.log.info("%s ---setup: 每个用例开始前后执行" % basename)
        p_mana.openingProgram()
        p_mana._rou_background()
        pass

    def tearDown(self):
        p_mana.driver.quit()
        p_mana.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    def test_showTitle(self):
        p_mana.setFunctionName(inspect.stack()[0][3])
        p_mana.title_execute()
        pass

    def test_showSurface(self):
        p_mana.setFunctionName(inspect.stack()[0][3])
        p_mana.surface_execute()
        pass



if __name__ == '__main__':
    unittest.main(verbosity=2)
