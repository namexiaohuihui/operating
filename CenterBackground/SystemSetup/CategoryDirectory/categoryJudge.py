# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: categoryJudge.py
@time: 2018/5/24 16:33
"""
from CenterBackground.SystemSetup import SystemCoexistence
from CenterBackground.SystemSetup.CategoryDirectory.categoryNames import CategoryNames

category = CategoryNames()


class CategoryJudge(SystemCoexistence):
    FATHER_TAGS_LOCATION = "5"

    def _rou_category(self):
        """
        :return:  暂时没有返回值
        """
        self._rou_system()
        pass
