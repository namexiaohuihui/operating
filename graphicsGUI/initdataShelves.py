# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: initdataShelves.py
@time: 2018/5/17 22:36
@Entry Name:operating
"""
import shelve

bob = {'name' : 'Bob Smith' , 'age' : 42, 'pay' :3000 , 'job' :'dev'}
sue = {'name' : 'Sue Jones' , 'age' : 45, 'pay' :4500 , 'job' :'hdw'}
tom = {'name' : 'Tom' , 'age' : 50, 'pay' :0 , 'job' :None}
db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()

