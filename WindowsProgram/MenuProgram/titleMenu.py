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
@file: titleMenu.py
@time: 2018/7/30 10:30
@desc:
'''
import os
from tkinter import *
from tkinter.messagebox import *
from WindowsProgram.makePopup import MakePopup
class TitleMenu(MakePopup):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)  # 缺少这个之后，除菜单以外的书都不会显示
        self.systemglobal['TitleMenu'] = self

    def makeMenuBar(self):
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)
        self.fileMenu()
        self.editMenu()
        self.imageMenu()

    def fileMenu(self):
        pulldown = Menu(self.menubar)
        pulldown.add_command(label='OPen..', command=self.notdone)
        pulldown.add_command(label='Quit', command=self.menuQuit)
        self.menubar.add_cascade(label='File', underline=0, menu=pulldown)

    def editMenu(self):
        pulldown = Menu(self.menubar)
        pulldown.add_command(label='Paste', command=self.notdone)
        pulldown.add_command(label='Spam', command=self.greeting)

        pulldown.add_separator()  # 下划线

        pulldown.add_command(label='Delect', command=self.greeting)
        pulldown.entryconfig(4, state=DISABLED)  # 设置这个之后表明上一个添加的label无法点击
        self.menubar.add_cascade(label='Edit', underline=0, menu=pulldown)

    def imageMenu(self):
        '''
        PhotoImage对象被保存为列表，这与其他组件不同。
        如果不保存，内容就不复存在。（Python编程第八章有介绍）
        :return:
        '''
        # photoFiles = ('ameng.gif','fengc.gif')
        photoFiles = ('开关.png', '日记.png', '星球.png')
        pulldown = Menu(self.menubar)
        self.photoObjs = []
        CUR_PATH = os.path.dirname(os.path.realpath(__file__))
        for filename in photoFiles:
            case_path = os.path.join(os.path.join(CUR_PATH, 'gifs'), filename)
            img = PhotoImage(file=case_path)
            pulldown.add_command(image=img, command=self.notdone)
            self.photoObjs.append(img)
        self.menubar.add_cascade(label='Image', underline=0, menu=pulldown)

    # def greeting(self):
    #     builtSystem.greeting('或得', '啥玩意')
    #
    # def notdone(self):
    #     builtSystem.notdone('没找到信息', '你这是干嘛')
    #
    # def menuQuit(self):
    #     builtSystem.menuQuit()

if __name__ == '__main__':
    title = TitleMenu()
    title.makeMenuBar()
    title.mainloop()