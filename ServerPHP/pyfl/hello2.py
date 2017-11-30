# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: hello.py
@time: 2017/11/29 22:15
@项目名称:operating
"""
# post请求
import urllib.request

import urllib.parse

url='http://www.tuling123.com/openapi/api'

data={"key": "your", "info": '你好'}
# Urllib的Post请求
data=urllib.parse.urlencode(data).encode('utf-8')

re=urllib.request.Request(url,data)

html=urllib.request.urlopen(re)

print(html.getcode(),html.msg)

print(html.read())
