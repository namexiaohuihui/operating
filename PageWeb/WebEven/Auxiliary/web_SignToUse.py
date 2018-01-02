# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: web_SignToUse.py
@time: 2018/1/2 17:40
"""

import os
import unittest
from PageWeb.WebEven.Auxiliary.ExclusiveOperation import exclusiveoperation
from practical.utils.logger import Log
class singn_to_use(unittest.TestCase,exclusiveoperation):

    @classmethod
    def setUpClass(self):
        # 该类运行时优先调用的函数
        basename = os.path.splitext(os.path.basename(__file__))[0]
        self.log = Log(basename)
        self.log.info("The program begins to execute. Don't stop me when you start.")

        self.sign_browser(self)

    @classmethod
    def tearDownClass(self):
        # 该类结束时最后调用的函数
        self.log.info("Make it complete and continue to press it next time...")
        self.driver.close()


    def test_ShoppingCart_login(self):
        """
        1.选择商品
        2.去结算
        :return:
        """
        excel = self.excel_Data()
        df = excel[0]
        row_col_data = excel[1]

        for number in range(len(row_col_data) - 1, len(row_col_data)):
            string = df.iloc[number]["输入"].split(',')
            account = string[0].split(':')[1]
            password = string[1].split(':')[1]

            self.sign_one(df.iloc[number]["函数"], account=account, password=password)

            from PageWeb.WebEven.Auxiliary.TemporaryData import temporarystorage
            df.iloc[number]["场景"] = temporarystorage().get_remarks()

            # self.save_csv(df)  # 将数据进行保存

    def sign_one(self, function, account=None, password=None):
        self.log.info("%s 开始执行" % function)
        self.is_visible_css_selectop(".am-dialog-button")
        if function == "homepage":  # 首页登录
            self.Interface_sliding()
            self.click_homepage(account=account, password=password)

        elif function == "shoppingCart":  # 购物车登录
            self.Interface_sliding()
            self.click_shopping_cart(account=account, password=password)

        elif function == "detailsGoods":  # 详情登录
            self.Interface_sliding()
            self.click_details(account=account, password=password)

        elif function == "waterTicket":  # 首页水票登录
            self.Interface_sliding()
            self.click_water_ticket(account=account, password=password)

        elif function == "detailsWaterTicket":  # 详情水票登录
            self.Interface_sliding()
            self.click_details_water_ticket(account=account, password=password)

        elif function == "detailsIntroduce":  # 详情介绍登录
            self.Interface_sliding()
            self.click_details_introduce(account=account, password=password)

        elif function == "detailsEvaluate":  # 详情评价登录
            self.Interface_sliding()
            self.click_details_evaluate(account=account, password=password)

        elif function == "waterPage":  # 水票页面登录
            self.click_water_page(account=account, password=password)

        elif function == "waterDetails":  # 水票详情页面登录
            self.click_water_details(account=account, password=password)

        elif function == "waterUser":  # 个人水票登录
            self.click_water_user(account=account, password=password)

        elif function == "deliverWater":  # 一键登录
            self.click_deliver_water(account=account, password=password)

        elif function == "order":  # 用户dingdan
            self.click_order(account=account, password=password)

        elif function == "userSign":  # 用户dingdan
            self.click_user_sign_in(account=account, password=password)
        else:
            print("The functions carried by the use case have not been found...")

    def click_homepage(self, account=None, password=None):  # 首页直接购买

        self.add_goods()  # 添加商品的操作

        self.is_visible_css_selectop(locator='.J_goBuy.m-cart-by')  # 点击去结算

        self.sign_switching_logon(account, password)

    def click_shopping_cart(self, account=None, password=None):  # 购物车里面购买

        self.add_goods()  # 添加商品的操作

        self.is_visible_css_selectop(locator='.m-cart-total')  # 进入购物车

        self.sleep_Rest()

        btn = self.is_visible_css_selectop('.J_btn.u-btn')  # 点击去结算

        if btn != False:
            self.sign_switching_logon(account, password)
        else:
            self.log.info("购物车页面出错")

    def click_details(self, account=None, password=None):

        self.is_visible_css_selectop('.shop-goods.shop-goods-cur>li:nth-child(1)')  # 点击去详情

        self.details_add_goods(account, password)

    def click_water_ticket(self, account=None, password=None):

        self.is_visible_css_selectop(".shop-tiket-items.J_buyTiket>a:nth-of-type(1)")

        detailLst = self.is_visible_css_selectop("#J_detailLst>p:last-child")

        if detailLst != False:
            self.sign_switching_logon(account, password)
        else:
            self.log.info("水票弹窗错误")

    def click_details_water_ticket(self, account=None, password=None):
        self.is_visible_css_selectop('.shop-goods.shop-goods-cur>li:nth-child(1)')  # 点击去详情

        detail = self.is_visible_css_selectop(".shop-tiket-items.detail-add>a:last-child")

        if detail != False:
            self.sign_switching_logon(account, password)
        else:
            self.log.info("商品详情水票弹窗错误")

    def click_details_introduce(self, account=None, password=None):
        self.is_visible_css_selectop('.shop-goods.shop-goods-cur>li:nth-child(1)')  # 点击进详情页

        self.is_visible_css_selectop('.goods-nav>a:nth-child(3)')  # 查看商品评价

        self.details_add_goods(account, password)

    def click_details_evaluate(self, account=None, password=None):
        self.is_visible_css_selectop('.shop-goods.shop-goods-cur>li:nth-child(1)')  # 点击进详情页

        self.is_visible_css_selectop('.goods-nav>a:last-child')  # 查看商品详情页

        self.details_add_goods(account, password)

    def click_water_page(self, account=None, password=None):
        self.is_visible_css_selectop('.nav-watikis')  # 水票页面
        self.is_visible_css_selectop(".am-dialog-button")
        self.sleep_Rest()
        self.is_visible_css_selectop('.shop-tiket-price>a:nth-child(2)')  # 购买
        self.is_visible_css_selectop('.buy-tiket-btn')  # 弹窗
        self.sign_switching_logon(account, password)

    def click_water_details(self, account=None, password=None):
        self.is_visible_css_selectop('.nav-watikis')  # 水票页面
        self.is_visible_css_selectop(".am-dialog-button")
        self.sleep_Rest()
        self.is_visible_css_selectop(".tiket-buy-lst>li:nth-child(1)")
        self.is_visible_css_selectop(".shop-tiket-items.detail-add>a:nth-of-type(1)")
        self.is_visible_css_selectop('.buy-tiket-btn')  # 弹窗
        self.sign_switching_logon(account, password)

    def click_water_user(self, account=None, password=None):
        self.is_visible_css_selectop('.nav-watikis')  # 水票页面
        self.is_visible_css_selectop(".am-dialog-button")
        self.sleep_Rest()
        self.is_visible_css_selectop(".select-watikis>a:nth-child(2)")
        self.sign_switching_logon(account, password)

    def click_deliver_water(self, account=None, password=None):
        self.is_visible_css_selectop('.nav-onekey')  # 一键送水
        self.is_visible_css_selectop('.onekey-btn.dis')
        self.sign_switching_logon(account, password)

    def click_order(self, account=None, password=None):
        self.is_visible_css_selectop(".nav-order")
        self.sign_switching_logon(account, password)

    def click_user_sign_in(self, account=None, password=None):
        self.is_visible_css_selectop(".nav-user")
        import datetime
        self.is_visible_css_selectop(".user-head")
        self.sign_user_login(account, password)

if __name__ == '__main__':
    unittest.main()

