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
@time: 2018/8/6 14:34
@desc:
'''
import operator
from tools import StringCutting
from tools.operationSelector import OperationSelector
from CenterBackground.GoodsManagement.CityGoods.conditionsJude import ConditionsJude


class FormGroupJude(ConditionsJude):
    MODEL_WORKBOOK_CITY = '筛选'

    def __init__(self):
        ConditionsJude.__init__(self)
        pass

    def return_status(self) -> str:
        s_status = self.financial_path[self.goods.yaml_formGroup()][self.goods.yaml_statusV()]
        return s_status

    def return_category(self) -> str:
        s_category = self.financial_path[self.goods.yaml_formGroup()][self.goods.yaml_categoryV()]
        return s_category

    def return_preferences(self) -> str:
        s_preferences = self.financial_path[self.goods.yaml_formGroup()][self.goods.yaml_preferencesV()]
        return s_preferences

    def create_select(self, direction: str) -> OperationSelector:
        '''
        创建操作select的对象
        :param direction:
        :return:
        '''
        op_se = OperationSelector(self.driver, direction)
        return op_se

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
        ov_str = self.overall[self.goods.excle_including()]
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
        ov_str = self.overall[self.goods.excle_default()]
        assert operator.eq(op_str, ov_str), information
        pass

    def value_option_traverse(self, value, information):
        op_se = self.create_select(value)
        op_list = op_se.getAllOptions()
        for value_str in op_list:
            # 设置option
            op_se.setSelectorText(value_str)
            # 点击搜索按钮
            self._visible_css_selectop(self.financial_path[self.goods.yaml_formGroup()][self.goods.yaml_searchB()])
            # 重新設置text之後，界面會進行刷新此時driver對象也發生改變需要重新進行獲取
            op_se = self.create_select(value)
            # 判断当前显示的option是否为设置的option
            op_str = op_se.getSelectedOptions()
            assert operator.eq(value_str, op_str), information

    def get_statusSelect(self):
        '''
        状态select下的option数据值获取，并进行比较
        :return:
        '''
        value = self.return_status()
        information = 'The option value included in the status select is incorrect....'
        self.value_options_jude(value, information)
        pass

    def get_statusDefault(self):
        '''
        状态select下option的默认值
        :return:
        '''
        value = self.return_status()
        information = 'The default value of option in status select is wrong...'
        self.value_options_default(value, information)
        pass

    def get_statusTraverse(self):
        value = self.return_status()
        information = 'An error occurred while traversing the option value of the status select...'
        self.value_option_traverse(value, information)
        pass

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

    def get_preferencesSelect(self):
        '''
        对象select下的option数据值获取，并进行比较
        :return:
        '''
        value = self.return_preferences()
        information = 'Object select contains all option values that are incorrectly compared...'
        self.value_options_jude(value, information)
        pass

    def get_preferencesDefault(self):
        '''
        对象select下option的默认值
        :return:
        '''
        value = self.return_preferences()
        information = 'The default value of option in object select is wrong...'
        self.value_options_default(value, information)

    def get_preferencesTraverse(self):
        value = self.return_preferences()
        information = 'An error occurred while traversing the option value of the preferences select...'
        self.value_option_traverse(value, information)
        pass

    def jude_attribute_text(self, attribute, information):
        attribute = self._visible_css_selectop_text(
            self.financial_path[self.goods.yaml_formGroup()][attribute])
        ov_attribute = self.overall[self.goods.excle_default()]
        assert operator.eq(attribute, ov_attribute), information
        pass

    def jude_input_conditions(self):
        attribute = self._visible_css_selectop_attribute(
            self.financial_path[self.goods.yaml_formGroup()][self.goods.yaml_conditionsV()],
            self.goods.yaml_placeholder())
        ov_attribute = self.overall[self.goods.excle_default()]
        information = 'Wrong placeholder attribute value in input box.'
        assert operator.eq(attribute, ov_attribute), information
        pass

    def jude_button_search(self):
        information = 'Search button text judgement error...'
        self.jude_attribute_text(self.goods.yaml_searchB(), information)
        pass

    def jude_button_export(self):
        information = 'Error in export button text judgement...'
        self.jude_attribute_text(self.goods.yaml_exportB(), information)
        pass
