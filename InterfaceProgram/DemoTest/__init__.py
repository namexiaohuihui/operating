# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: __init__.py.py
@time: 2018/6/13 21:02
@Entry Name:operating
"""
a = 10
b = 20
# 不需要中间变量，一步搞定
a, b = b, a
print(a,b)