# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: interactionNames.py
@time: 2018/5/25 15:40
"""
import os

import yaml

from utils.excelname.shopInteraction import InteractionController


# 当前脚本路径


class InteractionNames(InteractionController):
    def read_parseyaml(self, file_name=".yaml", basepath=None):
        '''
        遍历读取yaml文件
        '''
        if basepath:
            pass
        else:
            basepath = os.path.dirname(os.path.realpath(__file__))
        pageElements = {}
        # 遍历读取yaml文件
        for fpath, dirname, fnames in os.walk(basepath):
            for name in fnames:
                # yaml文件绝对路径
                yaml_file_path = os.path.join(fpath, name)
                # 排除一些非.yaml的文件
                if file_name in str(yaml_file_path):
                    with open(yaml_file_path, 'r', encoding='utf-8') as f:
                        page = yaml.load(f)
                        pageElements.update(page)

        return pageElements


if __name__ == '__main__':
    parse = InteractionNames().read_parseyaml("totalPathNames.yaml")
    print(parse)
