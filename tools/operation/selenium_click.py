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
        # 判断是否出现
        if ele is not False:
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
        """
        通过id进行js点击
        :param browser:
        :param prompt:
        :return:
        """
        try:
            browser.execute_script("document.getElementById(\'" + prompt + "\').click();")
        except Exception as a:
            function = inspect.stack()[0][3]  # 执行函数的函数名
            print("该函数(%s,%s,%s)出现了(%s)错误" % (self.basename, function, prompt, a))

    def css_confirm_prompt(self, browser, prompt):
        """
        输入元素路径通过js进行点击
        :param browser:
        :param prompt:
        :return:
        """
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
        screen = self.get_size(driver)

        x1 = screen[0] * 0.5
        y1 = screen[1] * 0.75

        TouchActions(driver).scroll(x1, y1).perform()

    def touchActions_tap(self, driver, element):
        # 点击元素
        TouchActions(driver).tap(element).perform()
        self.sleep_Rest()

    def differentiate_ele_click(self, browser, case_info, ordinal):
        info_bool = False
        if case_info['ele'] == 'id':
            self.id_click(browser, ordinal)
            info_bool = True
            pass
        elif case_info['ele'] == 'css':

            self.css_click(browser, ordinal)
            info_bool = True
            pass
        else:
            print("differentiate_ele_click在css中没有css找到way")
            pass
        return info_bool

    def differentiate_js_click(self, browser, case_info, ordinal):
        info_bool = False
        if case_info['ele'] == 'id':
            self.id_confirm_prompt(browser, ordinal)
            info_bool = True
            pass
        elif case_info['ele'] == 'css':
            self.css_confirm_prompt(browser, ordinal)
            info_bool = True
            pass
        else:
            print("differentiate_js_click在js中没有找到way")
            pass
        return info_bool

    def ele_click_and_mode(self, browser, case_info, ordinal):
        """
        判断相应的元素类型来执行动作
        :param browser: 浏览器对象
        :param case_info: 需要判断的数据
        :param ordinal: 元素路径
        :param parameter: 输入的内容
        :return:
        """
        case_info = case_info
        info_bool = False  # 检验程序是否需要执行下去

        if case_info['way'] == 'js':
            info_bool = self.differentiate_js_click(browser, case_info, ordinal)

        elif case_info['way'] == 'css':
            info_bool = self.differentiate_ele_click(browser, case_info, ordinal)

        else:
            print("ele_input_and_mode在way中没有数据信息")
            pass

        # 删除这个参数
        del case_info
        return info_bool

    def return_css_click(self, browser, prompt):
        """
        点击之后将element对象进行返回
        :param browser:
        :param prompt:
        :return:
        """
        ele = self.is_visible_css_selectop(browser, prompt)
        if ele is not False:  # 判断是否出现
            ele.click()
        else:
            self.error_log(browser)
        return ele
