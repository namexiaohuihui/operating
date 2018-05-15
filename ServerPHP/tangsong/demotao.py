# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: demotao.py
@time: 2018/5/13 22:13
@Entry Name:operating
"""
import requests
import json
# link = "http://admin2.t-lianni.com"
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}
# r = requests.get(link, params=headers)
#
# r = requests.get('http://httpbin.org/get', timeout=5, params=keys_dict)
# print(r.url)
# print(r.text)
keysss = {
    'username': '--',
    'password': '123456'
}
r = requests.post('http://---/login', data=keysss)
print(r.url)
text_neirong = json.loads(r.text)
print(text_neirong)
print(r.apparent_encoding)
print("----------------------")
