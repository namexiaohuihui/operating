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
@author:  ln_company
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file:  register_user.py
@time: 2019/1/27 17:01
@Software: PyCharm
@Site    : 
@desc:
"""
import os
import sys
from behave import *

# 获取项目路径下的目录
path_project = r"E:\operating"

os.chdir(path_project)

# 将项目路径保存
sys.path.append(path_project)

from BehaviorDriven.features.lib.register_page import RegisterPage

use_step_matcher('re')


@When('I open the register website "([^"]*)"')
def step_register(context, url):
    # context.register = RegisterPage(context)
    context.register.get_register_url(url)
    # context.browser.get(url)


@Then('I expect that the title is "([^"]*)"')
def step_register(context, title_name):
    # title = context.browser.title
    title = context.register.get_register_title()
    assert title_name in title


@When('I set with "([^"]*)" "([^"]*)"')
def step_register(context, user_obj, user_connet):
    context.register.send_register(user_obj, user_connet)
    pass


@When('I click with registerbutton')
def step_register(context):
    context.browser.find_element_by_id("mainRegA").click()
    pass


@Then('I expect that text "([^"]*)"')
def step_register(context, title_name):
    span_title = context.browser.find_element_by_css_selector("#m_mainAcode>span").text
    assert title_name in span_title
