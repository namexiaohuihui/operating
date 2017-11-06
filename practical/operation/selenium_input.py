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


class element_input(object):

    def id_input(self, browser, id, data):
        try:
            ele = browser.find_element_by_id(id)
            self.ele_clear_keys(ele, data)
        except:
            self.writeLog()

    def name_input(self, browser, name, data):
        try:
            ele = browser.find_element_by_name(name)
            self.ele_clear_keys(ele, data)
        except:
            self.writeLog()

    def css_input(self, browser, css, data):
        try:
            ele = browser.find_element_by_css_selector(css)
            self.ele_clear_keys(ele, data)
        except:
            self.writeLog()

    def xpath_input(self, browser, xpath, data):
        try:
            ele = browser.find_element_by_xpath(xpath)
            self.ele_clear_keys(ele, data)
        except:
            self.writeLog()

    def id_js_input(self, browser, ordinal, parameter):
        try:
            browser.execute_script("document.getElementById(\'" + ordinal + "\').value=\'" + parameter + "\';")
        except:
            self.writeLog()

    def ele_clear_keys(self, ele, data):
        ele.clear()
        ele.send_keys(data)
        sleep(1)

    def writeLog(self):
        basename = os.path.splitext(os.path.basename(__file__))[0]
        print("自己定义的_文件出现错误,名为名=%s" % \
              basename, )
        sys.exit(0)
        raise
