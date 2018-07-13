# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: web_navigation.py
@time: 2018/5/24 15:56

导航页面
"""
import os
import unittest

from CenterBackground.SystemSetup.NavigationDirectory.navigationSteps import NavigationSteps

naviga = NavigationSteps()


class NavigationSettings(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # 获取运行文件的类名
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        naviga.option_browser()  # 打开浏览器
        naviga.ps_user_login()  # 用户登录
        # 进入路径
        naviga._rou_navigation()

        pass

    @classmethod
    def tearDown(cls):
        try:
            # 该类结束时最后调用的函数
            naviga.driver.quit()
            # announ.sleep_time(1)
            pass
        except UnicodeDecodeError:
            pass
            # announ.log.info("又出现UTF-8的错误........")

    def test_all_naviga(self):
        naviga.content_header_title(self.basename)

