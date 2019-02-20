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
@time: 2018/7/31 16:46
@desc:
'''
import os
from tools.openpyxlExcel import OpenExcelPandas
from tools.YAMLconfig import readYaml
from tools.configs import readModel


def add_key(module, sheet):
    INVENTORY['module'] = module
    INVENTORY['sheet'] = sheet
    return INVENTORY


# 根据module的key值来读取相应的在ArgumentAdmin.yaml中相应的子dict内容
evaluation = 'evaluation'
inventory = 'inventory'
entersales = 'entersales'
emptybarrel = 'emptybarrel'
citys = 'citys'

# 根据sheet的value值来读取ArgumentAdmin.yaml中，用例的标签名
select = 'select'
label = 'label'
city = 'city'
tab = 'tab'
shelves = 'shelves'
jump = 'jump'
modetail = 'modetail'
emdetail = 'emdetail'

# 更新此处的key时，需要把ArgumentAdmin.yaml的key值也进行修改
INVENTORY = {
    'menu': 'goods',  # 菜单标识符的定义
    'module': 'no data',  # 菜单中模块标识符的定义
    'sheet': 'no data',  # 模块所对应的用例标签名
    'yaml': 'expression/GoodsPath.yaml'  # 菜单所对应的yaml路径
}


def get_argument_data():
    # 读取配置文件中设置用例关键字的信息
    argument = readYaml.read_expression("ArgumentAdmin.yaml")
    argument = argument[INVENTORY["menu"]]
    return argument


def _excel_Data(title_name):
    """
    yaml读取用例位置
    :return:
    """
    # 读取excel配置文件中存储的用例所在地
    conf = readModel.establish_con(model="excelmodel")

    # 读取配置文件中设置用例关键字的信息
    argument = get_argument_data()

    argument_menu = conf.get("admin_excel", argument['module'])
    argument_module = conf.get("admin_excel", argument[INVENTORY['module']]['module'])

    module_excle_path = os.path.join(argument_menu, argument_module)

    # 读取相应路径中的数据
    read = OpenExcelPandas(name=r'' + module_excle_path, sheet=argument[INVENTORY['module']][INVENTORY['sheet']])
    ex_data = read.internal_read_excel(title_name)

    df_index = ex_data.index
    ex_data = [ex_data.loc[df_i] for df_i in df_index]
    del argument
    return ex_data
