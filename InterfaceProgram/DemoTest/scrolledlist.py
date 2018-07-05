# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: scrolledlist.py
@time: 2018/7/5 22:57
@Entry Name:operating
"""
from tkinter import *
from tkinter import ttk
class ScrolledList(Frame):

    def __init__(self,options,parent = None):
        Frame.__init__(self,parent)
        self.pack(expand =YES,fill=BOTH)
        self.makeWidgets(options)

        Label(self,text="Radio demos").pack(side =TOP)
        # gift = StringVar()
        # Radiobutton(self, text='Greeting', variable=gift, value='card').pack(anchor=NW)
        # Radiobutton(self, text='Flowers', variable=gift, value='flowers').pack(anchor=NW)
        # Radiobutton(self, text='Nastygram', variable=gift, value='nastygram').pack(anchor=NW)
        # gift.set('Greeting')
        gifts = {'card': 'Greeting card', 'flowers': 'Flowers', 'nastygram': 'Nastygram'}
        self.var = StringVar()
        for key in gifts:
            Radiobutton(self,text=key,command=self.onPress,
                        variable=self.var,
                        value=key).pack(anchor=NW)
        self.var.set(' ') # 不设置默认值时，鼠标通过单选框时，会全部都自动选择

    def onPress(self):
        print(self.var.get())

    def handleList(self,event):
        index = self.listbox.curselection()
        label = self.listbox.get(index)
        self.runCommand(label)
        pass
    def makeWidgets(self,options):
        sbar = Scrollbar(self) # 不传入self会出现下拉框异常的情况s
        list = Listbox(self,relief=SUNKEN)
        sbar.config(command=list.yview)
        list.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT,fill=Y)
        list.pack(side=LEFT,expand=YES,fill=BOTH)
        pos = 0
        for label in options:
            list.insert(pos,label)
            pos += 1
            pass
        list.bind("<Double-1>",self.handleList)
        self.listbox = list
        pass
    def runCommand(self,selection):
        print('You selected',selection)
        pass

if __name__ == '__main__':
    options = (('Lumberjack-%s'%x) for x in range(20))
    ScrolledList(options).mainloop()