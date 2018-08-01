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
@file: conditionsJude.py
@time: 2018/7/31 14:47
@desc: 用例数据校验
'''
import os
from tools import StringCutting
from CenterBackground.GoodsManagement import GoodsConditions
from CenterBackground.GoodsManagement.GoodsParameter import FinancialParameter
from tools import readYaml
from CenterBackground import GoodsManagement

fpath = os.path.dirname(os.path.realpath(__file__))  # 返回该文件所在的目录
name = 'GoodsPath.yaml'


class ConditionsJude(GoodsConditions):
    goods = FinancialParameter()
    CHILD_TAGS_LOCATION = 1
    MODEL_WORKBOOK_CITY = '城市'
    MODEI_CASE_POSITION = 'city'

    def __init__(self):  # 执行读取yaml数据信息
        self.financial_path = readYaml.read_parseyaml(fpath, name)

    def _rou_interaction(self):
        """
        进入日常公告页面
        :return:  暂时没有返回值
        """
        self.child_tags = self.CHILD_TAGS_LOCATION
        self.father_tags = self.FATHER_TAGS_LOCATION
        self._rou_background()
        pass

    def get_active_city(self):
        city_ele = self._visible_returns_selectop(self.financial_path[self.goods.yaml_value()])
        for ele in city_ele:
            if ele.get_attribute(self.goods.ele_class()) is self.goods.ele_active():
                print('---')
                print(ele.text)
                print('---')
            else:
                print(ele.text)
