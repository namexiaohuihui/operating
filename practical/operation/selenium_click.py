# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: selenium_click
@time: 2017/6/20 22:07
"""
import os
# 这是元素点击类，传入相应的id，name，text，xpath，css就可以执行的点击事件
from time import sleep

from practical.Exception_error.DefinitionError import definition_error

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


class element_click(object):
    def id_click(self, browser, id):
        try:
            browser.find_element_by_id(id).click()
            sleep(2)
        except:
            self.writeLog(browser)

    def name_click(self, browser, name):
        try:
            browser.find_element_by_name(name).click()
            sleep(2)
        except:
            self.writeLog(browser)

    def text_click(self, browser, text):
        try:
            browser.find_element_by_link_text(text).click()
            sleep(2)
        except:
            self.writeLog(browser)

    def xpath_click(self, browser, xpath):
        try:
            browser.find_element_by_xpath(xpath).click()
            sleep(2)
        except:
            self.writeLog(browser)

    def css_click(self, browser, css):
        try:
            browser.find_element_by_css_selector(css).click()
            sleep(2)
        except:
            self.writeLog(browser)

    def css_confirm_prompt(self, browser, prompt):
        try:
            sleep(1)
            confirm = browser.find_element_by_css_selector(prompt)
            browser.execute_script("arguments[0].click();", confirm)
        except:
            self.writeLog(browser)

    def id_confirm_prompt(self, browser, prompt):
        try:
            sleep(1)
            browser.execute_script("document.getElementById(\'" + prompt + "\').click();")
        except:
            self.writeLog(browser)

    def writeLog(self, browser):
        basename = os.path.splitext(os.path.basename(__file__))[0]
        print("自己定义的_文件出现错误,名为名=%s" % \
              basename, )
        basename = os.path.splitext(os.path.basename(__file__))[0]
        # 组合日志文件名（当前文件名 + 当前时间）.比如：case_login_success_20150817192533
        de_error = definition_error()
        de_error.erroe_get(basename, browser)
        # raise
