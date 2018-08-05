# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: cityTabJude.py
@time: 2018/8/5 22:21
@Entry Name:operating
"""
from CenterBackground.GoodsManagement.CityGoods.conditionsJude import ConditionsJude

class CityTabJude(ConditionsJude):
    CHILD_TAGS_LOCATION = 1
    MODEL_WORKBOOK_CITY = '城市'
    MODEI_CASE_POSITION = 'city'
    def __init__(self):
        ConditionsJude.__init__()
    def get_already_citys(self):
        '''
        获取全部的数据信息
        :return:
        '''
        city_list = []
        city_ele = self._visible_returns_selectop(
            self.financial_path[self.goods.city_tab()][self.goods.yaml_value()])
        for ele in city_ele:
            if ele.get_attribute(self.goods.ele_class()) != 'pull-right':
                city_list.append(ele.text)
        print('全部的数据信息:----> %s' % active_name)
        pass
    def get_already_codes(self):
        city_list = []
        city_ele = self._visible_returns_selectop(
            self.financial_path[self.goods.city_tab()][self.goods.yaml_value()])
        # 遍历读取全部对象的code值
        for ele in city_ele:
            if operator.eq(ele.get_attribute(self.goods.ele_class()),self.goods.ele_active()):
                subclass_a = ele.find_element_by_tag_name(self.goods.yaml_label())
                active_code = subclass_a.get_attribute(self.goods.ele_class())
                city_list.append(StringCutting.re_zip_code(active_code))
        print('全部的数据信息的code:----> %s' % active_name)
        pass
    def get_active_city(self):
        city_ele = self._visible_returns_selectop(
            self.financial_path[self.goods.yaml_city_tab()][self.goods.yaml_value()])
        # 获取默认active
        for ele in city_ele:
            if operator.eq(ele.get_attribute(self.goods.ele_class()),self.goods.ele_active()):
                active_name = ele.text
                assert operator.eq(active_name,  self.overall[self.goods.excle_name()]), '进入之后，默认值不对'
                break
        print('默认展开的数据:----> %s' % active_name)

    def get_active_code(self):
        city_ele = self._visible_returns_selectop(
            self.financial_path[self.goods.city_tab()][self.goods.yaml_value()])
        # 获取默认active的code
        for ele in city_ele:
            if operator.eq(ele.get_attribute(self.goods.ele_class()),self.goods.ele_active()):
                subclass_a = ele.find_element_by_tag_name(self.goods.yaml_label())
                active_code = subclass_a.get_attribute(self.goods.ele_class())
                active_code = StringCutting.re_zip_code(active_code)
                assert operator.eq(active_code, self.overall[self.goods.excle_code()]), '进入之后，默认code不对'
                break
        print('默认数据的code:----> %s' % active_code)

    def click_switch_city(self):
        city_ele = self._visible_returns_selectop(
            self.financial_path[self.goods.city_tab()][self.goods.yaml_value()])
        # 获取全部不等于添加按钮的对象信息
        for ele in city_ele:
            if ele.get_attribute(self.goods.ele_class()) != 'pull-right':
                self.vac.element_click(ele)
                city_list.append(ele.text)

    def click_switch_code(self):
        city_list = {}
        # 找到界面上相应的数据对象
        city_ele = self._visible_returns_selectop(
            self.financial_path[self.goods.city_tab()][self.goods.yaml_value()])

        # 读取这些对象的全部数据信息
        for ele in city_ele:
            if operator.eq(ele.get_attribute(self.goods.ele_class()), self.goods.ele_active()):
                subclass_a = ele.find_element_by_tag_name(self.goods.yaml_label())
                city_list[ele.text] = subclass_a.get_attribute(self.goods.ele_class())

        # 遍历的同时执行判断
        for key,value in city_list.items():
            self.driver.get(value)
            city_active = self._visible_returns_selectop(
                self.financial_path[self.goods.city_tab()][self.goods.yaml_active()])
            assert operator.eq(key,city_active),'遍历点击之后，默认值不对'
