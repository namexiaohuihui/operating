# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: selenium_visible.py
@time: 2017/11/8 15:09
"""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from time import sleep

import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
import inspect


class action_visible(object):

    """
    根据元素某个条件来显性等待元素，并判断该元素是否存在
    """
    # 一直等待某元素可见，默认超时10秒
    def is_visible_xpath(self,driver,locator, timeout=10):
        try:
            ele = ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return ele
        except TimeoutException:
            # print("The element does not appear：   %s" % locator)
            # function = inspect.stack()[0][3]  # 执行函数的函数名
            # error_log(function)
            return False

    # 一直等待某元素可见，默认超时10秒
    def is_visible_css_selectop(self, driver, locator, timeout=3):
        try:
            ele = ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return ele
        except TimeoutException:
            # import inspect
            # print("The element does not appear：   %s" % locator)
            # function = inspect.stack()[0][3]  # 执行函数的函数名
            # error_log(function)

            return False

    # 一直等待某元素可见，默认超时10秒
    def is_visible_id(self, driver, locator, timeout=3):
        try:
            ele = ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, locator)))
            return ele
        except TimeoutException:
            return False



   # 一直等待某元素可见，默认超时10秒

    def is_visible_name(self, driver, locator, timeout=10):
        try:
            ele = ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.NAME, locator)))
            return ele
        except TimeoutException:
            return False




    """
        根据元素某个条件来显性等待元素，并判断该元素是否消失
    """

    # 一直等待某个元素消失，默认超时10秒
    def is_not_visible_xpath(self,driver,locator, timeout=10):
        try:
            ui.WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

        # 一直等待某个元素消失，默认超时10秒
    def is_not_visible_css_selectop(self, driver, locator, timeout=10):
        try:
            # element_to_be_clickable元素存在并且可用，以便确定元素是可点击的

            ui.WebDriverWait(driver, timeout).until_not(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
            return True
        except TimeoutException:
            return False

    # 一直等待某个元素消失，默认超时10秒
    def is_not_visible_id(self, driver, locator, timeout=10):
        try:
            ui.WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((By.ID, locator)))
            return True
        except TimeoutException:
            return False

    def is_not_visible__name(self, driver, locator, timeout=10):
        # 一直等待某个元素消失，默认超时10秒
        try:
            ui.WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((By.NAME, locator)))
            return True
        except TimeoutException:
            return False

    """
    # ----------------------------- 获取text以及attribute的内容值--------------------
    """
    def _visible_selectop_attribute(self,driver , locator,attr = "value" , timeout=5):
        # 判断元素是否存在，如果存在就获取元素的value属性内容
        try:
            _ele = ui.WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            text = _ele.get_attribute(attr)  # 创建元素对象
            return text
        except TimeoutException:

            return False

    def _visible_selectop_text(self,driver,locator, timeout=5, poll_frequency=0.5):
        # 判断元素是否存在，如果存在就进行获取元素的text属性
        try:
            _ele = ui.WebDriverWait(driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))

            text = _ele.text
            return text

        except TimeoutException:

            return False








    def scrollBar_top(self,browser):
        sleep_Rest()
        # 将滚动条移动到顶部的意思
        browser.execute_script("window.scrollTo(0,0)")

    def scrollBar_buttom(self,browser):
        sleep_Rest()
        # 将滚动条移动到底部的意思
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def sleep_Rest(self,ti=1):  # 延迟
        sleep(ti)

    def error_log(function):
        # 执行文件的文件名
        basename = os.path.splitext(os.path.basename(__file__))[0]

        # 拼接名字
        name_tion = basename + "_" + function

        # 调用错误类
        dError.error_output(name_tion, driver)
