# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: web_extract.py
@time: 2017/10/24 21:57
@项目名称:operating
"""
import unittest
import os
from time import sleep

from practical.Exception_error.DefinitionError import definition_error
from practical.constant.browser.browser_establish import browser_confirm
from practical.constant.parameter.parameter_data import parameter_content
from practical.operation import selenium_input, selenium_click


class discount_input(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        print("%s   开始执行" % cls.basename)
        cls.url_op(cls)

    @classmethod
    def tearDownClass(cls):
        print("%s   执行完毕" % cls.basename)
        cls.browser.close()

    #调用浏览器对象
    def url_op(self):
        bc = browser_confirm.__new__(browser_confirm)

        # 创建浏览器对象
        self.browser = bc.url_opens()

        # 创建参数对象
        self.parame = parameter_content()

    def test_case1(self):
        sleep(2)
        msg = '提现手续费应小于提现金额'
        print(msg)
        self.case_browser('0.1', '2', msg )

    def test_case2(self):
        msg = '请输入整数最多7位,小数后两位的价格格式'
        print(msg)
        self.case_browser('-', '2', msg)

    def test_case3(self):
        msg = '请输入整数最多7位,小数后两位的价格格式'
        print(msg)
        self.case_browser('2', '-', msg)

    def case_browser(self,amount,fee,msg):
        try:
            # 输入框的内容
            amount_load = ".form-control.intonum.amount"

            # 输入执行
            selenium_input.css_input(self.browser, amount_load, amount)

            # 输入框的内容
            fee_load = ".form-control.intoprice.fee"

            # 输入执行
            selenium_input.css_input(self.browser, fee_load, fee)

            #点击保存按钮
            selenium_click.css_click(self.browser, '.btn.btn-primary.feeSave')

            #弹窗上的数据信息
            sweet = self.browser.find_element_by_css_selector('.sweet-alert.showSweetAlert.visible >p').text

            sleep(2)

            #判断提示语是否正确
            assert sweet == msg , self.basename + 'Excessive Commission'

            #弹窗上的按钮
            selenium_click.css_click(self.browser, '.confirm')

            sleep(1)

        except:
            self.writelog()

    # 出现错误之后截图以及写入文档中
    def writelog(self):
         # 调用错误类吗，进行错误打印
        de_error = definition_error()
        de_error.erroe_get(self.basename, self.browser)


if __name__ == '__main__':
    unittest.main()