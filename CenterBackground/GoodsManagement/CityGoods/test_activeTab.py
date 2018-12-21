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
@author: 70486
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file: test_activeTab.py
@time: 2018/7/31 14:03
@desc:
'''
import os
import inspect
import unittest
from CenterBackground import GoodsManagement
from tools.excelname.Center.gongsMana import CityGoodsPage
from CenterBackground.GoodsManagement.CityGoods.activeTabJude import ActiveTabJude


class TestCityTab(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename

        # 传入子集的key，以及Excel文档中的sheet名字
        config = GoodsManagement.add_key(GoodsManagement.citys, GoodsManagement.tab)
        cls.city_tab = ActiveTabJude(config, cls.basename, CityGoodsPage)

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]
        pass

    def setUp(self):
        # 获取运行文件的类名
        self.city_tab.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.city_tab.openingProgram()
        self.city_tab._rou_background()

    def tearDown(self):
        self.city_tab.get_screenshot_image(method_obj=self)

        self.city_tab.driver.quit()
        self.city_tab.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_already_citys(self):
        '''
        读取全部的城市
        :return:
        '''
        self.city_tab.setFunctionName(inspect.stack()[0][3])
        self.city_tab.get_already_citys()
        pass

    def test_already_codes(self):
        '''
        获取全部城市的code
        :return:
        '''
        self.city_tab.setFunctionName(inspect.stack()[0][3])
        self.city_tab.get_already_codes()
        pass

    def test_active_city(self):
        '''
        寻找默认展开项
        :return:
        '''
        self.city_tab.setFunctionName(inspect.stack()[0][3])
        self.city_tab.get_active_city()
        pass

    def test_active_code(self):
        '''
        寻找默认展开项的编码
        :return:
        '''
        self.city_tab.setFunctionName(inspect.stack()[0][3])
        self.city_tab.get_active_code()
        pass

    def test_switch_city(self):
        '''
        点击全部的tab项
        :return:
        '''
        self.city_tab.setFunctionName(inspect.stack()[0][3])
        self.city_tab.click_switch_city()
        pass

    def test_switch_url(self):
        '''
        通过url来切换
        :return:
        '''
        self.city_tab.setFunctionName(inspect.stack()[0][3])
        self.city_tab.click_switch_code()
        pass

    def switch_switch(self):
        print("------------")
        print(os.path.basename(__file__))
        print(os.path.splitext(os.path.basename(__class__.__name__))[0])
        print(os.path.splitext(os.path.basename(__file__))[0])
        print(inspect.stack()[0][3])
        print("------------")


if __name__ == '__main__':
    unittest.main(verbosity=2)
