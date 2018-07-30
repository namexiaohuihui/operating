# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: demoCheck.py
@time: 2018/7/23 23:00
@Entry Name:operating
"""
from tkinter import *
from WindowsProgram.DemoTest.dialogTable import demos
from WindowsProgram.DemoTest.quitter import Quitter
class Demo(Frame):
    def __init__(self,parent = None,**options):
        Frame.__init__(self,parent,**options)
        self.pack()
        self.tools()
        Label(self,text = 'Check demos').pack()
        self.vars = []
        for key in demos:
            var = IntVar()
            Checkbutton(self,text = key,variable = var,command = demos[key]).pack(side=LEFT)
            self.vars.append(var)
        pass
    def report(self):
        for var in self.vars:
            # 当前开关设置 1 或者 0.
            # 1表示选中，0表示未选中
            print(var.get(),end = ' ' )
        print()
        pass
    def tools(self):
        frm = Frame(self)
        frm.pack(side = RIGHT)
        Button(frm,text = 'Statte' , command = self.report).pack(fill = X)
        Quitter(frm).pack(fill = X)
        pass


if __name__ == '__main__':
    Demo().mainloop()
