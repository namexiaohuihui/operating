# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: web_SignToUse.py
@time: 2018/1/2 17:40
"""

import unittest
import inspect
import time
import os

from PageWeb.WebEven.ConversionStorage import conversionstorage
from PageWeb.WebEven import AccountPrivacy as ap
from practical.utils.logger import Log

"""
#--------------------读取excel表格数据部分-----------------------------------------
"""
print("Start getting use cases : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

basename = os.path.splitext(os.path.basename(__file__))[0]
log = Log(basename)
overall_ExcelData = ap._excel_Data(filename="auxiliaryFile")
# print(overall_ExcelData)

print("Use case acquisition completion : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

"""
#-----------------程序执行函数---------------------
#-----------------函数指定运行的头文件-------------
"""


def modifier_Interface_sliding(func):
    # Interface_sliding()

    def modifier(*s, **gs):
        from time import ctime
        print("[%s] %s() called" % (ctime(), func.__name__))
        return func(*s, **gs)

    return modifier


class singn_to_use(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # 该类运行时优先调用的函数
        log.info("The program begins to execute. Don't stop me when you start.")

    @classmethod
    def tearDownClass(self):
        # 该类结束时最后调用的函数
        log.info("Make it complete and continue to press it next time...")
        # self.driver.close()

    def test_ShoppingCart_login(self):
        """
        1.选择商品
        2.去结算
        :return:
        """
        for number in range(1):

            # 将线程中的内容进行读取
            ap.driver = ap._browser()
            STR_ILOC = overall_ExcelData.iloc[number]

            STR_INPUT = STR_ILOC["输入"]

            # -1表示在这个方法体里面没有找到相应的字符；也同时说明不需要输入内容
            if  not STR_INPUT and (STR_INPUT.find(",") and STR_INPUT.find(":")) != -1:

                string = STR_ILOC["输入"].split(',')  # 获取登录账号密码
                account = string[0].split(':')[1]
                password = string[1].split(':')[1]
                log.info( STR_ILOC["函数"] + "aaa")
                self.click_homepage(account=account, password=password)
                # self._verify_login(STR_ILOC["函数"], account=account, password=password)
            else:
                self._verifying_reading(STR_ILOC["函数"])

            STR_ILOC["备注"] = conversionstorage().get_remarks()  # 登录的提示内容保存

            ap.driver.close()

        overall_ExcelData.to_excel("nihao.xlsx", index=False, encoding="gbk")  # 将数据进行保存

    """
       #-----------------程序判断函数---------------------
   """

    def _verify_login(self, function, account=None, password=None):
        # self._visible_css_selectop(".am-dialog-button")

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


        else:
            log.info("The functions carried by the use case have not been found..." + function)

    def _verifying_reading(self, function):
        log.info("%s 开始执行" % function)
        # self._visible_css_selectop(".am-dialog-button")

        if function == "Protocol":  # 注册页面点击内容
            self.click_protocol()

        elif function == "Privacy":  # 注册页面点击内容
            self.click_privacy()

        elif function == "MessageTip":  # 注册页面点击内容
            self.click_message_tip()

        else:
            log.info("The functions carried by the use case have not been found..." + function)

    # @modifier_Interface_sliding
    def click_homepage(self, account=None, password=None):  # 首页直接购买

        ap.add_goods()  # 添加商品的操作

        ap._visible_css_selectop(locator='.J_goBuy.m-cart-by')  # 点击去结算

        ap.sign_switching_logon(account, password)

    def click_shopping_cart(self, account=None, password=None):  # 购物车里面购买

        ap.add_goods()  # 添加商品的操作

        ap._visible_css_selectop(locator='.m-cart-total')  # 进入购物车

        ap.sleep_Rest()

        btn = ap._visible_css_selectop('.J_btn.u-btn')  # 点击去结算

        if btn != False:
            ap.sign_switching_logon(account, password)
        else:
            log.info("购物车页面出错")

    def click_details(self, account=None, password=None):  # 详情添加商品登陆

        ap._visible_css_selectop('.shop-goods.shop-goods-cur>li:nth-child(1)')  # 点击去详情

        ap.details_add_goods(account, password)

    def click_home_water_ticket(self, account=None, password=None):  # 首页选择水票登录

        ap._visible_css_selectop(".shop-tiket-items.J_buyTiket>a:nth-of-type(1)")

        detailLst = ap._visible_css_selectop("#J_detailLst>p:last-child")

        if detailLst != False:
            ap.sign_switching_logon(account, password)
        else:
            log.info("水票弹窗错误")

    def click_details_water_ticket(self, account=None, password=None):  # 详情选择水票登录
        ap._visible_css_selectop('.shop-goods.shop-goods-cur>li:nth-child(1)')  # 点击去详情

        ap._visible_css_selectop(".shop-tiket-items.detail-add>a:last-child")  # 添加购物车
        tiketBtn = ap._visible_css_selectop(".buy-tiket-btn")  # 添加购物车之后进行

        if tiketBtn != False:
            ap.sign_switching_logon(account, password)
        else:
            log.info("商品详情水票弹窗错误")

    def click_details_introduce(self, account=None, password=None):  # 详情介绍登录
        ap._visible_css_selectop('.shop-goods.shop-goods-cur>li:nth-child(1)')  # 点击进详情页

        ap._visible_css_selectop('.goods-nav>a:nth-child(3)')  # 查看商品评价

        ap.details_add_goods(account, password)

    def click_details_evaluate(self, account=None, password=None):  # 详情评价登录
        ap._visible_css_selectop('.shop-goods.shop-goods-cur>li:nth-child(1)')  # 点击进详情页

        ap._visible_css_selectop('.goods-nav>a:last-child')  # 查看商品详情页

        ap.details_add_goods(account, password)

    def click_water_page(self, account=None, password=None):  # 水票页面登录
        ap._visible_css_selectop('.nav-watikis')  # 水票页面
        ap._visible_css_selectop(".am-dialog-button")
        ap.sleep_Rest()
        ap._visible_css_selectop('.shop-tiket-price>a:nth-child(2)')  # 购买
        ap._visible_css_selectop('.buy-tiket-btn')  # 弹窗
        ap.sign_switching_logon(account, password)

    def click_water_details(self, account=None, password=None):  # 水票详情页面登录
        ap._visible_css_selectop('.nav-watikis')  # 水票页面
        ap._visible_css_selectop(".am-dialog-button")
        ap.sleep_Rest()
        ap._visible_css_selectop(".tiket-buy-lst>li:nth-child(1)")
        ap._visible_css_selectop(".shop-tiket-items.detail-add>a:nth-of-type(1)")
        ap._visible_css_selectop('.buy-tiket-btn')  # 弹窗
        ap.sign_switching_logon(account, password)

    def click_water_user(self, account=None, password=None):  # 个人水票登录
        ap._visible_css_selectop('.nav-watikis')  # 水票页面
        ap._visible_css_selectop(".am-dialog-button")
        ap.sleep_Rest()
        ap._visible_css_selectop(".select-watikis>a:nth-child(2)")
        ap.sign_switching_logon(account, password)

    def click_deliver_water(self, account=None, password=None):  # 一键登录
        ap._visible_css_selectop('.nav-onekey')  # 一键送水
        ap._visible_css_selectop('.onekey-btn.dis')
        ap.sign_switching_logon(account, password)

    def click_order(self, account=None, password=None):  # 用户dingdan
        ap._visible_css_selectop(".nav-order")
        ap.sign_switching_logon(account, password)

    def click_user_sign_in(self, account=None, password=None):  # 用户sgin
        ap._visible_css_selectop(".nav-user")
        ap._visible_css_selectop(".user-head")
        ap.sign_user_login(account, password)

    def click_pending_payment(self, account=None, password=None):  # 待付款跳转
        ap._visible_css_selectop(".nav-user")
        ap._visible_css_selectop(".msg-nav>a:nth-child(1)")
        ap.sign_switching_logon(account, password)

    def click_pending_delivery(self, account=None, password=None):  # 待发货跳转
        ap._visible_css_selectop(".nav-user")
        ap._visible_css_selectop(".msg-nav>a:nth-child(2)")
        ap.sign_switching_logon(account, password)

    def click_distribution(self, account=None, password=None):  # 配送中跳转
        ap._visible_css_selectop(".nav-user")
        ap._visible_css_selectop(".msg-nav>a:nth-child(3)")
        ap.sign_switching_logon(account, password)

    def click_be_evaluated(self, account=None, password=None):  # 待评价跳转
        ap._visible_css_selectop(".nav-user")
        ap._visible_css_selectop(".msg-nav>a:nth-child(4)")
        ap.sign_switching_logon(account, password)

    def click_red_envelopes(self, account=None, password=None):  # 红包跳转
        ap._visible_css_selectop(".nav-user")
        ap._visible_css_selectop(".user-sidebar>li:nth-child(1)")
        ap.sign_switching_logon(account, password)

    def click_card_coupons(self, account=None, password=None):  # 卡券跳转
        ap._visible_css_selectop(".nav-user")
        ap._visible_css_selectop(".user-sidebar>li:nth-child(2)")
        ap.sign_switching_logon(account, password)

    def click_use_water_ticket(self, account=None, password=None):  # 水票跳转
        ap._visible_css_selectop(".nav-user")
        ap._visible_css_selectop(".user-sidebar>li:nth-child(3)")
        ap.sign_switching_logon(account, password)

    def click_address(self, account=None, password=None):  # 地址跳转
        ap._visible_css_selectop(".nav-user")
        ap._visible_css_selectop(".user-sidebar>li:nth-child(4)")
        ap.sign_switching_logon(account, password)

    def click_protocol(self):  # 注册页面点击内容
        ap._visible_css_selectop(".nav-user")
        ap._visible_css_selectop(".user-head")
        ap._visible_css_selectop('.login-type>a:nth-child(2)')  # 切换注册
        # ap._visible_css_selectop('#J_protocol')
        ap.driver.execute_script("document.getElementById('J_protocol').click();")
        overBox = ap.driver.find_element_by_css_selector(".over-box").text
        print(overBox)
        ap._visible_css_selectop('.close')

    def click_privacy(self):  # 注册页面点击内容
        ap._visible_css_selectop(".nav-user")
        ap._visible_css_selectop(".user-head")
        ap._visible_css_selectop('.login-type>a:nth-child(2)')  # 切换注册
        # ap._visible_css_selectop('#J_protocol')
        ap.driver.execute_script("document.getElementById('J_privacy').click();")
        overBox = ap.driver.find_element_by_css_selector(".over-box").text
        print(overBox)
        ap._visible_css_selectop('.close')

    def click_message_tip(self):  # 注册页面点击内容
        ap._visible_css_selectop(".nav-user")
        ap._visible_css_selectop(".user-head")
        ap._visible_css_selectop('.login-type>a:nth-child(2)')  # 切换注册
        message = ap.driver.find_element_by_css_selector(".message-tip").text
        # 储存登陆之后的提示
        conversionstorage().set_remarks(message)


if __name__ == '__main__':
    unittest.main()
