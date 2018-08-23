# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: cityTabJude.py
@time: 2018/8/5 22:21
@Entry Name:operating
"""
import operator
from tools import StringCutting
from CenterBackground.GoodsManagement import CityGoods
from CenterBackground.judeVerification import JudgmentVerification
from tools.excelname.Center.gongsMana import CityGoodsPage


class ActiveTabJude(JudgmentVerification):

    def __init__(self, option):
        JudgmentVerification.__init__(self, CityGoods.add_key(option))
        self.cGoods = CityGoodsPage()
        pass

    def get_label_tab(self):
        '''
        获取tab的全部对象
        :return:
        '''
        city_ele = self._visible_returns_selectop(
            self.financial[self.cGoods.yaml_city_tab()][self.cGoods.yaml_value()])
        return city_ele

    def father_screening_child(self, compare, information):
        # 返回指定css路径的对象
        city_obj = self._visible_return_selectop(
            self.financial[self.cGoods.yaml_city_tab()][self.cGoods.yaml_obj()])

        # 通过css获取该对象下面指定的子元素
        city_active = city_obj.find_element_by_css_selector(
            self.financial[self.cGoods.yaml_city_tab()][self.cGoods.yaml_active()])

        assert operator.eq(compare, city_active.text), information
        pass

    def father_re_child(self, ele):
        # 父类通过指定的元素名来找到子元素，子元素获取指定属性值，通过正则解析出数字
        subclass_a = ele.find_element_by_tag_name(
            self.financial[self.cGoods.yaml_city_tab()][self.cGoods.yaml_label()])
        active_code = subclass_a.get_attribute(self.cGoods.ele_href())
        active_code = StringCutting.re_zip_code(active_code)
        return active_code

    def get_already_citys(self):
        '''
        获取全部的数据信息
        :return:
        '''
        city_list = []
        city_ele = self.get_label_tab()
        for ele in city_ele:
            if ele.get_attribute(self.cGoods.ele_class()) != 'pull-right':
                city_list.append(ele.text)
        print('全部的数据信息:----> %s' % city_list)
        pass

    def get_already_codes(self):
        city_list = []
        city_ele = self.get_label_tab()
        # 遍历读取全部对象的code值
        for ele in city_ele:
            if ele.get_attribute(self.cGoods.ele_class()) != 'pull-right':
                active_code = self.father_re_child(ele)
                city_list.append(active_code)
        print('全部的数据信息的code:----> %s' % city_list)
        pass

    def get_active_city(self):
        city_ele = self.get_label_tab()
        # 获取默认active
        for ele in city_ele:
            if operator.eq(ele.get_attribute(self.cGoods.ele_class()), self.cGoods.yaml_active()):
                active_name = ele.text
                # 产品要求的默认城市跟实际当中的默认城市是否一致
                assert operator.eq(active_name, self.overall[self.cGoods.whole_city()]), '进入之后，默认值不对'
                break
        print('默认展开的数据:----> %s' % active_name)

    def get_active_code(self):
        city_ele = self.get_label_tab()
        # 获取默认active的code
        for ele in city_ele:
            if operator.eq(ele.get_attribute(self.cGoods.ele_class()), self.cGoods.yaml_active()):
                active_code = self.father_re_child(ele)
                # 比较默认城市的code值是否正确
                assert operator.eq(int(active_code), int(self.overall[self.cGoods.whole_code()])), '进入之后，默认code不对'
                break
        print('默认数据的code:----> %s' % active_code)

    def click_switch_city(self):
        '''
        根据text进行切换
        :return:
        '''
        city_list = []
        city_ele = self.get_label_tab()
        # 获取全部不等于添加按钮的对象信息
        for ele in city_ele:
            if ele.get_attribute(self.cGoods.ele_class()) != 'pull-right':
                city_list.append(ele.text)

        for ele_number in range(len(city_list)):
            # 获取tab全部数据信息
            city_ele = self.get_label_tab()
            # 根据位置进行点击
            self.vac.element_click(city_ele[ele_number])
            self.father_screening_child(city_list[ele_number], '遍历TEXT，默认值不对')
        pass

    def click_switch_code(self):
        '''
        根据URL进行切换
        :return:
        '''
        city_list = {}
        # 找到界面上相应的数据对象
        city_ele = self.get_label_tab()

        # 读取这些对象的全部数据信息
        for ele in city_ele:
            if ele.get_attribute(self.cGoods.ele_class()) != 'pull-right':
                subclass_a = ele.find_element_by_tag_name(
                    self.financial[self.cGoods.yaml_city_tab()][self.cGoods.yaml_label()])
                city_list[ele.text] = subclass_a.get_attribute(self.cGoods.ele_href())

        # 遍历的同时执行判断
        for key, value in city_list.items():
            # 进入指定的url
            self.driver.get(value)
            self.father_screening_child(key, '遍历URL，默认值不对')
