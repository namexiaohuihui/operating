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
(config, BASENAME, BundledItems)


class TestReleaseWater(unittest.TestCase):
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + basename
        config = Commodities.add_key(Commodities.platform, Commodities.release)
        cls.rWatiki = ReleaseWatiki(config, cls.basename, BundledItems)

    def setUp(self):
        # 获取运行文件的类名
        self.rWatiki.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.rWatiki.openingProgram()
        self.rWatiki._rou_background()

    def tearDown(self):
        self.rWatiki.driver.quit()
        self.rWatiki.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_popupclosed(self):
        self.rWatiki.setFunctionName(inspect.stack()[0][3])
        self.rWatiki.close_popup()
        pass

    def test_buttoncancel(self):
        self.rWatiki.setFunctionName(inspect.stack()[0][3])
        self.rWatiki.close_popup()
        pass

    def test_optionsave(self):
        self.rWatiki.setFunctionName(inspect.stack()[0][3])
        self.rWatiki.show_sweetAlert()
        pass

    def test_optioncancel(self):
        self.rWatiki.setFunctionName(inspect.stack()[0][3])
        self.rWatiki.click_information()
        pass

    def test_optionpackages(self):
        self.rWatiki.setFunctionName(inspect.stack()[0][3])
        self.rWatiki.ticket_choose()
        pass

    def test_releaseSuccess(self):
        self.rWatiki.setFunctionName(inspect.stack()[0][3])
        self.rWatiki.releaseSuccess()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
