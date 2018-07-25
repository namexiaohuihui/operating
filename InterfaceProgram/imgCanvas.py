# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: imgCanvas.py
@time: 2018/7/25 21:57
@Entry Name:operating
"""
import os
gifdir = "../gifs/"
from sys import argv
from tkinter import *
# python imgCanvas.py 日记.png
CUR_PATH = os.path.dirname(os.path.realpath(__file__))
print(argv)
filename = argv[1] if len(argv) > 1 else '开关.png'   # name on cmdline?
case_path = os.path.join(os.path.join(CUR_PATH, 'gifs'), filename)

win = Tk()
img = PhotoImage(file=case_path)
can = Canvas(win)
can.pack(fill=BOTH)
can.config(width=img.width(), height=img.height())        # size to img size
can.create_image(2, 2, image=img, anchor=NW)
win.mainloop()
class ImgCanvas(object):
    pass