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
    def is_visible(self,driver,locator, timeout=10):
        try:
            ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    # 一直等待某个元素消失，默认超时10秒
    def is_not_visible(self,driver,locator, timeout=10):
        try:
            ui.WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    # 一直等待某元素可见，默认超时10秒
    def is_visible(self, driver, locator, timeout=10):
        try:
            ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except TimeoutException:
            return False

        # 一直等待某个元素消失，默认超时10秒
    def is_not_visible(self, driver, locator, timeout=10):
        try:
            ui.WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except TimeoutException:
                return False

    # 一直等待某元素可见，默认超时10秒
    def is_visible(self, driver, locator, timeout=10):
        try:
            ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, locator)))
            return True
        except TimeoutException:
            return False

        # 一直等待某个元素消失，默认超时10秒
    def is_not_visible(self, driver, locator, timeout=10):
        try:
            ui.WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((By.ID, locator)))
            return True
        except TimeoutException:
                return False







# 一直等待某元素可见，默认超时10秒
def is_visible(driver,locator, timeout=10):
    try:
        ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False


# 一直等待某个元素消失，默认超时10秒
def is_not_visible(driver,locator, timeout=10):
    try:
        ui.WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False
