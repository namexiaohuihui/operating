# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: hello.py
@time: 2017/11/29 22:15
@项目名称:operating
"""

# 序列化
import  json

dict1={'name':'雷子','age':24,'address':'北京'}

print (u'未序列化前的数据类型为:',type(dict1))
print (u'未序列化前的数据:',dict1)
#对dict1进行序列化的处理
str1=json.dumps(dict1)
print (u'序列化后的数据类型为:',type(str1))
print (u'序列化后的数据为:',str1)
#对str1进行反序列化
dict2=json.loads(str1)
print (u'反序列化后的数据类型:',type(dict2))
print (u'反序列化后的数据：',dict2)



import  json,requests

r=requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')

print (r.text,u'数据类型:',type(r.text))
#对数据进行反序列化的操作
dic=json.loads(r.text)
print (dic,u'数据类型:',type(dic))
str1=json.dumps(r.text)
print (str1,u'数据类型:',type(str1))