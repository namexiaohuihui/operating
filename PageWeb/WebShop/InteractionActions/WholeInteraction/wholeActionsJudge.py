# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: wholeActionsJudge.py
@time: 2018/5/25 15:10
"""
from PageWeb.WebShop.SystemSetup import SystemCoexistence


class wholeActionsJudge(SystemCoexistence):
    TREEW_TAGS_LOCATION = "1"

    def _rou_brand(self):
        """
        进入日常公告页面
        :return:  暂时没有返回值
        """
        self._rou_interaction()
        pass
