# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: web_home.py
@time: 2018/1/21 16:43
@Entry Name:operating
https://foofish.net/python-decorator.html 装饰器的使用
"""
import unittest
import inspect
import time
import os

from PageWeb.WebEven.ConversionStorage import conversionstorage
from practical.utils import stringCutting  as sc
from PageWeb.WebEven import AccountPrivacy as ap
from practical.utils.logger import Log


"""
#--------------------读取excel表格数据部分-----------------------------------------
"""
print("Start getting use cases : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

basename = os.path.splitext(os.path.basename(__file__))[0]
log = Log(basename)
overall_ExcelData = ap._excel_Data(filename="auxiliaryFile",SHEETNAME=1)
# print(overall_ExcelData)

print("Use case acquisition completion : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

"""
#-----------------函数指定运行的头文件-------------
"""


def modifier_Interface_sliding(func): # 装饰器中调用浏览器和界面滚动
    # Interface_sliding()

    def modifier(*s, **gs):
        print("自动滚动的开始执行 %s() called" % (ctime(), func.__name__))
        # 将线程中的内容进行读取
        ap.driver = ap._browser()
        ap.Interface_sliding()
        return func(*s, **gs)

    return modifier

class verify_home(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # 该类运行时优先调用的函数
        log.info("The program begins to execute. Don't stop me when you start.")

    @classmethod
    def tearDownClass(self):
        # 该类结束时最后调用的函数
        log.info("Make it complete and continue to press it next time...")
        ap.driver.close()

    def function_overall(self, function):
        self.overall = overall_ExcelData.loc[function]

        # 获取登录账号密码
        string = sc.specified_cut(self.overall["输入"], ",")

        # 切割字符并获取第二份的内容，将数据里面的空格清空
        account = sc.specified_cut(string[0], ":")[1].strip()

        # 切割字符并获取第二份的内容，将数据里面的空格清空
        password = sc.specified_cut(string[1], ":")[1].strip()

        return account,password

    @modifier_Interface_sliding
    def test_homepage(self, account=None, password=None):  # 首页直接购买
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        funs = self.function_overall(function)

        ap.add_goods()  # 添加商品的操作

        ap._visible_css_selectop(locator='.J_goBuy.m-cart-by')  # 点击去结算

        ap.sign_switching_logon(funs[0], funs[1])

    @modifier_Interface_sliding
    def test_shopping_cart(self, account=None, password=None):  # 购物车里面购买
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        funs = self.function_overall(function)

        ap.add_goods()  # 添加商品的操作

        ap._visible_css_selectop(locator='.m-cart-total')  # 进入购物车

        ap.sleep_Rest()

        ap._visible_css_selectop('.J_btn.u-btn')  # 点击去结算

        ap.sign_switching_logon(funs[0], funs[1])

    @modifier_Interface_sliding
    def test_details_goods(self, account=None, password=None):  # 详情添加商品登陆
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        funs = self.function_overall(function)

        ap._visible_css_selectop('.shop-goods.shop-goods-cur li:nth-child(1)')  # 点击去详情

        ap.sign_switching_logon(funs[0], funs[1])

    @modifier_Interface_sliding
    def test_water_ticket(self, account=None, password=None):  # 首页选择水票登录
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        funs = self.function_overall(function)

        ap._visible_css_selectop(".shop-tiket-items.J_buyTiket a:nth-of-type(1)")

        ap._visible_css_selectop("#J_detailLst>p:last-child")

        ap.sign_switching_logon(funs[0], funs[1])

    @modifier_Interface_sliding
    def test_details_water(self, account=None, password=None):  # 详情选择水票登录
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        funs = self.function_overall(function)

        ap._visible_css_selectop('.shop-goods.shop-goods-cur>li:nth-child(1)')  # 点击去详情

        ap._visible_css_selectop(".shop-tiket-items.detail-add>a:last-child")  # 添加购物车
        ap._visible_css_selectop(".buy-tiket-btn")  # 添加购物车之后进行

        ap.sign_switching_logon(funs[0], funs[1])

    @modifier_Interface_sliding
    def test_details_introduce(self, account=None, password=None):  # 详情介绍登录
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        funs = self.function_overall(function)

        ap._visible_css_selectop('.shop-goods.shop-goods-cur>li:nth-child(1)')  # 点击进详情页

        ap._visible_css_selectop('.goods-nav>a:nth-child(3)')  # 查看商品评价

        ap.sign_switching_logon(funs[0], funs[1])

    @modifier_Interface_sliding
    def test_details_evaluate(self, account=None, password=None):  # 详情评价登录
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        funs = self.function_overall(function)

        ap._visible_css_selectop('.shop-goods.shop-goods-cur>li:nth-child(1)')  # 点击进详情页

        ap._visible_css_selectop('.goods-nav>a:last-child')  # 查看商品详情页

        ap.sign_switching_logon(funs[0], funs[1])

