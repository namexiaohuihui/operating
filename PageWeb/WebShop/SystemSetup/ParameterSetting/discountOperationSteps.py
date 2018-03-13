# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: discountOperationSteps.py
@time: 2018/3/12 14:03

"""

import os
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
    FUNCTION_NAME = ""
    def openingProgram(self,basename,exclefile):
        # 拿出文件名和工作薄
        exclename = exclefile[0]
        exclesheet = exclefile[1]

        # 定义日志
        self.log = Log(basename)

        # 读取文档信息
        self.overallExcelData = self._excel_Data(exclename,exclesheet)

        self.option_browser()  # 打开浏览器
        self.ps_user_login()  # 用户登录



    """
        该类中专用的函数
    """

    def _rou_fun(self):
        self._routepath()  # 调用进入目录的函数
        self._function_overall()  # 调用获取用户的函数

    def _function_overall(self):
        # 获取用例信息
        self.overall = self.overallExcelData.loc[self.FUNCTION_NAME]
        # print(self.overall)

    def _routepath(self):
        # 进入相应的目录
        self._visible_css_selectop(self.sidebar)
        self._visible_css_selectop(self.treew)
        self._visible_css_selectop(self.tabs_discount)

    # ------------------------------------输入模块
    def confirmInput(self, caseTitle, eleInformation):
        """通过输入框进行数据输入"""
        title = self.overall[caseTitle]  # 根据用例title来读取数据

        information = self._verify_parameter(title)  # 判断数据是否为None，如果是就返回一个空值‘’
        self._visible_json_input(eleInformation, information)  # 通过元素id利用json进行输入输入

    def waterInput(self):
        """页面商品输入框"""
        # 商品折扣
        self.confirmInput(self.ps_count_goods_discount(), self.goods_discount)

        # 商品id
        self.confirmInput(self.ps_count_goods_id(), self.goods_id)

    def watikiInput(self):
        """页面水票输入框"""
        # 水票折扣
        self.confirmInput(self.ps_count_watiki_discount(), self.watiki_discount)

        # 水票id
        self.confirmInput(self.ps_count_watikis_id(), self.watikis_id)

        # 商品最高抵扣
        self.confirmInput(self.ps_count_watikis_max(), self.watikis_max)

    def confirmationSubmission(self):
        """信息输入框和按钮合并的函数"""
        # 数据输入
        self.waterInput()
        self.watikiInput()
        # 保存按钮
        self._visible_css_selectop(self.discountSave)

    # ----------------------数据库模块----------------
    def _verify_content(self):
        my_sql = self.overall[self.whole_query_statement()]  # 获取sql语句
        return my_sql

    def excleValue(self):

        # 读取excle表格需要输入的内容
        gd_dis = self.overall[self.ps_count_goods_discount()]
        gd_id = self.overall[self.ps_count_goods_id()]
        wa_dis = self.overall[self.ps_count_watiki_discount()]
        wa_id = self.overall[self.ps_count_watikis_id()]
        wa_max = self.overall[self.ps_count_watikis_max()]

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
        re_ex = self._verify_operator(re_value, excle_value)

        log.info("参与比较的函数为 %s 比较结果为 %s " % (self.FUNCTION_NAME, re_ex))

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
            list_code = self._verify_attr_name(my_sql, list_name, list_attr)
            log.info(list_code)
        else:
            log.info("mysql 语句为空不需要进入.....")

    # ---------------其他模块------------------
    def obtain_city_name(self):
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

        # 提示信息的验证：再次确认的提示
        self.windowVerification(self.modal_body_p, self.whole_output(), self.btn_primary)

        # 提交之后返回的数据进行验证
        self.windowVerification(self.visible_h2, self.whole_result(), self.confirm)

    def promptErrorInformation(self):
        # 点击提交时，因输入内容有误导致的弹窗
        self.windowVerification(self.visible_p, self.whole_result(), self.confirm)

    def isSelected(self):
        """执行单选框为选中状态时就进行点击的动作"""

        # 水优惠单选框的点击
        gd_check = self._visible_return_selectop(self.goods_check)
        self.visibleIsSelected(gd_check)

        # 水票优惠单选框的点击
        wa_check = self._visible_return_selectop(self.watiki_check)
        self.visibleIsSelected(wa_check)

    def notSelected(self, selectop):
        """执行单选框为未选中状态时就进行点击的动作"""

        # 获取单选框对象
        _check = self._visible_return_selectop(selectop)

        # 执行点击命令
        self.visibleNotSelected(_check)

    def waterSelectedInput(self):
        """
        水优惠项的点击以及优惠数据输入
        :return:
        """
        self.notSelected(self.goods_check)
        self.waterInput()

    def watikiSelectedInput(self):
        """
        水票优惠项的点击以及优惠数据输入
        :return:
        """
        self.notSelected(self.watiki_check)
        self.watikiInput()

    # 保存按钮的点击
    def visibleDiscountSave(self):
        self._visible_css_selectop(self.discountSave)

    # 水单选框的点击以及信息输入
    def goodsCheckClick(self):
        self.notSelected(self.goods_check)


