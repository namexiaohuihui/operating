# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: peoplegui.py
@time: 2018/5/17 22:42
@Entry Name:operating
"""

from tkinter import *
from tkinter.messagebox import showerror
import shelve
shelvename = 'people-shelve'
fieldnames = ('name','age','job','pay')
entries = {}
def makeWidgets():
    # global entries
    window = Tk()
    window.title('查看数据库')
    form=Frame(window)
    form.pack()
    # entries = {}
    for (ix,label) in enumerate(('key',)+ fieldnames):
        print(ix,label)
        lab=Label(form,text=label)
        ent=Entry(form)
        lab.grid(row=ix,column=0)
        ent.grid(row=ix,column=1)
        entries[label] = ent
    Button(window,text='Fetch',command=fecthRecord).pack(side=LEFT)
    Button(window,text='Update',command=updateRecord).pack(side=LEFT)
    Button(window,text='Quit',command=window.quit).pack(side=RIGHT)
    return window

def fecthRecord():
    key = entries['key'].get()
    print("huoqu kye %s " % key)
    try:
        record=db[key]
        print(record,"neirong")
    except:
        showerror(title='Error',message='No such key')
    else:
        for field in fieldnames:
            print(field,'field')
            entries[field].delete(0,END)
            entries[field].insert(0,record[field])

def updateRecord():
    key = entries['key'].get()
    if key in db: # 判断当前的key是否存在db中
        record = db[key]
    else:
        record = ('Bob Smith',42,50000,'fasfas')
    print(record, "nihao")
    record = {'name' : 'Bob Smith' , 'age' : 42, 'pay' :3000 , 'job' :'dev'}
    for field in fieldnames:
        record[field] = entries[field].get()
    db[key] = record
    print("zuihou",record)

db = shelve.open(shelvename)
window = makeWidgets()
window.mainloop()
db.close()