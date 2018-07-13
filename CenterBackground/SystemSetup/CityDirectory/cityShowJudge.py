# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: cityShowJudge.py
@time: 2018/5/24 16:20
"""
from CenterBackground.SystemSetup import SystemCoexistence
from CenterBackground.SystemSetup.CityDirectory.cityShowNames import CityShowNames

city_show = CityShowNames()


class CityShowJudge(SystemCoexistence):
    TREEW_TAGS_LOCATION = "4"

    def _rou_city_show(self):
        """
        :return:  暂时没有返回值
        """
        self._rou_system()
        pass
