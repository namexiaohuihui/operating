# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: web_category.py
@time: 2018/5/24 16:33
"""
import os
import unittest

from CenterBackground.SystemSetup.CategoryDirectory.categoryJudge import CategoryJudge

category = CategoryJudge()


class TestCategorySystem(unittest.TestCase):
    '''类目'''
    def setUp(cls):
        # 获取运行文件的类名
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        category.option_browser()  # 打开浏览器
        category.ps_user_login()  # 用户登录
        # 进入路径
        category._rou_category()

        pass

    def tearDown(cls):
        try:
            # 该类结束时最后调用的函数
            category.driver.quit()
            pass
        except UnicodeDecodeError:
            pass

    def test_all_category(self):
        category.content_header_title(self.basename)

if __name__ == '__main__':
    unittest.main(verbosity=2)
