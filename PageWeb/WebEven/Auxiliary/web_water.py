# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: web_water.py
@time: 2018/1/21 17:12
@Entry Name:operating
"""
import inspect
import os
import time
import unittest

from PageWeb.WebEven import AccountPrivacy as ap
from utils import Log
from PageWeb.WebEven.Auxiliary.namebean import letter_parameter_names
"""
#--------------------读取excel表格数据部分-----------------------------------------
"""
print("Start getting use cases : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

basename = os.path.splitext(os.path.basename(__file__))[0]
log = Log(basename)
overall_ExcelData = ap._excel_Data(filename="auxiliaryFile", SHEETNAME=4)
# print(overall_ExcelData)
lpn = letter_parameter_names()
print("Use case acquisition completion : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


class verify_water(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        ap.driver = ap._browser()  # 打开浏览器
        # 该类运行时优先调用的函数
        log.info("The program begins to execute. Don't stop me when you start.")

    @classmethod
    def tearDownClass(self):
        # 该类结束时最后调用的函数
        log.info("Make it complete and continue to press it next time...")
        # 关闭当前浏览器
        # ap.driver.close()
        # 退出当前driver并且关闭所有的相关窗口
        ap.driver.quit()

    def function_overall(self, function):
        self.overall = overall_ExcelData.loc[function]

        # 切割字符并获取第二份的内容，将数据里面的空格清空
        account = self.overall[lpn.even_account()]

        # 切割字符并获取第二份的内容，将数据里面的空格清空
        password = self.overall[lpn.even_password()]

        return account, password

    def test_water_page(self, account=None, password=None):  # 水票页面登录
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        funs = self.function_overall(function)

        ap._visible_css_selectop(lpn.water_watikis)  # 水票页面
        ap._visible_css_selectop(lpn.water_dialog) # 点击水票

        ap._visible_css_selectop(lpn.water_tiket_price)  # 购买

        ap._visible_css_selectop(lpn.water_sign_login)  # 弹窗
        ap.sign_switching_logon(funs[0], funs[1])

    def test_water_details(self, account=None, password=None):  # 水票详情页面登录
        # 实现进入修改手机页面之后返回
        function = inspect.stack()[0][3]  # 执行函数的函数名
        funs = self.function_overall(function)

        ap._visible_css_selectop(lpn.water_watikis)  # 水票页面
        ap._visible_css_selectop(lpn.water_dialog)  # 点击水票

        ap._visible_css_selectop(lpn.water_watikis_detail) #　水票详情页面
        ap._visible_css_selectop(lpn.water_add_detail) #点击购买

        ap._visible_css_selectop(lpn.water_sign_login)  # 弹窗
        ap.sign_switching_logon(funs[0], funs[1])

    def test_water_user(self, account=None, password=None):  # 个人水票登录
        function = inspect.stack()[0][3]  # 执行函数的函数名
        funs = self.function_overall(function)

        ap._visible_css_selectop(lpn.water_watikis)  # 水票页面
        ap._visible_css_selectop(lpn.water_dialog)  # 点击水票

        ap._visible_css_selectop(lpn.water_nth_detail) #个人水票

        ap._visible_css_selectop(lpn.water_sign_login)  # 弹窗
        ap.sign_switching_logon(funs[0], funs[1])