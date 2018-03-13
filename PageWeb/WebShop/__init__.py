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

import unittest
class SubClassD(unittest.TestCase,SubClassC):

    def __init__(self):

        print('init action in subclass D')
        unittest.TestCase.__init__(self)
        SubClassC.__init__(self)



if __name__ == '__main__':

    b = SubClassD()
    b.opopopo()
