# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: test_demo.py
@time: 2018/1/16 11:51
"""
from demo import demo_test
def modifier_Interface_sliding(func):
    #Interface_sliding()

    def modifier(*s, **gs):
        from time import ctime
        print("[%s] %s() called" % (ctime(), func.__name__))
        return func(*s, **gs)

    return modifier

print(demo_test.abdq)
demo_test.abdq = "88"
print(demo_test.abdq)
aa = demo_test.dong()
demo_test.abdq = aa
print(demo_test.abdq)
demo_test.abdq = 33
print(demo_test.dingdong())
print(modifier_Interface_sliding(demo_test.dingdong()))
