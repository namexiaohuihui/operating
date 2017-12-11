# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: meibaombing.py
@time: 2017/12/11 17:34
https://testerhome.com/topics/646
http://blog.sina.com.cn/s/blog_68f262210102v4yy.html
"""
print("11")
import os
from selenium import webdriver


PATH = lambda  p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)
desired_caps = {}
desired_caps['device'] = 'Android'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
