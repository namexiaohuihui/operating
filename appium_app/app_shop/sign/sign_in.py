# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: sign_in.py
@time: 2017/7/17 13:45
"""
import os
from selenium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

desired_caps = {}
desired_caps['device'] = 'Android'
desired_caps['browserName'] = ''
desired_caps['version'] = '5.1.1'
desired_caps['app'] = PATH('C:\Users\Stephen\Desktop\Cweixin6510android1080.apk')
desired_caps['app-package'] = 'com.tencent.mm'
desired_caps['app-activity'] = '.ui.LauncherUI'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

el = driver.find_element_by_name("Add Contact")
el.click()

textfields = driver.find_elements_by_tag_name("textfield")
textfields[0].send_keys("My Name")
textfields[2].send_keys("someone@somewhere.com")

driver.find_element_by_name("Save").click()

driver.quit()