# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: entry.py
@time: 2018/7/3 22:20
@Entry Name:operating
https://blog.csdn.net/u014027051/article/details/53813152/ 事件绑定
文本输入框及获取
"""
from tkinter import *

fields = 'Name','Job','Pay'
def fetch(entries):
    for entrt in entries:
        print("Input -> %s " % entrt.get())

def makeform(root,ields):
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row,width=5,text = field)
        ent = Entry(row)
        row.pack(side=TOP,fill=X)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT,expand =YES,fill = X)
        entries.append(ent)
    return entries

if __name__ == '__main__':
    root = Tk()
    ents = makeform(root,fields)
    root.bind('<Return>',(lambda event:fetch(ents)))
    root.bind('<Double-1>',(lambda event:fetch(ents)))

    Button(root,text = 'Getch',command = (lambda :fetch(ents))).pack(side = LEFT)
    root.mainloop()
