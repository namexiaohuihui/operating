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
import json
import inspect
import unittest
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

下文重复出现的内容注释：
1.@unittest.skip(r"跳过:XXXX") ：告诉unittest框架我要跳过这个用例，并打印出信息（跳过:XXXX）
"""

print("Start getting use cases : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 获取文件名
basename = os.path.splitext(os.path.basename(__file__))[0]
# 定义类参数
jv = judgment_verification()
log = Log(basename)
lpn = letter_parameter_names()
# 读取数据内容
overall_ExcelData = jv._excel_Data(filename="discount", SHEETNAME=1)

print("Use case acquisition completion : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


class verify_discount(unittest.TestCase):
    """
       继承函数
    """

    def setUp(cls):
        # 该类运行时优先调用的函数
        # log.info("The program begins to execute. Don't stop me when you start.")
        jv.option_browser()  # 打开浏览器
        jv.ps_user_login()  # 用户登录

    def tearDown(cls):
        try:
            # 该类结束时最后调用的函数
            # log.info("Make it complete and continue to press it next time...")
            # jv.driver.quit()
            # overall_ExcelData.to_excel(basename + ".xlsx", index=False, encoding="gbk")
            pass
        except UnicodeDecodeError:
            log.info("又出现UTF-8的错误........")

    """
        该类中专用的函数
    """

    def _rou_fun(self):
        self._routepath()  # 调用进入目录的函数
        self._function_overall()  # 调用获取用户的函数

    def _function_overall(self):
        # 获取用例信息
        self.overall = overall_ExcelData.loc[self.function]
        # print(self.overall)

    def _routepath(self):
        # 进入相应的目录
        jv._visible_css_selectop(lpn.sidebar)
        jv._visible_css_selectop(lpn.treew)
        jv._visible_css_selectop(lpn.tabs_discount)

    # ------------------------------------输入模块
    def confirmInput(self, caseTitle, eleInformation):
        """通过输入框进行数据输入"""
        title = self.overall[caseTitle]  # 根据用例title来读取数据

        information = jv._verify_parameter(title)  # 判断数据是否为None，如果是就返回一个空值‘’
        jv._visible_json_input(eleInformation, information)  # 通过元素id利用json进行输入输入

    def waterInput(self):
        """页面商品输入框"""
        # 商品折扣
        self.confirmInput(lpn.ps_count_goods_discount(), lpn.goods_discount)

        # 商品id
        self.confirmInput(lpn.ps_count_goods_id(), lpn.goods_id)

    def watikiInput(self):
        """页面水票输入框"""
        # 水票折扣
        self.confirmInput(lpn.ps_count_watiki_discount(), lpn.watiki_discount)

        # 水票id
        self.confirmInput(lpn.ps_count_watikis_id(), lpn.watikis_id)

        # 商品最高抵扣
        self.confirmInput(lpn.ps_count_watikis_max(), lpn.watikis_max)

    def confirmationSubmission(self):
        """信息输入框和按钮合并的函数"""
        # 数据输入
        self.waterInput()
        self.watikiInput()
        # 保存按钮
        jv._visible_css_selectop(lpn.discountSave)

    # ----------------------数据库模块----------------
    def _verify_content(self):
        my_sql = self.overall[lpn.whole_query_statement()]  # 获取sql语句
        return my_sql

    def excleValue(self):

        # 读取excle表格需要输入的内容
        gd_dis = self.overall[lpn.ps_count_goods_discount()]
        gd_id = self.overall[lpn.ps_count_goods_id()]
        wa_dis = self.overall[lpn.ps_count_watiki_discount()]
        wa_id = self.overall[lpn.ps_count_watikis_id()]
        wa_max = self.overall[lpn.ps_count_watikis_max()]

        # 如果需要输入内容就返回内容否则返回一个空值
        gbSult = gd_dis if gd_dis  else False
        waSult = wa_dis if wa_dis  else False
        if gbSult and waSult:
            # 将需要输入的参数弄成一个列表
            excle_value = {'goods': {'discount': gd_dis,
                                     'exception': gd_id},
                           'watiki': {'discount': wa_dis,
                                      'exception': wa_id,
                                      'max': wa_max}}
        elif gbSult:
            # 将需要输入的参数弄成一个列表
            excle_value = {'goods': {'discount': gd_dis,
                                     'exception': gd_id},
                           'watiki': {'discount': '',
                                      'exception': '',
                                      'max': ''}}
        elif waSult:
            # 将需要输入的参数弄成一个列表
            excle_value = {'goods': {'discount': '',
                                     'exception': ''},
                           'watiki': {'discount': wa_dis,
                                      'exception': wa_id,
                                      'max': wa_max}}
        else:
            excle_value = '[]'

        return excle_value

    def _get_content(self, value_text):
        """比较数据库中的数据跟excle的数据是否一致"""

        excle_value = self.excleValue()  # 获取excle中的数据
        re_value = json.loads(value_text[0])  # 获取数据库中的数据

        # 数据比较
        re_ex = jv._verify_operator(re_value, excle_value)

        log.info("参与比较的函数为 %s 比较结果为 %s " % (self.function,re_ex))

    def _verify_content_data(self):
        """
        用于优惠信息数据的比较(有点模糊以后完善）
        比较数据库的内容和excle的内容是否一致
        :return:
        """
        # 　查询数据库
        my_sql = self._verify_content()
        if my_sql != None:
            #  判断sql是否存在，并返回df数据
            re_df = jv._verify_match(my_sql)
            #  获取数据中指定key的内容
            value_text = re_df['value']
            #   比较数据
            self._get_content(value_text)
        else:
            log.info("mysql 语句为空不需要进入.....")

    def _verify_content_mysql(self, list_name, list_attr):
        """
        用于查询城市数据以及页面读取的城市数据校验
        :param list_name: 城市名
        :param list_attr: 城市编码
        :return:
        """
        # 查询数据库
        my_sql = self._verify_content()
        if my_sql != None:
            list_code = jv._verify_attr_name(my_sql, list_name, list_attr)
            log.info(list_code)
        else:
            log.info("mysql 语句为空不需要进入.....")

    # ---------------其他模块------------------
    def obtain_city_name(self):
        tags = jv.driver.find_elements_by_css_selector(lpn.city_name)
        return tags

    def windowVerification(self, prompt, title, button):
        """
        获取弹窗中的信息，并进行点击操作
        :param prompt: 根据prompt来获取弹窗中的提示信息
        :param title: 根据titke去寻找用例中的数据
        :param button: 弹窗中的点击按钮
        :return:
        """
        # 获取弹窗中的提示信息
        _content_text = jv._visible_css_selectop_text(prompt)
        # 比较弹窗提示信息跟大大要求的是否一致
        jv._verify_operator(_content_text, self.overall[title])
        # 弹窗中的按钮点击
        jv._visible_css_selectop(button)

    def promptVerification(self):

        # 提示信息的验证：再次确认的提示
        self.windowVerification(lpn.modal_body_p,lpn.whole_output(),lpn.btn_primary)

        # 提交之后返回的数据进行验证
        self.windowVerification(lpn.visible_h2, lpn.whole_result(), lpn.confirm)

    def promptErrorInformation(self):
        # 点击提交时，因输入内容有误导致的弹窗
        self.windowVerification(lpn.visible_p, lpn.whole_result(), lpn.confirm)

    def isSelected(self):
        """执行单选框为选中状态时就进行点击的动作"""

        # 水优惠单选框的点击
        gd_check = jv._visible_return_selectop(lpn.goods_check)
        jv.visibleIsSelected(gd_check)

        # 水票优惠单选框的点击
        wa_check = jv._visible_return_selectop(lpn.watiki_check)
        jv.visibleIsSelected(wa_check)

    def notSelected(self,selectop):
        """执行单选框为未选中状态时就进行点击的动作"""

        # 获取单选框对象
        _check = jv._visible_return_selectop(selectop)

        # 执行点击命令
        jv.visibleNotSelected(_check)

    def waterSelectedInput(self):
        """
        水优惠项的点击以及优惠数据输入
        :return:
        """
        self.notSelected(lpn.goods_check)
        self.waterInput()

    def watikiSelectedInput(self):
        """
        水票优惠项的点击以及优惠数据输入
        :return:
        """
        self.notSelected(lpn.watiki_check)
        self.watikiInput()

    # ---------------用例部分-----------------
    @unittest.skip(r"跳过:test_city_number")
    def test_city_number(self):
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

    @unittest.skip(r"跳过:test_display_switch")
    def test_display_switch(self):
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
        oper = jv._verify_operator(content.text, cont)
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

    @unittest.skip(r"跳过:test_display_switch")
    def test_cancel_input(self):
        """不设置优惠时对输入框进行校验"""
        # 获取函数名，并相应的目录下面
        self.function = inspect.stack()[0][3]
        self._rou_fun()

        gd_check = jv._visible_return_selectop(lpn.goods_check)
        wa_check = jv._visible_return_selectop(lpn.watiki_check)
        # 单选框为选中状态就进行点击
        jv.visibleIsSelected(gd_check)
        jv.visibleIsSelected(wa_check)

        # self.waterInput()
        """通过输入框进行数据输入"""
        gd_dis = jv._visible_css_selectop_Id(lpn.goods_discount)
        gd_id = jv._visible_css_selectop_Id(lpn.goods_id)
        wa_dis = jv._visible_css_selectop_Id(lpn.watiki_discount)
        wa_id = jv._visible_css_selectop_Id(lpn.watikis_id)
        wa_max = jv._visible_css_selectop_Id(lpn.watikis_max)

        cancelInput = 'true' if gd_dis and gd_id and wa_dis and wa_id and wa_max else 'false';

        jv._verify_operator(cancelInput, self.overall[lpn.whole_result()])

    @unittest.skip(r"跳过:test_all_cancel")
    def test_all_cancel(self):
        """不设置优惠直接提交"""
        # 获取函数名
        self.function = inspect.stack()[0][3]
        self._rou_fun()

        # 执行单选框为选中状态时就进行点击的动作
        self.isSelected()

        # 提交
        jv._visible_css_selectop(lpn.discountSave)

        # 提示信息
        _content_text = jv._visible_css_selectop_text(lpn.modal_body_p)
        jv._verify_operator(_content_text, self.overall[lpn.whole_output()])
        log.info(_content_text)

        # 二次提交
        jv._visible_css_selectop(lpn.btn_primary)

        """二次提交之后的返回信息"""
        _confirm_text = jv._visible_css_selectop_text(lpn.visible_h2)  # 标题
        jv.sleep_time()
        jv._verify_operator(_confirm_text, self.overall[lpn.whole_result()])
        jv.sleep_time()
        log.info(_confirm_text)

        jv._visible_css_selectop(lpn.confirm)  # 提示框的确定按钮

        # 比较数据库中的数据和输入的数据是否一致
        self._verify_content_data()

    @unittest.skip(r"跳过:test_all_choice")
    def test_all_choice(self):
        """设置优惠直接提交"""
        # 获取函数名
        self.function = inspect.stack()[0][3]
        self._rou_fun()

        # 水单选框的点击以及信息输入
        self.waterSelectedInput()

        # 水票单选框的点击以及信息输入
        self.watikiSelectedInput()

        # 提交按钮的点击
        jv._visible_css_selectop(lpn.discountSave)

        # 执行弹窗的点击动作
        self.promptVerification()

        # 数据库信息比较
        self._verify_content_data()

    # @unittest.skip(r"跳过:test_water_NotInput")
    def test_water_NotInput(self):
        # 获取函数名
        self.function = inspect.stack()[0][3]
        self._rou_fun()

        # 水单选框的点击以及信息输入
        self.notSelected(lpn.goods_check)
        self.waterInput()

        # 提交按钮的点击
        jv._visible_css_selectop(lpn.discountSave)

        # 输入错误内容时，弹窗的提示
        self.promptErrorInformation()

        log.info("执行完了.....")

if __name__ == '__main__':
    unittest.main()
