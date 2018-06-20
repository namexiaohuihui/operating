# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: optionmenu.py
@time: 2018/6/20 10:38
@Entry Name:operating
"""
from tkinter import  *
root = Tk()

var1 = StringVar()
var2 = StringVar()
shenme = ('guilao1','zhishenm','haha','shen')
opt1 = OptionMenu(root,var1,'eggs','toast','guilao1','zhishenm','haha','shen')
opt2 = OptionMenu(root,var2,'bacon','sausage')
for value in shenme:
    opt2.value = value
opt1.pack(fill = X)
opt2.pack(fill = X)

var1.set('span')
var2.set('han')
def state():
    print(var1.get(),var2.get())
Button(root,command = state , text = 'state').pack()
root.mainloop()