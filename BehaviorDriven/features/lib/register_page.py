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
@file:  register_page.py
@time: 2019/1/27 17:51
@Software: PyCharm
@Site    : 
@desc:
"""
from selenium.webdriver.common.by import By

from BehaviorDriven.features.lib.pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, context):
        super(RegisterPage, self).__init__(context.browser)
        pass

    def send_register(self, register, register_connext):
        register = self.find_element_register(By.ID, register)
        register.send_keys(register_connext)
        pass
