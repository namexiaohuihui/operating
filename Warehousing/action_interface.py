# -*- coding: utf-8 -*-
"""
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
@author:    ln_company
@license:   (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@Software:  PyCharm
@file:      action_interface.py
@time:      2018/12/17 17:07
@desc:
"""

import os
from time import sleep

import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class ActionVisible(object):
    def __init__(self, browser):
        self.driver = browser

    def is_visible_driver(self, way, locator):
        """
        判断类型
        :param way:
        :return:
        """
        if 'css' == way or 'Css' == way:
            ele_by = (By.CSS_SELECTOR, locator)
            pass
        elif 'id' == way or 'Id' == way:
            ele_by = (By.ID, locator)
            pass
        elif 'xpath' == way or 'Xpath' == way:
            ele_by = (By.XPATH, locator)
            pass
        elif 'name' == way or 'Name' == way:
            ele_by = (By.NAME, locator)
            pass
        else:
            raise Exception("differentiate_element_text:你写的ele判断有误")
        return ele_by
        pass

    def differentiate_all_exist(self, ele_by, timeout=5):
        """
        一直等待某元素可见，默认超时5秒,返回全部找到的数据元素组
        :param ele_by:
        :param timeout:
        :return:
        """
        try:
            ele = ui.WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(ele_by))
            return ele
        except Exception as e:
            # self.error_log(driver, e)
            print("%s 元素找不到 is_visibles_css_selectop " % locator)
            return False

    def differentiate_single_exist(self, ele_by, timeout=5):
        """
        返回单个元素
        :param ele_by:
        :param timeout:
        :return:
        """
        try:
            ele = ui.WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(ele_by))
            return ele
        except TimeoutException:
            return False

    def differentiate_not_exist(self, ele_by, timeout=5):
        """
        判断元素是否消失
        element_to_be_clickable元素存在并且可用，以便确定元素是可点击的
        :param ele_by:
        :param timeout:
        :return:
        """
        try:
            ui.WebDriverWait(self.driver, timeout).until_not(EC.element_to_be_clickable(ele_by))
            return True
        except TimeoutException:
            return False

    def is_visible_single_driver(self, locator, way='css', timeout=5):
        """
        查找单个元素
        :param locator:
        :param way:
        :param timeout:
        :return:
        """
        ele_by = self.is_visible_driver(way, locator)
        return self.differentiate_single_exist(ele_by, timeout)

    def is_visible_all_driver(self, locator, way='css', timeout=5):
        """
        根据路径查找全部符合条件的元素
        :param locator:
        :param way:
        :param timeout:
        :return:
        """
        ele_by = self.is_visible_driver(way, locator)
        return self.differentiate_all_exist(ele_by, timeout)

    def is_visible_not_driver(self, locator, way='css', timeout=5):
        """
        判断某个元素是否消失
        :param locator:
        :param way:
        :param timeout:
        :return:
        """

        ele_by = self.is_visible_driver(way, locator)
        return self.differentiate_not_exist(ele_by, timeout)

    def is_visible_value_driver(self, locator, way='css', attr=None, timeout=5):
        """
        获取元素的text或者attribute
        :param locator: 元素路径
        :param way: 传入的locator为:(css,id,xpath,name)等
        :param attr:  为none时获取元素text,不为空时获取元素的attribute属性值
        :param timeout: 元素可见超时时间
        :return:
        """
        attribute = self.is_visible_single_driver(locator, way, timeout)
        if attr:
            attribute = attribute.get_attribute(attr)
        else:
            attribute = attribute.text
        return attribute

    def ac_move_to_element(self, locator):
        """
        该函数适用于：
        1.浏览器设置为手机模式
        2.对手机端进行操作
        鼠标移动到指定的元素上并进行点击
        :param locator:
        :return:
        """
        action_ele = self.is_visible_css_selectop(locator)
        ActionChains(self.driver).move_to_element(action_ele).perform()
        el.click()
        pass

    def scrollBar_mobile_browser(self, action_type):
        """
        将页面滚动条移动到顶部或者底部
        :param action_type:
        :return:
        """
        sleep(1)
        if 'top' == action_type:
            # 将滚动条移动到顶部的意思
            self.driver.execute_script("window.scrollTo(0,0)")
        elif 'buttom' == action_type:
            # 将滚动条移动到底部的意思
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def return_css_click(self, browser, prompt):
        """
        点击之后将element对象进行返回
        :param browser:
        :param prompt:
        :return:
        """
        ele_by = self.is_visible_driver(way, locator)
        ele = self.is_visible_css_selectop(browser, prompt)
        if ele:  # 判断是否出现
            ele_by.click()
        else:
            self.error_log(browser)
        return ele
