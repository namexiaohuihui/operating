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
@file:  enciconment.py
@time: 2019/1/27 16:51
@Software: PyCharm
@Site    : 
@desc:
"""

import os
import time
import os
import sys

from selenium import webdriver

# 获取项目路径下的目录
path_project = r"E:\operating"

os.chdir(path_project)

# 将项目路径保存
sys.path.append(path_project)

from BehaviorDriven.features.lib.register_page import RegisterPage

driver_path = 'E:\drivers\Drivers'


def before_all(context):
    context.browser = webdriver.Chrome(executable_path=os.path.join(driver_path, 'chromedriver239-68.exe'))
    context.browser.maximize_window()
    context.browser.implicitly_wait(5)

    context.register = RegisterPage(context)


def after_all(context):
    time.sleep(5)
    context.browser.close()
