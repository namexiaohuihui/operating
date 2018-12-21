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
@file:      handle_action.py
@time:      2018/12/21 14:15
@desc:
"""
from Warehousing.TestStore import SavaYamlPath
from Warehousing.screeningSelecy import ScreeningSelecy
from tools.Logger import Log
from tools.openpyxlExcel import OpenExcelPandas
from tools.configs import readModel
from tools.YAMLconfig import readYaml

module = 'module'

no_data = ('open', 'input', 'login')


class HandleAction(object):
    """做初始化的操作"""

    def __init__(self, basename):
        self.is_action = ScreeningSelecy()
        # 定义日志
        self.log = Log(basename)
        # 获取元素路径的位置
        yaml_path = SavaYamlPath().get_path_file()
        print("路径", yaml_path)
        self.financial = readYaml.read_expression(yaml_path)

    def execution_method(self, case):
        method_type, method_way, op_data = case.loc['操作'], case.loc['执行方法'], case.loc['输入数据']
        locator, expect_data = case.loc['操作元素'], case.loc['预期结果']
        if locator:
            if expect_data:
                if 'select' == method_type:
                    print("下拉")
                    method_way = self.function_getattr(method_way)
                    self.is_action.setSelectData(self.financial[locator], 'css')
                    option_text = method_way()
                    if ',' in expect_data:
                        assert expect_data == option_text, '下拉全部值不对' + option_text + expect_data
                        pass
                    else:
                        assert expect_data == option_text, "下拉默认值不对"
                else:
                    method_way = self.function_getattr(method_way)
                    way = 'css'
                    option_text = method_way(self.financial[locator], way)
                    assert expect_data == option_text, "界面文字不对"
                    print("文字")
                pass
            else:
                way_type = 'tag'
                way = 'css'
                method_way = self.function_getattr(method_way)
                method_way(locator, way_type, way)
                pass
        else:
            method_way = self.function_getattr(method_way)
            method_way(op_data)

        pass

    def function_getattr(self, fun_attr):
        fun_attr = getattr(self.is_action, fun_attr, False)
        return fun_attr
        pass

    pass
