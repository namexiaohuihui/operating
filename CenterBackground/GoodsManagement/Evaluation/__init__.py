# -*- coding: utf-8 -*-
'''
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
@author:  ln_company
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file: __init__.py.py
@time: 2018/8/14 15:18
@desc:
'''


# 文件参数路径
def add_key(value):
    INVENTORY['sheet'] = value
    return INVENTORY


# 根据sheet的value值来读取ArgumentAdmin.yaml中，用例的标签名
select = 'select'
label = 'label'
tap = 'tap'
# 更新此处的key时，需要把ArgumentAdmin.yaml的key值也进行修改
'''
{
# 都是定义ArgumentAdmin.yaml文件的标识
'menu': 'goods',                            # 菜单标识符的定义
'module': 'citys',                          # 菜单中模块标识符的定义
'sheet': 'create',                          # 模块所对应的用例标签名
'yaml': 'expression/GoodsPath.yaml'         # 菜单所对应的yaml路径
}


'''
INVENTORY = {
    'menu': 'goods',
    'module': 'evaluation',
    'sheet': '没有默认值',
    'yaml': 'expression/GoodsPath.yaml'
}
