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
@file: customTabs.py
@time: 2018/8/21 10:15
@desc:
'''
import operator
from tools.operation.selenium_click import action_click
from tools import StringCutting

_att = 'a'
_href = 'href'
_class = 'class'
_active = 'active'


class CustomTypeError(Exception):
    pass


class CustomTabs(object):
    '''
    Use the tabs path to get the value of the element and the corresponding active.
    Parse the label attributes in the element to get the qualified code.
    '''

    def __init__(self, driver, parth):
        self.driver = driver
        self.parth = parth
        self.ac = action_click()
        pass

    def is_visibles(self):
        '''
          is_visibles_css_selectop传入self并没有实际的意义,如果不传就要实例化ac对象
          :return:
        '''
        self.ul_li = self.ac.is_visibles_css_selectop(self.driver, self.parth)
        if type(self.ul_li) is bool:
            raise CustomTypeError("You can't find the tabs element.")

    def visibles_tabs(self, reduce=0):
        '''
        将后面不需要的button给排除
        :param reduce:
        :return:
        '''
        self.is_visibles()
        reduce = int(reduce)
        for l in range(reduce):
            length = len(self.ul_li) - 1
            self.ul_li.pop(length)

    def active_tab(self, reduce=0):
        '''
        比较li标签的class值
        :return:
        '''
        self.visibles_tabs(reduce)
        for li in self.ul_li:
            ac_at = li.get_attribute(_class)
            if operator.eq(_active, ac_at):
                return li
        return 'active_tab: no li'

    def city_code(self, li):
        li_a = li.find_element_by_tag_name(_att)
        li_a = li_a.get_attribute(_href)
        li_a = StringCutting.re_zip_code(li_a)
        return li_a

    def custom_keys(self, reduce=0):
        '''
        全部城市和编码
        :return:  城市为key，编码为value
        '''
        self.visibles_tabs(reduce)
        custom_d = {}
        for li in self.ul_li:
            li_a = li.find_element_by_tag_name(_att)
            li_a = li_a.get_attribute(_href)
            custom_d[li_a.text.strip()] = StringCutting.re_zip_code(li_a)
        return custom_d

    def active_keys(self):
        '''
        默认城市和编码
        :return: 城市为key，编码为value
        '''
        li = self.active_tab()
        li_a = li.find_element_by_tag_name(_att)
        li_a = li_a.get_attribute(_href)
        active_d = {li_a.text.strip(): StringCutting.re_zip_code(li_a)}
        return active_d

    def instance_citys(self, reduce=0):
        '''
        :param parth:
        :return:  全部城市
        '''
        self.visibles_tabs(reduce)
        list_text = [li.text.strip() for li in self.ul_li]
        return list_text

    def active_city(self):
        '''
        默认城市
        :return:
        '''
        li = self.active_tab()
        li_text = li.text.strip()
        return li_text

    def instance_codes(self, reduce=0):
        '''
        :return: 全部元素的编码
        '''
        self.visibles_tabs(reduce)
        list_code = [self.city_code(li) for li in self.ul_li]
        return list_code

    def active_code(self):
        '''
        默认城市编码
        :return:
        '''
        li = self.active_tab()
        li_code = self.city_code(li)
        return li_code

    def judge_source(self, reduce=0):
        self.visibles_tabs(reduce)
        length = len(self.ul_li)
        for l in range(length):
            self.ac.element_click(self.ul_li[l])
            self.visibles_tabs(reduce)
        pass

    def judge_source_url(self, reduce):
        list_text = self.judge_citys(reduce)  # 读取全部的城市
        length = len(self.ul_li)  # 读取数据长度
        self.visibles_tabs(reduce)
        for l in range(length):
            # 读取默认值对象的href属性
            li_a = self.ul_li[l].find_element_by_tag_name(_att)
            li_a = li_a.get_attribute(_href)
            # 输入网址
            self.driver.get(li_a)
            # 数据比较
            self.judge_city(list_text[l])
            self.visibles_tabs(reduce)
        pass

    def judge_citys(self, reduce=0, ov_default=True):
        list_text = self.instance_citys(reduce)
        assert operator.eq(True, ov_default), 'All labels in the title are misjudged.'
        return list_text

    def judge_city(self, ov_default):
        ct_default = self.active_city()
        assert operator.eq(ct_default, ov_default), 'The caption tabs element text is judged incorrectly.'
        pass

    def judge_codes(self, reduce=0, ov_default=True):
        list_code = self.instance_codes(reduce)
        assert operator.eq(True, ov_default), 'All labels in the title are misjudged.'
        return list_code

    def judge_code(self, ov_default):
        ct_default = self.active_code()
        ov_default = StringCutting.specified_cut_ber(ov_default, '.')
        assert operator.eq(ct_default, ov_default), 'The header label attribute is incorrect.'
        pass
