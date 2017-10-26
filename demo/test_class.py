# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: test_class.py
@time: 2017/10/26 11:58
"""
class user_class:
    def __init__(self):
        self.id = ''
        self.phone = ''
        self.add_time = ''

    def to_string(self,test):
        print('\n'.join(['%s:%s' % item for item in test.__dict__.items()]))
