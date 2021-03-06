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


def read_expression(name='ArgumentAdmin.yaml'):
    """
    指定yaml文件路径名,来读取数据信息
    :param name:  yaml文件名
    :return:
    """
    yaml_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), name)
    pageElements = read_parseyaml(yaml_file_path)
    return pageElements


def read_expression_key(name, read_key):
    """
    指定yaml文件路径名,来读取数据信息
    通过key值来解析相应的值
    :param name: yaml文件名
    :param read_key: 需要值所对应的key
    :return:
    """
    # 将数据转成文件形式
    pageElements = read_parseyaml(name)
    pageElements = pageElements[read_key]
    return pageElements


def read_parseyaml(yaml_file_path):
    '''
    指定文件路径以及文件名来读取数据信息
    :param fpath: 文件路径
    :param name: 文件名称
    :return:
    '''
    pageElements = {}
    # 排除一些非.yaml的文件
    if '.yaml' in str(yaml_file_path):
        with open(yaml_file_path, 'r', encoding='utf-8') as f:
            page = yaml.load(f)
            pageElements.update(page)
    return pageElements