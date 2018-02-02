# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: web_withdrawals.py
@time: 2017/10/24 21:57
@项目名称:operating
描述：提现界面的case

主要验证输入框输入的内容：
1.小数
2.在范围内容的数值
3.特殊符号
4.负数
5.不在范围内的数值
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
#--------------------读取excel表格数据部分-----------------------------------------
https://www.cnblogs.com/hongfei/p/3858256.html
"""
print("Start getting use cases : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

basename = os.path.splitext(os.path.basename(__file__))[0]
log = Log(basename)
overall_ExcelData = jv._excel_Data(filename="withdrawals", SHEETNAME=1)
# print(overall_ExcelData)
lpn = letter_parameter_names()
print("Use case acquisition completion : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


class verify_withdrawals(unittest.TestCase):
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
        jv._visible_css_selectop(lpn.tabs_withdrawals)

    def _sendkey_input(self):
        # 对指定输入框进行输入
        drawals = self.overall[lpn.ps_with_extract()]
        jv._visible_json_input(lpn.amount_load, drawals)

        time.sleep(1)

        minyuan_text = jv._visible_css_selectop_text(lpn.minyuan)
        self.assertEqual(drawals, minyuan_text, self.function + " : fail")  # 比较动态计算的内容

        jv._visible_json_input(lpn.fee_load, self.overall[lpn.ps_with_cost()])

        jv._visible_css_selectop(lpn.extractSave)

        time.sleep(2)

    def _verify_mysql(self, my_sql):
        # 数据库查询
        drawals = self.overall[lpn.ps_with_extract()]
        dures = self.overall[lpn.ps_with_cost()]
        regular = re.match('^SELECT', my_sql)
        if regular != None:
            time.sleep(2)
            # 读取数据库内容
            result = jv.mysql_single_selects(my_sql)
            value = result["value"]
            value_split = value.split(",")

            # 比较数据是否正确
            self.assertEqual(value_split[0], drawals, self.function + " : fail")
            self.assertEqual(value_split[1], dures, self.function + " : fail")

    def _total_case(self, visible_text):
        # case的汇总
        self._routepath()
        self._function_overall()  # 获取df 的内容值
        time.sleep(2)
        self.case_browser(visible_text)  # 执行逻辑

    """
    case函数
    """

    def test_less_than(self):
        # 提现金额小于手续费
        self.function = inspect.stack()[0][3]  # 执行函数的函数名
        log.info("The validation scenario is:... %s" % self.function)
        self._total_case(lpn.visible_p)

    def test_all_zero(self):
        # 两个都输入0
        self.function = inspect.stack()[0][3]  # 执行函数的函数名
        log.info("The validation scenario is:... %s" % self.function)
        self._total_case(lpn.visible_p)

    def test_greater_than(self):
        # 提现金额大于手续费
        self.function = inspect.stack()[0][3]  # 执行函数的函数名
        log.info("The validation scenario is:... %s" % self.function)
        self._total_case(lpn.visible_h2)

    def test_chinese_characters(self):
        # 两个都输入中文
        self.function = inspect.stack()[0][3]  # 执行函数的函数名
        log.info("The validation scenario is:... %s" % self.function)

        self._total_case(lpn.visible_p)

    def test_english_letter(self):
        # 两个都输入字母
        self.function = inspect.stack()[0][3]  # 执行函数的函数名
        log.info("The validation scenario is:... %s" % self.function)

        self._total_case(lpn.visible_p)

    def test_special_character(self):
        # 两个都输入特殊符号

        self.function = inspect.stack()[0][3]  # 执行函数的函数名
        log.info("The validation scenario is:... %s" % self.function)

        self._total_case(lpn.visible_p)

    def test_decimal(self):
        # 两个都输入小数

        self.function = inspect.stack()[0][3]  # 执行函数的函数名
        log.info("The validation scenario is:... %s" % self.function)

        self._total_case(lpn.visible_p)

    def test_decimal_integer(self):
        # 提现金额输入小数,手续费输入整数
        self.function = inspect.stack()[0][3]  # 执行函数的函数名
        log.info("The validation scenario is:... %s" % self.function)

        self._total_case(lpn.visible_p)

    def test_integer_decimal(self):
        # 提现金额输入整数,手续费输入小数
        self.function = inspect.stack()[0][3]  # 执行函数的函数名
        log.info("The validation scenario is:... %s" % self.function)

        self._total_case(lpn.visible_p)

    def test_integer_overrun(self):
        # 提现金额输入正常数字,手续费输入超长整数
        self.function = inspect.stack()[0][3]  # 执行函数的函数名
        log.info("The validation scenario is:... %s" % self.function)

        self._total_case(lpn.visible_p)

    def test_overrun_integer(self):
        # 提现金额输入超长数字,手续费输入正常
        self.function = inspect.stack()[0][3]  # 执行函数的函数名
        log.info("The validation scenario is:... %s" % self.function)

        self._total_case(lpn.visible_p)

    def case_browser(self, visible_text):

        self._sendkey_input()  # 实现数据输入

        sweet = jv._visible_css_selectop_text(visible_text)  # 获取提示框的数据
        time.sleep(2)

        # 读取提示框的内容然后保存到df中
        overall_ExcelData.loc[self.function, lpn.whole_result()] = sweet

        # 提示框中的确定按钮
        jv._visible_css_selectop(lpn.confirm)

        # 查询数据库
        my_sql = self.overall[lpn.whole_query_statement()]  # 获取sql语句
        if my_sql != None:
            self._verify_mysql(my_sql)


if __name__ == '__main__':
    unittest.main()
