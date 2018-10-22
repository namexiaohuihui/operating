# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: __init__.py
@time: 2018/5/24 16:49
file keys Defined in the
"""


def add_key(module: str, sheet: str):
    """
    set dict module and sheet in value
    :param module:
    :param sheet:
    :return:
    """
    INVENTORY['module'] = module
    INVENTORY['sheet'] = sheet
    return INVENTORY


# 根据module的key值来读取相应的在ArgumentAdmin.yaml中相应的子dict内容
collective = 'collective'
single = 'single'
dispatch = 'dispatch'

# 根据sheet的value值来读取ArgumentAdmin.yaml中，用例的标签名
city = 'city'
select = 'select'
page = 'page'
views = 'views'
close = 'close'
transfer = 'transfer'
replace = 'replace'
details = 'details'
record = 'record'
particulars = 'particulars'

# 更新此处的key时，需要把ArgumentAdmin.yaml的key值也进行修改
INVENTORY = {
    'menu': 'indent',  # 菜单标识符的定义
    'module': 'no data',  # 菜单中模块标识符的定义
    'sheet': 'no data',  # 模块所对应的用例标签名
    'yaml': 'expression/WholeCondition.yaml'  # 菜单所对应的yaml路径
}
