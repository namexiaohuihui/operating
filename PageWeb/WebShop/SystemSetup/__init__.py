# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: __init__.py.py
@time: 2018/1/23 9:55
"""

from PageWeb.WebShop import BackgroundCoexistence


class SystemCoexistence(BackgroundCoexistence):
    # 该菜单在所属目录的绝对位置
    SIDEBAR_TAGS_LOCATION = "9"

    # 该菜单的用例所处位置的总目录
    MODEI_KEY_POSITION = "systemsetup"

    def _rou_system(self):
        """
        进入日常公告页面
        :return:  暂时没有返回值
        """
        self.treew_tags = self.TREEW_TAGS_LOCATION
        self.sidebar_tags = self.SIDEBAR_TAGS_LOCATION
        self._rou_background()
        pass

    def content_header_title(self, basename) -> '临时函数到时候去除':
        sidebar_title = self._visible_css_selectop_text(self.sidebar)
        content_title = self._visible_css_selectop_text(self.content_header)
        print("%s 进入页面成功" % basename) if sidebar_title == content_title else print("%s 进入页面失败" % basename)

