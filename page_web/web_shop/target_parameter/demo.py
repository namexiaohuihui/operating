# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: demo.py
@time: 2017/12/19 17:02
"""
from practical.py_mysql.pymysql_main import pymysqls

class DictObj(object):
    def __init__(self,map):
        self.map = map

    def __setattr__(self, name, value):
        if name == 'map':
             object.__setattr__(self, name, value)
             return;
        print ('set attr called ',name,value)
        self.map[name] = value

    def __getattr__(self,name):
        v = self.map[name]
        if isinstance(v,(dict)):
            return DictObj(v)
        if isinstance(v, (list)):
            r = []
            for i in v:
                r.append(DictObj(i))
            return r
        else:
            return self.map[name];

    def __getitem__(self,name):
        return self.map[name]

if __name__ == '__main__':
    print("11")
    pm = pymysqls.__new__(pymysqls)
    # pm.connects_cureors('localhost', 3306, 'root', 'xiaodingdong', 'ph_exclusive', 'utf8')
    pm.connects_cureors('load', 3306, 'root', 'xiaodingdong', 'table', 'utf8')
    sql = ""

    result = pm.selects(sql)

    import json
    for res in result:
        print("******************************************")
        book = DictObj(res);
        print('\n'.join(['%s:%s' % item for item in book.__dict__.items()]))