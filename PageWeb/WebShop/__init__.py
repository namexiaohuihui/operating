# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: __init__.py.py
@time: 2017/10/23 22:55
@项目名称:operating
"""
class FatherA1(object):

    def __init__(self):

        print('init action in father class A1')

class FatherA(FatherA1):

    def __init__(self):

        print('init action in father class A')
        super().__init__()

class SubClassB(FatherA):

    def __init__(self):

        print('init action in subclass B')

        super().__init__()

class SubClassF(object):

    def __init__(self):

        print('init action in subclass F')

        super().__init__()

class SubClassE(SubClassF):

    def __init__(self):

        print('init action in subclass E')

        super().__init__()

class SubClassC(SubClassB,SubClassE):
    base = 1
    def __init__(self):

        print('init action in subclass C')

        SubClassB.__init__(self)
        SubClassE.__init__(self)
    def opopopo(self):
        print("wosifangfa")


    def foo(self):
        return self.base
    def foo1(self):
        pass
import unittest
class SubClassD(unittest.TestCase,SubClassC):

    def __init__(self):

        print('init action in subclass D')
        unittest.TestCase.__init__(self)
        SubClassC.__init__(self)



def foo(n):
    return abs(n)

def foo1(n):
    return lambda x:x+abs(n)

if __name__ == '__main__':

    list1 = [3, 5, -4, -1, 0, -2, -6]

    kg1 = lambda x : (abs(x))
    print(sorted(list1,key=(kg1)))

    fo = foo1(6)
    print(sorted(list1,key=fo))

    print(fo(8))

    kg2 = lambda x : abs(x) + 6
    print(kg2(-3))
    print(sorted(list1, key=kg2))
