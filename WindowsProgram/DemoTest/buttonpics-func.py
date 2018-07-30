# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: buttonpics-func.py
@time: 2018/7/25 22:12
@Entry Name:operating
"""
import os
from tkinter import *                # get base widget set
from glob import glob                # 遍历目录下面的全部文件
import demoCheck                     # attach checkbutton demo to me
import random                        # pick a picture at random
CUR_PATH = os.path.dirname(os.path.realpath(__file__))
# gifdir = r'E:\operating\WindowsProgram\DemoTest\gifs'                  # where to look for GIF files
case_path = os.path.join(os.path.join(CUR_PATH, 'gifs'), "*.png")
def draw():
    name, photo = random.choice(images)
    print(images)
    print(name)
    print(photo)
    lbl.config(text=name)
    pix.config(image=photo)

root=Tk()
lbl = Label(root,  text="none", bg='blue', fg='red')
pix = Button(root, text="Press me", command=draw, bg='white')
lbl.pack(fill=BOTH)
pix.pack(pady=10)
demoCheck.Demo(root, relief=SUNKEN, bd=2).pack(fill=BOTH)
print(case_path)
files = glob(case_path)                              # GIFs for now
images = [(x, PhotoImage(file=x)) for x in files]           # load and hold
print(files)
root.mainloop()
