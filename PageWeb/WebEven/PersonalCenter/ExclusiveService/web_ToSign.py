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
from practical.utils.OpenpyxlExcel import READEXCEL,PANDASDATA


class signtoyou(unittest.TestCase, exclusiveoperation):
    @classmethod
    def setUpClass(self):
        # 该类运行时优先调用的函数
        basename = os.path.splitext(os.path.basename(__file__))[0]
        self.log = Log(basename)
        self.log.info("The program begins to execute. Don't stop me when you start.")
        #self.setStart(self)

    @classmethod
    def tearDownClass(self):
        # 该类结束时最后调用的函数
        self.log.info("Make it complete and continue to press it next time...")

    def sign_one(self,function,account=None,password=None):
        self.setStart()
        if self.is_visible_css_selectop('.am-dialog-button') is not False:
            # 城市选择框.上线版本是不虚言进行选择的
            tt = self.driver.find_element_by_css_selector('.am-dialog-button')
            self.touchActions_tap(tt)

        else:  # 即使发生错误也要继续执行
            self.Interface_sliding()

            size = self.driver.find_elements_by_css_selector(".J_add.shop-goods-add.icon-font.icon-plus-str")
            self.driver.execute_script("arguments[0].click();", size[0])  # 找到商品并进行点击
            self.sleep_Rest(2)
            if function == "homepage":
                self.homepage(account=account,password=password)
            elif function == "click_shopping_cart":
                self.click_shopping_cart(account=account,password=password)
            else:
                self.log.info("The functions carried by the use case have not been found...")

    def homepage(self,account=None,password=None):
        cart = self.is_visible_css_selectop(locator='.J_goBuy.m-cart-by')  # 点击去结算
        self.sign_switching_logon(account,password)

    def click_shopping_cart(self,account=None,password=None):
        cart = self.is_visible_css_selectop(locator='.m-cart-total')  # 进入购物车
        self.sleep_Rest(5)
        btn = self.is_visible_css_selectop('.J_btn.u-btn') #　点击去买账
        if btn != False:self.sign_switching_logon(account, password)
        else: self.log.info("购+物车页面出错")
    def test_ShoppingCart_login(self):
        """
        1.选择商品
        2.去结算
        :return:
        """
        self.read = READEXCEL(r'E:\drivers\CasePlan\CasrScene\BuyersWechat\买家微信信息管理场景.xlsx')

        whole = self.read.position_sheet_row_value() # 获取case
        row_col_data = whole[0] #
        title_data = whole[1]

        pan = PANDASDATA(row_col_data)
        df = pan.definition_DataFrame(index="2017-12-24",periods=len(tuple(row_col_data)),columns=title_data)
        for number in range(len(row_col_data)) :
            self.log.info("%s 开始执行" % df.iloc[number]["场景"])
            string = df.iloc[number]["输入"].split(',')
            account = string[0].split(':')[1]
            password = string[1].split(':')[1]
            self.sign_one(df.iloc[number]["函数"],account=account,password=password)
            from PageWeb.WebEven.PersonalCenter.ExclusiveService.TemporaryData import temporarystorage
            df.iloc[number]["场景"] = temporarystorage().get_remarks()
            self.log.info("%s 执行完毕" % df.iloc[number]["场景"])
        df.to_csv("wenhao.csv", index=False, encoding="gbk")

if __name__ == '__main__':
    unittest.main()
