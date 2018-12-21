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
@file: test_customerTabs.py
@time: 2018/8/20 16:08
@desc:
'''
import os
import inspect
import unittest
from CenterBackground import MovementUser
from CenterBackground.commoditiesJude import CommoditiesJude
from tools.excelname.Center.consumers import Consumers


class TestCustomerTabs(unittest.TestCase):
    # 定义头部button中，后面2位不需要
    BUTTON_REDUCE_NUMBER = 1

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        config = MovementUser.add_key(MovementUser.customer, MovementUser.city)
        cls.cust_t = CommoditiesJude(config, cls.basename, Consumers)

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]
        pass

    def setUp(self):
        # 获取运行文件的类名
        self.cust_t.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.cust_t.openingProgram()
        self.cust_t._rou_background()
        pass

    def tearDown(self):
        self.cust_t.get_screenshot_image(method_obj=self)

        self.cust_t.driver.quit()
        self.cust_t.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_active_tab(self):
        self.cust_t.setFunctionName(inspect.stack()[0][3])
        self.cust_t.active_city('class')
        pass

    def test_already_tabs(self):
        self.cust_t.setFunctionName(inspect.stack()[0][3])
        self.cust_t.already_citys(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_tab(self):
        self.cust_t.setFunctionName(inspect.stack()[0][3])
        self.cust_t.switch_city(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_url(self):
        self.cust_t.setFunctionName(inspect.stack()[0][3])
        self.cust_t.switch_url('class', reduce=self.BUTTON_REDUCE_NUMBER)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
