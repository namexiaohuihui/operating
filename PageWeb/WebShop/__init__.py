# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: __init__.py.py
@time: 2017/10/23 22:55
@项目名称:operating
"""
from PageWeb.WebShop.judgmentVerification import JudgmentVerification


class BackgroundCoexistence(JudgmentVerification):
    # 设置菜单字目录上的标题
    content_header = ".content-header > h1"

    # -------------------------定义主菜单的所在位置------------------------
    def set_sidebar_number(self, number: int) -> "通过number定义子菜单的所在位置":
        self.sidebar = ".sidebar-menu>li:nth-child(%s)>.dropdown-toggle" % number

    def sidebar_number_get(self) -> "获取子菜单的所在位置":
        return self.sidebar

    # -------------------通过第三方参数来设置或者读取子菜单的位置
    sidebar_tags = property(sidebar_number_get, set_sidebar_number, doc="Setting an error or getting the main menu.")

    # -------------------------定义子菜单的所在位置------------------------
    def set_treeview_number(self, number: int) -> "通过number定义子菜单的所在位置":
        self.treew = ".treeview-menu.menu-open li:nth-child(%s)" % number

    def treeview_number_get(self) -> "获取子菜单的所在位置":
        return self.treew

    # -------------------通过第三方参数来设置或者读取子菜单的位置
    treew_tags = property(treeview_number_get, set_treeview_number, doc="Error setting or getting subtags.")

    # -----------------进入目录路径----------------
    def _rou_background(self):
        """
        进入日常公告页面
        :return:  暂时没有返回值
        """
        self._visible_css_selectop(self.sidebar_tags)
        self._visible_css_selectop(self.treew_tags)
        pass
