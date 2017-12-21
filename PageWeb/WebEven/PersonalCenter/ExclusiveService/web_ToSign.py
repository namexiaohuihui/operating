# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: web_ToSign.py
@time: 2017/12/20 23:07
@项目名称:operating
"""
import os
import unittest

from PageWeb.WebEven.PersonalCenter.ExclusiveService.ExclusiveOperation import exclusiveoperation
from practical.utils.logger import Log


class signtoyou(unittest.TestCase,exclusiveoperation):
    @classmethod
    def setUpClass(cls):
        # 该类运行时优先调用的函数
        basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.log = Log(basename)
        cls.log.info("The program begins to execute. Don't stop me when you start.")
        cls.setStart(cls)

    @classmethod
    def tearDownClass(cls):
        # 该类结束时最后调用的函数
        cls.log.info("Make it complete and continue to press it next time...")

    def sign_one(self):

        if self.is_visible_css_selectop('.am-dialog-button') is not False:
            # 城市选择框.上线版本是不虚言进行选择的
            tt = self.driver.find_element_by_css_selector('.am-dialog-button')
            self.touchActions_tap(tt)

        else:# 即使发生错误也要继续执行
            self.Interface_sliding()

            size = self.driver.find_elements_by_css_selector(".J_add.shop-goods-add.icon-font.icon-plus-str")
            self.driver.execute_script("arguments[0].click();", size[0]) #　找到商品并进行点击
            self.sleep_Rest(2)
            cart = self.is_visible_css_selectop(locator ='.J_goBuy.m-cart-by') # 去结算按钮转变为可点击时
            self.touchActions_tap(cart) # 找到商品并进行点击

            # 登陆
            btn = self.is_visible_css_selectop('.btn>a:nth-child(1)')
            self.touchActions_tap(btn)

            login = self.is_visible_css_selectop('.login-type>a:nth-child(1)') # 切换登陆方式
            self.touchActions_tap(login)

            self.driver.execute_script("document.getElementById('J_tel').value="+'123'+";")
            self.driver.execute_script("document.getElementById('J_pwd').value="+'123'+";")

            morange = self.driver.find_element_by_css_selector(".u-btn.u-btn-morange")#输入内容
            self.driver.execute_script("arguments[0].click();", morange)
            self.log.info(self.is_visible_css_selectop('.toast-cont').text)# 错误错误的原因




    def test_ShoppingCart_login(self):
        """
        1.选择商品
        2.去结算
        :return:
        """
        self.log.info("kaishidnegl")
        self.sign_one()
        self.log.info("执行wnag")

if __name__ == '__main__':
    unittest.main()