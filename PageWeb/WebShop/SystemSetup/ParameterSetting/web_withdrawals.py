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
import os
import unittest
import inspect
import time

from PageWeb.WebShop.OverallSituation import overallsituation
from practical.utils import stringCutting  as sc
from PageWeb.WebShop import JudgmentVerification as jv
from practical.utils.logger import Log

"""
#--------------------读取excel表格数据部分-----------------------------------------
https://www.cnblogs.com/hongfei/p/3858256.html
"""
print("Start getting use cases : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

basename = os.path.splitext(os.path.basename(__file__))[0]
log = Log(basename)
overall_ExcelData = jv._excel_Data(filename="parameterSetting", SHEETNAME=1)
# print(overall_ExcelData)
ov = overallsituation()
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

    def function_overall(self, function):
        self.overall = overall_ExcelData.loc[function]
        print("---------------")
        print(self.overall)
        print("---------------")

    def _routepath(self):
        jv._visible_return_selectop(".sidebar-menu li:nth-child(2)")
        jv._visible_css_selectop(".treeview-menu.menu-open li:nth-child(1)")
        jv._visible_css_selectop(".nav.nav-tabs li:nth-child(4)")

    def _sendkey_input(self):
        jv._visible_json_input("amount", self.overall["手续费"])
        jv._visible_json_input("fee", self.overall["提现"])
        jv._visible_css_selectop(".btn.btn-primary.feeSave")

    def test_procedures_high_withdrawals(self):
        function = inspect.stack()[0][3]  # 执行函数的函数名
        log.info("The validation scenario is:... %s" % function )

        self._routepath()
        self.function_overall(function) # 获取df 的内容值
        self.case_browser(function) # 执行逻辑
        time.sleep(5)

    def test_procedures_low_withdrawals(self):
        function = inspect.stack()[0][3]  # 执行函数的函数名
        log.info("The validation scenario is:... %s" % function)

        self._routepath()
        self.function_overall(function)
        self.case_browser1(function)
        time.sleep(5)

    def case_browser(self, function):
        self._sendkey_input()
        sweet = jv._visible_css_selectop_text(".sweet-alert.showSweetAlert.visible h2:nth-of-type(1)")

        self.assertEqual(sweet, self.overall["输出"], function)

        # 读取提示框的内容然后保存到df中
        ov = ov.setContent(sweet)
        self.overall["结果"] = ov.getContent()
        print("nimadebiegw " + self.overall["结果"])

    def case_browser1(self, function):
        self._sendkey_input()
        sweet = jv._visible_css_selectop_text(".sweet-alert.showSweetAlert.visible p:nth-of-type(1)")

        self.assertEqual(sweet, self.overall["输出"], function)
        # 读取提示框的内容然后保存到df中
        ov = ov.setContent(sweet)
        self.overall["结果"] = ov.getContent()
        print("zheshishenm shuju " + self.overall["结果"])
        overall_ExcelData.to_csv("zailai.csv", index=False, encoding="gbk")


if __name__ == '__main__':
    unittest.main()
    # overall_ExcelData.to_csv("buhao.csv", index=False, encoding="gbk")
