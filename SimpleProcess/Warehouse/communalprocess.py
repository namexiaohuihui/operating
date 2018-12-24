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
@file:  gongyong.py
@time: 2018/12/23 13:13
@Software: PyCharm
@Site    : 
@desc:
"""
from time import sleep
from tools.configs import readModel


class CommunalProcess(object):
    def __init__(self, open_browser):
        self.open_browser = open_browser

    def warehousing_login(self):
        """
        登录操作
        :param user_name:
        :param pass_ward:
        :return:
        """
        conf = readModel.establish_con(model="model")  # 获取账号密码
        account = conf.get("username", "atorage_account")
        password = conf.get("username", "atorage_password")
        # 账号
        self.open_browser.is_visible_inputs(locator='phone', way='id', parameter=account)
        # 密码
        self.open_browser.is_visible_inputs(locator='password', way='id', parameter=password)
        # 点击登录
        self.open_browser.is_visible_clicks(locator='loginBtn', way='id')
        del conf
        sleep(1)
        pass

    def access_muen_module(self, muen_int, module_int):
        # 进入菜单
        muen_int = '.nav.nav-list>li:nth-child(%s)' % muen_int
        self.open_browser.is_visible_clicks(locator=muen_int, way='css')

        # 进入模块
        module_int = 'li.hsub.open>ul>li:nth-child(%s)' % module_int
        self.open_browser.is_visible_clicks(locator=module_int, way='css')
