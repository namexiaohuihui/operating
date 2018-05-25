# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: categoryJudge.py
@time: 2018/5/24 16:33
"""
from PageWeb.WebShop.SystemSetup import SystemCoexistence
from PageWeb.WebShop.SystemSetup.CategoryDirectory.categoryNames import CategoryNames

category = CategoryNames()


class CategoryJudge(SystemCoexistence):
    TREEW_TAGS_LOCATION = "5"

    def _rou_category(self):
        """
        进入日常公告页面
        :return:  暂时没有返回值
        """
        self._rou_system()
        pass
