# -*- coding: utf-8 -*-

import os
from time import sleep
import inspect
import unittest
import sys
from page_web.web_shop.target_parameter.parameter.discount import discount_input

"""
@__author__ :70486 
@file: web_goods_participate.py
@time: 2017/11/8 21:59
@项目名称:operating
"""

class goods_participate(discount_input, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.setUpStart(cls, basename=basename, ordinal=cls.goods_id)

    @classmethod
    def tearDownClass(cls):
        cls.tearDownStop(cls)

    # 输入一串很长的数字，长度大于或者等于6
    def test_goods_participate_one(self):
        # 获取函数名
        function = sys._getframe().f_code.co_name

        # 提示框上输出的内容
        massegn = self.gp_separate

        parameter = "0.9"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        self.gp_verification(list_parameter=list_parameter)


    # 输入数字,小于或者等于4
    def qwetest_goods_participate_two(self):
        # 获取函数名
        function = sys._getframe().f_code.co_name
        print(function)

        parameter = "1234"
        # 运行的函数function，输入框需要输入的参数parameter
        self.gp_verification(function=function, parameter=parameter)

    # 输入负数
    def qwetest_goods_participate_three(self):
        # 获取函数名
        function = sys._getframe().f_code.co_name
        print(function)

        parameter = "-1"
        mess = self.gp_separate
        # 运行的函数function，输入框需要输入的参数parameter
        self.gp_verification(function=function, parameter=parameter)

        # 获取提示框的提示内容
        visible = self.showSweetAlert_visible(process=self.visible_p)

        # 将提示框里面内容的数字提取出来
        # totalCount = stringCutting.extract_number(visible=visible)

        # self.visible_massegn_assert(function=function, massegn=totalCount, visible=visible)

    # 输入多个商品，中间是中文形式下的逗号
    def qwetest_goods_participate_four(self):
        # 获取函数名
        function = sys._getframe().f_code.co_name
        print(function)

        parameter = "---，****，////"
        mess = self.gp_separate
        # 运行的函数function，输入框需要输入的参数parameter
        self.gp_verification(function=function, parameter=parameter)

    # 输入中文
    def qwetest_goods_participate_five(self):
        # 获取函数名
        function = sys._getframe().f_code.co_name
        print(function)

        parameter = "---，****，////"
        mess = self.gp_separate
        # 运行的函数function，输入框需要输入的参数parameter
        self.gp_verification(function=function, parameter=parameter)

     # 输入非统一商品
    def qwetest_goods_participate_six(self):
        # 获取函数名
        function = sys._getframe().f_code.co_name
        print(function)

        parameter = "---，****，////"
        mess = self.gp_proper
        # 运行的函数function，输入框需要输入的参数parameter
        self.gp_verification(function=function, parameter=parameter)

    # 输入长度=5的数字
    def qwetest_goods_participate_seven(self):
        # 获取函数名
        function = sys._getframe().f_code.co_name
        print(function)

        parameter = "---，****，////"
        mess = self.gp_non_existent
        # 运行的函数function，输入框需要输入的参数parameter
        self.gp_verification(function=function, parameter=parameter)

    # 英文状态下的逗号连续输入
    def qwetest_goods_participate_eight(self):
        # 获取函数名
        function = sys._getframe().f_code.co_name
        print(function)

        parameter = "---，****，////"
        mess = self.gp_separate
        # 运行的函数function，输入框需要输入的参数parameter
        self.gp_verification(function=function, parameter=parameter)

    # 未知情况出现:出现错误之后强制提交
    def qwetest_goods_participate_nine(self):
        # 获取函数名
        function = sys._getframe().f_code.co_name
        print(function)

        parameter = "---，****，////"
        mess = self.gp_incorrect
        # 运行的函数function，输入框需要输入的参数parameter
        # self.gp_verification(function=function, parameter=parameter)





if __name__ == '__main__':
    unittest.main
