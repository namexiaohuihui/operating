# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: quitter.py
@time: 2018/7/23 23:05
@Entry Name:operating
"""
from tkinter import *                          # get widget classes
from tkinter.messagebox import askokcancel     # get canned std dialog

class Quitter(Frame):                          # subclass our GUI
    def __init__(self, parent=None):           # constructor method
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(side=LEFT, expand=YES, fill=BOTH)

    def quit(self):
        ans = askokcancel('Verify exit', "Really quit?")
        if ans: Frame.quit(self)
        print("click --> %s" %ans)

if __name__ == '__main__':  Quitter().mainloop()