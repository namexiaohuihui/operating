# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: web_goods_discount.py
@time: 2017/11/2 9:53
"""

import re
import os
import inspect
import unittest
from CenterBackground.SystemSetup.ParameterSetting.discountOperationSteps import DiscountOperationSteps

"""
import的解释:
re:正则
time：时间
inspect :　获取函数名
unittest：用例框架
Log：log日志
DiscountOperationSteps ： 用例操作类

折扣页面:主要验证下面的问题:
1.小数
2.符合要求的数值
3.负数
4.特殊字符
5.中文
6.满足数值要求但符合要求

下文重复出现的内容注释：
1.@unittest.skip(r"跳过:XXXX") ：告诉unittest框架我要跳过这个用例，并打印出信息（跳过:XXXX）
"""
# 获取文件名
# basename = os.path.splitext(os.path.basename(__file__))[0]
# 定义类参数
# jv = JudgmentVerification()
# log = Log(basename)
# lpn = DiscountParameterNames()
# 读取数据内容
# overall_ExcelData = jv._excel_Data(filename="discount", SHEETNAME=1)
# 定义需要读取的文件名以及工作薄

disSte = DiscountOperationSteps()
class TestVerifyDiscount(unittest.TestCase):

    """
     优惠  继承函数
    """

    @classmethod
    def setUpClass(cls):
        # 该类运行时优先调用的函数
        # log.info("The program begins to execute. Don't stop me when you start.")
        basename = os.path.splitext(os.path.basename(__file__))[0]
        EXCLE_FILE = disSte.getDiscountExcle()
        disSte.openingProgram(basename, EXCLE_FILE)
        # 进入路径
        disSte._rou_fun()

    @classmethod
    def tearDownClass(cls):
        try:
            # 该类结束时最后调用的函数
            # log.info("Make it complete and continue to press it next time...")
            disSte.driver.quit()
            # overall_ExcelData.to_excel(basename + ".xlsx", index=False, encoding="gbk")
            pass
        except UnicodeDecodeError:
            disSte.log.info("又出现UTF-8的错误........")

    # ---------------用例部分-----------------

    # @unittest.skip(r"跳过:test_city_number")
    def test_city_number(self):
        """获取城市数量以及名字(编码)是否正确"""
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])
        # 获取城市信息
        tags = disSte.obtain_city_name()
        list_name = [] # 储存城市名
        list_attr = [] # 储存城市编码
        for tag in tags:
            list_name.append(tag.text) # 添加城市名
            # 正则切割数据，提取编码
            attr = tag.get_attribute('href')
            regular = re.search(r'[1-9]\d{5}(?!\d)', attr)
            # 添加编码
            list_attr.append(int(regular.group()))
        # 将页面上获取到的数据进行比较
        disSte._verify_content_mysql(list_name, list_attr)

    # @unittest.skip(r"跳过:test_all_cancel")
    def test_all_cancel(self):
        """不设置优惠直接提交"""
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 执行输入指令
        disSte.confirmationSubmission()

        # 执行弹窗的点击动作
        disSte.promptVerification()

        # 执行数据比较的任务，不做此类操作
        # disSte._verify_content_data()

    # @unittest.skip(r"跳过:test_all_choice")
    def test_all_choice(self):
        """设置优惠直接提交"""
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 执行输入指令
        disSte.confirmationSubmission()

        # 执行弹窗的点击动作
        disSte.promptVerification()

        # 执行数据比较的任务
        disSte._verify_content_data()

    # @unittest.skip(r"跳过:test_water_NotInput")
    def test_water_NotInput(self):
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 执行输入指令
        disSte.confirmationSubmission()

        # 执行弹窗的点击动作，
        disSte.promptErrorInformation()

    # @unittest.skip(r"跳过:test_water_choice")
    def test_water_choice(self):
        """设置水优惠信息"""
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 执行输入指令
        disSte.confirmationSubmission()

        # 执行弹窗的点击动作
        disSte.promptVerification()

        # 执行数据比较的任务
        disSte._verify_content_data()

    # @unittest.skip(r"跳过:test_water_discount")
    def test_water_discount(self):
        """只设水折扣"""
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 执行输入指令
        disSte.confirmationSubmission()

        # 执行弹窗的点击动作
        disSte.promptVerification()

        # 执行数据比较的任务
        disSte._verify_content_data()



    # @unittest.skip(r"跳过:test_watikis_NotInput")
    def test_watikis_NotInput(self):
        """勾选水票优惠但不输入优惠信息"""
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 执行输入指令
        disSte.confirmationSubmission()

        # 执行弹窗的点击动作，
        disSte.promptErrorInformation()


    # @unittest.skip(r"跳过:test_watikis_choice")
    def test_watikis_choice(self):
        """设置水票优惠信息"""
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 执行输入指令
        disSte.confirmationSubmission()

        # 执行弹窗的点击动作
        disSte.promptVerification()

        # 执行数据比较的任务
        disSte._verify_content_data()

    # @unittest.skip(r"跳过:test_watikis_discount")
    def test_watikis_discount(self):
        """只设水票折扣"""
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 执行输入指令
        disSte.confirmationSubmission()

        # 执行弹窗的点击动作
        disSte.promptVerification()

        # 执行数据比较的任务
        disSte._verify_content_data()

    # @unittest.skip(r"跳过:test_watikis_discountMaxZero")
    def test_watikis_discountMaxZero(self):
        """只水票折扣，并且最高抵扣为默认值"""
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 执行输入指令
        disSte.confirmationSubmission()

        # 执行弹窗的点击动作
        disSte.promptVerification()

        # 执行数据比较的任务
        disSte._verify_content_data()



    # @unittest.skip(r"跳过:test_watikis_max")
    def test_watikis_max(self):
        """只设最高抵扣"""
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 执行输入指令
        disSte.confirmationSubmission()

        # 执行弹窗的点击动作
        disSte.promptErrorInformation()


    # @unittest.skip(r"跳过:test_watikis_DiscounMax")
    def test_watikis_DiscounMax(self):
        """设置水票折扣和最高抵扣"""
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 执行输入指令
        disSte.confirmationSubmission()

        # 执行弹窗的点击动作
        disSte.promptVerification()

        # 执行数据比较的任务
        disSte._verify_content_data()


if __name__ == '__main__':
    unittest.main()
