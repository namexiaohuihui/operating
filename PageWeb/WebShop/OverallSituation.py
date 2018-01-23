# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: OverallSituation.py
@time: 2018/1/23 9:57
"""


# 使用装饰器(decorator),
# 这是一种更pythonic,更elegant的方法,
# 单例类本身根本不知道自己是单例的,因为他本身(自己的代码)并不是单例的
def singleton(cls, *args, **kw):
    instances = {}

    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class overallsituation(object):
    def setContent(self,content):
        self.content = content
    def getContent(self):
        return self.content
