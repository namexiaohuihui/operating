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
@author:    ln_company
@license:   (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@Software:  PyCharm
@file:      seller_pork.py
@time:      2018/12/24 17:24
@desc:
"""
from time import sleep
from SimpleProcess.openbrowser import OpenBrowper
from tools.screeningdrop import ScreeningDrop
from tools.configs import readModel


class SellerWork(object):
    def __init__(self, muen_i):
        self.op_br = OpenBrowper()
        self.op_br.open_driver('seller_url')

        self.warehousing_login()
        self.access_muen_module(muen_i)
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
        account = conf.get("username", "seller_account")
        password = conf.get("username", "seller_password")
        # 账号
        self.op_br.is_visible_inputs(locator='phone', way='id', parameter=account)
        # 密码
        self.op_br.is_visible_inputs(locator='password', way='id', parameter=password)
        # 点击登录
        self.op_br.is_visible_clicks(locator='loginBtn', way='id')

        del conf
        sleep(1)
        pass

    def access_muen_module(self, muen_int):
        # 进入菜单
        muen_int = '.nav.nav-list>li:nth-child(%s)' % muen_int
        self.op_br.is_visible_clicks(locator=muen_int, way='css')
        pass

    def seller_info_number(self):
        # 读取info的数据并把int数据切割
        info_text = self.op_br.is_visible_singles("div.dataTables_info", 'css')

        if info_text:
            info_text = str.split(info_text.text, '，')[-1]
            searchObj = re.search("\d+", info_text)
            info_text = int(searchObj.group() if searchObj else searchObj)
            if (info_text % 6) > 0:
                number = 1
            else:
                number = 0
            info_text = int((info_text / 6)) + number
        return info_text