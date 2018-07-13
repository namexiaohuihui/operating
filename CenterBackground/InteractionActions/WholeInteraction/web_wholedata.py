# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: web_wholedata.py
@time: 2018/5/28 15:07
"""
import inspect
import os
import sys
import unittest

# 获取项目路径下的目录
os.chdir('E:\\operating')
# 将项目路径保存
sys.path.append('E:\\operating')

from CenterBackground.InteractionActions.WholeInteraction.wholeActionsJudge import WholeActionsJudge

whole = WholeActionsJudge()


class InterationOrderLable(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> '定义log文件/读取excel数据/开启浏览器':
        # 获取运行文件的类名
        basename = os.path.splitext(os.path.basename(__file__))[0]
        # 打开浏览器，定义log日志。读取excle文档数据
        whole.openingProgram(basename, whole.MODEL_WORKBOOK_DATA)
        whole._rou_interaction()

    @classmethod
    def tearDownClass(cls) -> '关闭浏览器,做程序结尾工作':
        try:
            # whole.driver.close()
            # whole.driver.quit()
            pass
        except:
            print("又见UTF-8错误")
        finally:
            print('关闭浏览器,做程序结尾工作')

    def test_whole_title(self):
        whole.setFunctionName(inspect.stack()[0][3])
        whole.order_whole_title()

    def test_whole_page(self):
        whole.setFunctionName(inspect.stack()[0][3])
        whole.order_whole_page()

    def test_whole_screening(self):
        whole.setFunctionName(inspect.stack()[0][3])
        whole.screening_selector()

    def test_day_appointment(self):
        whole.setFunctionName(inspect.stack()[0][3])
        whole.appointment_bunber()

    def test_day_communicate(self):
        whole.setFunctionName(inspect.stack()[0][3])
        whole.appointment_bunber()

    def test_day_large_quantity(self):
        whole.setFunctionName(inspect.stack()[0][3])
        whole.appointment_bunber()

    def test_day_seconds(self):
        whole.setFunctionName(inspect.stack()[0][3])
        whole.appointment_bunber()

    def test_day_offline(self):
        whole.setFunctionName(inspect.stack()[0][3])
        whole.appointment_bunber()

    def test_area_screening(self):
        whole.setFunctionName(inspect.stack()[0][3])
        whole.area_screening_conditions()

    def test_status_screening(self):
        whole.setFunctionName(inspect.stack()[0][3])
        whole.status_screening_conditions()

if __name__ == '__main__':
    unittest.main()
