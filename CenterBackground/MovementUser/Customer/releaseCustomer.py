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
@file:      releaseCustomer.py
@time:      2018/9/10 17:03
@desc:
"""
from CenterBackground.MovementUser.releaseUser import ReleaseUser


class ReleaseCustomer(ReleaseUser):
    """
    重写点击注册按钮,原因为:
    按钮元素不一样,无法统一同一个名称。
    主要重写了click_release方法
    """

    def click_release(self):
        '''
        点击注册按钮
        :return:
        '''
        release = self.financial[self.bi.yaml_suregister()]
        self.vac.css_click(self.driver, release)
