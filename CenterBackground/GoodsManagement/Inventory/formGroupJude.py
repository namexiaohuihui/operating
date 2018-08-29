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
@file: formGroupJude.py
@time: 2018/8/13 17:02
@desc:
'''
import operator
from tools.screeningdrop import ScreeningDrop
from CenterBackground.judeVerification import JudgmentVerification
from CenterBackground.GoodsManagement import Inventory
from tools.excelname.Center.gongsMana import CityGoodsPage


class FormGroupJude(JudgmentVerification):

    def __init__(self, option):
        JudgmentVerification.__init__(self, Inventory.add_key(option))
        self.cGoods = CityGoodsPage()
        pass

    def return_status(self) -> str:
        s_status = self.financial[self.cGoods.yaml_formGroup()][self.cGoods.yaml_status()]
        return s_status

    def return_category(self) -> str:
        s_category = self.financial[self.cGoods.yaml_formGroup()][self.cGoods.yaml_category()]
        return s_category

    def return_preferences(self) -> str:
        s_preferences = self.financial[self.cGoods.yaml_formGroup()][self.cGoods.yaml_preferences()]
        return s_preferences

    def create_select(self, direction: str) -> ScreeningDrop:
        '''
        创建操作select的对象
        :param direction:
        :return:
        '''
        op_se = ScreeningDrop(self.driver, direction)
        return op_se

    # 获取按钮对象
    def button_formSub(self, att):
        form_group = self.financial[self.cGoods.yaml_formGroup()]
        attribute = self._visible_returns_selectop(
            form_group['formSub'])
        attribute = attribute[int(form_group[att]) - 1]
        return attribute

    def jude_attribute_text(self, att, information):
        attribute = self.button_formSub(att).text
        ov_attribute = self.overall[self.cGoods.whole_default()]
        assert operator.eq(attribute, ov_attribute), information
        pass

    def value_options_jude(self, value: str, information: str):
        '''
        根据指定的路径获取select下面的全部option值
        :param value:
        :param information:
        :return:
        '''
        op_se = self.create_select(value)
        # 获取全部的options
        op_str = op_se.options_to_str()
        ov_str = self.overall[self.cGoods.whole_including()]
        assert operator.eq(op_str, ov_str), information
        pass

    def value_options_default(self, value: str, information: str):
        '''
        根据指定的路径获取select下默认的option值
        :param value:
        :param information:
        :return:
        '''
        op_se = self.create_select(value)
        op_str = op_se.getSelectedOptions()
        ov_str = self.overall[self.cGoods.whole_default()]
        assert operator.eq(op_str, ov_str), information
        pass

    def value_option_traverse(self, value, information):
        op_se = self.create_select(value)
        op_list = op_se.getAllOptions()
        for value_str in op_list:
            # 设置option
            op_se.setSelectorText(value_str)
            # 点击搜索按钮
            # 获取按钮对象
            self.button_formSub(self.cGoods.yaml_search()).click()
            # 重新設置text之後，界面會進行刷新此時driver對象也發生改變需要重新進行獲取
            op_se = self.create_select(value)
            # 判断当前显示的option是否为设置的option
            op_str = op_se.getSelectedOptions()
            assert operator.eq(value_str, op_str), information

    def get_categorySelect(self):
        '''
        类目select下的option数据值获取，并进行比较
        :return:
        '''
        value = self.return_category()
        information = 'TOption value comparison error included in category select...'
        self.value_options_jude(value, information)
        pass

    def get_categoryDefault(self):
        '''
        类目select下option的默认值
        :return:
        '''
        value = self.return_category()
        information = 'The default value of option in category select is wrong...'
        self.value_options_default(value, information)

    def get_categoryTraverse(self):
        value = self.return_category()
        information = 'An error occurred while traversing the option value of the category select...'
        self.value_option_traverse(value, information)
        pass

    def jude_input_conditions(self):
        attribute = self._visible_css_selectop_attribute(
            self.financial[self.cGoods.yaml_formGroup()][self.cGoods.yaml_conditions()],
            self.cGoods.yaml_placeholder())
        ov_attribute = self.overall[self.cGoods.whole_default()]
        information = 'Wrong placeholder attribute value in input box.'
        assert operator.eq(attribute, ov_attribute), information
        pass

    def jude_button_search(self):
        information = 'Search button text judgement error...'
        self.jude_attribute_text(self.cGoods.yaml_search(), information)
        pass

    def jude_button_export(self):
        information = 'Error in export button text judgement...'
        self.jude_attribute_text(self.cGoods.yaml_export(), information)
        pass
