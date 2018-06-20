# -*- coding: utf-8 -*-
"""
@__author__ :DingDong
@file: menu_win-multi.py
@time: 2018/6/19 21:35
@Entry Name:operating
"""

from tkinter import  *
import sys
print(sys.path)
import os
#获取项目路径下的目录
os.chdir('E:\\operating')
#打印出项目路径下的目录
for file in os.listdir(os.getcwd()):
     print(file)
#将项目路径保存
sys.path.append('E:\\operating')
from InterfaceProgram.DemoTest.menu_win import makemenu
root = Tk()
for i in range(3):
    win = Toplevel(root)
    makemenu(win)
    Label(win,bg='black',height = 5,width = 25).pack(expand = YES ,fill = BOTH)
Button(root,text = "Bye",command = root.quit).pack()
root.mainloop()