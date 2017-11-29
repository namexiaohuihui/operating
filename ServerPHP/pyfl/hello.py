# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: hello.py
@time: 2017/11/29 22:15
@项目名称:operating
"""

import urllib.request

url='http://www.baidu.com'
# Urllib的GET请求
response=urllib.request.Request(url=url)

html=urllib.request.urlopen(response)

print("getcode %s" % html.getcode())

print("headers %s" % html.headers)
