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


class element_click(element_visible):
    def id_click(self, browser, prompt):

        if self.is_visible_id(browser, prompt):
            browser.find_element_by_id(prompt).click()
        else:
            self.writeLog(browser)
        '''
        try:
            self.is_visible_id(browser,prompt)
            browser.find_element_by_id(prompt).click()
            sleep(2)
        except:
            self.writeLog(browser)
        '''

    def name_click(self, browser, prompt):
        if self.is_visible_name(browser, prompt):
            browser.find_element_by_name(prompt).click()
        else:
            self.writeLog(browser)

    def text_click(self, browser, prompt):
        try:
            browser.find_element_by_link_text(prompt).click()
        except:
            self.writeLog(browser)

    def xpath_click(self, browser, prompt):

        if self.is_visible_xpath(browser, prompt):
            browser.find_element_by_xpath(prompt).click()
        else:
            self.writeLog(browser)

    def css_click(self, browser, prompt):

        if self.is_visible_css_selectop(self=self, browser=browser, locator=prompt):
            sleep(2)
            browser.find_element_by_css_selector(prompt).click()
        else:
            self.writeLog(browser)

    def element_click(self, element):
        element.click()
        sleep(1)

        '''
        try:
            browser.find_element_by_css_selector(prompt).click()
            sleep(2)
        except:
            self.writeLog(browser)
        '''

    def css_confirm_prompt(self, browser, prompt):

        if self.is_visible_css_selectop(browser, prompt):
            confirm = browser.find_element_by_css_selector(prompt)
            browser.execute_script("arguments[0].click();", confirm)
        else:
            self.writeLog(browser)

        '''
        try:
            sleep(1)
            confirm = browser.find_element_by_css_selector(prompt)
            browser.execute_script("arguments[0].click();", confirm)
        except:
            self.writeLog(browser)
        '''

    def id_confirm_prompt(self, browser, prompt):
        if self.is_visible_css_selectop(browser, prompt):
            browser.execute_script("document.getElementById(\'" + prompt + "\').click();")
        else:
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
