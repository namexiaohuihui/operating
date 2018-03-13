# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: discountOperationSteps.py
@time: 2018/3/12 14:03

"""

import os
from utils.Logger import Log
from PageWeb.WebShop.judgmentVerification import JudgmentVerification
from PageWeb.WebShop.SystemSetup.ParameterSetting.discountParameterNames import DiscountParameterNames

"""
优惠用例所需要的执行的步骤全在这里
继承：
DiscountParameterNames :用例所涉及的参数名称以及提示
JudgmentVerification ： 数据验证以及工具的使用
"""


class DiscountOperationSteps(JudgmentVerification, DiscountParameterNames):

    def openingProgram(self,basename,exclefile):
        # 拿出文件名和工作薄
        exclename = exclefile[0]
        exclesheet = exclefile[1]

        # 定义日志
        self.log = Log(basename)

        # 读取文档信息
        self.overallExcelData = self._excel_Data(exclename,exclesheet)

        self.option_browser()  # 打开浏览器
        self.ps_user_login()  # 用户登录



