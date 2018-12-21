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
import os
from tools.openpyxlExcel import OpenExcelPandas
from tools.YAMLconfig import readYaml


class SavaYamlPath(object):
    # 单例类判断。如果该类创建过就不需要重新创建了
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(SavaYamlPath, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

    def get_path_file(self, path_file=None):
        if path_file:
            self.yaml_path = path_file
            return self.yaml_path
        elif self.yaml_path:
            return self.yaml_path


class StoreDefault(object):
    def __init__(self):
        # 根据module的key值来读取相应的在ArgumentAdmin.yaml中相应的子dict内容
        self.store = 'store'
        self.staff = 'staff'

        # 根据sheet的value值来读取ArgumentAdmin.yaml中，用例的标签名
        self.select = 'select'
        self.page = 'page'

    # 文件参数路径
    def add_key(self, module, sheet):
        # 更新此处的key时，需要把ArgumentAdmin.yaml的key值也进行修改
        self.INVENTORY = {
            'menu': 'statement',  # 菜单标识符的定义
            'module': module,  # 菜单中模块标识符的定义
            'sheet': sheet,  # 模块所对应的用例标签名
            'yaml': 'storage/Warehousing.yaml'  # 菜单所对应的yaml路径
        }

        # yaml读取用例位置
        argument = readYaml.read_expression("AtorageAdmin.yaml")
        argument = argument[self.INVENTORY["menu"]]
        self.module_excle_path = os.path.join(argument['excel'], argument[module]['excel'])
        self.INVENTORY['sheet'] = argument[module][sheet]
        SavaYamlPath().get_path_file(self.INVENTORY['yaml'])

    def _excel_Data(self, title_name):
        """
        读取用例
        :return:
        """
        # 读取相应路径中的数据
        read = OpenExcelPandas(name=r'' + self.module_excle_path, sheet=self.INVENTORY['sheet'])
        ex_data = read.internal_read_excel(title_name)
        # ex_data = [row for row in ex_data.itertuples(index=True)]
        df_index = ex_data.index
        ex_data = [ex_data.loc[df_i] for df_i in df_index]
        return ex_data
