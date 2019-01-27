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
@file:  base_page.py
@time: 2019/1/27 17:52
@Software: PyCharm
@Site    : 
@desc:
"""


class BasePage(object):
    def __init__(self, browser):
        self.browser = browser
        pass

    # 打开浏览器
    def get_register_url(self, url):
        self.browser.get(url)

    # 获取title
    def get_register_title(self):
        return self.browser.title

    # 定义元素
    def find_element_register(self, *loc):
        register = self.browser.find_element(*loc)
        return register
