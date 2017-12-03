# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: jsonChuli.py
@time: 2017/12/2 13:46
@项目名称:TestDemo
"""
import json
from collections import namedtuple


def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())

def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)

def json_shuju():
    url = "https://api.douban.com/v2/book/1220562"
    data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
    # Parse JSON into an object with attributes corresponding to dict keys.
    x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    print(x.name, x.hometown.name, x.hometown.id)

    y = json2obj(data)
    print(y.name, y.hometown.name, y.hometown.id)

class User(object):
    def __init__(self, name, username, *args, **kwargs):
        self.name = name
        self.username = username

    def object_decoder(self,obj):
        if '__type__' in obj and obj['__type__'] == 'User':
            return User(obj['name'], obj['username'])
        return obj

    def json_lizi(self,date):
        j = json.loads(date)
        u = User(**j)
        print('\n'.join(['%s:%s' % item for item in u.__dict__.items()]))

        date = '{"__type__": "User", "name": "John Smith", "username": "jsmith"}'
        json.loads(date, object_hook=self.object_decoder())
        print(type(User))

class User2:
    def __init__(self, name, username, *args, **kwargs):
        self.name = name
        self.username = username

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)
    def lizi(self):
        to1 = User2("tbrown", "Tom Brown")
        to3 = User2("tbrown", "Tom Brown").to_json()

        to2 = User2.from_json(User2("tbrown", "Tom Brown").to_json()).to_json()
        to4 = User2.from_json(User2("tbrown", "Tom Brown").to_json())
        print(to1)
        print(to1.name)
        print(to1.username)
        print(to2)
        go1 = User2.from_json(to3)


        """
        go1 = User2.from_json(to1)
        print(go1.name)
        print(go1.username)
        print(User2.from_json(to2))
        """



if __name__ == '__main__':
    to1 = User2("tbrown", "Tom Brown")
    to3 = User2("tbrown", "Tom Brown").to_json()

    to2 = User2.from_json(User2("tbrown", "Tom Brown").to_json()).to_json()
    to4 = User2.from_json(User2("tbrown", "Tom Brown").to_json())
    print(to1)
    print(to1.name)
    print(to1.username)
    print(to2)


