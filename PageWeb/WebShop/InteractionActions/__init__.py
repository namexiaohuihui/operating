# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: __init__.py.py
@time: 2018/5/24 16:49
"""

from PageWeb.WebShop import BackgroundCoexistence


class InteractionCoexistence(BackgroundCoexistence):
    SIDEBAR_TAGS_LOCATION = "1"

    def _rou_interaction(self):
        """
        进入日常公告页面
        :return:  暂时没有返回值
        """
        self.treew_tags = self.TREEW_TAGS_LOCATION
        self.sidebar_tags = self.SIDEBAR_TAGS_LOCATION
        self._rou_background()
        pass
