# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: discountOperationSteps.py
@time: 2018/3/12 14:03

"""

import json

from CenterBackground.SystemSetup import SystemCoexistence
from CenterBackground.SystemSetup.ParameterSetting.discountLabelNames import DiscountParameterNames

"""
优惠用例所需要的执行的步骤全在这里
继承：
DiscountParameterNames :用例所涉及的参数名称以及提示
JudgmentVerification ： 数据验证以及工具的使用
"""


class DiscountOperationSteps(SystemCoexistence, DiscountParameterNames):
    # -----------------------------------文件配置参数----------------------------------
    GOODS_RADIO_STATUS = False  # 商品单选框的期望结果
    WATIKIS_RADIO_STATUS = False  # 水票单选框的期望结果

    MODEI_CASE_POSITION = "discount"

    # ----------------------------------文件配置函数-----------------------------------

    def _rou_fun(self):
        """
        进入相应的页面，并获取用例信息
        :return:  暂时没有返回值
        """
        self._visible_css_selectop(self.sidebar)
        self._visible_css_selectop(self.treew)
        self._visible_css_selectop(self.tabs_discount)

    def setRadioStatus(self):
        """
        设置执行用户时，单选框的状态
        GOODS_RADIO_STATUS = False  # 商品单选框的期望结果
        WATIKIS_RADIO_STATUS = False  # 水票单选框的期望结果
        :return:
        """
        self.GOODS_RADIO_STATUS = self.stringToValueBoolean(self.overallExcelData.loc[self.CountGoodsChoice])
        self.WATIKIS_RADIO_STATUS = self.stringToValueBoolean(self.overallExcelData.loc[self.CountWatikiChoice])

    # ------------------------------------输入模块-----------------------------

    def waterInput(self):
        """页面商品输入框"""
        # 商品折扣
        self.confirmInput(self.Countgoodsdiscount(), self.goods_discount)

    def watikiInput(self):
        """页面水票输入框"""
        # 水票折扣
        self.confirmInput(self.CountWatikiDiscount(), self.watiki_discount)

        # 商品最高抵扣
        self.confirmInput(self.CountWatikisMax(), self.watikis_max)

    def confirmationSubmission(self):
        """信息输入框和按钮合并的函数"""
        # 数据输入
        self.waterSelectedInput()
        self.watikiSelectedInput()
        # 保存按钮
        self.visibleDiscountSave()

    # ---------------------------------数据库模块--------------------------
    def _verify_content(self):
        my_sql = self.overall[self.wholeQueryStatement()]  # 获取sql语句
        return my_sql

    def getOverall(self, verify):
        meter = self.overall[verify]
        parameter = self._verify_parameter(meter)
        return parameter

    def _verify_attr_name(self, my_sql, *codeattr):
        re_df = self._verify_match(my_sql)
        re_df = self.list_to_pandas(re_df, ('name', 'code'))
        # 比较两个list的内容
        self.separation(re_df, 'name', codeattr[0])
        self.separation(re_df, 'code', codeattr[1])

    def separation(self, re_df, title, content):
        """
        数据验收
        :param re_df:
        :param title:
        :param content:
        :return:
        """
        # 读取数据并转换成list
        re_name = list(re_df[title])
        # 执行比较的动作
        self.verify_operator(re_name, content)

    def floatToStr(self, count):
        if type(count) is float:
            return str(int(count))
        else:
            return count

    def excleValue(self):

        # 读取excle表格需要输入的内容
        gd_dis = self.floatToStr(self.getOverall(self.Countgoodsdiscount()))
        wa_dis = self.floatToStr(self.getOverall(self.CountWatikiDiscount()))
        wa_max = self.floatToStr(self.getOverall(self.CountWatikisMax()))

        if self.GOODS_RADIO_STATUS and self.WATIKIS_RADIO_STATUS:  # 商品和水票都输入了
            excle_value = {'goods': {'discount': gd_dis
                                     },
                           'watiki': {'discount': wa_dis,
                                      'max': wa_max}}

        elif self.GOODS_RADIO_STATUS:  # 只有商品输入
            excle_value = {'goods': {'discount': gd_dis}}

        elif self.WATIKIS_RADIO_STATUS:  # 只有水票输入
            excle_value = {'watiki': {'discount': wa_dis,
                                      'max': wa_max}}
        else:
            excle_value = None

        return excle_value

    def _getContent(self, valueText):
        """
        比较数据库中的数据跟excle的数据是否一致
        :param value_text: 需要进行比较的数据信息
        :return:
        """
        excleValue = self.excleValue()  # 获取excle中的数据
        # 数据比较
        reEx = self.verify_operator(valueText, excleValue)

        self.log.info("执行用例的函数为： %s 数据库比较结果为: %s " % (self.FUNCTION_NAME, reEx))

    def getValteText(self, verify, value='value'):
        """
        根据数据类型为list的，进行转换成字符串并切割位于数据前后的“[]”
        之后在将切割好的数据转换成json数据（即dict类型）
        根据key来读取数据内容，读取出来的数据类型为str
        需要转换成dict
        :param verify: 数据源
        :param value: 需要读取的key
        :return:
        """
        # 将list转换成str
        verify = json.dumps(verify, ensure_ascii=False)
        # 切割str中前后位置的"[]"
        verify = verify[1:len(verify) - 1]
        # 将str转换成dict
        verify = json.loads(verify)

        # 根据key值读取数据将其转换成dict
        verify = json.loads(verify[value])

        return verify

    def _verify_content_data(self):
        """
        用于优惠信息数据的比较(有点模糊以后完善）
        比较数据库的内容和excle的内容是否一致
        :return:
        """
        # 　读取sql语句
        my_sql = self._verify_content()

        # 判断语句是否None
        if my_sql:
            #  根据sql语句并返回数据
            re_df = self._verify_match(my_sql)

            if re_df:
                #  获取数据中指定key的内容
                value_text = self.getValteText(re_df)

                #  比较数据
                self._getContent(value_text)
            else:
                self.log.info("mysql 语句有误,执行查询时没找到数据.....")
        else:
            self.log.info("mysql 语句为空不执行动作 %s " % my_sql)

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
            self._verify_attr_name(my_sql, list_name, list_attr)
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
        self.verify_operator(_content_text, self.overall[title])
        # 弹窗中的按钮点击
        self._visible_css_selectop(button)

    def promptVerification(self):
        """
        点击提交之后，弹窗的二次确认
        and
        提交之后接口返回的提示信息,该信息为正确的信息
        :return:
        """
        # 提示信息的验证：再次确认的提示
        # self.windowVerification(self.modal_body_p, self.whole_output(), self.btn_primary)

        # 提交之后返回的数据进行验证
        # self.windowVerification(self.visible_h2, self.whole_result(), self.confirm)

        self.returnDataVerification(self.visible_h2)

    def returnVerification(self):
        """
            点击提交之后，弹窗的二次确认
            and
            提交之后接口返回的提示信息,该信息为错误的信息
            :return:
        """
        self.returnDataVerification(self.visible_p)

    def returnDataVerification(self, returnData):
        """
            点击提交之后，弹窗的二次确认
            and
            提交之后接口返回的提示信息
            :return:
        """
        # 提示信息的验证：再次确认的提示
        self.windowVerification(self.modal_body_p, self.whole_output(), self.btn_primary)

        # 提交之后返回的数据进行验证
        self.windowVerification(returnData, self.whole_result(), self.confirm)

    def promptErrorInformation(self):
        """
        信息有误进行提交时，弹窗的提示
        :return:
        """
        self.windowVerification(self.visible_p, self.whole_output(), self.confirm)

    def radioSelected(self, selectop, radioStatus):
        """
        通过单选框元素进行状态的点击
        :param selectop:  单选框的对象
        :return:
        """
        # 获取单选框对象
        _check = self._visible_return_selectop(selectop)

        # 执行单选框为选中状态的指令
        self.visibleRadioSelected(_check, status=radioStatus)

    def waterSelectedInput(self):
        """
        商品优惠项的点击以及优惠数据输入
        :return:
        """
        # 读取商品优惠的设置是否打开
        self.GOODS_RADIO_STATUS = self.stringToValueBoolean(self.overall[self.CountGoodsChoice()])
        # 商品优惠单选框的点击
        self.radioSelected(self.goods_check, self.GOODS_RADIO_STATUS)

        # 数据输入
        self.waterInput() if self.GOODS_RADIO_STATUS else self.log.info(
            "%s的设置为 %s" % (self.CountGoodsChoice(), self.GOODS_RADIO_STATUS))

    def watikiSelectedInput(self):
        """
        水票优惠项的点击以及优惠数据输入
        :return:
        """
        # 读取水票优惠的设置是否打开
        self.WATIKIS_RADIO_STATUS = self.stringToValueBoolean(self.overall[self.CountWatikiChoice()])

        # 水票优惠单选框的点击
        self.radioSelected(self.watiki_check, self.WATIKIS_RADIO_STATUS)

        # 数据输入
        self.watikiInput() if self.WATIKIS_RADIO_STATUS else self.log.info(
            "%s的设置为 %s" % (self.CountWatikiChoice(), self.WATIKIS_RADIO_STATUS))

    def visibleDiscountSave(self):
        """
        页面保存按钮的点击
        :return:
        """
        self._visible_css_selectop(self.discountSave)
