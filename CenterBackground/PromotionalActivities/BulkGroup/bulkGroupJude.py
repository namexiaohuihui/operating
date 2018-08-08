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
@file: BulkGroupJude.py
@time: 2018/8/8 17:35
@desc:
'''
import os
from tools import readYaml

fpath = os.path.dirname(os.path.realpath(__file__))  # 返回该文件所在的目录
name = 'BulkGroup.yaml'
from CenterBackground.PromotionalActivities import PromotionalBulk
class BulkGroupJude(PromotionalBulk):
    MODEI_CASE_POSITION = 'bulk' # 用例名字
    CHILD_TAGS_LOCATION = 7

    def __init__(self):  # 执行读取yaml数据信息
        self.financial_path = readYaml.read_parseyaml(fpath, name)
        pass

    def _rou_interaction(self):
        """
        进入日常公告页面
        :return:  暂时没有返回值
        """
        self.child_tags = self.CHILD_TAGS_LOCATION
        self.father_tags = self.FATHER_TAGS_LOCATION
        self._rou_background()
        pass
