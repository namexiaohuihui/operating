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
@file:      test_ancientlabel.py
@time:      2018/9/19 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import SystemSetting
from CenterBackground.surfacejude import SurfaceJude
from tools.excelname.Center.systemparameter import SystemParameter

basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename

config = SystemSetting.add_key(SystemSetting.ancient, SystemSetting.page)

a_label = SurfaceJude(config, basename, SystemParameter)


class TestAncientLabel(unittest.TestCase):
    """
    页面展示项的标题
    """
    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        a_label.log.info("%s ---setup: 每个用例开始前后执行" % basename)
        a_label.openingProgram()
        a_label._rou_background()
        pass

    def tearDown(self):
        a_label.driver.quit()
        a_label.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    def test_showTitle(self):
        a_label.setFunctionName(inspect.stack()[0][3])
        a_label.title_execute()
        pass

    def test_showSurface(self):
        a_label.setFunctionName(inspect.stack()[0][3])
        a_label.surface_execute()
        pass



if __name__ == '__main__':
    unittest.main(verbosity=2)
