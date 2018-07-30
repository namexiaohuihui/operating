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
@file: selectWidgets.py
@time: 2018/7/30 13:51
@desc:
'''
from tkinter import *
from tkinter import ttk
from WindowsProgram.makePopup import MakePopup



class SelectWidgets(MakePopup):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)  # 缺少这个之后，除菜单以外的书都不会显示
        self.systemglobal['SelectWidgets'] = self
        pass

    def makeWidgetsRadio(self):

        self.cnames = StringVar(value=self.countrynames)
        self.gift = StringVar()
        self.sentmsg = StringVar()
        self.statusmsg = StringVar()

        # Create and grid the outer content frame
        c = ttk.Frame(self, padding=(5, 5, 12, 0))
        c.grid(column=0, row=0, sticky=(N, W, E, S))
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create the different widgets; note the variables that many
        # of them are bound to, as well as the button callback.
        # Note we're using the StringVar() 'cnames', constructed from 'countrynames'
        self.lbox = Listbox(c, listvariable=self.cnames, height=5)
        lbl = ttk.Label(c, text="Send to country's leader:")
        row = 1
        for key in self.countrycodes:
            ttk.Radiobutton(c, text=key, command=self.onPress,
                        variable=self.gift,
                        value=key).grid(column=1, row=row, sticky=W, padx=20)
            row +=1
        send = ttk.Button(c, text='Send Gift', command=self.sendGift, default='active')
        self.sentlbl = ttk.Label(c, textvariable=self.sentmsg, anchor='center')
        self.status = ttk.Label(c, textvariable=self.statusmsg, anchor=W)

        # Grid all the widgets
        self.lbox.grid(column=0, row=0, rowspan=6, sticky=(N, S, E, W))
        lbl.grid(column=1, row=0, padx=10, pady=5)
        send.grid(column=2, row=4, sticky=E)
        self.sentlbl.grid(column=1, row=5, columnspan=2, sticky=N, pady=5, padx=5)
        self.status.grid(column=0, row=6, columnspan=2, sticky=(W, E))
        c.grid_columnconfigure(0, weight=1)
        c.grid_rowconfigure(5, weight=1)

        # Set event bindings for when the selection in the listbox changes,
        # when the user double clicks the list, and when they hit the Return key
        self.lbox.bind('<<ListboxSelect>>', self.showPopulation)
        self.lbox.bind('<Double-1>', self.sendGift)
        self.bind('<Return>', self.sendGift)

        # Colorize alternating lines of the listbox
        for i in range(0, len(self.countrynames), 2):
            self.lbox.itemconfigure(i, background='#f0f0ff')

        self.gift.set('card')
        self.sentmsg.set('')
        self.statusmsg.set('')
        self.lbox.selection_set(0)
        self.showPopulation()
        pass

    def showPopulation(self,*args):
        idxs = self.lbox.curselection()
        if len(idxs) == 1:
            idx = int(idxs[0])
            name = self.countrynames[idx]
            self.statusmsg.set("The population of %s (%s)" % (name,  self.gift.get()))
        self.sentmsg.set('')

    def sendGifts(self,*args):
        idxs = self.lbox.curselection()
        if len(idxs) == 1:
            idx = int(idxs[0])
            self.lbox.see(idx)
            # Gift sending left as an exercise to the reader
            if len(args) == 0:
                name = self.countrynames[idx]
                self.sentmsg.set("Sent %s to leader of %s" % (name,  self.gift.get()))
            if len(args) == 1:
                self.sentmsg.set(args[0])
            if len(args) == 2:
                self.sentmsg.set("LinuxUser %s and LinuxPass %s" % (args[0], args[1]))
