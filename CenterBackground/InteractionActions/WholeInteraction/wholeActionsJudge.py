# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: wholeActionsJudge.py
@time: 2018/5/25 15:10
"""
# from CenterBackground.InteractionActions import WholeInteraction
from CenterBackground.InteractionActions import InteractionCoexistence
from tools.screeningdrop import ScreeningDrop
import os

class WholeActionsJudge(InteractionCoexistence):
    # excle文档中case所在工作薄的名称
    MODEL_WORKBOOK_LABEL = '标签'
    MODEL_WORKBOOK_DATA = '数据'
    MODEL_WORKBOOK_EVENT = '交互'


    # 当前子目录在菜单下的所属位置
    FATHER_TAGS_LOCATION = "1"

    # 根据key值，读取modei文件下保存用例的存放位置
    MODEI_CASE_POSITION = "whole"

    # MYSQL_DF, LABLE_DF
    def __init__(self) -> '对象实例化时就直接解析yaml中的数据信息,方便之后直接使用':
        self.parseyaml_location()
        self.parseyaml_content()


