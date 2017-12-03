# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: selenium_visible.py
@time: 2017/11/8 15:09
"""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui

class element_visible(object):

    # 一直等待某元素可见，默认超时10秒
    def is_visible_xpath(self,driver,locator, timeout=10):
        try:
            ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    # 一直等待某个元素消失，默认超时10秒
    def is_not_visible_xpath(self,driver,locator, timeout=10):
        try:
            ui.WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    # 一直等待某元素可见，默认超时10秒
    def is_visible_css_selectop(self, driver, locator, timeout=3):
        try:
            ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            # print("需要等待的元素出现了 %s" % locator)
            return True
        except TimeoutException:
            print("需要等待的元素没有展现 %s" % locator)
            return False

        # 一直等待某个元素消失，默认超时10秒
    def is_not_visible_css_selectop(self, driver, locator, timeout=10):
        try:
            ui.WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except TimeoutException:
                return False

    # 一直等待某元素可见，默认超时10秒
    def is_visible_id(self, driver, locator, timeout=3):
        try:
            ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, locator)))
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


   # 一直等待某元素可见，默认超时10秒

    def is_visible_name(self, driver, locator, timeout=10):
        try:
            ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.NAME, locator)))
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

    def scrollBar_top(self,browser):
        import time
        time.sleep(1)
        # 将滚动条移动到顶部的意思
        browser.execute_script("window.scrollTo(0,0)")

    def scrollBar_buttom(self,browser):
        import time
        time.sleep(1)
        # 将滚动条移动到底部的意思
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
