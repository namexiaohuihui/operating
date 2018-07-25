# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: attachgui.py
@time: 2018/5/17 21:54
@Entry Name:operating
"""
import sys
print(sys.path)
from tkinter import *
from InterfaceProgram.DemoTest.graphicsTkinter002 import MyGui

# 应用主窗口
mainwin=Tk()
Label(mainwin,text=__name__).pack()

# 弹出窗口
popup = Toplevel()
Label(popup,text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()