# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: web_SignToUse.py
@time: 2018/1/2 17:40
"""

import os
import unittest

from PageWeb.WebEven.Auxiliary.ExclusiveOperation import exclusiveoperation
from PageWeb.WebEven.ConversionStorage import conversionstorage
from practical.utils.logger import Log

"""
#--------------------读取excel表格数据部分-----------------------------------------
"""
def excel_Data(file_path=None):
    """
    从excel表格中获取数据并进行转换
    :param file_path:
    :return:
    """
    # 获取excel路径
    from practical.config import readModel
    if file_path == None: file_path = readModel.establish_con().get("excel", "auxiliaryFile")

    # 读取相应路径中的数据
    from practical.utils.OpenpyxlExcel import READEXCEL, PANDASDATA
    read = READEXCEL(file_path)

    # 获取case
    whole = read.position_sheet_row_value()
    # 获取内容
    row_col_data = whole[0]  #
    # 获取标题
    title_data = whole[1]

    # 数据转换
    pan = PANDASDATA(row_col_data)
    df = pan.definition_DataFrame(index="2017-12-24", periods=len(tuple(row_col_data)), columns=title_data)

    return df, row_col_data

"""
#-----------------程序执行函数---------------------
"""
def modifier_Interface_sliding(func):
    #Interface_sliding()

    def modifier(*s, **gs):
        from time import ctime
        print("[%s] %s() called" % (ctime(), func.__name__))
        return func(*s, **gs)

    return modifier

class singn_to_use(unittest.TestCase, exclusiveoperation):
    @classmethod
    def setUpClass(self):
        # 该类运行时优先调用的函数
        basename = os.path.splitext(os.path.basename(__file__))[0]
        self.log = Log(basename)
        self.log.info("The program begins to execute. Don't stop me when you start.")

    @classmethod
    def tearDownClass(self):
        # 该类结束时最后调用的函数
        self.log.info("Make it complete and continue to press it next time...")
        # self.driver.close()

    def test_ShoppingCart_login(self):
        """
        1.选择商品
        2.去结算
        :return:
        """
        excel = excel_Data()
        df = excel[0]
        row_col_data = excel[1]
        print(df)
        print(row_col_data)
        for number in range(1):
            # for number in range(23, 24):
            STR_INPUT = df.iloc[number]["输入"]
            if STR_INPUT.find(",") and STR_INPUT.find(":") != -1:
                string = df.iloc[number]["输入"].split(',')
                account = string[0].split(':')[1]
                password = string[1].split(':')[1]

                self.sign_one(df.iloc[number]["函数"], account=account, password=password)
            else:
                self.sign_one(df.iloc[number]["函数"])

            df.iloc[number]["备注"] = conversionstorage().get_remarks()

            self.driver.close()

        df.to_excel("nihao.xlsx", index=False, encoding="gbk")  # 将数据进行保存

    """
       #-----------------程序判断函数---------------------
   """

    def sign_one(self, function, account=None, password=None):
        self.log.info("%s 开始执行" % function)
        self.sign_browser()
        # self.is_visible_css_selectop(".am-dialog-button")

        if function == "homepage":  # 首页登录
            # self.Interface_sliding()
            self.click_homepage(account=account, password=password)

        elif function == "shoppingCart":  # 购物车登录
            self.Interface_sliding()
            self.click_shopping_cart(account=account, password=password)

        elif function == "detailsGoods":  # 详情登录
            self.Interface_sliding()
            self.click_details(account=account, password=password)

        elif function == "HomeWaterTicket":  # 首页水票登录
            self.Interface_sliding()
            self.click_home_water_ticket(account=account, password=password)

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

        elif function == "userSign":  # 用户sgin
            self.click_user_sign_in(account=account, password=password)

        elif function == "PendingPayment":  # 待付款跳转
            self.click_pending_payment(account=account, password=password)

        elif function == "PendingDelivery":  # 待发货跳转
            self.click_pending_delivery(account=account, password=password)

        elif function == "Distribution":  # 配送中跳转
            self.click_distribution(account=account, password=password)

        elif function == "BeEvaluated":  # 待评价跳转
            self.click_be_evaluated(account=account, password=password)

        elif function == "RedEnvelopes":  # 红包跳转
            self.click_red_envelopes(account=account, password=password)

        elif function == "CardCoupons":  # 卡券跳转
            self.click_card_coupons(account=account, password=password)

        elif function == "UseWaterTicket":  # 水票跳转
            self.click_use_water_ticket(account=account, password=password)

        elif function == "Address":  # 地址跳转
            self.click_address(account=account, password=password)

        elif function == "Protocol":  # 注册页面点击内容
            self.click_protocol()

        elif function == "Privacy":  # 注册页面点击内容
            self.click_privacy()

        elif function == "MessageTip":  # 注册页面点击内容
            self.click_message_tip()


        else:
            self.log.info("The functions carried by the use case have not been found..." + function)

    @modifier_Interface_sliding
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

    def click_details(self, account=None, password=None):  # 详情添加商品登陆

        self.is_visible_css_selectop('.shop-goods.shop-goods-cur>li:nth-child(1)')  # 点击去详情

        self.details_add_goods(account, password)

    def click_home_water_ticket(self, account=None, password=None):  # 首页选择水票登录

        self.is_visible_css_selectop(".shop-tiket-items.J_buyTiket>a:nth-of-type(1)")

        detailLst = self.is_visible_css_selectop("#J_detailLst>p:last-child")

        if detailLst != False:
            self.sign_switching_logon(account, password)
        else:
            self.log.info("水票弹窗错误")

    def click_details_water_ticket(self, account=None, password=None):  # 详情选择水票登录
        self.is_visible_css_selectop('.shop-goods.shop-goods-cur>li:nth-child(1)')  # 点击去详情

        self.is_visible_css_selectop(".shop-tiket-items.detail-add>a:last-child")  # 添加购物车
        tiketBtn = self.is_visible_css_selectop(".buy-tiket-btn")  # 添加购物车之后进行

        if tiketBtn != False:
            self.sign_switching_logon(account, password)
        else:
            self.log.info("商品详情水票弹窗错误")

    def click_details_introduce(self, account=None, password=None):  # 详情介绍登录
        self.is_visible_css_selectop('.shop-goods.shop-goods-cur>li:nth-child(1)')  # 点击进详情页

        self.is_visible_css_selectop('.goods-nav>a:nth-child(3)')  # 查看商品评价

        self.details_add_goods(account, password)

    def click_details_evaluate(self, account=None, password=None):  # 详情评价登录
        self.is_visible_css_selectop('.shop-goods.shop-goods-cur>li:nth-child(1)')  # 点击进详情页

        self.is_visible_css_selectop('.goods-nav>a:last-child')  # 查看商品详情页

        self.details_add_goods(account, password)

    def click_water_page(self, account=None, password=None):  # 水票页面登录
        self.is_visible_css_selectop('.nav-watikis')  # 水票页面
        self.is_visible_css_selectop(".am-dialog-button")
        self.sleep_Rest()
        self.is_visible_css_selectop('.shop-tiket-price>a:nth-child(2)')  # 购买
        self.is_visible_css_selectop('.buy-tiket-btn')  # 弹窗
        self.sign_switching_logon(account, password)

    def click_water_details(self, account=None, password=None):  # 水票详情页面登录
        self.is_visible_css_selectop('.nav-watikis')  # 水票页面
        self.is_visible_css_selectop(".am-dialog-button")
        self.sleep_Rest()
        self.is_visible_css_selectop(".tiket-buy-lst>li:nth-child(1)")
        self.is_visible_css_selectop(".shop-tiket-items.detail-add>a:nth-of-type(1)")
        self.is_visible_css_selectop('.buy-tiket-btn')  # 弹窗
        self.sign_switching_logon(account, password)

    def click_water_user(self, account=None, password=None):  # 个人水票登录
        self.is_visible_css_selectop('.nav-watikis')  # 水票页面
        self.is_visible_css_selectop(".am-dialog-button")
        self.sleep_Rest()
        self.is_visible_css_selectop(".select-watikis>a:nth-child(2)")
        self.sign_switching_logon(account, password)

    def click_deliver_water(self, account=None, password=None):  # 一键登录
        self.is_visible_css_selectop('.nav-onekey')  # 一键送水
        self.is_visible_css_selectop('.onekey-btn.dis')
        self.sign_switching_logon(account, password)

    def click_order(self, account=None, password=None):  # 用户dingdan
        self.is_visible_css_selectop(".nav-order")
        self.sign_switching_logon(account, password)

    def click_user_sign_in(self, account=None, password=None):  # 用户sgin
        self.is_visible_css_selectop(".nav-user")
        self.is_visible_css_selectop(".user-head")
        self.sign_user_login(account, password)

    def click_pending_payment(self, account=None, password=None):  # 待付款跳转
        self.is_visible_css_selectop(".nav-user")
        self.is_visible_css_selectop(".msg-nav>a:nth-child(1)")
        self.sign_switching_logon(account, password)

    def click_pending_delivery(self, account=None, password=None):  # 待发货跳转
        self.is_visible_css_selectop(".nav-user")
        self.is_visible_css_selectop(".msg-nav>a:nth-child(2)")
        self.sign_switching_logon(account, password)

    def click_distribution(self, account=None, password=None):  # 配送中跳转
        self.is_visible_css_selectop(".nav-user")
        self.is_visible_css_selectop(".msg-nav>a:nth-child(3)")
        self.sign_switching_logon(account, password)

    def click_be_evaluated(self, account=None, password=None):  # 待评价跳转
        self.is_visible_css_selectop(".nav-user")
        self.is_visible_css_selectop(".msg-nav>a:nth-child(4)")
        self.sign_switching_logon(account, password)

    def click_red_envelopes(self, account=None, password=None):  # 红包跳转
        self.is_visible_css_selectop(".nav-user")
        self.is_visible_css_selectop(".user-sidebar>li:nth-child(1)")
        self.sign_switching_logon(account, password)

    def click_card_coupons(self, account=None, password=None):  # 卡券跳转
        self.is_visible_css_selectop(".nav-user")
        self.is_visible_css_selectop(".user-sidebar>li:nth-child(2)")
        self.sign_switching_logon(account, password)

    def click_use_water_ticket(self, account=None, password=None):  # 水票跳转
        self.is_visible_css_selectop(".nav-user")
        self.is_visible_css_selectop(".user-sidebar>li:nth-child(3)")
        self.sign_switching_logon(account, password)

    def click_address(self, account=None, password=None):  # 地址跳转
        self.is_visible_css_selectop(".nav-user")
        self.is_visible_css_selectop(".user-sidebar>li:nth-child(4)")
        self.sign_switching_logon(account, password)

    def click_protocol(self):  # 注册页面点击内容
        self.is_visible_css_selectop(".nav-user")
        self.is_visible_css_selectop(".user-head")
        self.is_visible_css_selectop('.login-type>a:nth-child(2)')  # 切换注册
        # self.is_visible_css_selectop('#J_protocol')
        self.driver.execute_script("document.getElementById('J_protocol').click();")
        overBox = self.driver.find_element_by_css_selector(".over-box").text
        print(overBox)
        self.is_visible_css_selectop('.close')

    def click_privacy(self):  # 注册页面点击内容
        self.is_visible_css_selectop(".nav-user")
        self.is_visible_css_selectop(".user-head")
        self.is_visible_css_selectop('.login-type>a:nth-child(2)')  # 切换注册
        # self.is_visible_css_selectop('#J_protocol')
        self.driver.execute_script("document.getElementById('J_privacy').click();")
        overBox = self.driver.find_element_by_css_selector(".over-box").text
        print(overBox)
        self.is_visible_css_selectop('.close')

    def click_message_tip(self):  # 注册页面点击内容
        self.is_visible_css_selectop(".nav-user")
        self.is_visible_css_selectop(".user-head")
        self.is_visible_css_selectop('.login-type>a:nth-child(2)')  # 切换注册
        message = self.driver.find_element_by_css_selector(".message-tip").text
        # 储存登陆之后的提示
        conversionstorage().set_remarks(message)


if __name__ == '__main__':
    unittest.main()
