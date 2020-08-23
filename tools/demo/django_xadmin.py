# -*- coding: utf-8 -*- 
# @author:  ln_company
# @license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
# @software: PyCharm
# @time: 20:49 2019/12/31
# @File  : django_xadmin.py
# @Desc  :


import unittest
import os
import time

import ddt
import pandas as pd
import selenium.webdriver.support.expected_conditions as EC

from tools.openpyxlExcel import OpenExcelPandas
from tools.browser_establish import browser_confirm
from tools.operation.selenium_click import action_click
from tools.operation.selenium_input import action_input
from tools.extendBeantifulSoup import ExtendBeantifulSoup


def _excel_Data():
    """
    读取用例
    :return:
    """
    # 读取相应路径中的数据
    read = OpenExcelPandas(name=r'E:\operating\tools\demo\登录账号密码.xls', sheet='正常')
    ex_data = read.internal_read_excel('序号')
    df_index = ex_data.index
    ex_data = [ex_data.loc[df_i] for df_i in df_index]
    return ex_data


@ddt.ddt
class DjangoXadmin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        bc = browser_confirm.__new__(browser_confirm)
        cls.driver = bc.url_opens("http://127.0.0.1:8000/xadmin/")
        cls.vac = action_click()
        cls.vai = action_input()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    @ddt.data(*_excel_Data())
    def test_demo(self, case):
        user_name = case["账号"]
        pass_word = case["密码"]
        self.vai.id_input(self.driver, "id_username", user_name)
        self.vai.id_input(self.driver, "id_password", pass_word)
        self.vac.css_click(self.driver, ".btn.btn-lg.btn-primary.btn-block")
        if self.driver.title != "" and EC.title_contains("主页面 | DingDong"):
            self.vac.css_click(self.driver, "#nav-accordion > div:nth-child(6) > div.panel-heading > h6 > a")
            self.vac.css_click(self.driver, "#nav-panel-6 > a:nth-child(1)")
            ebs = ExtendBeantifulSoup(self.driver, "#changelist-form > div.results.table-responsive > table")
            daily = ebs.lable_table_list('thead', 'th').interfaceToPandas()
            data_set = ebs.lable_table_list('tbody', 'td').interfaceToPandas()
            daily = list(daily.iloc[0])
            data_set.columns = daily
            print("-----------------------------------------------------")
            data_set.to_excel(r'E:\operating\tools\demo\页面内容.xls', index=False, encoding="gbk", sheet_name="爬墙")
        else:
            print("失败")
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
