# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: dialogTable.py
@time: 2018/7/23 22:59
@Entry Name:operating
"""
# define a name:callback demos table

from tkinter.filedialog   import askopenfilename        # get standard dialogs
from tkinter.colorchooser import askcolor               # they live in Lib\tkinter
from tkinter.messagebox   import askquestion, showerror
from tkinter.simpledialog import askfloat

demos = {
    'Open':  askopenfilename,
    'Color': askcolor,
    'Query': lambda: askquestion('Warning', 'You typed "rm *"\nConfirm?'),
    'Error': lambda: showerror('Error!', "He's dead, Jim"),
    'Input': lambda: askfloat('Entry', 'Enter credit card number')
}
