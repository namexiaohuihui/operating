# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: NewMenuDome.py
@time: 2018/6/26 10:35
@Entry Name:operating
创建一个简易的菜单框，里面设置按钮
"""
import os
from tkinter import *
from tkinter.messagebox import *

countrycodes = ('lnlife', 'lnlife1', 'lnlif2', 'lnlife3')
countrynames = ('203', '204')
filedas = ('Linuxuser', 'Linuxpass')


class NewMenuDemo(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)  # 缺少这个之后，除菜单以外的书都不会显示
        self.createWidgets()
        self.master.title('标题测试框')
        self.master.iconname("图标名称")

    def createWidgets(self):
        self.makeMenuBar()  # 设置菜单
        self.makeToolBar()  # 设置底部操作按钮
        self.makeEntryBar()  # 设置输入框
        self.makeWidgets()  # 设置下拉筛选框
        self.makeRadio()  # 设置单选按钮
        self.makeTexts()  # 设置显示的文本内容

    def sendGift(self, *args):
        idxs = self.lbox.curselection()
        print('环境',idxs)
        if len(idxs) == 1: # 判断是否选择环境
            idx = int(idxs[0])
            self.lbox.see(idx)
            name = countrynames[idx]
            code = str.strip(self.var.get()) # 判断是否选择lnlife
            print('目录',code)
            if code != '':
                username = self.entrie[filedas[0]]
                password = self.entrie[filedas[1]]
                print("账号密码:",username.get(),password.get())
                if username.get() and password.get():
                    self.promptInformation("The user is logged in.")
                else:
                    self.promptInformation("Please enter your account password.")
            else:
                self.promptInformation("Please check the directory you are in.")
        else:
            self.promptInformation("The environment has no choice.")

    def showPopulation(self, *args):
        '''
        单击ListboxSelect该动作
        :param args:
        :return:
        '''
        idxs = self.lbox.curselection()
        if len(idxs) == 1:
            idx = int(idxs[0])
            population = countrynames[idx]
            self.statusmsg.set("The population of %s " % population)
        self.sentmsg.set('')

    def makeTexts(self):
        self.sentmsg = StringVar()
        self.statusmsg = StringVar()
        'W代表西(west),E代表东(east),S代表南(south),N代表北(north)'
        status = Label(self, background='yellow', textvariable=self.statusmsg, anchor='center')
        sentlbl = Label(self, height=2, width=35, textvariable=self.sentmsg, foreground='red')
        status.pack(side=TOP)
        sentlbl.pack(side=TOP)
        self.sentmsg.set('')
        self.statusmsg.set('')
        self.showPopulation()

    def makeRadio(self):
        Label(self, text="Radio demos").pack(side=TOP)

        self.var = StringVar()
        for key in countrycodes:
            Radiobutton(self, text=key, command=self.onPress,
                        variable=self.var,
                        value=key).pack(anchor=W)
        self.var.set(' ')  # 不设置默认值时，鼠标通过单选框时，会全部都自动选择
        # 单击ListboxSelect触发事件
        self.lbox.bind('<<ListboxSelect>>', self.showPopulation)
        # 双击ListboxSelect触发事件，
        # self.lbox.bind('<Double-1>', self.sendGift)

    def makeWidgets(self):
        cnames = StringVar(value=countrynames)
        self.lbox = Listbox(self, listvariable=cnames, height=5)
        sbar = Scrollbar(self)  # 列表：下拉框不传入self会出现下拉框异常的情况
        sbar.config(command=self.lbox.yview)
        self.lbox.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        self.lbox.pack(side=RIGHT, expand=YES, fill=BOTH)
        for i in range(0, len(countrynames), 2):
            self.lbox.itemconfigure(i, background='#f0f0ff')
            self.lbox.selection_set(0)  # 默认选择项
        pass

    def makeEntryBar(self):
        self.entrie = {}
        nihao = Frame(self)
        nihao.pack(side=BOTTOM, fill=X)
        for field in filedas:
            row = Frame(nihao, cursor='hand2', relief=SUNKEN, bd=2)
            lab = Label(row, width=8, text=field)
            ent = Entry(row)
            row.pack(side=TOP, fill=X)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            # self.entrie.append(lab)
            self.entrie[field] = ent
        self.bind('<Return>', (lambda event: self.sendGift(self.entrie)))

    def makeToolBar(self):
        toolbar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
        toolbar.pack(side=BOTTOM, fill=X)
        Button(toolbar, text='Quit', command=self.menuQuit).pack(side=RIGHT)
        Button(toolbar, text='Hello', command=(lambda: self.sendGift(self.entrie))).pack(side=LEFT)

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

    def greeting(self):
        greeting('或得', '啥玩意')

    def notdone(self):
        notdone('没找到信息', '你这是干嘛')

    def menuQuit(self):
        if askyesno('确定退出', '你确定要退出吗?'):
            Frame().quit()


    def onPress(self):
        print('单选按钮为 : ',self.var.get())

    def promptInformation(self, msg):
        # 信息显示栏
        self.sentmsg.set(msg)


if __name__ == '__main__':
    root = Tk()
    NewMenuDemo(root).mainloop()  # TK运行必须调用该函数，不然不显示界面
    pass
