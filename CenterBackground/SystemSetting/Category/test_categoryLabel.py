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
@file:      test_categorylabel.py
@time:      2018/9/19 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import SystemSetting
from CenterBackground.surfacejude import SurfaceJude
from tools.excelname.Center.systemparameter import SystemParameter


class TestCategoryLabel(unittest.TestCase):
    """
    页面展示项的标题
    """

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        config = SystemSetting.add_key(SystemSetting.category, SystemSetting.page)

        cls.c_label = SurfaceJude(config, cls.basename, SystemParameter)

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]
        pass

    def setUp(self):
        # 获取运行文件的类名
        self.c_label.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.c_label.openingProgram()
        self.c_label._rou_background()
        pass

    def tearDown(self):
        self.c_label.get_screenshot_image(method_obj=self)

        self.c_label.driver.quit()
        self.c_label.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_showSurface(self):
        self.c_label.setFunctionName(inspect.stack()[0][3])
        datatatle = self.c_label.financial[self.c_label.bi.yaml_datatatle()]
        datatatle = self.c_label._visible_returns_selectop(datatatle)
        datatatle = [i.text for i in datatatle]
        self.c_label.log.info(datatatle)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
