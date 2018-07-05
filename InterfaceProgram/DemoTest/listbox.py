# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: listbox.py
@time: 2018/7/5 22:05
@Entry Name:operating
"""
from tkinter import *
from tkinter import ttk

def sendGift(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        print(idxs)
        idx = int(idxs[0])
        print(idx)
        lbox.see(idx)
        # name = countrynames[idx]
        name = tnames[idx]
        # Gift sending left as an exercise to the reader
        print("Sent %s to leader of %s" % (gifts[gift.get()], name))

def showPopulation(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        code = countrycodes[idx]
        name = countrynames[idx]
        popn = populations[code]
        statusmsg.set("The population of %s (%s) is %d" % (name, code, popn))
    sentmsg.set('')

root = Tk()
root.geometry('+400+200')
root.minsize(400, 200)
root.title("test")

tnames = 'python', 'TCL', 'ruby'
cnames = StringVar()
lbox = Listbox(root, listvariable=cnames, height=10)
lbox.grid()
# lbox.bind('<<ListboxSelect>>', showPopulation)
# lbox.bind('<Double-1>', sendGift)
# ttk.Button(root, text="submit", command=changeItems).grid()
send = ttk.Button(root, text='Send Gift', command=sendGift, default='active').grid()

gift = StringVar()
c = ttk.Frame(root, padding=(5, 5, 12, 0))
gifts = { 'card':'Greeting card', 'flowers':'Flowers', 'nastygram':'Nastygram'}
g1 = ttk.Radiobutton(c, text=gifts['card'], variable=gift, value='card')
g2 = ttk.Radiobutton(c, text=gifts['flowers'], variable=gift, value='flowers')
g3 = ttk.Radiobutton(c, text=gifts['nastygram'], variable=gift, value='nastygram')
gift.set('card')
c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(5, weight=1)
g1.grid(column=1, row=1, sticky=W, padx=20)
g2.grid(column=1, row=2, sticky=W, padx=20)
g3.grid(column=1, row=3, sticky=W, padx=20)
c.grid(column=0, row=0, sticky=(S))
cnames.set(tnames)
root.mainloop()