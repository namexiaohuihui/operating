# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: navigationSteps.py
@time: 2018/5/24 15:58
"""
from PageWeb.WebShop.SystemSetup import SystemCoexistence
from PageWeb.WebShop.SystemSetup.NavigationDirectory.navigationNames import NavigationNames

naviga = NavigationNames()


class NavigationSteps(SystemCoexistence):
    TREEW_TAGS_LOCATION = "3"

    def _rou_navigation(self):
        """
        进入日常公告页面
        :return:  暂时没有返回值
        """
        self._rou_system()
        pass
