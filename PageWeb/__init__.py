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
    neirong = [{'code': 450100, 'name': '南宁市'}, {'code': 450200, 'name': '柳州市'}, {'code': 430100, 'name': '长沙市'}, {'code': 451000, 'name': '百色市'}, {'code': 451100, 'name': '贺州市'}, {'code': 420100, 'name': '武汉市'}, {'code': 500100, 'name': '重庆市辖区'}]
    for code in neirong:
        # print(code)
        for (d, x) in code.items():
            print("key:" + d + ",value:" + str(x))