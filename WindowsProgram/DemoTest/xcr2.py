# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: xcr2.py
@time: 2018/7/5 23:37
@Entry Name:operating
"""
from tkinter import *                # get base widget set
gifts = {'card': 'Greeting card', 'flowers': 'Flowers', 'nastygram': 'Nastygram'}

class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text="Radio demos").pack(side=TOP)
        self.var = StringVar()
        for key in gifts:
            Radiobutton(self, text=key,
                              command=self.onPress,
                              variable=self.var,
                              value=key).pack(anchor=NW)
        self.var.set(key) # select last to start
        Button(self, text='State', command=self.report).pack(fill=X)

    def onPress(self):
        pick = self.var.get()
        print('you pressed', pick)
        print('result:', demos[pick]())

    def report(self):
        print(self.var.get())

if __name__ == '__main__': Demo().mainloop()
