# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: simpleedit.py
@time: 2018/7/28 19:52
@Entry Name:operating
"""


from tkinter import *

class ScrolledList(Frame):
    def __init__(self, options, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)                   # make me expandable
        self.makeWidgets(options)

    def handleList(self, event):
        index = self.listbox.curselection()                # on list double-click
        label = self.listbox.get(index)                    # fetch selection text 等于 self.listbox.get('active')
        self.runCommand(label)                             # and call action here
                                                           # or get(ACTIVE)
    def makeWidgets(self, options):
        vscroll = Scrollbar(self)
        hscroll = Scrollbar(self,orient='horizontal')
        list = Listbox(self)

        vscroll.config(command=list.yview,relief=SUNKEN)                                      # 设置界面数据信息
        hscroll.config(command=list.xview,relief=SUNKEN)
        # 设置界面数据信息
        list.config(yscrollcommand=vscroll.set,relief=SUNKEN)               # vscroll和list绑定关系 other,selectmode设置listbox是否可以多选
        list.config(xscrollcommand=hscroll.set)               # sbar和list绑定关系 other,selectmode设置listbox是否可以多选

        vscroll.pack(side=RIGHT, fill=Y)                                        # pack first=clip last
        hscroll.pack(side=BOTTOM, fill=X)                                        # pack first=clip last
        list.pack(side=LEFT, expand=YES, fill=BOTH)

        # list clipped first
        pos = 0
        for label in options:                              # add to listbox
            list.insert(pos, label)                        # or insert(END,label)
            pos += 1                                       # or enumerate(options)
       #list.config(selectmode=SINGLE, setgrid=1)          # select,resize modes
        list.bind('<Double-1>', self.handleList)           # set event handler
        self.listbox = list

    def runCommand(self, selection):                       # redefine me lower
        print('You selected:', selection)

if __name__ == '__main__':
    options = (('----------------------------Lumberjack-%s' % x) for  x in range(20))  # or map/lambda, [...]
    ScrolledList(options).mainloop()
