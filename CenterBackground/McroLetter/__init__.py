# -*- coding: utf-8 -*-
"""
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  -  /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                        `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

               佛祖保佑         永无BUG
@author:    ln_company
@license:   (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@Software:  PyCharm
@file:      __init__.py.py
@time:      2018/11/19 10:22
@desc:
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
consult = 'consult'
message = 'message'
worktime = 'worktime'

# 根据sheet的value值来读取ArgumentAdmin.yaml中，用例的标签名
tabs = 'tabs'
select = 'select'
page = 'page'

# 更新此处的key时，需要把ArgumentAdmin.yaml的key值也进行修改
INVENTORY = {
    'menu': 'mcroLetter',  # 菜单标识符的定义,每个init都有自己独立的
    'module': 'no data',  # 菜单中模块标识符的定义
    'sheet': 'no data',  # 模块所对应的用例标签名
    'yaml': 'expression/McroLetter.yaml'  # 菜单所对应的yaml路径,每个init都有自己独立的
}
