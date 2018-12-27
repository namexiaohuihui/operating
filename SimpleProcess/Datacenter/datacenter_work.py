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
@file:  datacenter_work.py
@time: 2018/12/26 22:39
@Software: PyCharm
@Site    : 
@desc:
"""
from time import sleep
from SimpleProcess.openbrowser import OpenBrowper
from tools.screeningdrop import ScreeningDrop
from tools.configs import readModel


class DatacenterWork(object):
    def __init__(self, muen_i, module_i):
        self.op_br = OpenBrowper()
        self.op_br.open_driver('datacenter_url')

        self.warehousing_login()
        self.access_muen_module(muen_i, module_i)
        pass

    def get_object_work(self):
        return self.op_br

    def close_quit_driver(self):
        self.op_br.driver.quit()

    def get_option_text(self, label_path):
        screen = ScreeningDrop(self.op_br.driver, label_path, attr='css')
        option_text = screen.getSelectedOptions()
        del screen
        return option_text
        pass

    def warehousing_login(self):
        """
        登录操作
        :param user_name:
        :param pass_ward:
        :return:
        """
        conf = readModel.establish_con(model="model")  # 获取账号密码
        account = conf.get("username", "datacenter_account")
        password = conf.get("username", "datacenter_password")
        # 账号
        self.op_br.is_visible_inputs(locator='username', way='id', parameter=account)
        # 密码
        self.op_br.is_visible_inputs(locator='password', way='id', parameter=password)
        # 点击登录
        self.op_br.is_visible_clicks(locator='loginBtn', way='id')

        del conf
        sleep(1)
        pass

    def access_muen_module(self, muen_int, module_i):
        # 进入菜单
        muen_int = '.nav.nav-list>li:nth-child(%s)' % muen_int
        self.op_br.is_visible_clicks(locator=muen_int, way='css')

        if type(module_i) is int:
            module_i = 'li.hsub.open>ul>li:nth-child(%s)' % module_i
            self.op_br.is_visible_clicks(locator=module_i, way='css')
        pass
