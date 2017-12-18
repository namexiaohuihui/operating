# -*- coding: utf-8 -*-

from practical.py_mysql.pymysql_main import pymysqls

__author__ = 'Administrator'
"""
@file: __init__.py.py
@time: 2017/12/18 11:29
"""

class ParameterContent:
    def __init__(self, parameter, content, *args, **kwargs):
        self.parameter = parameter
        self.content = content

    # to_json和from_json将传入的数据序列化处理之后，已对象的形式返回
    def to_json(self):
        # 序列化对象
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        # 反序列化对象
        json_dict = json.loads(json_str)
        return cls(**json_dict)

    # 创建对象。。并返回
    def object_decoder(self, obj):
        if '__type__' in obj and obj['__type__'] == 'ParameterContent':
            return ParameterContent(obj["parameter"], obj["content"])
        return obj

def obj_test(result,obj):
    data_list = []
    for res in result:
        test = obj
        dictionaries = {}
        jsondatar = json.dumps(res, ensure_ascii=False)
        rebuild = json.loads(jsondatar)
        test.__dict__ = rebuild
        dictionaries[test.id] = test
        data_list.append(dictionaries)
    return data_list;
import time

class DictObj(object):
    def __init__(self,map):
        self.map = map

    def __setattr__(self, name, value):
        if name == 'map':
             object.__setattr__(self, name, value)
             return;
        print ('set attr called ',name,value)
        self.map[name] = value

    def __getattr__(self,name):
        v = self.map[name]
        if isinstance(v,(dict)):
            return DictObj(v)
        if isinstance(v, (list)):
            r = []
            for i in v:
                r.append(DictObj(i))
            return r
        else:
            return self.map[name];

    def __getitem__(self,name):
        return self.map[name]

pm = pymysqls.__new__(pymysqls)
pm.connects_cureors('load', 3306, 'root', '123', 'table', 'utf8')
# pm.connects_cureors('load', 3306, 'root', '123', 'table', 'utf8')
sql = "SELECT a.*," \
      "CASE " \
      "WHEN a.start_time > unix_timestamp(now()) THEN '1' " \
      "WHEN a.start_time < unix_timestamp(now()) AND a.end_time < unix_timestamp(now()) THEN '2' " \
      "WHEN a.start_time < unix_timestamp(now()) AND a.end_time > unix_timestamp(now()) THEN '3' " \
      "ELSE '4' END AS stusta " \
      "FROM ad AS a " \
      "LEFT JOIN bc AS p " \
      "ON a.postion_id = p.id " \
      "WHERE p.`no` = '1001' AND p.area_code = '0';"

result = pm.selects(sql)

import json

for res in result:
    jsondatar = json.dumps(res, ensure_ascii=False)
    rebuild = json.loads(jsondatar)
    book = DictObj(rebuild);
    print('\n'.join(['%s:%s' % item for item in book.__dict__.items()]))