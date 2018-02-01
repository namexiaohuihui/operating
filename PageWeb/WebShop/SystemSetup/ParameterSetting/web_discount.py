# -*- coding: utf-8 -*-
import inspect
import os
import sys
import unittest

from PageWeb.WebShop.TargetParameter.SingleVerification import discount_input

__author__ = 'Administrator'
"""
@file: web_goods_discount.py
@time: 2017/11/2 9:53
"""
import inspect
import os
import time
import unittest
import re
from PageWeb.WebShop import JudgmentVerification as jv
from PageWeb.WebShop.SystemSetup.ParameterSetting.namebean import letter_parameter_names
from utils.Logger import Log

"""
商品折扣数:主要验证下面的问题:
1.小数
2.符合要求的数值
3.负数
4.特殊字符
5.中文
6.满足数值要求但符合要求
"""

print("Start getting use cases : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

basename = os.path.splitext(os.path.basename(__file__))[0]
log = Log(basename)
overall_ExcelData = jv._excel_Data(filename="parameterSetting", SHEETNAME=1)
# print(overall_ExcelData)
lpn = letter_parameter_names()
print("Use case acquisition completion : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


class verify_discount(unittest.TestCase):
    """
       继承函数
   """

    def setUp(cls):
        # 该类运行时优先调用的函数
        # log.info("The program begins to execute. Don't stop me when you start.")
        jv.driver = jv._browser()  # 打开浏览器
        jv.user_login()  # 用户登录

    def tearDown(cls):
        # 该类结束时最后调用的函数
        # log.info("Make it complete and continue to press it next time...")
        jv.driver.quit()
        # overall_ExcelData.to_excel(basename + ".xlsx", index=False, encoding="gbk")

    """
        该类中专用的函数
        """

    def _function_overall(self):
        # 获取用例信息
        self.overall = overall_ExcelData.loc[self.function]
        # print(self.overall)

    def _routepath(self):
        # 进入相应的目录
        jv._visible_return_selectop(lpn.sidebar)
        jv._visible_css_selectop(lpn.treew)
        jv._visible_css_selectop(lpn.tabs_discount)

    def _verify_parameter(self, content):
        if content is None:
            content = ''
        return content

    def _sendkey_input(self):
        # 商品折扣
        gd_discount = self.overall[lpn.ps_count_goods_discount()]
        gd_discount = self._verify_parameter(gd_discount)
        jv._visible_json_input(lpn.goods_discount, gd_discount)

        # 商品id
        gd_id = self.overall[lpn.ps_count_goods_id()]
        gd_id = self._verify_parameter(gd_id)
        jv._visible_json_input(lpn.goods_id, gd_id)

        # 水票折扣
        wa_discount = self.overall[lpn.ps_count_watiki_discount()]
        wa_discount = self._verify_parameter(wa_discount)
        jv._visible_json_input(lpn.watiki_discount, wa_discount)

        # 水票id
        wa_id = self.overall[lpn.ps_count_watikis_id()]
        wa_id = self._verify_parameter(wa_id)
        jv._visible_json_input(lpn.watikis_id, wa_id)

        # 商品最高抵扣
        wa_max = self.overall[lpn.ps_count_watiki_max()]
        wa_max = self._verify_parameter(wa_max)
        jv._visible_json_input(lpn.watikis_max, wa_max)

        jv._visible_css_selectop(lpn.discountSave)

    def test_goods_discount_one(self):
        """验证商品打折数输入大于10的问题"""
        # 获取函数名
        self.function = inspect.stack()[0][3]
        self._routepath()
        self._function_overall()  # 获取df 的内容值
        time.sleep(2)

        self._sendkey_input()  # 实现数据输入

    def test_goods_discount_two(self):
        """验证商品打折数输入小于0的问题:即输入负数"""
        # 获取函数名
        function = sys._getframe().f_code.co_name

        self._routepath()
        self._function_overall()  # 获取df 的内容值
        time.sleep(2)

        self._sendkey_input()  # 实现数据输入

    def test_goods_discount_three(self):
        """验证商品打折数输入在符合范围内但小数点后有多位的情况"""
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
        """验证商品打折数输入中文字符"""

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
