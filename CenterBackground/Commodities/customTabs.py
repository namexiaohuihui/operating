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
from tools.operation.selenium_visible import action_visible as av
from tools import StringCutting


class CustomTabs(object):
    '''
    Use the tabs path to get the value of the element and the corresponding active.
    Parse the label attributes in the element to get the qualified code.
    '''

    def __init__(self, driver):
        self.driver = driver
        pass

    def visibles_tabs(self, parth):
        '''
        is_visibles_css_selectop传入self并没有实际的意义。。。
        如果不传就要实例化av对象
        :param parth:
        :return:
        '''
        self.ul_li = av.is_visibles_css_selectop(self, self.driver, parth)

    def custom_keys(self, parth, att):
        self.visibles_tabs(parth)
        custom_d = {}
        for li in self.ul_li:
            li_a = li.find_element_by_tag_name('a')
            li_a = li_a.get_attribute(att)
            custom_d[li_a.text.strip()] = StringCutting.re_zip_code(li_a)
        return custom_d

    def instance_text(self, parth):
        self.visibles_tabs(parth)
        list_text = [li.text.strip() for li in self.ul_li]
        return list_text

    def instance_code(self, parth, att):
        self.visibles_tabs(parth)
        list_code = []
        for li in self.ul_li:
            li_a = li.find_element_by_tag_name('a')
            li_a = li_a.get_attribute(att)
            li_a = StringCutting.re_zip_code(li_a)
            li_code.append(li_a)
        return list_code

    def active_tab(self, parth, att):
        '''
        找到页面中tabs中默认选取的对象
        :param parth:
        :param att:
        :return:
        '''
        self.visibles_tabs(parth)
        for li in self.ul_li:
            if 'active' in li.get_attribute(att):
                break
        return li

    def active_keys(self, parth, att):
        li = self.active_tab(parth, att)
        active_d = {}
        li_a = li.find_element_by_tag_name('a')
        li_a = li_a.get_attribute(att)
        active_d[li_a.text.strip()] = StringCutting.re_zip_code(li_a)
        return active_d

    def active_text(self, parth, att):
        li = self.active_tab(parth, att)
        li_text = li.text.strip()
        return li_text

    def active_code(self, parth, att):
        li = self.active_tab(parth, att)
        li_code = li.find_element_by_tag_name('a')
        li_code = li_code.get_attribute(att)
        li_code = StringCutting.re_zip_code(li_code)
        return li_code
