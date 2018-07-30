# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: __init__.py.py
@time: 2017/10/23 22:55
@项目名称:operating
"""
from CenterBackground.judgmentVerification import JudgmentVerification
from tools.extendBeantifulSoup import ExtendBeantifulSoup
import time

class BackgroundCoexistence(JudgmentVerification):
    # 设置菜单字目录上的标题
    content_header = ".content-header > h1"

    # -------------------------定义主菜单的所在位置------------------------
    def set_sidebar_number(self, number: int) -> "通过number定义子菜单的所在位置":
        self.sidebar = ".sidebar-menu>li:nth-child(%s)>.dropdown-toggle" % number

    def sidebar_number_get(self) -> "获取子菜单的所在位置":
        return self.sidebar

    # -------------------通过第三方参数来设置或者读取主菜单的位置-------------
    sidebar_tags = property(sidebar_number_get, set_sidebar_number, doc="Setting an error or getting the main menu.")

    # -------------------------定义子菜单的所在位置------------------------
    def set_treeview_number(self, number: int) -> "通过number定义子菜单的所在位置":
        self.treew = ".treeview-menu.menu-open>li:nth-child(%s)" % number

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

    def tbody_td_data(self, content, button_next, title_key):
        '''
        爬取数据展示栏的内容，可翻页爬取
        :param content: 数据所在页面中的位置
        :param button_next: 翻页按钮的位置
        :param title_key: df序列号数据设置项
        :return:
        '''
        # 1.定义爬虫对象
        ebs = ExtendBeantifulSoup(self.driver, content)
        soup_list = []
        # 2.循环读取页面数据
        while True:  # 先进入页面读取数据，然后判断下一页按钮是否存在，存在就点击。不存在就跳过 ---->不严谨
            # 获取界面数据并将标签为tbody的数据切割出来
            cutting = ebs.lable_table_parsing('tbody')
            soup_list.append(cutting)
            if self._visible_css_selectop(button_next):
                pass
            else:
                break

        # 3.将页面数据进行爬取
        for tags in soup_list:
            ebs.lable_cutting_tags(tags, "td")
        # 4.获取df数据标题
        ebs.daily = self.get_order_title(self.names_key.yaml_orderkey())

        # 5.将数据转换成df
        df = ebs.interfaceToPandas()

        if type(df) != int:
            # 6.重新设置序列号
            df = df.set_index([list(df[title_key])])
            # print("页面数据不为空")
        else:
            print("页面数据为空")
            pass
        return df

    def parsing_tbody(self, content, button_next, operation):
        # 获取页面全部数据
        self.LABLE_DF = self.tbody_td_data(content, button_next, "#订单编号")
        if type(self.LABLE_DF) is int:
            print("我就可以再来一次空吧")
        else:
            # 将空格全部去除
            list_operation = self.LABLE_DF[operation]
            list_operation = list(map(lambda x: x.replace(' ', ''), list_operation))
            self.LABLE_DF[operation] = list_operation