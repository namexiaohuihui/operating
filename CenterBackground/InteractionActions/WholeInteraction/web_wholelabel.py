# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: web_wholelabel.py
@time: 2018/5/28 15:02

新增思路:
1. 是否需要将路径名称的key写到文档上
2. 收集数据的函数不做判断操作
"""
import inspect
import os
import unittest

from CenterBackground.InteractionActions.WholeInteraction.wholeActionsJudge import WholeActionsJudge

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
        whole.driver.close()

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
        whole.select_option_time()

    def test_lable_radio(self):
        '''标签默认值检验及点击'''
        whole.setFunctionName(inspect.stack()[0][3])
        whole.select_lable_radio()

    def test_area_region(self):
        '''经理、主管、所属区域默认值校验'''
        whole.setFunctionName(inspect.stack()[0][3])
        whole.select_area_region()

    def test_status_type(self):
        '''订单来源和状态的默认值校验'''
        whole.setFunctionName(inspect.stack()[0][3])
        whole.order_source_status()

    def test_order_value(self):
        '''订单下拉和关键字框默认值校验'''
        whole.setFunctionName(inspect.stack()[0][3])
        whole.order_value_placeholder()

    def test_buyer_value(self):
        '''买家下拉和关键字框默认值校验'''
        whole.setFunctionName(inspect.stack()[0][3])
        whole.buyer_value_placeholder()

    def test_other_value(self):
        '''其他下拉框和关键字框默认值校验'''
        whole.setFunctionName(inspect.stack()[0][3])
        whole.other_value_placeholder()


if __name__ == '__main__':
    unittest.main(verbosity=2)
