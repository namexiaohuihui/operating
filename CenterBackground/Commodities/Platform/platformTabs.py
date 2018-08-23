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
@author:  ln_company
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file: platformTabs.py
@time: 2018/8/20 16:08
@desc:
'''
import unittest
import os
import inspect
from CenterBackground import Commodities
from CenterBackground.Commodities.commoditiesJude import CommoditiesJude

# 传入子集的key，以及Excel文档中的sheet名字
group = CommoditiesJude(Commodities.platform, Commodities.city)


class PlatformTabs(unittest.TestCase):

    def setUp(self):
        # 获取运行文件的类名
        self.basename = os.path.splitext(os.path.basename(__file__))[0]
        print("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        group.openingProgram(self.basename)
        group._rou_background()

    def tearDown(self):
        group.driver.quit()
        print("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass
