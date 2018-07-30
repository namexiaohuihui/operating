# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: web_brand.py
@time: 2018/5/24 16:44
"""
import os
import unittest

from CenterBackground.SystemSetup.BrandDirectory.brandJudge import BrandJudge

brand = BrandJudge()


class TestBrandSystem(unittest.TestCase):
    '''品牌类'''
    def setUp(cls):
        # 获取运行文件的类名
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        brand.option_browser()  # 打开浏览器
        brand.ps_user_login()  # 用户登录
        # 进入路径
        brand._rou_brand()

        pass

    def tearDown(cls):
        try:
            # 该类结束时最后调用的函数
            brand.driver.quit()
            # announ.sleep_time(1)
            pass
        except UnicodeDecodeError:
            pass
            # announ.log.info("又出现UTF-8的错误........")

    def test_all_brand(self):
        brand.content_header_title(self.basename)

if __name__ == '__main__':
    unittest.main(verbosity=2)