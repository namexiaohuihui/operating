# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: web_invitation.py
@time: 2017/12/2 15:05
@项目名称:operating
"""
import os
import unittest

from PageWeb.web_shop.target_parameter.UnifiedVerification import unified_verification

"""
给予奖励设置:主要验证下面的问题:
1.小数
2.符合要求的数值
3.负数
4.特殊字符
5.中文
6.满足数值要求但符合要求
"""


class invitation_input(unittest.TestCase, unified_verification):
    @classmethod
    def setUpClass(cls):
        basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.setUpStart(cls, basename=basename)

    @classmethod
    def tearDownClass(cls):
        cls.tearDownStop(cls)

    def test_invitation_one(self, parameter=None):
        # 输入内容后点击提交，并且二次提醒的时候也提交
        if parameter is None:
            parameter = ["1", "2", "3", "4"]  # 需要输入的内容

        # 执行：输入、提交、验证的功能
        self.list_submission(parameter, self.saveTime, True)

    def test_invitation_two(self, parameter=None):
        # 　输入内容后点击提交，在二次提示的时候取消提交
        if parameter is None:
            parameter = ["1", "2", "3", "4"]  # 需要输入的内容
        # 执行：输入、取消提交
        self.dic_cancel(parameter)

    def test_invitation_there(self, parameter=None):
        # 输入不符合规矩的内容，点击提交出现提示信息
        if parameter is None:
            parameter = ["1", "2", "3", "4"]  # 需要输入的内容

        # 执行:输入/提交/验证
        self.dic_verification(parameter, massegn='请输入小时,仅支持输入正整数')

    def test_invitation_four(self, parameter=None):
        # 输入不符合规矩的内容，点击提交出现提示信息
        if parameter is None:
            parameter = ["1", "2", "3", "4"]  # 需要输入的内容

        # 执行:输入/提交/验证
        self.dic_verification(parameter, massegn='请输入天数,仅支持输入正整数')

    def test_invitation_five(self, parameter=None):
        # 输入不符合规矩的内容，点击提交出现提示信息
        if parameter is None:
            parameter = ["1", "2", "3", "4"]  # 需要输入的内容

        # 执行:输入/提交/验证
        self.dic_verification(parameter, massegn='请输入价格,仅支持输入正整数')

    def test_invitation_five(self, parameter=None):
        # 输入不符合规矩的内容，点击提交出现提示信息
        if parameter is None:
            parameter = ["1", "2", "3", "4"]  # 需要输入的内容

        # 执行:输入/提交/验证
        self.dic_verification(parameter, massegn='请输入收益价格,仅支持输入正整数')

if __name__ == '__main__':
    unittest.main()
