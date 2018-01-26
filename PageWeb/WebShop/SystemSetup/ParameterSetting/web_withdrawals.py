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
overall_ExcelData = jv._excel_Data(filename="parameterSetting", SHEETNAME=1)
# print(overall_ExcelData)
lpn = letter_parameter_names()
print("Use case acquisition completion : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


class verify_withdrawals(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # 该类运行时优先调用的函数
        log.info("The program begins to execute. Don't stop me when you start.")
        jv.driver = jv._browser()  # 打开浏览器
        jv.user_login()  # 用户登录

    @classmethod
    def tearDown(cls):
        # 该类结束时最后调用的函数
        log.info("Make it complete and continue to press it next time...")
        jv.driver.quit()


    def __del__(self):
        print("------------------------------")

    def function_overall(self, function):
        # 获取用例信息
        self.overall = overall_ExcelData.loc[function]

    def _routepath(self):
        # 进入相应的目录
        jv._visible_return_selectop(lpn.sidebar)
        jv._visible_css_selectop(lpn.treew)
        jv._visible_css_selectop(lpn.tabs_withdrawals)

    def _sendkey_input(self):
        # 对指定输入框进行输入
        jv._visible_json_input(lpn.amount_load, self.overall[lpn.parameter_procedures()])
        jv._visible_json_input(lpn.fee_load, self.overall[lpn.parameter_withdrawals()])
        jv._visible_css_selectop(lpn.extractSave)

    def test_procedures_high_withdrawals(self):
        # 提现金额大于手续费
        function = inspect.stack()[0][3]  # 执行函数的函数名
        log.info("The validation scenario is:... %s" % function )

        self._routepath()
        self.function_overall(function) # 获取df 的内容值
        self.case_browser(function,lpn.visible_h2) # 执行逻辑
        time.sleep(5)

    def test_procedures_low_withdrawals(self):
        # 两个都输入0
        function = inspect.stack()[0][3]  # 执行函数的函数名
        log.info("The validation scenario is:... %s" % function)

        self._routepath()
        self.function_overall(function)
        self.case_browser(function,lpn.visible_p)
        time.sleep(5)

    def case_browser(self, function ,visible_text):
        self._sendkey_input()
        sweet = jv._visible_css_selectop_text(visible_text)

        # 读取提示框的内容然后保存到df中
        self.overall[lpn.whole_result()] = sweet

    def case_browser1(self, function):
        self._sendkey_input()
        sweet = jv._visible_css_selectop_text(".sweet-alert.showSweetAlert.visible p:nth-of-type(1)")

        self.assertEqual(sweet, self.overall[lpn.whole_output()], function)
        # 读取提示框的内容然后保存到df中
        self.overall[lpn.whole_result()] = sweet

        print("zheshishenm shuju " + self.overall[lpn.whole_result()])
        # overall_ExcelData.to_csv("zailai.csv", index=False, encoding="gbk")


if __name__ == '__main__':
    unittest.main()
    # overall_ExcelData.to_csv("buhao.csv", index=False, encoding="gbk")
