# -*- coding: utf-8 -*-

import os
from time import sleep
import inspect
import unittest
import sys
from page_web.web_shop.target_parameter.parameter.discount import discount_input

"""
@__author__ :70486 
@file: web_watiki_discount.py
@time: 2017/11/15 22:42
@项目名称:operating
"""
# 捆绑的折扣

class watiki_discount(discount_input, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.setUpStart(cls, basename=basename, ordinal=cls.watiki_discount)

    @classmethod
    def tearDownClass(cls):
        cls.tearDownStop(cls)

    def test_goods_discount_one(self):
        """验证捆绑打折数输入大于10的问题"""
        # 获取函数名
        function = inspect.stack()[0][3]

        # 输入错误出现的提示
        massegn = self.gb_between

        parameter = "111"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        # 传入名字和需要输入的参数
        self.gd_verification(list_parameter=list_parameter)

    def test_goods_discount_two(self):
        """验证捆绑打折数输入小于0的问题:即输入负数"""
        # 获取函数名
        function = sys._getframe().f_code.co_name

        # 输入错误出现的提示
        massegn = self.gb_format

        parameter = "-1"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        # 传入名字和需要输入的参数
        self.gd_verification(list_parameter=list_parameter)

    def test_goods_discount_three(self):
        """验证捆绑打折数输入在符合范围内但小数点后有多位的情况"""
        # 获取函数名
        function = sys._getframe().f_code.co_name
        # 输入错误出现的提示
        massegn = self.gb_format

        parameter = "2.33333"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        # 传入名字和需要输入的参数
        self.gd_verification(list_parameter=list_parameter)

    def test_goods_discount_four(self):
        """验证捆绑打折数输入中文字符"""

        # 获取函数名
        function = sys._getframe().f_code.co_name
        # 输入错误出现的提示
        massegn = self.gb_format

        parameter = "你好"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        # 传入名字和需要输入的参数
        self.gd_verification(list_parameter=list_parameter)

    def test_goods_discount_five(self):
        """输入符合条件的内容，并且成功提交"""
        # 获取函数名
        function = sys._getframe().f_code.co_name

        # 提示框上输出的内容
        massegn = self.system_successful

        parameter = "0.2"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        # 传入名字和需要输入的参数
        self.correct_function(list_parameter=list_parameter)

        # 提交参数之后，进行再次确认提示，并完成其后的全部工作
        self.integration_confirm_prompt()

    def test_goods_discount_six(self):
        """输入符合条件的内容，在二次确认提交的时候取消"""
        # 获取函数名
        function = sys._getframe().f_code.co_name

        # 提示框上输出的内容
        massegn = self.system_successful

        parameter = "0.9"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        # 传入名字和需要输入的参数
        # 调用公告方法进行数据输入和判断
        self.correct_function(list_parameter=list_parameter)

        # 　－－－－－－－－－－－－－后续优化
        # 点击提交按钮
        self.arguments_confirm_prompt(prompt=self.settingSave)

        # 点击取消按钮
        self.arguments_confirm_prompt(prompt=self.btn_default)

if __name__ == '__main__':
    unittest.main()
