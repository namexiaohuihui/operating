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
from CenterBackground.GoodsManagement.CityGoods.activeTabJude import ActiveTabJude

city_tab = ActiveTabJude()


class TestCityTab(unittest.TestCase):

    def setUp(self):
        print("setup: 每个用例开始前后执行")
        # 获取运行文件的类名
        basename = os.path.splitext(os.path.basename(__file__))[0]
        # 打开浏览器，定义log日志。读取excle文档数据
        city_tab.openingProgram(basename, city_tab.MODEL_WORKBOOK_CITY)
        city_tab._rou_interaction()

    def tearDown(self):
        city_tab.driver.quit()
        print("teardown: 每个用例结束后执行")
        pass

    def test_already_citys(self):
        '''
        读取全部的城市
        :return:
        '''
        city_tab.setFunctionName(inspect.stack()[0][3])
        city_tab.get_already_citys()
        pass

    def test_already_codes(self):
        '''
        获取全部城市的code
        :return:
        '''
        city_tab.setFunctionName(inspect.stack()[0][3])
        city_tab.get_already_codes()
        pass

    def test_active_city(self):
        '''
        寻找默认展开项
        :return:
        '''
        city_tab.setFunctionName(inspect.stack()[0][3])
        city_tab.get_active_city()
        pass

    def test_active_code(self):
        '''
        寻找默认展开项的编码
        :return:
        '''
        city_tab.setFunctionName(inspect.stack()[0][3])
        city_tab.get_active_code()
        pass

    def test_switch_city(self):
        '''
        点击全部的tab项
        :return:
        '''
        city_tab.setFunctionName(inspect.stack()[0][3])
        city_tab.click_switch_city()
        pass

    def test_switch_url(self):
        '''
        通过url来切换
        :return:
        '''
        city_tab.setFunctionName(inspect.stack()[0][3])
        city_tab.click_switch_code()
        pass

    def switch_switch(self):
        print("------------")
        print(os.path.basename(__file__))
        print(os.path.splitext(os.path.basename(__class__.__name__))[0])
        print(os.path.splitext(os.path.basename(__file__))[0])
        print(inspect.stack()[0][3])
        print("------------")
