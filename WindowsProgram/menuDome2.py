# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: NewMenuDome.py
@time: 2018/6/26 10:35
@Entry Name:operating
创建一个简易的菜单框，里面设置按钮
"""
from tkinter import *
from tkinter.messagebox import *
from WindowsProgram.makePopup import MakePopup
from WindowsProgram.InteractionProgram.loginEntry import LoginEntry
from WindowsProgram.InteractionProgram.selectWidgets import SelectWidgets
from WindowsProgram.MenuProgram.titleMenu import TitleMenu


class NewMenuDemo(MakePopup):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)  # 缺少这个之后，除菜单以外的书都不会显示
        self.createWidgets()
        self.systemglobal['NewMenuDemo'] = self
        self.master.title('标题测试框')
        self.master.iconname("图标名称")

    def createWidgets(self):
        TitleMenu().makeMenuBar()  # 设置菜单
        LoginEntry().makeEntryBar()  # 设置输入框
        SelectWidgets().makeWidgetsRadio()  # 设置下拉筛选框
