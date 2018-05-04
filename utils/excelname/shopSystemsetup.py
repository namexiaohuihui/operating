# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: shopSystemsetup.py
@time: 2018/4/13 14:13
"""
from utils.excelname.excelBeanName import ExcelTitle

class ShopParameterSetting(ExcelTitle):
    """
    参数设置页面，优惠设置项的用例标题
    """
    def WithExtract(self):
        return "提现"

    def WithCost(self):
        return "手续费"

    def Countgoodsdiscount(self):
        return "商品折扣"

    def CountGoodsChoice(self):
        return "商品选择框"

    def CountGoodsId(self):
        return "不参与商品"

    def CountWatikiChoice(self):
        return "水票选择框"

    def CountWatikiDiscount(self):
        return "水票折扣"

    def CountWatikisId(self):
        return "不参与水票"

    def CountWatikisMax(self):
        return "最高抵扣"

class ShopNoticeController(ExcelTitle):
    """
        参数设置页面，公告设置项的标题
    """
    def dailyCity(self):
        return "城市"

    def dailyTitle(self):
        return "状态"

    def dailyContent(self):
        return "内容"

    def dailyDeadline(self):
        return "有限期"

    def dailySqlTwo(self):
        return "sql2"
