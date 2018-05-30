# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: web_wholelabel.py
@time: 2018/5/28 15:02
"""
import inspect
import os
import unittest

from PageWeb.WebShop.InteractionActions.WholeInteraction.wholeActionsJudge import WholeActionsJudge

whole = WholeActionsJudge()


class OrderWholeLabel(unittest.TestCase):

    @classmethod
    def setUp(cls) -> '定义log文件/读取excel数据/开启浏览器':
        # 获取运行文件的类名
        basename = os.path.splitext(os.path.basename(__file__))[0]
        # 打开浏览器，定义log日志。读取excle文档数据
        whole.openingProgram(basename, whole.MODEL_WORKBOOK_LABEL)
        whole._rou_interaction()

    @classmethod
    def tearDown(cls) -> '关闭浏览器,做程序结尾工作':
        print('关闭浏览器,做程序结尾工作')

    def test_default_active(self):
        '''默认展示是否正确'''
        whole.setFunctionName(inspect.stack()[0][3])
        whole.city_active_default()

    def test_city_code(self):
        '''判断城市和编码'''
        whole.setFunctionName(inspect.stack()[0][3])
        whole.city_code_judge()

    def test_switch_city(self):
        '''切换城市tab'''
        whole.setFunctionName(inspect.stack()[0][3])
        whole.city_replace_active()

    def test_time_select(self):
        '''时间下拉和刻度默认值的校验'''
        whole.setFunctionName(inspect.stack()[0][3])
        whole.select_option_judge()

if __name__ == '__main__':
    unittest.main(verbosity=2)
