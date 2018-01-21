# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: selenium_input.py
@time: 2017/6/21 0:01
"""
import os
# 这是元素输入类，传入相应的id，name，text，xpath，css以及内容就可以执行输入的指令
from time import sleep

from practical.operation.selenium_visible import action_visible
from practical.utils import DefinitionErrors as dError

r'''
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
'''


class action_input(action_visible):
    def id_input(self, browser, id, parameter):
        ele = self.is_visible_id(browser, id)
        if ele != False:  # 判断是否出现
            # 元素输入
            self.ele_clear_keys(ele, parameter)
        else:
            self.error_log(browser)
        '''
        try:
            ele = browser.find_element_by_id(id)
            self.ele_clear_keys(ele, parameter)
        except:
            self.writeLog(browser)
        '''

    def name_input(self, browser, name, parameter):
        ele = self.is_visible_name(browser, id)
        if ele != False:  # 判断是否出现
            # 元素输入
            self.ele_clear_keys(ele, parameter)
        else:
            self.error_log(browser)

    def css_input(self, browser, css, parameter, timeout=5):
        ele = self.is_visible_css_selectop(browser, css)
        if ele != False:  # 判断是否出现
            # 元素输入
            self.ele_clear_keys(ele, parameter)
        else:
            self.error_log(browser)

    def xpath_input(self, browser, xpath, parameter):
        ele = self.is_visible_xpath(browser, css)
        if ele != False:  # 判断是否出现
            # 元素输入
            self.ele_clear_keys(ele, parameter)
        else:
            self.error_log(browser)

    def transmitList(self,browser, combination):
        for num in range(len(combination)):
            meter = combination[num]
            self.css_input(browser,meter.parameter,meter.content)

    def transmitDictionaries(self,browser, combination):
        for _key, _value in combination.items():
            self.css_input(browser, _value, _key)

    def id_js_input(self, browser, ordinal, parameter):
        try:
            browser.execute_script("document.getElementById(\'" + ordinal + "\').value=\'" + parameter + "\';")
        except:
            self.writeLog(browser)


    # 光标从ele元素上移除
    def blur_ele(self, browser, ele):
        browser.execute_script("arguments[0].blur();", ele)

    # 根据id从该元素上进行移除
    def blur_id(self, browser, ordinal):
        browser.execute_script("document.getElementById(\'" + ordinal + "\').blur();")

    # 光标移动到id为ordinal的元素上
    def focus_id(self, browser, ordinal):
        browser.execute_script("document.getElementById(\'" + ordinal + "\').focus();" )

    # 光标移动到ele元素上
    def focus_ele(self, browser, ele):
        browser.execute_script("arguments[0].focus();", ele)

    # 执行输入的操作
    def ele_clear_keys(self, ele, parameter):
        ele.clear()
        ele.send_keys(parameter)
        sleep(2)
