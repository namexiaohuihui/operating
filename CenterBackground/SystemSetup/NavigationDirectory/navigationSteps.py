# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: navigationSteps.py
@time: 2018/5/24 15:58
"""
from CenterBackground.SystemSetup import SystemCoexistence
from CenterBackground.SystemSetup.NavigationDirectory.navigationNames import NavigationNames

naviga = NavigationNames()


class NavigationSteps(SystemCoexistence):
    FATHER_TAGS_LOCATION = "3"

    def _rou_navigation(self):
        """
        :return:  暂时没有返回值
        """
        self._rou_system()
        pass
