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
# 商品数量

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



    def qwetest_goods_participate_two(self,function=None):
        """输入数字,小于或者等于4"""
        # 获取函数名
        if function==None:
            function = sys._getframe().f_code.co_name
        # 提示框上输出的内容
        massegn = self.gp_non_existent

        parameter = "1234"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        self.gp_verification(list_parameter=list_parameter)

    def qwetest_goods_participate_three(self,function=None):
        """输入负数"""
        # 获取函数名
        if function==None:
            function = sys._getframe().f_code.co_name
        # 提示框上输出的内容
        massegn = self.gp_separate

        parameter = "-1"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        self.gp_verification(list_parameter=list_parameter)

    def qwetest_goods_participate_four(self,function=None):
        """输入多个商品，中间是中文形式下的逗号"""
        # 获取函数名
        if function==None:
            function = sys._getframe().f_code.co_name

        # 提示框上输出的内容
        massegn = self.gp_separate

        parameter = "---，****，////"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        self.gp_verification(list_parameter=list_parameter)

    def qwetest_goods_participate_five(self,function=None):
        """ 输入中文 """
        # 获取函数名
        if function==None:
            function = sys._getframe().f_code.co_name
        # 提示框上输出的内容
        massegn = self.gp_separate

        parameter = "你好吗?"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        self.gp_verification(list_parameter=list_parameter)

    def qwetest_goods_participate_six(self,function=None):
        """输入非统一商品"""
        # 获取函数名
        if function==None:
            function = sys._getframe().f_code.co_name
        # 提示框上输出的内容
        massegn = self.gp_proper

        parameter = "-----"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        self.gp_verification(list_parameter=list_parameter)

    def qwetest_goods_participate_seven(self,function=None):
        """输入长度=5的数字"""
        # 获取函数名
        if function==None:
            function = sys._getframe().f_code.co_name
        # 提示框上输出的内容
        massegn = self.gp_non_existent

        parameter = "98521"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        self.gp_verification(list_parameter=list_parameter)

    def qwetest_goods_participate_eight(self,function=None):
        """英文状态下的逗号连续输入"""
        # 获取函数名
        if function==None:
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

        # 提示框上输出的内容
        massegn = self.gp_incorrect

        """错误之后强制提交：方法一"""
        self.qwetest_goods_participate_one(function)

        self.setting_save_click(massegn=massegn)

        """错误之后强制提交：方法二"""
        self.qwetest_goods_participate_two(function)

        self.setting_save_click(massegn=massegn)

        """错误之后强制提交：方法三"""
        self.qwetest_goods_participate_three(function)

        self.setting_save_click(massegn=massegn)

        """错误之后强制提交：方法四"""
        self.qwetest_goods_participate_four(function)

        self.setting_save_click(massegn=massegn)

        """错误之后强制提交：方法五"""
        self.qwetest_goods_participate_five(function)

        self.setting_save_click(massegn=massegn)

        """错误之后强制提交：方法六"""
        self.qwetest_goods_participate_six(function)

        self.setting_save_click(massegn=massegn)

        """错误之后强制提交：方法七"""
        self.qwetest_goods_participate_seven(function)

        self.setting_save_click(massegn=massegn)

        """错误之后强制提交：方法八"""
        self.qwetest_goods_participate_eight(function)

        self.setting_save_click(massegn=massegn)


    def qwetest_goods_participate_ten(self):
        """输入正确的商品数量进行提交"""
        # 获取函数名
        function = sys._getframe().f_code.co_name
        # 提示框上输出的内容
        massegn = self.gp_non_existent

        parameter = "222"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        # 传入名字和需要输入的参数
        self.correct_function(list_parameter=list_parameter)

        # 提交参数之后，进行再次确认提示，并完成其后的全部工作
        self.integration_confirm_prompt()

    def qwetest_goods_participate_eleven(self):
        """输入正确的商品数量进行提交，并在二次确认中点击取消按钮"""
        # 获取函数名
        function = sys._getframe().f_code.co_name
        # 提示框上输出的内容
        massegn = self.gp_non_existent

        parameter = "222"

        # 严守格式：function = 函数名，massegn = 提示信息，parameter = 输入参数
        list_parameter = [function, massegn, parameter]

        # 传入名字和需要输入的参数
        self.correct_function(list_parameter=list_parameter)

        # 点击取消按钮
        self.arguments_confirm_prompt(prompt=self.btn_default)



if __name__ == '__main__':
    unittest.main
