# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: demoThereThereOne.py
@time: 2018/5/13 22:36
@Entry Name:operating
"""
import requests
import pprint
keys_dict = {'key1':'value1','key2':'value2'}
r=requests.get('http://httpbin.org/get',timeout = 5,params=keys_dict)
print(r.url)
print(r.text)

r=requests.post('http://httpbin.org/post',data=keys_dict)
pprint.pprint(r.text)
