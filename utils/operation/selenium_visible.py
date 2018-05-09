# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: selenium_visible.py
@time: 2017/11/8 15:09
"""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from time import sleep
import os

import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from tools import DefinitionErrors as dError


class action_visible(object):
    # ------------------------------等待某个元素可见，默认超时10秒-------------------
    def is_visible_xpath(self, driver, locator, timeout=10):
        # 一直等待某元素可见，默认超时10秒
        try:
            ele = ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return ele
        except TimeoutException:
            # print("The element does not appear：   %s" % locator)
            # function = inspect.stack()[0][3]  # 执行函数的函数名
            # error_log(function)
            return False

    def is_visible_css_selectop(self, driver, locator, timeout=3):
        # 一直等待某元素可见，默认超时10秒
        try:
            ele = ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return ele
        except TimeoutException:
            return False

    def is_visible_id(self, driver, locator, timeout=3):
        # 一直等待某元素可见，默认超时10秒
        try:
            ele = ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, locator)))
            return ele
        except TimeoutException:
            return False

    def is_visible_name(self, driver, locator, timeout=10):
        # 一直等待某元素可见，默认超时10秒
        try:
            ele = ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.NAME, locator)))
            return ele
        except TimeoutException:
            return False

    # ------------------------------等待某个元素不可见，默认超时10秒-------------------
    def is_not_visible_xpath(self, driver, locator, timeout=10):
        # 一直等待某个元素消失，默认超时10秒
        try:
            ui.WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    def is_not_visible_css_selectop(self, driver, locator, timeout=10):
        # 一直等待某个元素消失，默认超时10秒
        try:
            # element_to_be_clickable元素存在并且可用，以便确定元素是可点击的

            ui.WebDriverWait(driver, timeout).until_not(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
            return True
        except TimeoutException:
            return False

    def is_not_visible_id(self, driver, locator, timeout=10):
        # 一直等待某个元素消失，默认超时10秒
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

    # ----------------------------- 获取text以及attribute的内容值--------------------
    def _visible_selectop_attribute(self, driver, locator, attr="value", timeout=5):
        """
        判断元素是否存在，如果存在就获取元素的value属性内容
        :param driver: 浏览器对象
        :param locator: 元素定位方式
        :param attr: 元素属性，默认为value
        :param timeout: 默认超时时间为5
        :return:  一直想不通的是获取disabled属性时为什么返回的是一个布尔值
        """
        try:
            _ele = ui.WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            attribute = _ele.get_attribute(attr)  # 创建元素对象
            return attribute
        except TimeoutException:
            return False

    def _visible_selectop_id(self, driver, locator, attr="value", timeout=5):
        """
        判断元素是否存在，如果存在就获取元素的value属性内容
        :param driver: 浏览器对象
        :param locator: 元素定位方式
        :param attr: 元素属性，默认为value
        :param timeout: 默认超时时间为5
        :return:  一直想不通的是获取disabled属性时为什么返回的是一个布尔值
        """
        try:
            _ele = ui.WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.ID, locator)))
            attribute = _ele.get_attribute(attr)  # 创建元素对象
            return attribute
        except TimeoutException:
            return False

    def _visible_selectop_text(self, driver, locator, timeout=5, poll_frequency=0.5):
        # 判断元素是否存在，如果存在就进行获取元素的text属性
        try:
            _ele = ui.WebDriverWait(driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            text = _ele.text
            return text
        except TimeoutException:
            return False

    # --------------------------其他一些等待条件的使用-----------------
    def _visible_text_css(self, driver, locator, text, timeout=5):
        """
        定位的元素是否带有相应的文本信息
        可用于判断一个元素的文字是否符合
        :param driver:
        :param locator:  一组（by，locator），这里只需要输入css_selector的元素定位参数
        :param text: 需要被检验的文本内容
        :param timeout: 一组webelement
        :return:
        """
        _ele = ui.WebDriverWait(driver, timeout).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, locator), text))
        return _ele

    def _visible_contains_title(self, driver, text, timeout=5):
        """
        等待网页标题包含指定的大小写敏感字符串
        可用于判断网页是否打开，并打开之后的网页跟要求的是否一致
        :param driver:
        :param text: 被校验的包含在标题中的字符串
        :param timeout:
        :return: 成功返回True，失败返回False
        """
        _ele = ui.WebDriverWait(driver, timeout).until(
            EC.title_contains(text))
        return _ele

    def _visible_is_title(self, driver, text, timeout=5):
        """
        等待网页标题包含指定的大小写敏感字符串
        可用于判断网页是否打开，并打开之后的网页跟要求的是否一致
        :param driver:
        :param text:网页的标题
        :param timeout:
        :return: 成功返回True，失败返回False
        """
        _ele = ui.WebDriverWait(driver, timeout).until(
            EC.title_is(text))
        return _ele

    def _visible_of_wide_high(self, driver, locator, timeout=5):
        """
        元素是否可见，并且宽和高都大于0
        可用于判断一个一出现的元素大小是否符合要求
        :param driver:
        :param locator:
        :param timeout:
        :return: 返回一个WebElement
        """
        _ele = ui.WebDriverWait(driver, timeout).until(
            EC.visibility_of((By.CSS_SELECTOR, locator)))
        return _ele

    # -----------------------------------滚动条的移动------------------------
    def scrollBar_top(self, browser):
        sleep_Rest()
        # 将滚动条移动到顶部的意思
        browser.execute_script("window.scrollTo(0,0)")

    def scrollBar_buttom(self, browser):
        sleep_Rest()
        # 将滚动条移动到底部的意思
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # -------------------------延时以及错误的定义---------------------------
    def sleep_Rest(self, ti=1):  # 延迟
        sleep(ti)

    def error_log(self, driver):
        # 执行文件的文件名
        basename = os.path.splitext(os.path.basename(__file__))[0]

        # 调用错误类
        dError.error_output(basename, driver)
