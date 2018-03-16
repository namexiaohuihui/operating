# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: __init__.py.py
@time: 2017/12/20 23:03
@项目名称:operating
"""
class nihao(object):
    global x
    x = 79
    def xx(self):
        return x
    def yy(self):
        return x

class nibuhao(object):
    x = 79
    def xx(self):
        return self.x

    def yy(self):
        return self.x

if __name__ == '__main__':
    ni=nihao()
    print(ni.xx())
    print(ni.yy())
    bu = nibuhao()
    print(bu.xx())
    print(bu.yy())