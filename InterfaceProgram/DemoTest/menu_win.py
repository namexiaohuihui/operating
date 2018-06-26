# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: menu_win.py
@time: 2018/6/13 22:01
@Entry Name:operating
使用menu来创建菜单
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
    showwarning("什么？？", "哈哈 %s " % list(demos_win[demo]()))

def makemenu(win):
    top =Menu(win) # 设置菜单归属于这个窗口。 win = top-level window
    win.config(menu=top) # set its menu option
    file=Menu(top)
    file.add_command(label='New...',command=notdone,underline = 0)
    file.add_command(label='Open...',command=zheshitaochaugn,underline = 0)
    file.add_command(label='Quit...',command=win.quit,underline = 0)
    top.add_cascade(label='File',menu=file,underline=0)
    # tearoff设置该菜单是否可以独立运行，默认为True。true为允许
    edit = Menu(top,tearoff=False)
    edit.add_command(label='Cut.....', command=notdone, underline=0)
    edit.add_command(label='Paste.....', command=notdone, underline=0)
    edit.add_separator() # 添加分隔符
    top.add_cascade(label='shabi', menu=edit, underline=0)

    submenu = Menu(edit,tearoff =True)
    submenu.add_command(label='Spam',command = win.quit,underline = 0)
    submenu.add_command(label='Eggs',command = notdone,underline = 0)
    edit.add_cascade(label='Stuff', menu=submenu, underline=0)

    dialog = Menu(top, tearoff=False)
    for key in demos_win:
        funcc = (lambda handler = showjinggao,name = key : handler(name))
        dialog.add_command(label=key, command=funcc, underline=0)
    top.add_cascade(label='taocan', menu=dialog, underline=0)
def setBgColor():
    (triple,hexstr) = askcolor()
    if hexstr:
        print(hexstr)

        push.config(bg=hexstr)
if __name__ == '__main__':
    print("1-----------------------1")
    root = Tk() # 创建菜单窗口，or Toplevel()
    root.title('menu-win') # 设置标题 set window-mgr info
    makemenu(root)
    print("2-----------------------1")
    msg = Label(root,text='Window menu basics')
    msg.pack(expand =YES,fill = BOTH)
    msg.config(relief=SUNKEN,width = 40,height = 7,bg = 'beige')
    print("3-----------------------1")
    # global push
    push = Button(msg,text = 'Set Background Color',command = setBgColor)
    push.config(height = 3,font=('items',20,'bold'))
    # global push均匀分配给其他组件,fill对齐方式
    push.pack(side=TOP)
    # push.pack(side=TOP,expand=YES,fill=BOTH)
    root.mainloop()
    print("4-----------------------1")