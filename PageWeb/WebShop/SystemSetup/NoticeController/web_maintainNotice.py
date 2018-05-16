# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: web_maintainNotice.py
@time: 2018/5/15 18:23
"""
import os
import inspect
import unittest
from PageWeb.WebShop.SystemSetup.NoticeController.dailyOperationSteps import DailyOperationSteps
disSte = DailyOperationSteps()

class MaintainNotice(unittest.TestCase):
    # 用例sheet的位置
    CASE_EXCLE_POSITION = 2

    @classmethod
    def setUp(cls):
        # 获取运行文件的类名
        basename = os.path.splitext(os.path.basename(__file__))[0]
        # 打开浏览器，定义log日志。读取excle文档数据
        disSte.setDailyBulletin(basename, CASE_EXCLE_POSITION)
        # 进入路径
        disSte._rou_DailyFun()
        pass

    @classmethod
    def tearDown(cls):
        try:
            # 该类结束时最后调用的函数
            disSte.driver.quit()
            # disSte.sleep_time(1)
            pass
        except UnicodeDecodeError:
            disSte.log.info("又出现UTF-8的错误........")