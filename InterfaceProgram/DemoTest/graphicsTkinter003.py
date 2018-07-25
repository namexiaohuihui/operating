# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: graphicsTkinter001.py
@time: 2018/5/17 21:37
@Entry Name:operating
"""
from tkinter import *
from tkinter.messagebox import showinfo

def reply(name):
    showinfo(title='弹窗',message='你的名字： %s !' % name)

top = Tk()
top.title('账号登陆')
# top.iconbitma('1178420.gif')

Label(top,text='请输入你的名字 :').pack(side=TOP)

ent = Entry(top)
ent.pack(side=TOP)

btn = Button(top,text='登陆',command=lambda :reply(ent.get()))
btn.pack(side=TOP)

top.mainloop()
