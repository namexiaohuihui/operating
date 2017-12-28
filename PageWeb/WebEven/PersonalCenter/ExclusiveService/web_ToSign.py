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


class signtoyou(unittest.TestCase, exclusiveoperation):
    @classmethod
    def setUpClass(self):
        # 该类运行时优先调用的函数
        basename = os.path.splitext(os.path.basename(__file__))[0]
        self.log = Log(basename)
        self.log.info("The program begins to execute. Don't stop me when you start.")
        # self.setStart(self)

    @classmethod
    def tearDownClass(self):
        # 该类结束时最后调用的函数
        self.log.info("Make it complete and continue to press it next time...")

    def sign_one(self, function, account=None, password=None):
        self.setStart()
        if self.is_visible_css_selectop('.am-dialog-button') is not False:
            # 城市选择框.上线版本是不虚言进行选择的
            self.is_visible_css_selectop('.am-dialog-button')

        else:  # 即使发生错误也要继续执行
            self.Interface_sliding()

            if function == "homepage":
                self.click_homepage(account=account, password=password)

            elif function == "shoppingCart":
                self.click_shopping_cart(account=account, password=password)

            elif function == "details":
                self.click_details(account=account, password=password)

            else:
                self.log.info("The functions carried by the use case have not been found...")

    def click_homepage(self, account=None, password=None):  # 首页直接购买

        self.add_goods()  # 添加商品的操作

        self.is_visible_css_selectop(locator='.J_goBuy.m-cart-by')  # 点击去结算

        self.sign_switching_logon(account, password)

    def click_shopping_cart(self, account=None, password=None):  # 购物车里面购买

        self.add_goods()  # 添加商品的操作

        self.is_visible_css_selectop(locator='.m-cart-total')  # 进入购物车

        self.sleep_Rest()

        btn = self.is_visible_css_selectop('.J_btn.u-btn')  # 点击去买账

        if btn != False:
            self.sign_switching_logon(account, password)
        else:
            self.log.info("购物车页面出错")

    def click_details(self, account=None, password=None):

        self.is_visible_css_selectop('.shop-goods.shop-goods-cur>li:nth-child(1)')  # 点击去详情

        self.is_visible_css_selectop('.add-cart')  # 添加购物车

        self.sleep_Rest()

        self.is_visible_css_selectop('.buy-tiket-btn.cart')  # 添加购物车

        self.log.info("添加商品的提示： %s" % self.is_visible_css_selectop_text('.toast-cont'))  # 错误错误的原因

        self.sleep_Rest()

        self.is_visible_css_selectop('.buy.cur')  # 去结算

        self.sign_switching_logon(account, password)

    def test_ShoppingCart_login(self):
        """
        1.选择商品
        2.去结算
        :return:
        """
        excel = self.excel_Data()
        df = excel[0]
        row_col_data = excel[1]

        for number in range(len(row_col_data)):
            if number == 2:
                self.log.info("%s 开始执行" % df.iloc[number]["场景"])

                string = df.iloc[number]["输入"].split(',')
                account = string[0].split(':')[1]
                password = string[1].split(':')[1]
                self.sign_one(df.iloc[number]["函数"], account=account, password=password)

                from PageWeb.WebEven.PersonalCenter.ExclusiveService.TemporaryData import temporarystorage
                df.iloc[number]["场景"] = temporarystorage().get_remarks()

                self.log.info("%s 执行完毕" % df.iloc[number]["场景"])
            else:
                self.log.info("跳过")

        self.save_csv(df)  # 将数据进行保存


if __name__ == '__main__':
    unittest.main()
