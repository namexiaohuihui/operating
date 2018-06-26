# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: menu_frm.py
@time: 2018/6/19 21:50
@Entry Name:operating
菜单框
"""
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename # 系统该文件打开对话框
from tkinter.colorchooser import askcolor # 在Lib\tkinter中
from tkinter.simpledialog import askfloat

demos_win = {
    'Color':askcolor,
    'Query':lambda: askquestion('Warning','You typed "rm *" \n Confirm?'),
    'Erroe':lambda: showerror('Erroe!',"He~s dead, Jim"),
    'Input': lambda :askfloat('Entry','Enter credit card number')
}

def notdone():
    showerror('这是什么','不知道好像很高级')

def zheshitaochaugn():
    windonws = askopenfilename()
    showwarning("文件", "你打开的文件为 %s " % windonws)

def showjinggao(demo):
    # print("标题%s内容 %s " % (demo,demos_win[demo]()))
    showwarning("标题 : %s" % demo,demos_win[demo]())

def makemenu(parent):
    menubar =Frame(parent) # 设置菜单归属于这个窗口。 parent = top-level window
    menubar.pack(side = TOP,fill=X)

    fbutton = Menubutton(menubar,text = 'File',underline = 0)
    fbutton.pack(side=LEFT)

    file=Menu(fbutton)
    file.add_command(label='New...',command=notdone,underline = 0)
    file.add_command(label='Open...',command=zheshitaochaugn,underline = 0)
    file.add_command(label='Quit...',command=parent.quit,underline = 0)
    fbutton.config(menu = file)

    # tearoff设置该菜单是否可以独立运行，默认为True。true为允许
    ebutton = Menubutton(menubar, text='Edit', underline=0)
    ebutton.pack(side=LEFT)
    edit = Menu(ebutton,tearoff=False)
    edit.add_command(label='Cut.....', command=notdone, underline=0)
    edit.add_command(label='Paste.....', command=notdone, underline=0)
    edit.add_separator() # 添加分隔符
    ebutton.config(menu=edit) # 给菜单绑定下拉

    submenu = Menu(edit,tearoff =True)
    submenu.add_command(label='Spam',command = parent.quit,underline = 0)
    submenu.add_command(label='Eggs',command = notdone,underline = 0)
    edit.add_cascade(label='Stuff', menu=submenu, underline=0)

    dbutton = Menubutton(menubar, text='shibi', underline=0)
    dbutton.pack(side=LEFT)
    dialog = Menu(dbutton, tearoff=False)
    for key in demos_win:
        funcc = (lambda handler = showjinggao,name = key : handler(name))
        dialog.add_command(label=key, command=funcc, underline=0)
    # menubar.add_cascade(label='taocan', menu=dialog, underline=0)
    dbutton.config(menu=dialog)
    return menubar

if __name__ == '__main__':
    print("1-----------------------1")
    root = Tk() # 创建菜单窗口，or Toplevel()
    root.title('menu-frm') # 设置标题 set window-mgr info
    makemenu(root)
    print("2-----------------------1")
    msg = Label(root,text='Window menu basics')
    msg.pack(expand =YES,fill = BOTH)
    msg.config(relief=SUNKEN,width = 40,height = 7,bg = 'beige')
    print("3-----------------------1")
    root.mainloop()
    print("4-----------------------1")