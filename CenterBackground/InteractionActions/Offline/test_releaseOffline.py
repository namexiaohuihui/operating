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
@file:      test_releaseOffline.py
@time:      2018/10/23 17:33
@desc:
"""
import os
import inspect
import unittest
from .offlineGenerate import OfflineGenerate
from CenterBackground.InteractionActions.operationViewJude import OperationViewJude
from CenterBackground import InteractionActions
from tools.excelname.Center.Interaction import InteractionController



class TestReleaseOffline(unittest.TestCase):
    """
    发布内容
    """

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        config = InteractionActions.add_key(InteractionActions.offline, InteractionActions.release)
        cls.generate = OfflineGenerate(config, cls.basename, InteractionController)

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]
        pass

    def setUp(self):
        # 获取运行文件的类名
        self.generate.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.generate.openingProgram()
        self.generate._rou_background()
        pass

    def tearDown(self):
        self.generate.get_screenshot_image(method_obj=self)

        self.generate.driver.quit()
        self.generate.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_defaultSingleGood(self):
        """
        默认流程发布单个商品
        :return:
        """
        self.generate.setFunctionName(inspect.stack()[0][3])
        self.generate.operating_environment()

    def test_ungenerate(self):
        """
        直接点击
        :return:
        """
        self.generate.setFunctionName(inspect.stack()[0][3])
        self.generate.operating_environment()

    def test_purecharacter(self):
        """
        输入中文
        :return:
        """
        self.generate.setFunctionName(inspect.stack()[0][3])
        self.generate.operating_environment()
        pass

    def test_closewindows(self):
        """
        点击取消
        :return:
        """
        self.generate.setFunctionName(inspect.stack()[0][3])
        self.generate.defaule_environment()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
