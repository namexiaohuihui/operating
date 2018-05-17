# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: graphicsTkinter001.py
@time: 2018/5/17 21:37
@Entry Name:operating
"""
from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title='popup',message='Button GG')


window = Tk()
button = Button(window,text='press',command=reply())
button.pack()
window.mainloop()