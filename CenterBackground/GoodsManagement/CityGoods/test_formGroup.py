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
from CenterBackground.GoodsManagement import CityGoods

form_group = FormGroupJude(CityGoods.select)


class TestFormGroup(unittest.TestCase):

    def setUp(self):
        # 获取运行文件的类名
        self.basename = os.path.splitext(os.path.basename(__file__))[0]
        print("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        form_group.openingProgram(self.basename)
        form_group._rou_background()

    def tearDown(self):
        form_group.driver.quit()
        print("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    # ----------------------------状态筛选框-------------------------------
    def test_statusSelect(self):
        '''
        执行获取状态全部optios值的用例
        :return:
        '''
        form_group.setFunctionName(inspect.stack()[0][3])
        form_group.get_statusSelect()
        pass

    def test_statusDefault(self):
        '''
        执行状态默认值的用例
        :return:
        '''
        form_group.setFunctionName(inspect.stack()[0][3])
        form_group.get_statusDefault()
        pass

    def test_statusTraverse(self):
        '''
        执行遍历选择状态中全部option值的用例
        :return:
        '''
        form_group.setFunctionName(inspect.stack()[0][3])
        form_group.get_statusTraverse()
        pass

    # ----------------------------类目筛选框-------------------------------
    def test_categorySelect(self):
        '''
        执行获取类目全部optios值的用例
        :return:
        '''
        form_group.setFunctionName(inspect.stack()[0][3])
        form_group.get_categorySelect()
        pass

    def test_categoryDefault(self):
        '''
        执行类目默认值的用例
        :return:
        '''
        form_group.setFunctionName(inspect.stack()[0][3])
        form_group.get_categoryDefault()
        pass

    def test_categoryTraverse(self):
        '''
        执行遍历选择类目中全部option值的用例
        :return:
        '''
        form_group.setFunctionName(inspect.stack()[0][3])
        form_group.get_categoryTraverse()
        pass

    # ----------------------------对象筛选框-------------------------------
    def test_preferencesSelect(self):
        '''
        执行获取对象全部optios值的用例
        :return:
        '''
        form_group.setFunctionName(inspect.stack()[0][3])
        form_group.get_preferencesSelect()
        pass

    def test_preferencesDefault(self):
        '''
        执行对象默认值的用例
        :return:
        '''
        form_group.setFunctionName(inspect.stack()[0][3])
        form_group.get_preferencesDefault()
        pass

    def test_preferencesTraverse(self):
        '''
        执行遍历选择对象中全部option值的用例
        :return:
        '''
        form_group.setFunctionName(inspect.stack()[0][3])
        form_group.get_preferencesTraverse()
        pass

    # ----------------------------輸入框以及按鈕-------------------------------
    def test_conditionsInput(self):
        form_group.setFunctionName(inspect.stack()[0][3])
        form_group.jude_input_conditions()
        pass

    def test_button_search(self):
        form_group.setFunctionName(inspect.stack()[0][3])
        form_group.jude_button_search()
        pass

    def test_button_export(self):
        form_group.setFunctionName(inspect.stack()[0][3])
        form_group.jude_button_export()
        pass
