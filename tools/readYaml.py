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
@author: 70486
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file: readYaml.py
@time: 2018/7/31 15:18
@desc:
'''

import os
import yaml
def read_parseyaml(fpath, name):
    '''
    指定文件路径以及文件名来读取数据信息
    :param fpath: 文件路径
    :param name: 文件名称
    :return:
    '''
    pageElements = {}
    yaml_file_path = os.path.join(fpath, name)
    # 排除一些非.yaml的文件
    if '.yaml' in str(yaml_file_path):
        with open(yaml_file_path, 'r', encoding='utf-8') as f:
            page = yaml.load(f)
            pageElements.update(page)
    return pageElements
# name = 'GoodsPath.yaml'
# print(read_parseyaml(r'E:\operating\CenterBackground\GoodsManagement\CityGoods',name))