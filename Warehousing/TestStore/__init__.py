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
@time:      2018/12/17 16:14
@desc:
"""


class StoreDefault(object):
    # 根据module的key值来读取相应的在ArgumentAdmin.yaml中相应的子dict内容
    store = 'store'
    staff = 'staff'

    # 根据sheet的value值来读取ArgumentAdmin.yaml中，用例的标签名
    select = 'select'
    page = 'page'

    # 更新此处的key时，需要把ArgumentAdmin.yaml的key值也进行修改
    INVENTORY = {
        'menu': 'statement',  # 菜单标识符的定义
        'module': 'no data',  # 菜单中模块标识符的定义
        'sheet': 'no data',  # 模块所对应的用例标签名
        'yaml': 'storage/Warehousing.yaml'  # 菜单所对应的yaml路径
    }

    # 文件参数路径
    def add_key(module, sheet):
        INVENTORY['module'] = module
        INVENTORY['sheet'] = sheet
        return INVENTORY
