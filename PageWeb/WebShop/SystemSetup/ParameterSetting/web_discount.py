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
from PageWeb.WebShop.JudgmentVerification import judgment_verification
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
jv = judgment_verification()
log = Log(basename)
lpn = letter_parameter_names()
overall_ExcelData = jv._excel_Data(filename="discount", SHEETNAME=1)
# print(overall_ExcelData)
print("Use case acquisition completion : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


class verify_discount(unittest.TestCase):
    """
       继承函数
    """

    def setUp(cls):
        # 该类运行时优先调用的函数
        # log.info("The program begins to execute. Don't stop me when you start.")
        jv.driver = jv.option_browser()  # 打开浏览器
        jv.ps_user_login()  # 用户登录

    def tearDown(cls):
        # 该类结束时最后调用的函数
        # log.info("Make it complete and continue to press it next time...")
        jv.driver.quit()
        # overall_ExcelData.to_excel(basename + ".xlsx", index=False, encoding="gbk")

    """
        该类中专用的函数
    """

    def _rou_fun(self):
        self._routepath()
        self._function_overall()

    def _function_overall(self):
        # 获取用例信息
        self.overall = overall_ExcelData.loc[self.function]
        # print(self.overall)

    def _routepath(self):
        # 进入相应的目录
        jv._visible_css_selectop(lpn.sidebar)
        jv._visible_css_selectop(lpn.treew)
        jv._visible_css_selectop(lpn.tabs_discount)

    def _sendkey_input(self):
        # 商品折扣
        gd_discount = self.overall[lpn.ps_count_goods_discount()]
        gd_discount = jv._verify_parameter(gd_discount)
        jv._visible_json_input(lpn.goods_discount, gd_discount)

        # 商品id
        gd_id = self.overall[lpn.ps_count_goods_id()]
        gd_id = jv._verify_parameter(gd_id)
        jv._visible_json_input(lpn.goods_id, gd_id)

        # 水票折扣
        wa_discount = self.overall[lpn.ps_count_watiki_discount()]
        wa_discount = jv._verify_parameter(wa_discount)
        jv._visible_json_input(lpn.watiki_discount, wa_discount)

        # 水票id
        wa_id = self.overall[lpn.ps_count_watikis_id()]
        wa_id = jv._verify_parameter(wa_id)
        jv._visible_json_input(lpn.watikis_id, wa_id)

        # 商品最高抵扣
        wa_max = self.overall[lpn.ps_count_watiki_max()]
        wa_max = jv._verify_parameter(wa_max)
        jv._visible_json_input(lpn.watikis_max, wa_max)

        # 保存按钮
        jv._visible_css_selectop(lpn.discountSave)

    def _verify_content(self):
        my_sql = self.overall[lpn.whole_query_statement()]  # 获取sql语句
        return my_sql

    def _verify_content_data(self):
        my_sql = self._verify_content()
        re_df = jv._verify_match(my_sql)
        re_name = re_df['value']
        print(re_name)
        for ree in re_name:
            print(ree)

    def _verify_content_mysql(self, list_name, list_attr):
        # 查询数据库
        my_sql = self._verify_content()
        if my_sql != None:
            list_code = jv._verify_attr_name(my_sql, list_name, list_attr)
            log.info(list_code)
        else:
            log.info("mysql 语句为空不需要进入.....")

    """
    重复被重复使用的地方。
    将其结合到一个函数统一调用
    """

    def obtain_city_name(self):
        tags = jv.driver.find_elements_by_css_selector(lpn.city_name)
        return tags

    def qwetest_city_number(self):
        # 获取城市数量以及名字(编码)是否正确
        # 获取函数名
        self.function = inspect.stack()[0][3]
        self._rou_fun()
        tags = self.obtain_city_name()

        list_name = []
        list_attr = []
        for tag in tags:
            list_name.append(tag.text)
            attr = tag.get_attribute('href')
            regular = re.search(r'[1-9]\d{5}(?!\d)', attr)
            list_attr.append(int(regular.group()))

        self._verify_content_mysql(list_name, list_attr)

    def qwetest_display_switch(self):
        # 判断显示项是否正确
        # 获取函数名
        self.function = inspect.stack()[0][3]
        self._rou_fun()
        tags = self.obtain_city_name()

        # 找到页面默认展示项的位置
        for tag in range(len(tags)):
            try:
                tags[tag].get_attribute('class')
                break
            except:
                pass

        # 跟需求上的展示项是否一致
        content = tags[tag]
        cont = self.overall[lpn.ps_count_goods_discount()]
        oper = operator.eq(content.text, cont)

        log.info("默认展示页面 %s ----  : %s" % (oper, basename))

        list_name = []
        list_attr = []
        for tag in range(len(tags)):
            jv.vac.element_click(tags[tag])  # 元素点击
            tags = self.obtain_city_name()  # 点击之后会重新刷新页面，需要重新定位元素

            list_name.append(tags[tag].text)

            attr = jv.driver.current_url
            regular = re.search(r'[1-9]\d{5}(?!\d)', attr)
            list_attr.append(int(regular.group()))

        self._verify_content_mysql(list_name, list_attr)

    def test_all_choice(self):
        """不设置优惠直接提交"""
        # 获取函数名
        self.function = inspect.stack()[0][3]
        self._rou_fun()
        time.sleep(2)
        self._verify_content_data()
        # gd_check = jv._visible_return_selectop(lpn.goods_check)
        # wa_check = jv._visible_return_selectop(lpn.watiki_check)
        #
        # # 单选框为选中状态就进行点击
        # if gd_check.is_selected() :
        #     jv.vac.element_click(gd_check)  # 元素点击
        # if wa_check.is_selected() :
        #     jv.vac.element_click(wa_check)  # 元素点击
        #
        # jv.sleep_time(2)
        #
        # # 提交
        # jv._visible_css_selectop(lpn.discountSave)
        #
        # # 提示信息
        # _content_text = jv._visible_css_selectop_text(lpn.modal_body_p)
        # operator.eq(_content_text,self.overall[lpn.whole_output()])
        #
        # # 二次提交
        # jv._visible_css_selectop(lpn.btn_default)

        # _confirm_text = jv._visible_css_selectop_text(lpn.confirm)
        # operator.eq(_confirm_text,self.overall[lpn.whole_result()])


if __name__ == '__main__':
    unittest.main()
