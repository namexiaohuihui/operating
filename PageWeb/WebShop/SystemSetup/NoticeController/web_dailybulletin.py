# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: web_dailybulletin.py
@time: 2018/4/9 18:04

"""
import re
import os
import inspect
import unittest
from PageWeb.WebShop.SystemSetup.NoticeController.dailyOperationSteps import DailyOperationSteps

disSte = DailyOperationSteps()

class DailyBulletin(unittest.TestCase):
    """公告用例类"""
    @classmethod
    def setUp(cls):
        # 该类运行时优先调用的函数
        # log.info("The program begins to execute. Don't stop me when you start.")
        basename = os.path.splitext(os.path.basename(__file__))[0]
        disSte.setDailyBulletin(basename)
        # 进入路径
        disSte._rou_DailyFun()
        # disSte.openingProgram(basename, EXCLE_FILE)

    @classmethod
    def tearDown(cls):
        try:
            # 该类结束时最后调用的函数
            # log.info("Make it complete and continue to press it next time...")
            # jv.driver.quit()
            # overall_ExcelData.to_excel(basename + ".xlsx", index=False, encoding="gbk")
            pass
        except UnicodeDecodeError:
            log.info("又出现UTF-8的错误........")

    @unittest.skip(r"跳过:test_AllTitle")
    def test_AllTitle(self):
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 进入路径
        disSte.getAllTitle()
        pass

    @unittest.skip(r"跳过:test_AllTitle")
    def test_AllContent(self):
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllContent()

    @unittest.skip(r"跳过:test_AllCity")
    def test_AllCity(self):
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllCity()

    @unittest.skip(r"跳过:test_SingleCity")
    def test_SingleCity(self):
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllCity()

    # @unittest.skip(r"跳过:test_SingleCity")
    def test_AllCityRelease(self):
        # 获取函数名
        disSte.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        disSte.getAllRelease()

if __name__ == '__main__':
    unittest.main(verbosity=2)
