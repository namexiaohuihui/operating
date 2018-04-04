# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: __init__.py.py
@time: 2017/12/20 23:03
@项目名称:operating
"""
def nihaoma(value,text):
    import operator
    return operator.eq(value,text)

if __name__ == '__main__':
    value = {"goods":{"discount":"1","exception":"10370"},"watiki":{"discount":"5","exception":"10253","max":"75"}}
    nihao ={'goods': {'discount': '1', 'exception': '10370'}, 'watiki': {'discount': '5', 'exception': '10253', 'max': '75'}}
    print(nihaoma(value,nihao))

    excle_value = {'goods': {'discount': 1,
                             'exception': 1},
                   'watiki': {'discount': 1,
                              'exception': 1,
                              'max': 1}}
    print(type(excle_value))