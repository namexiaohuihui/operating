# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: cityShowJudge.py
@time: 2018/5/24 16:20
"""
from PageWeb.WebShop.SystemSetup import SystemCoexistence
from PageWeb.WebShop.SystemSetup.CityDirectory.cityShowNames import CityShowNames

city_show = CityShowNames()


class CityShowJudge(SystemCoexistence):
    TREEW_TAGS_LOCATION = "4"

    def _rou_city_show(self):
        """
        进入日常公告页面
        :return:  暂时没有返回值
        """
        self._rou_system()
        pass
