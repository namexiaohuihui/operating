# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: hello.py
@time: 2017/11/29 22:15
@项目名称:operating
"""

import urllib.request

import urllib.parse
# requests库的http请求、
"""
　①get请求：requests.get(‘url‘) 
　　②post请求：requests.post("url/post")
　　③put请求：requests.put("url/put")
　　④delete请求：requests.delete("url/delete")
　　⑤head请求：requests.head("url/get")
　　⑥options请求：requests.options("url/get")
"""
import requests

url='http://www.baidu.com'

r = requests.get(url)

print(r.headers)
print(r.elapsed.microseconds) # 打印运行时间


payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)
