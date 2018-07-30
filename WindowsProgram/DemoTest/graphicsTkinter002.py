# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: graphicsTkinter001.py
@time: 2018/5/17 21:37
@Entry Name:operating
"""
from tkinter import *
from tkinter.messagebox import showinfo

class MyGui(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        button = Button(self, text='press', command=self.reply())
        button.pack()
    def reply(self):
        showinfo(title='popup',message='Button GG')


if __name__ == '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()