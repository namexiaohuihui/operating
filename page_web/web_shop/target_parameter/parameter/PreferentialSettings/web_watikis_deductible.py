# -*- coding: utf-8 -*-

import os
from time import sleep
import inspect
import unittest
import sys
from page_web.web_shop.target_parameter.parameter.SingleVerification import discount_input


"""
@__author__ :70486 
@file: web_watikis_deductible.py
@time: 2017/11/15 22:45
@项目名称:operating
"""

"""
捆绑的折扣的数量:主要验证下面的问题:
1.小数
2.符合要求的数值
3.负数
4.特殊字符
5.中文
6.满足数值要求但符合要求
"""
class watikis_deductible(discount_input, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.setUpStart(cls, basename=basename, ordinal=cls.watikis_max)

    @classmethod
    def tearDownClass(cls):
        cls.ResultFeedback(cls)

    def test_goods_discount_one(self):
        """输入超于最大值的内容"""

        # 获取函数名
        function = inspect.stack()[0][3]

        # 输入错误出现的提示
        massegn = "chaoguozuidazhile"

        # 输入的内容
        parameter = "111"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        # 传入名字和需要输入的参数
        self.PreferentialVerification(list_parameter=list_parameter)

    def test_goods_discount_two(self):
        """输入小于最小值的内容"""
        # 获取函数名
        function = sys._getframe().f_code.co_name

        # 输入错误出现的提示
        massegn = self.gb_format

        parameter = "-1"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        # 传入名字和需要输入的参数
        self.PreferentialVerification(list_parameter=list_parameter)


    def test_goods_discount_three(self):
        """输入小数"""
        # 获取函数名
        function = sys._getframe().f_code.co_name
        # 输入错误出现的提示
        massegn = self.gb_format

        parameter = "2.33333"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        # 传入名字和需要输入的参数
        self.PreferentialVerification(list_parameter=list_parameter)


    def test_goods_discount_four(self):
        """输入中文及其他特殊符号"""

        # 获取函数名
        function = sys._getframe().f_code.co_name
        # 输入错误出现的提示
        massegn = self.gb_format

        parameter = "你好"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        # 传入名字和需要输入的参数
        self.PreferentialVerification(list_parameter=list_parameter)

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
        self.integration_confirm_prompt(Situation=True)

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
        self.integration_confirm_prompt()


if __name__ == '__main__':
    unittest.main()
