# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: brandJudge.py
@time: 2018/5/24 16:45
"""
from CenterBackground.SystemSetup import SystemCoexistence
from CenterBackground.SystemSetup.BrandDirectory.brandNames import BrandNames

brand = BrandNames()


class BrandJudge(SystemCoexistence):
    TREEW_TAGS_LOCATION = "6"

    def _rou_brand(self):
        """
        :return:  暂时没有返回值
        """
        self._rou_system()
        pass
