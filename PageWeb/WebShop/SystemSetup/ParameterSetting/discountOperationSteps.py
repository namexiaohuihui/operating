# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: discountOperationSteps.py
@time: 2018/3/12 14:03

"""

import os
import time
import json
import inspect
import unittest
from utils.Logger import Log
from PageWeb.WebShop.judgmentVerification import JudgmentVerification
from PageWeb.WebShop.SystemSetup.ParameterSetting.discountParameterNames import DiscountParameterNames

"""
优惠用例所需要的执行的步骤全在这里
继承：
DiscountParameterNames :用例所涉及的参数名称以及提示
JudgmentVerification ： 数据验证以及工具的使用
"""


class DiscountOperationSteps(JudgmentVerification, DiscountParameterNames):

#-----------------------------------文件配置参数----------------------------------
    FUNCTION_NAME = "" # 执行函数的名称
    RADIO_STATUS = False # 单选框的期望结果

    def setFunctionName(self,functionName):
        self.FUNCTION_NAME = functionName

    def setRadioStatus(self,radioStatus):
        self.RADIO_STATUS = radioStatus


#----------------------------------文件配置函数-----------------------------------
    def openingProgram(self, basename, exclefile):
        """
        定义log日志文件以及读取用例数据
        :param basename:  执行用例的文件名
        :param exclefile:  需要读取用例的文件名
        :return:  暂时没有返回值
        """
        # 拿出文件名和工作薄
        exclename = exclefile[0]
        exclesheet = exclefile[1]

        # 定义日志
        self.log = Log(basename)

        # 读取文档信息
        self.overallExcelData = self._excel_Data(exclename, exclesheet)

        self.option_browser()  # 打开浏览器
        self.ps_user_login()  # 用户登录


    def _rou_fun(self):
        """
        进入相应的页面，并获取用例信息
        :return:  暂时没有返回值
        """
        self._visible_css_selectop(self.sidebar)
        self._visible_css_selectop(self.treew)
        self._visible_css_selectop(self.tabs_discount)

        # 根据用例标题获取用例
        self.overall = self.overallExcelData.loc[self.FUNCTION_NAME]


    # ------------------------------------输入模块
    def confirmInput(self, caseTitle, eleInformation):
        """通过输入框进行数据输入"""
        title = self.overall[caseTitle]  # 根据用例title来读取数据

        information = self._verify_parameter(title)  # 判断数据是否为None，如果是就返回一个空值‘’

        self._visible_json_input(eleInformation, information)  # 通过元素id利用json进行输入输入

    def waterInput(self):
        """页面商品输入框"""
        # 商品折扣
        self.confirmInput(self.psCountgoodsdiscount(), self.goods_discount)

        # 商品id
        self.confirmInput(self.psCountGoodsId(), self.goods_id)

    def watikiInput(self):
        """页面水票输入框"""
        # 水票折扣
        self.confirmInput(self.psCountWatikiDiscount(), self.watiki_discount)

        # 水票id
        self.confirmInput(self.psCountWatikisId(), self.watikis_id)

        # 商品最高抵扣
        self.confirmInput(self.psCountWatikisMax(), self.watikis_max)

    def confirmationSubmission(self):
        """信息输入框和按钮合并的函数"""
        # 数据输入
        self.waterSelectedInput()
        self.watikiSelectedInput()
        # 保存按钮
        self.visibleDiscountSave()

    # ----------------------数据库模块----------------
    def _verify_content(self):
        my_sql = self.overall[self.whole_query_statement()]  # 获取sql语句
        return my_sql

    def excleValue(self):

        # 读取excle表格需要输入的内容
        gd_dis = self.overall[self.psCountgoodsdiscount()]
        gd_id = self.overall[self.psCountGoodsId()]
        wa_dis = self.overall[self.psCountWatikiDiscount()]
        wa_id = self.overall[self.psCountWatikisId()]
        wa_max = self.overall[self.psCountWatikisMax()]

        # 如果需要输入内容就返回内容否则返回一个空值
        gbSult = gd_dis if gd_dis  else ''
        waSult = wa_dis if wa_dis  else ''
        if gbSult or waSult:
            # 将需要输入的参数弄成一个列表
            excle_value = {'goods': {'discount': gd_dis,
                                     'exception': gd_id},
                           'watiki': {'discount': wa_dis,
                                      'exception': wa_id,
                                      'max': wa_max}}
        else:
            excle_value = '[]'

        return excle_value

    def _get_content(self, value_text):
        """
        比较数据库中的数据跟excle的数据是否一致
        :param value_text: 需要进行比较的数据信息
        :return:
        """
        excle_value = self.excleValue()  # 获取excle中的数据
        re_value = json.loads(value_text[0])  # 获取数据库中的数据

        # 数据比较
        re_ex = self._verify_operator(re_value, excle_value)

        self.log.info("执行用例的函数为： %s 数据库比较结果为: %s " % (self.FUNCTION_NAME, re_ex))

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
            re_df = self._verify_match(my_sql)
            #  获取数据中指定key的内容
            value_text = re_df['value']
            #   比较数据
            self._get_content(value_text)
        else:
            self.log.info("mysql 语句为空不需要进入.....")

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
            list_code = self._verify_attr_name(my_sql, list_name, list_attr)
            self.log.info(list_code)
        else:
            self.log.info("mysql 语句为空不需要进入.....")

    # ---------------其他模块------------------
    def obtain_city_name(self):
        """
        获取全部城市的名字
        :return:
        """
        tags = self.driver.find_elements_by_css_selector(self.city_name)
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
        _content_text = self._visible_css_selectop_text(prompt)
        # 比较弹窗提示信息跟大大要求的是否一致
        self._verify_operator(_content_text, self.overall[title])
        # 弹窗中的按钮点击
        self._visible_css_selectop(button)

    def promptVerification(self):
        """
        点击提交之后，弹窗的二次确认
        and
        提交之后接口返回的提示信息
        :return:
        """
        # 提示信息的验证：再次确认的提示
        self.windowVerification(self.modal_body_p, self.whole_output(), self.btn_primary)

        # 提交之后返回的数据进行验证
        self.windowVerification(self.visible_h2, self.whole_result(), self.confirm)

    def promptErrorInformation(self):
        """
        信息有误进行提交时，弹窗的提示
        :return:
        """
        self.windowVerification(self.visible_p, self.whole_result(), self.confirm)

    def radioSelected(self, selectop):
        """
        通过单选框元素进行状态的点击
        :param selectop:  单选框的对象
        :return:
        """
        # 获取单选框对象
        _check = self._visible_return_selectop(selectop)

        # 执行单选框为选中状态的指令
        self.visibleRadioSelected(_check, status=self.RADIO_STATUS)

    def waterSelectedInput(self):
        """
        商品优惠项的点击以及优惠数据输入
        :return:
        """
        # 读取商品优惠的设置是否打开
        self.RADIO_STATUS = self.stringToValueBoolean(self.overall[self.psCountGoodsChoice()])
        # 商品优惠单选框的点击
        self.radioSelected(self.goods_check)
        self.waterInput() if self.RADIO_STATUS else self.log(
            "%s的设置为 %s" %(self.psCountGoodsChoice(),self.RADIO_STATUS))

    def watikiSelectedInput(self):
        """
        水票优惠项的点击以及优惠数据输入
        :return:
        """
        # 读取水票优惠的设置是否打开
        self.RADIO_STATUS = self.stringToValueBoolean(self.overall[self.psCountWatikiChoice()])
        # 水票优惠单选框的点击
        self.radioSelected(self.watiki_check)
        self.watikiInput() if self.RADIO_STATUS else self.log(
            "%s的设置为 %s" % (self.psCountWatikiChoice(), self.RADIO_STATUS))



    def visibleDiscountSave(self):
        """
        页面保存按钮的点击
        :return:
        """
        self._visible_css_selectop(self.discountSave)


