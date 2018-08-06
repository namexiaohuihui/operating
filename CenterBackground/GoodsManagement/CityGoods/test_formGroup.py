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
@file: test_formGroup.py
@time: 2018/8/6 14:30
@desc:
'''
import os
import inspect
import unittest
from CenterBackground.GoodsManagement.CityGoods.formGroupJude import FormGroupJude

form_group = FormGroupJude()


class TestFormGroup(unittest.TestCase):
    def setUp(self):
        print("setup: 每个用例开始前后执行")
        # 获取运行文件的类名
        basename = os.path.splitext(os.path.basename(__file__))[0]
        # 打开浏览器，定义log日志。读取excle文档数据
        form_group.openingProgram(basename, form_group.MODEL_WORKBOOK_CITY)
        form_group._rou_interaction()

    def tearDown(self):
        form_group.driver.quit()
        print("teardown: 每个用例结束后执行")
        pass

    def test_statusSelect(self):
        form_group.setFunctionName(inspect.stack()[0][3])
        form_group.get_already_citys()
        pass

    def test_statusDefault(self):
        pass

    def test_statusTraverse(self):
        pass
