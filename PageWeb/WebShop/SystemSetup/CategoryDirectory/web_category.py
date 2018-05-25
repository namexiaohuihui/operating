# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: web_category.py
@time: 2018/5/24 16:33
"""
import os
import unittest

from PageWeb.WebShop.SystemSetup.CategoryDirectory.categoryJudge import CategoryJudge

category = CategoryJudge()


class CategorySystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 获取运行文件的类名
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        category.option_browser()  # 打开浏览器
        category.ps_user_login()  # 用户登录
        # 进入路径
        category._rou_category()

        pass

    @classmethod
    def tearDownClass(cls):
        try:
            # 该类结束时最后调用的函数
            category.driver.quit()
            # announ.sleep_time(1)
            pass
        except UnicodeDecodeError:
            pass
            # announ.log.info("又出现UTF-8的错误........")

    def test_all_category(self):
        print("%s 进入页面成功" % self.basename)
