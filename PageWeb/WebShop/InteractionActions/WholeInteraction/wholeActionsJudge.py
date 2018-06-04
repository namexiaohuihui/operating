# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: wholeActionsJudge.py
@time: 2018/5/25 15:10
"""
# from PageWeb.WebShop.InteractionActions import WholeInteraction
from PageWeb.WebShop.InteractionActions import InteractionCoexistence
from tools.operationSelector import OperationSelector


class WholeActionsJudge(InteractionCoexistence):
    # excle文档中case所在工作薄的名称
    MODEL_WORKBOOK_LABEL = '标签'

    # 当前子慕课在菜单下的所属位置
    TREEW_TAGS_LOCATION = "1"

    # 根据key值，读取modei文件下保存用例的存放位置
    MODEI_CASE_POSITION = "whole"

    # MYSQL_DF, LABLE_DF
    def __init__(self) -> '对象实例化时就直接解析yaml中的数据信息,方便之后直接使用':
        self.parseyaml_location()
        self.parseyaml_content()

    # def city_active_confirm(self):
    # loantion = self.select_path['citytab']['value']
    # self._visible_return_selectop(loantion)


