# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: selenium_click
@time: 2017/6/20 22:07
# 这是元素点击类，传入相应的id，name，text，xpath，css就可以执行的点击事件
"""
import inspect

from selenium.webdriver.common.touch_actions import TouchActions

from tools.operation.selenium_visible import action_visible

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
import os


class action_click(action_visible):
    basename = os.path.splitext(os.path.basename(__file__))[0]

    def id_click(self, browser, prompt):
        ele = self.is_visible_id(browser, prompt)
        if ele is not False:  # 判断是否出现
            self.element_click(ele)
        else:
            self.error_log(browser)

    def name_click(self, browser, prompt):
        ele = self.is_visible_name(browser, prompt)
        if ele is not False:  # 判断是否出现
            self.element_click(ele)
        else:
            self.error_log(browser)

    def xpath_click(self, browser, prompt):
        ele = self.is_visible_xpath(browser, prompt)
        if ele is not False:  # 判断是否出现
            self.element_click(ele)
        else:
            self.error_log(browser)

    def css_click(self, browser, prompt):
        ele = self.is_visible_css_selectop(browser, prompt)
        if ele is not False:  # 判断是否出现
            self.element_click(ele)
        return ele

    def element_click(self, element):
        element.click()
        self.sleep_Rest()

    def ele_confirm_prompt(self, browser, prompt):
        ele = self.is_visible_css_selectop(browser, prompt)
        if ele is not False:  # 判断是否出现
            browser.execute_script("arguments[0].click();", ele)
        else:
            self.error_log(browser)

    def id_confirm_prompt(self, browser, prompt):
        try:
            browser.execute_script("document.getElementById(\'" + prompt + "\').click();")
        except Exception as a:
            function = inspect.stack()[0][3]  # 执行函数的函数名
            print("该函数(%s,%s,%s)出现了(%s)错误" % (self.basename, function, prompt, a))

    def css_confirm_prompt(self, browser, prompt):
        try:
            self.sleep_Rest()
            browser.execute_script("document.querySelector(\'" + prompt + "\').click();")
        except Exception as a:
            function = inspect.stack()[0][3]  # 执行函数的函数名
            print("%s :没有找到这个元素: %s \n %s" % (function, prompt, a))

    def touchActions_selectop_prompt(self, browser, prompt):
        ele = self.is_visible_css_selectop(browser, prompt)
        if ele is not False:
            self.touchActions_tap(browser, ele)
        else:
            self.error_log(browser)

    """
    # 通过TouchActions来进行点击的。模拟手机来进行
    """

    def get_size(self, driver):
        # 获取浏览器的大小
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        return (x, y)

    def Interface_sliding(self, driver):
        # 实行上下滑动的效果
        screen = self.get_size()

        x1 = screen[0] * 0.5
        y1 = screen[1] * 0.75

        TouchActions(driver).scroll(x1, y1).perform()

    def touchActions_tap(self, driver, element):
        # 点击元素
        TouchActions(driver).tap(element).perform()
        self.sleep_Rest()

    """
    点击之后将element对象进行返回
    """

    def return_css_click(self, browser, prompt):
        ele = self.is_visible_css_selectop(browser, prompt)
        if ele is not False:  # 判断是否出现
            ele.click()
        else:
            self.error_log(browser)
        return ele
