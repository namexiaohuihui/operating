# -*- coding: utf-8 -*-
import os
from time import sleep

__author__ = 'Administrator'
"""
@file: web_goods_discount.py
@time: 2017/11/2 9:53
"""

import inspect
import unittest
import sys
from page_web.web_shop.target_parameter.parameter.discount.discount import discount_input


class goods_discount(discount_input, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.setUpStart(cls, basename =basename,ordinal=cls.goods_discount)

    @classmethod
    def tearDownClass(cls):
        print("%s   执行完毕" % cls.basename)
        cls.tearDownStop(cls)

    '''
    验证城市以及数量是否正确
    '''

    def qwetest_number(self):
        ele_div = self.browser.find_element_by_css_selector('.box-city')
        ele_a = ele_div.find_elements_by_tag_name('a')
        # 打印数量
        print(len(ele_a))

    '''
    验证商品打折数输入大于10的问题
    '''

    def qwetest_goods_discount_one(self):
        # 获取函数名
        function = inspect.stack()[0][3]
        print(function)

        # 输入错误出现的提示
        massegn = '请输入0.1~9.9之间的数'

        # 传入名字和需要输入的参数
        # 调用公告方法进行数据输入和判断
        self.verification(function, '111', massegn)

    '''
    验证商品打折数输入小于0的问题:即输入负数
    '''

    def qwetest_goods_discount_two(self):
        # 获取函数名
        function = sys._getframe().f_code.co_name
        print(function)

        # 传入名字和需要输入的参数
        # 调用公告方法进行数据输入和判断
        self.verification(function, '-1')

    '''
    验证商品打折数输入在符合范围内但小数点后有多位的情况
    '''

    def qwetest_goods_discount_three(self):
        # 获取函数名
        function = sys._getframe().f_code.co_name
        print(function)

        # 传入名字和需要输入的参数
        # 调用公告方法进行数据输入和判断
        self.verification(function, '2.333')

    '''
    验证商品打折数输入中文字符
    '''

    def qwetest_goods_discount_four(self):
        # 获取函数名
        function = sys._getframe().f_code.co_name
        print(function)

        # 传入名字和需要输入的参数
        # 调用公告方法进行数据输入和判断
        self.verification(function, '你好')

    # 输入符合条件的内容，并且成功提交
    def test_goods_discount_five(self):
        # 获取函数名
        function = sys._getframe().f_code.co_name
        print(function)

        # 传入名字和需要输入的参数
        # 调用公告方法进行数据输入和判断
        self.correct_function('2.7',function=function)

        # 二次确认的：同意按钮点击
        self.integration_confirm_prompt(function=function)

    # 输入符合条件的内容，在二次确认提交的时候取消。
    def test_goods_discount_six(self):
        # 获取函数名
        function = sys._getframe().f_code.co_name
        print(function)

        # 传入名字和需要输入的参数
        # 调用公告方法进行数据输入和判断
        self.correct_function('3.6',function=function)

        self.arguments_confirm_prompt(self.btn_default)


if __name__ == '__main__':
    unittest.main()
