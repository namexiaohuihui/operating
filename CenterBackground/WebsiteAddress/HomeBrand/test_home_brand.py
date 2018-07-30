# -*- coding: utf-8 -*-
'''
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  -  /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                        `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

               佛祖保佑         永无BUG
@author: 70486
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file: test_website.py
@time: 2018/7/30 17:08
@desc:
'''
import os
import unittest
from CenterBackground.WebsiteAddress.HomeBrand.homeBrandJudge import HomeBrandJudge

home_brand = HomeBrandJudge()


class TestNews(unittest.TestCase):
    '''参数'''

    @classmethod
    def setUpClass(cls):
        # 获取运行文件的类名
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        home_brand.option_browser()  # 打开浏览器
        home_brand.ps_user_login()  # 用户登录
        # 进入路径
        home_brand._rou_task()
        pass

    @classmethod
    def tearDownClass(cls):
        try:
            # 该类结束时最后调用的函数
            # home_brand.driver.quit()
            pass
        except UnicodeDecodeError:
            pass
            # announ.log.info("又出现UTF-8的错误........")

    def test_all_home_brand(self):
        home_brand.content_header_title(self.basename)
