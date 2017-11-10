# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: selenium_input.py
@time: 2017/6/21 0:01
"""
import os
# 这是元素输入类，传入相应的id，name，text，xpath，css以及内容就可以执行输入的指令
import sys
from time import sleep

from practical.Exception_error.DefinitionError import definition_error
from practical.operation.selenium_visible import element_visible

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
'''


class element_input(element_visible):
    def id_input(self, browser, id, parameter):

        if self.is_visible_id(browser, id): #判断是否出现
            # 元素输入
            ele = browser.find_element_by_id(id)
            self.ele_clear_keys(ele, parameter)
        else:
            self.writeLog(browser)
        '''
        try:
            ele = browser.find_element_by_id(id)
            self.ele_clear_keys(ele, parameter)
        except:
            self.writeLog(browser)
        '''

    def name_input(self, browser, name, parameter):

        if self.is_visible_name(browser, name): #判断是否出现
            # 元素输入
            ele = browser.find_element_by_name(name)
            self.ele_clear_keys(ele, parameter)
        else:
            self.writeLog(browser)

    def css_input(self, browser, css, parameter):
        if self.is_visible_css_selectop(browser, css): #判断是否出现
            # 元素输入
            ele = browser.find_element_by_css_selector(css)
            self.ele_clear_keys(ele, parameter)
        else:
            self.writeLog(browser)

    def xpath_input(self, browser, xpath, parameter):
        if self.is_visible_xpath(browser, xpath): #判断是否出现
            # 元素输入
            ele = browser.find_element_by_xpath(xpath)
            self.ele_clear_keys(ele, parameter)
        else:
            self.writeLog(browser)


    def id_js_input(self, browser, ordinal, parameter):
        try:
            browser.execute_script("document.getElementById(\'" + ordinal + "\').value=\'" + parameter + "\';")
        except:
            self.writeLog(browser)

    def ele_clear_keys(self, ele, parameter):
        ele.clear()
        ele.send_keys(parameter)

    def writeLog(self, browser):
        basename = os.path.splitext(os.path.basename(__file__))[0]
        print("自己定义的_文件出现错误,名为名=%s" % \
              basename, )
        basename = os.path.splitext(os.path.basename(__file__))[0]
        # 组合日志文件名（当前文件名 + 当前时间）.比如：case_login_success_20150817192533
        de_error = definition_error()
        de_error.erroe_get(basename, browser)
        # sys.exit(0)
        # raise
