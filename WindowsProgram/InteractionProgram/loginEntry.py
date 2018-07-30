# -*- coding: utf-8 -*-
'''
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  -  /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                        `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

               佛祖保佑         永无BUG
@author: 70486
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file: loginEntry.py
@time: 2018/7/30 11:51
@desc:
'''
from tkinter import *
from WindowsProgram.makePopup import MakePopup


class LoginEntry(MakePopup):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)  # 缺少这个之后，除菜单以外的书都不会显示
        self.systemglobal['LoginEntry'] = self
        pass

    def makeEntryBar(self):
        self.entrie = {}
        entry = Frame(self)
        entry.pack(side=BOTTOM, fill=X)
        for field in self.filedas:
            row = Frame(entry, cursor='hand2', relief=SUNKEN, bd=2)
            lab = Label(row, width=8, text=field)
            ent = Entry(row)
            row.pack(side=TOP, fill=X)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            # self.entrie.append(lab)
            self.entrie[field] = ent
        # self.bind('<Return>', (lambda event: self.sendGift(self.entrie))) # 绑定键盘事件，这句没什么用先隐藏
