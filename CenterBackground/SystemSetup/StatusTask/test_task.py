# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: web_task.py
@time: 2018/5/25 14:12
"""
import os
import unittest

from CenterBackground.SystemSetup.StatusTask.taskJudge import TaskJudge

task = TaskJudge()


class TestTaskSystem(unittest.TestCase):
    '''定时'''
    @classmethod
    def setUpClass(cls):
        # 获取运行文件的类名
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        task.option_browser()  # 打开浏览器
        task.ps_user_login()  # 用户登录
        # 进入路径
        task._rou_task()
        pass

    @classmethod
    def tearDownClass(cls):
        try:
            # 该类结束时最后调用的函数
            # task.driver.quit()
            # announ.sleep_time(1)
            pass
        except UnicodeDecodeError:
            pass
            # announ.log.info("又出现UTF-8的错误........")

    def test_all_task(self):
        task.content_header_title(self.basename)
