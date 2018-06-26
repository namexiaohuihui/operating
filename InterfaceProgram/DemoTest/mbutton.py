# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: mbutton.py
@time: 2018/6/20 10:32
@Entry Name:operating
将菜单写到按钮上
"""
from tkinter import *
root = Tk()
mbutton = Menubutton(root,text = 'Food')
pickl = Menu(mbutton)
mbutton.config(menu = pickl)

pickl.add_command(label = 'spam',command = root.quit)
pickl.add_command(label = 'eggs',command = root.quit)
pickl.add_command(label = 'bacon',command = root.quit)

mbutton.pack()
mbutton.config(bg = 'white',bd = 4,relief = RAISED)
root.mainloop()