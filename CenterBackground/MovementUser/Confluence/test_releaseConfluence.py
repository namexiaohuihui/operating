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
@file:      test_releaseConfluence.py
@time:      2018/9/10 16:10
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import MovementUser
from CenterBackground.MovementUser.Sweating.setSweating import ReleaseConfluence
from tools.excelname.Center.consumers import Consumers

basename = os.path.splitext(os.path.basename(__file__))[0]
# 传入子集的key，以及Excel文档中的sheet名字
config = MovementUser.add_key(MovementUser.confluence, MovementUser.release)
release = ReleaseConfluence(config, basename, Consumers) # 重写了点击按钮


class TestReleaseConfluence(unittest.TestCase):
    def setUp(self):
        # 获取运行文件的类名
        # 打开浏览器，定义log日志。读取excle文档数据
        release.openingProgram()
        release._rou_background()
        release.log.info("%s ---setup: 每个用例开始前后执行" % basename)

    def tearDown(self):
        release.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        release.driver.quit()
        pass

    def test_popupclosed(self):
        release.setFunctionName(inspect.stack()[0][3])
        release.close_popup()

        pass

    def test_buttoncancel(self):
        release.setFunctionName(inspect.stack()[0][3])
        release.close_popup()
        pass

    def test_releaseSuccess(self):
        release.setFunctionName(inspect.stack()[0][3])
        release.releaseSuccess()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
