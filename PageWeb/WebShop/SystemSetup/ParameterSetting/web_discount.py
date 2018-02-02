# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: web_goods_discount.py
@time: 2017/11/2 9:53
"""

import os
import re
import sys
import time
import inspect
import unittest
import operator  # 任何对象都可以比较功能
from utils.Logger import Log
from PageWeb.WebShop import JudgmentVerification as jv
from PageWeb.WebShop.SystemSetup.ParameterSetting.namebean import letter_parameter_names

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
overall_ExcelData = jv._excel_Data(filename="discount", SHEETNAME=1)
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

    def _verify_mysql(self, my_sql, list_name, list_attr):
        # 数据库查询
        regular = re.match('^SELECT', my_sql)

        if regular != None:
            # 读取数据库内容
            result = jv.total_vertical_selects(my_sql)
            re_df = jv._conversion_pandas(result)

            re_name = re_df['name']
            re_code = re_df['code']

            # 比较两个list的内容
            verify_code = operator.eq(re_code, list_attr)
            verify_name = operator.eq(re_name, list_name)
            list_code = []
            for code in  range(len(verify_code)):
                content = "编号： %s 结果为 %s,城市名： %s 结果为 %s" \
                          % (list_attr[code], verify_code[code], list_name[code],verify_name[code])
                list_code.append(content)

            print(list_code)

    def test_display_switch(self):
        # 获取城市数量以及名字(编码)是否正确
        # 获取函数名
        self.function = inspect.stack()[0][3]
        self._routepath()
        self._function_overall()  # 获取df 的内容值
        tags = jv.driver.find_elements_by_css_selector(lpn.city_name)


    def test_city_number(self):
        # 获取城市数量以及名字(编码)是否正确
        # 获取函数名
        self.function = inspect.stack()[0][3]
        self._routepath()
        self._function_overall()  # 获取df 的内容值
        tags = jv.driver.find_elements_by_css_selector(lpn.city_name)
        list_text = []
        list_attr = []
        for tag in tags:
            list_text.append(tag.text)
            attr = tag.get_attribute('href')
            regular = re.search(r'[1-9]\d{5}(?!\d)', attr)
            list_attr.append(int(regular.group()))
            # 查询数据库
        my_sql = self.overall[lpn.whole_query_statement()]  # 获取sql语句
        if my_sql != None:
            self._verify_mysql(my_sql, list_text, list_attr)

    def qwetest_all_choice(self):
        """验证商品打折数输入大于10的问题"""
        # 获取函数名
        self.function = inspect.stack()[0][3]
        self._routepath()
        self._function_overall()  # 获取df 的内容值
        time.sleep(2)

        self._sendkey_input()  # 实现数据输入


if __name__ == '__main__':
    unittest.main()
