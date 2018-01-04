# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: Web_PersonalData.py
@time: 2018/1/4 22:03
@项目名称:operating
"""
import unittest
from PageWeb.WebEven.ExclusiveService.AccountPrivacy import account_privacy
import os
class personal_Privacy(unittest.TestCase,account_privacy):

    @classmethod
    def setUp(cls):
        basename = os.path.splitext(os.path.basename(__file__))[0]
        account_privacy.start_program(basename)


    @classmethod
    def tearDown(self):
        account_privacy.stop_program()

    def test_personal_nickname_one(self):
        # 个人昵称第一步:只查看昵称
        self.log.info("")
        self.path_Route()


if __name__ == '__main__':
    pass