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
@file:      test_previewfocus.py
@time:      2018/11/6 11:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import GeneralizeAssist
from CenterBackground.GeneralizeAssist.Focus.operateJude import OperateJude
from tools.excelname.Center.generalize import Generalize


class TestPreviewFocus(unittest.TestCase):
    """
    预览
    """

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename

        # 传入子集的key，以及Excel文档中的sheet名字
        config = GeneralizeAssist.add_key(GeneralizeAssist.focus, GeneralizeAssist.preview)

        cls.f_pre = OperateJude(config, cls.basename, Generalize)

    def setUp(self):
        # 获取运行文件的类名
        self.f_pre.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.f_pre.openingProgram()
        self.f_pre._rou_background()

    def tearDown(self):
        self.f_pre.driver.quit()
        self.f_pre.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_previewCancel(self):
        self.f_pre.setFunctionName(inspect.stack()[0][3])
        self.f_pre.conditions_screening()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
