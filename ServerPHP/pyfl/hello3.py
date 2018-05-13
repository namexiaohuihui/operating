# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: hello.py
@time: 2017/11/29 22:15
@项目名称:operating
"""

import urllib.request
import types
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
import time
from collections import namedtuple

class user_class(object):
    args = {}
    date = ""
    files = ""
    form = {}
    headers = {}
    json = ""
    origin = ""
    url = ""


import json
class kk ():
    def obj_test(self, result, obj):
        data_list = []
        for res in result:
            # 定义存储对象
            test = obj
            # 定义字典
            dictionaries = {}
            # 将数据转换成json
            jsondatar = json.dumps(res, ensure_ascii=False)
            # dumps的模块可以把特定的对象序列化处理为字符串
            # loads反序列化把这2个字符串转换成list和dict
            rebuild = json.loads(jsondatar)
            print(" rebuild %s" % rebuild)
            test.__dict__ = rebuild
            dictionaries[test.key] = test
            print(" test %s" % test )
            print(" test.id %s" % test.key )
            data_list.append(dictionaries)
        return data_list;

    def wori(self):
        url = 'http://www.baidu.com'

        r = requests.get(url)

        print(r.headers)  # 打印运行信息
        print(r.elapsed.microseconds)  # 打印运行时间

        payload = {'key1': 'value1', 'key2': 'value2'}
        r = requests.post("http://httpbin.org/post", data=payload)
        # print(r.text)
        s = kk()
        time.sleep(2)
        # date = {"key": "your", "info": '你好'}
        date = r.text

        # print(s.obj_test(date, qu()))
        test = user_class()
        dictionaries = {}
        jsondatar = json.dumps(date, ensure_ascii=False)
        rebuild = json.loads(jsondatar)
        print(" rebuild %s" % rebuild)
        time.sleep(2)
        test.__dict__ = rebuild
        dictionaries[test.key] = test
        print(" test %s" % test)
        print(" test.id %s" % test.key)
        print(" --------------------------------------")
        print('\n'.join(['%s:%s' % item for item in test.__dict__.items()]))

    def zailai(self):
        date = {"kk": "11kk", "ll": {"qw11": "qw111", "qwe": "123"}}
        for key, valus in date.items():
            print('{k}:{v}'.format(k=key, v=valus))
            # print('\n'.join(['%s:%s' % item for item in valus.__dict__.items()]))
            print(type(valus))
            if type(valus) == dict:
                for key, valuss in valus.items():
                    print("--------------")
                    print('{k}:{v}'.format(k=key, v=valuss))
                print("*******************")
            elif type(valus) == str:
                print("+++++++++++++++++")
            else:
                print("/*-")

    def douban(self):
        url = "https://api.douban.com/v2/book/1220562"
        response = urllib.request.Request(url=url)
        html = urllib.request.urlopen(response)
        date = json.loads(html.read())
        print("read %s" % date["rating"])

    def yijianzhuanhguan(self):
        data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
        kk = qu()
        # Parse JSON into an object with attributes corresponding to dict keys.
        x = json.loads(data, object_hook=lambda d: namedtuple('date', d.keys())(*d.values()))
        print(x.name)
        print(x.hometown)

    def _json_object_hook(self,d):
        return namedtuple('X', d.keys())(*d.values())

    def json2obj(self,data):
        return json.loads(data, object_hook=_json_object_hook)
class qu():
    name = ""
    hometown = {}

if __name__ == '__main__':
    data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
    dalaoe = kk()
    print(dalaoe.json2obj(data))