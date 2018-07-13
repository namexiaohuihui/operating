# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: web_information.py
@time: 2018/5/25 14:23
"""
import os
import unittest

from CenterBackground.SystemSetup.QueryInformation.informationJudge import InformationJudge

information = InformationJudge()

class InformationSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 获取运行文件的类名
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        information.option_browser()  # 打开浏览器
        information.ps_user_login()  # 用户登录
        # 进入路径
        information._rou_information()

        pass

    @classmethod
    def tearDownClass(cls):
        try:
            # 该类结束时最后调用的函数
            information.driver.quit()
            # announ.sleep_time(1)
            pass
        except UnicodeDecodeError:
            pass
            # announ.log.info("又出现UTF-8的错误........")

    def test_all_information(self):
        information.content_header_title(self.basename)

