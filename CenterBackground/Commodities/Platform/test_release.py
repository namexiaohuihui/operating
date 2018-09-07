# -*- coding: utf-8 -*-
'''
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
@file:      test_release.py
@time:      2018/8/30 15:56
@desc:
'''
import os
import inspect
import unittest
from CenterBackground import Commodities
from CenterBackground.Commodities.Platform.releasewater import ReleaseWatiki
from tools.excelname.Center.bundledItems import BundledItems

BASENAME = os.path.splitext(os.path.basename(__file__))[0]
config = Commodities.add_key(Commodities.platform, Commodities.release)
rWatiki = ReleaseWatiki(config, BASENAME, BundledItems)


class TestReleaseWater(unittest.TestCase):
    def setUp(self):
        # 获取运行文件的类名
        self.basename = os.path.splitext(os.path.basename(__file__))[0]
        rWatiki.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        rWatiki.openingProgram()
        rWatiki._rou_background()

    def tearDown(self):
        rWatiki.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        rWatiki.driver.quit()
        pass

    def test_popupclosed(self):
        rWatiki.setFunctionName(inspect.stack()[0][3])
        rWatiki.close_popup()
        pass

    def test_buttoncancel(self):
        rWatiki.setFunctionName(inspect.stack()[0][3])
        rWatiki.close_popup()
        pass

    def test_optionsave(self):
        rWatiki.setFunctionName(inspect.stack()[0][3])
        rWatiki.show_sweetAlert()
        pass

    def test_optioncancel(self):
        rWatiki.setFunctionName(inspect.stack()[0][3])
        rWatiki.click_information()
        pass

    def test_optionpackages(self):
        rWatiki.setFunctionName(inspect.stack()[0][3])
        rWatiki.ticket_choose()
        pass

    def test_releaseSuccess(self):
        rWatiki.setFunctionName(inspect.stack()[0][3])
        rWatiki.releaseSuccess()
        pass
