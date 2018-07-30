# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: scrolledtext.py
@time: 2018/7/28 21:07
@Entry Name:operating
"""

print('PP4E scrolledtext')
from tkinter import *

class ScrolledText(Frame):
    def __init__(self, parent=None, text='', file=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)                 # make me expandable
        self.makewidgets()
        self.settext(text, file)

    def makewidgets(self):
        sbar = Scrollbar(self)
        text = Text(self, relief=SUNKEN)
        sbar.config(command=text.yview)                  # xlink sbar and text
        text.config(yscrollcommand=sbar.set)             # move one moves other
        sbar.pack(side=RIGHT, fill=Y)                    # pack first=clip last
        text.pack(side=LEFT, expand=YES, fill=BOTH)      # text clipped first
        self.text = text

    def settext(self, text='', file=None):
        if file:
            text = open(file, 'r').read()
        self.text.delete('1.0', END)                     # delete current text
        self.inserttext('1.0', text)                     # add at line 1, col 0
        self.text.mark_set(INSERT, '1.0')                # set insert cursor
        self.text.focus()                                # save user a click

    def gettext(self):                                   # returns a string
        return self.text.get('1.0', END+'-1c')           # first through last

    def inserttext(self,index : str ,text='', file=None):
        '''
        :param index:  从第index位置进行插入，例：66.33 ： 从66行第33列位置进行插入
        :param text:
        :param file:
        :return:
        '''
        if file:
            text = open(file, 'r').read()
        self.text.insert(index, text)                    # 指定位置插入数据，index诶字符串。点号前面为行后面为列

if __name__ == '__main__':
    root = Tk()
    if len(sys.argv) > 1:
        st = ScrolledText(file=sys.argv[1])              # filename on cmdline
    else:
        st = ScrolledText(file=r'C:\Users\70486\Desktop\9780596158118\PP4E-Examples-1.4\Examples\PP4E\Gui\Tour\scrolledtext.py')         # or not: two lines
        # st = ScrolledText(text='Words\ngo here')         # or not: two lines
    def show(event):
        print(repr(st.gettext()))                        # show as raw string
    root.bind('<Key-Escape>', show)                      # esc = dump text
    st.neizhifun()
    root.mainloop()
