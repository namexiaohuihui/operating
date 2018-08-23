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
@file: groupJude.py
@time: 2018/8/14 15:55
@desc:
'''
from CenterBackground.judeVerification import JudgmentVerification
from CenterBackground.GoodsManagement import Evaluation
from tools.excelname.Center.gongsMana import CityGoodsPage
from tools.operationSelector import OperationSelector


class GroupJude(JudgmentVerification):
    def __init__(self, option):
        JudgmentVerification.__init__(self, Evaluation.add_key(option))
        self.cGoods = CityGoodsPage()
        pass

    # -----------------------统一返回元素的位置----------
    def quality_direction(self):
        '''
        返回quality元素对应的路径
        :return:
        '''
        value = self.financial[self.cGoods.page_evaluation()][self.cGoods.page_quality()]
        return value

    def cond_direction(self):
        '''
        返回cond元素对应的路径
        :return:
        '''
        value = self.financial[self.cGoods.page_evaluation()][self.cGoods.yaml_type()]
        return value

    def time_direction(self):
        '''
        返回time元素对应的路径
        :return:
        '''
        value = self.financial[self.cGoods.page_evaluation()][self.cGoods.page_timeType()]
        return value

    # -----------------------下拉框对象定义------------------------
    def create_select(self, direction: str) -> OperationSelector:
        '''
        创建操作select的对象
        :param direction:
        :return:
        '''
        op_se = OperationSelector(self.driver, direction)
        return op_se

    # ----------------------用例二级判断，可抽取到父类-------------------
    def button_formSub(self, att):
        form_group = self.financial[self.cGoods.page_evaluation()]
        attribute = self._visible_returns_selectop(
            form_group['formSub'])
        attribute = attribute[int(form_group[att]) - 1]
        return attribute

    def jude_attribute_text(self, att, information):
        attribute = self.button_formSub(att).text
        ov_attribute = self.overall[self.cGoods.whole_default()]
        assert self.verify_dataframe(attribute, ov_attribute), information
        pass

    def options_jude(self, value, information):
        # 将select内置的options全部转成str，每个item之间用逗号隔开
        op_str = self.create_select(value).options_to_str()

        # 获取用例设置全部的options值
        ov_str = self.overall[self.cGoods.whole_including()]

        assert self.verify_dataframe(op_str, ov_str), information

    def default_jude(self, value, information):
        # 将select内置的options全部转成str，每个item之间用逗号隔开
        op_str = self.create_select(value).getSelectedOptions()

        # 获取用例设置全部的options值
        ov_str = self.overall[self.cGoods.whole_default()]

        assert self.verify_dataframe(op_str, ov_str), information

    def traverse_jude(self, value, information):
        # 将select内置的options全部转成str，每个item之间用逗号隔开
        op_se = self.create_select(value)
        op_list = op_se.getAllOptions()

        for value_str in op_list:
            # 设置option
            op_se.setSelectorText(value_str)
            # 点击搜索按钮
            self.button_formSub(self.cGoods.yaml_search()).click()

            # 重新設置option之後，界面會進行刷新此時driver對象也發生改變需要重新進行獲取
            op_se = self.create_select(value)

            # 判断当前显示的option是否为设置的option
            op_str = op_se.getSelectedOptions()

            # 判断用户设置的option最后显示是否正确
            assert self.verify_dataframe(value_str, op_str), information

        pass

    # --------------------------------------------------------
    # ---------------------用例直接调用进行使用-------------------
    # ---------------------quality用例位置----------------------
    # --------------------------------------------------------
    def get_quality(self):
        value = self.quality_direction()
        information = 'The total data judgment of the quality select is an error.'
        self.options_jude(value, information)
        pass

    def get_qualityDefault(self):
        value = self.quality_direction()
        information = 'The quality select default options judgment is error.'
        self.default_jude(value, information)
        pass

    def get_qualityTraverse(self):
        value = self.quality_direction()
        information = 'The quality select traversal option is an error.'
        self.traverse_jude(value, information)
        pass

    # --------------------------------------------------------
    # ---------------------用例直接调用进行使用-------------------
    # ---------------------conditions用例位置-------------------
    # --------------------------------------------------------
    def get_conditions(self):
        value = self.cond_direction()
        information = 'The total data judgment of the conditions select is an error.'
        self.options_jude(value, information)
        pass

    def get_conndDefault(self):
        value = self.cond_direction()
        information = 'The conditions select default options judgment is error.'
        self.default_jude(value, information)
        pass

    def get_conndTraverse(self):
        value = self.cond_direction()
        information = 'The conditions select traversal option is an error.'
        self.traverse_jude(value, information)
        pass

    # --------------------------------------------------------
    # ---------------------用例直接调用进行使用-------------------
    # ---------------------timetype用例位置---------------------
    # --------------------------------------------------------
    def get_timeOrder(self):
        value = self.time_direction()
        information = 'The total data judgment of the get_timeOrder select is an error.'
        self.options_jude(value, information)
        pass

    def get_timeDefault(self):
        value = self.time_direction()
        information = 'The get_timeOrder select default options judgment is error.'
        self.default_jude(value, information)
        pass

    def get_timeTraverse(self):
        value = self.time_direction()
        information = 'The get_timeOrder select traversal option is an error.'
        self.traverse_jude(value, information)
        pass

    # --------------------------------------------------------
    # ---------------------用例直接调用进行使用-------------------
    # ---------------------conditionsInput用例位置--------------
    # --------------------------------------------------------
    def get_conditionsInput(self):
        # 读取输入框上显示的内容
        attribute = self._visible_css_selectop_attribute(
            self.financial[self.cGoods.yaml_formGroup()][self.cGoods.yaml_conditions()],
            self.cGoods.yaml_placeholder())
        # 读取用例默认应显示的内容
        ov_attribute = self.overall[self.cGoods.whole_default()]
        # 错误时的提示信息
        information = 'Wrong placeholder attribute value in input box.'
        # 比较用例和输入框显示的内容是否一致
        assert self.verify_dataframe(attribute, ov_attribute), information
        pass

    def get_timename(self):
        # 读取输入框上显示的内容
        attribute = self._visible_css_selectop_attribute(
            self.financial[self.cGoods.page_evaluation()][self.cGoods.page_timename()])
        # 读取用例默认应显示的内容
        ov_attribute = self.overall[self.cGoods.whole_default()]
        # 错误时的提示信息
        information = 'Wrong timename attribute value in input box.'
        # 比较用例和输入框显示的内容是否一致
        assert self.verify_dataframe(attribute, ov_attribute), information
        pass

    def jude_button_search(self):
        information = 'Search button text judgement error...'
        self.jude_attribute_text(self.cGoods.yaml_search(), information)
        pass

    def jude_button_export(self):
        information = 'Error in export button text judgement...'
        self.jude_attribute_text(self.cGoods.yaml_export(), information)
        pass