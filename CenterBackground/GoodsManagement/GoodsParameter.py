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
@file: financialParameter.py
@time: 2018/7/31 15:00
@desc: 获取Excel表格以及其他文档的数据信息
'''
import os
from tools import readYaml
from tools.excelname.adminGongsMana import CityGoodsPage


class FinancialParameter(CityGoodsPage):

    def financial_yaml(self, fpath, name):
        '''
        指定文件路径以及文件名来读取数据信息
        :param fpath: 文件路径
        :param name: 文件名称
        :return:
        '''
        return readYaml.read_parseyaml(fpath, name)
