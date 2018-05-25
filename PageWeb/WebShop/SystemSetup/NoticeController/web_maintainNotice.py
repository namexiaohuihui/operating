# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: web_maintainNotice.py
@time: 2018/5/15 18:23
"""
import inspect
import os
import unittest

from PageWeb.WebShop.SystemSetup.NoticeController.announcementClass import AnnouncementClass

announ = AnnouncementClass()


class MaintainNotice(unittest.TestCase):
    # 用例sheet的位置
    CASE_EXCLE_POSITION = 2

    @classmethod
    def setUpClass(cls):
        # 设计模式有误，需要设置这个参数。。唉-----------------不严谨
        announ.modify_key = False
        # 获取运行文件的类名
        basename = os.path.splitext(os.path.basename(__file__))[0]
        # 打开浏览器，定义log日志。读取excle文档数据
        announ.setDailyBulletin(basename, cls.CASE_EXCLE_POSITION)
        # 进入路径
        announ._rou_MaintenanceFun()

        pass

    @classmethod
    def tearDownClass(cls):
        try:
            # 该类结束时最后调用的函数
            announ.driver.quit()
            # announ.sleep_time(1)
            pass
        except UnicodeDecodeError:
            announ.log.info("又出现UTF-8的错误........")

    # @unittest.skip(r"跳过:test_AllTitle")
    def test_AllTitle(self) -> "检查页面上标签是否正确":
        # 获取函数名
        announ.setFunctionName(inspect.stack()[0][3])

        # 进入路径
        announ.getAllTitle()
        pass

    # @unittest.skip(r"跳过:test_AllContent")
    def test_AllContent(self) -> "获取页面展示的数据是否正确":
        # 获取函数名
        announ.setFunctionName(inspect.stack()[0][3])

        # 获取数据进行比较
        announ.notice_all_content()

        # @unittest.skip(r"跳过:test_dailyToOverdue")

    def test_dailyToOverdue(self):
        """
        发布公告，公告为未开始
        :return: None
        """
        announ.setFunctionName(inspect.stack()[0][3])
        announ.prepare_judge_time()
        pass
