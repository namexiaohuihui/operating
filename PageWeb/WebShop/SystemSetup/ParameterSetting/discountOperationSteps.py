# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: discountOperationSteps.py
@time: 2018/3/12 14:03

"""


import os


"""
优惠用例所需要的执行的步骤全在这里
继承：
DiscountParameterNames :用例所涉及的参数名称以及提示
JudgmentVerification ： 数据验证以及工具的使用
"""
class DiscountOperationSteps():
    basename = os.path.splitext(os.path.basename(__file__))[0]



print(DiscountOperationSteps.basename)