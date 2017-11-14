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

    def qwetest_goods_participate_one(self,function=None):
        """输入一串很长的数字，长度大于或者等于6"""

        # 获取函数名
        if function==None:
            function = sys._getframe().f_code.co_name

        # 提示框上输出的内容
        massegn = self.gp_separate

        parameter = "0.9"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        self.gp_verification(list_parameter=list_parameter)



    def qwetest_goods_participate_two(self):
        """输入数字,小于或者等于4"""
        # 获取函数名
        function = sys._getframe().f_code.co_name
        # 提示框上输出的内容
        massegn = self.gp_non_existent

        parameter = "1234"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        self.gp_verification(list_parameter=list_parameter)

    def qwetest_goods_participate_three(self):
        """输入负数"""
        # 获取函数名
        function = sys._getframe().f_code.co_name
        # 提示框上输出的内容
        massegn = self.gp_separate

        parameter = "-1"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        self.gp_verification(list_parameter=list_parameter)

    def qwetest_goods_participate_four(self):
        """输入多个商品，中间是中文形式下的逗号"""
        # 获取函数名
        function = sys._getframe().f_code.co_name

        # 提示框上输出的内容
        massegn = self.gp_separate

        parameter = "---，****，////"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        self.gp_verification(list_parameter=list_parameter)

    def qwetest_goods_participate_five(self):
        """ 输入中文 """
        # 获取函数名
        function = sys._getframe().f_code.co_name
        # 提示框上输出的内容
        massegn = self.gp_separate

        parameter = "你好吗?"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        self.gp_verification(list_parameter=list_parameter)

    def qwetest_goods_participate_six(self):
        """输入非统一商品"""
        # 获取函数名
        function = sys._getframe().f_code.co_name
        # 提示框上输出的内容
        massegn = self.gp_proper

        parameter = "-----?"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        self.gp_verification(list_parameter=list_parameter)

    def qwetest_goods_participate_seven(self):
        """输入长度=5的数字"""
        # 获取函数名
        function = sys._getframe().f_code.co_name
        # 提示框上输出的内容
        massegn = self.gp_non_existent

        parameter = "98521"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        self.gp_verification(list_parameter=list_parameter)

    def qwetest_goods_participate_eight(self):
        """英文状态下的逗号连续输入"""
        # 获取函数名
        function = sys._getframe().f_code.co_name
        # 提示框上输出的内容
        massegn = self.gp_non_existent

        parameter = "111,1111,2222"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        self.gp_verification(list_parameter=list_parameter)

    def test_goods_participate_nine(self):
        """焦点移出出现错误提示之后，点击提交按钮进行提交"""
        # 获取函数名
        function = sys._getframe().f_code.co_name
        self.qwetest_goods_participate_one(function)

        self.arguments_confirm_prompt(prompt=self.settingSave)
        print("tijiao an niu dianji ")

        visible = self.showSweetAlert_visible(process=self.visible_p)

        # 判断规划的提示跟实际的提示是否一致
        # massegn为规划的提示，visible为实际的提示
        # function 为调用这个不见函数的方法
        self.visible_massegn_assert(visible=visible)

        # 点击提示框中的确定按钮，表示已经查看
        self.arguments_confirm_prompt(prompt=self.confirm)


    def qwetest_goods_participate_ten(self):
        """输入正确的商品数量进行提交"""
        # 获取函数名
        function = sys._getframe().f_code.co_name
        # 提示框上输出的内容
        massegn = self.gp_non_existent

        parameter = "222"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        self.gp_verification(list_parameter=list_parameter)





if __name__ == '__main__':
    unittest.main
