# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: testa.py
@time: 2017/7/13 16:18
"""
from py_mysql.pymysql_main import pymysqls

pm = pymysqls.__new__(pymysqls)
#pm.connects()
#pm.cureors()
pm.connects_cureors('host',3306,'user','pass','db','charset')
sql = "SELECT * FROM table WHERE phone = %s;"
data = ('--')
pm.selects(sql,data)
