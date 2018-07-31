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
@file: interactionNames.py
@time: 2018/7/30 17:52
@desc:
'''

import yaml
import os
from tools.excelname.shopInteraction import InteractionController

basepath = os.path.dirname(os.path.realpath(__file__))


class InteractionNames(InteractionController):

    def together_catalog(self, fpath, name):
        '''
        指定文件路径以及文件名来读取数据信息
        :param fpath: 文件路径
        :param name: 文件名称
        :return:
        '''
        page_list = {}
        yaml_file_path = os.path.join(fpath, name)
        with open(yaml_file_path, 'r', encoding='utf-8') as f:
            page = yaml.load(f)
            page_list.update(page)
        return page_list

    def read_parseyaml(self, files):
        '''
        遍历读取yaml文件
        '''
        pageElements = {}
        # 遍历读取yaml文件
        for fpath, dirname, fnames in os.walk(basepath):
            for name in fnames:
                # yaml文件绝对路径
                yaml_file_path = os.path.join(fpath, name)
                # 排除一些非.yaml的文件
                if files in str(yaml_file_path):
                    with open(yaml_file_path, 'r', encoding='utf-8') as f:
                        page = yaml.load(f)
                        pageElements.update(page)
        return pageElements

    pass


if __name__ == '__main__':
    print(InteractionNames().read_parseyaml("totalLableNanme.yaml"))
