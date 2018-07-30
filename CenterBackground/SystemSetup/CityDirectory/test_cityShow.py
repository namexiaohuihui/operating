# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: web_cityShow.py
@time: 2018/5/24 16:17
"""
import os
import unittest
from CenterBackground.SystemSetup.CityDirectory.cityShowJudge import CityShowJudge
city_show = CityShowJudge()

class TestCityShow(unittest.TestCase):
    '''城市'''
    @classmethod
    def setUpClass(cls):
        # 获取运行文件的类名
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        city_show.option_browser()  # 打开浏览器
        city_show.ps_user_login()  # 用户登录
        # 进入路径
        city_show._rou_city_show()

        pass

    @classmethod
    def tearDownClass(cls):
        try:
            # 该类结束时最后调用的函数
            city_show.driver.quit()
            # announ.sleep_time(1)
            pass
        except UnicodeDecodeError:
            pass
            # announ.log.info("又出现UTF-8的错误........")

    def test_all_city_show(self):
        city_show.content_header_title(self.basename)
