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
from tools.operation.selenium_visible import action_visible as av
from tools import StringCutting

_att = 'a'
_href = 'href'
_class = 'class'
_active = 'active'


class CustomTabs(object):
    '''
    Use the tabs path to get the value of the element and the corresponding active.
    Parse the label attributes in the element to get the qualified code.
    '''

    def __init__(self, driver, parth):
        self.driver = driver
        self.parth = parth
        pass

    def visibles_tabs(self):
        '''
        is_visibles_css_selectop传入self并没有实际的意义,如果不传就要实例化av对象
        :return:
        '''
        self.ul_li = av.is_visibles_css_selectop(self, self.driver, self.parth)

    def active_tab(self):
        '''
        比较li标签的class值
        :return:
        '''
        self.visibles_tabs()
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

    def custom_keys(self):
        '''
        全部城市和编码
        :return:  城市为key，编码为value
        '''
        self.visibles_tabs()
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

    def instance_citys(self):
        '''
        :param parth:
        :return:  全部城市
        '''
        self.visibles_tabs()
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

    def instance_codes(self):
        '''
        :return: 全部元素的编码
        '''
        self.visibles_tabs()
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

    def judge_source(self):
        pass

    def judge_citys(self, ov_default=True):
        list_text = self.instance_citys()
        assert operator.eq(True, ov_default), 'All labels in the title are misjudged.'
        pass

    def judge_city(self, ov_default):
        ct_default = self.active_city()
        assert operator.eq(ct_default, ov_default), 'The caption tabs element text is judged incorrectly.'
        pass

    def judge_codes(self, ov_default=True):
        list_code = self.instance_codes()
        print(list_code)
        assert operator.eq(True, ov_default), 'All labels in the title are misjudged.'
        pass

    def judge_code(self, ov_default):
        ct_default = self.active_code()
        ov_default = StringCutting.specified_cut_ber(ov_default, '.')
        assert operator.eq(ct_default, ov_default), 'The header label attribute is incorrect.'
        pass
