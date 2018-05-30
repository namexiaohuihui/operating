# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: __init__.py.py
@time: 2018/4/9 18:00
"""

"""
    def test_case01(self):
        assert 1 == 1, "tongguo "
        print("nihao")

    def test_case02(self):
        assert 1 == 2, "cuowuxinxi "

    def test_case03(self):
        assert k == 2, "cuowuxinxi "

"""
from PageWeb.WebShop.SystemSetup import SystemCoexistence


class DailyNotice(SystemCoexistence):

    # 当前子目录的所在位置
    TREEW_TAGS_LOCATION = "2"

    # 该目录下的用例在modei文件中所属的key值
    MODEI_CASE_POSITION = "dailybulletin"

