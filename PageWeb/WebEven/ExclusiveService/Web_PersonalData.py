# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: Web_PersonalData.py
@time: 2018/1/4 22:03
@项目名称:operating
"""
import unittest
from PageWeb.WebEven.ExclusiveService import AccountPrivacy
import os
from practical.utils.logger import Log

class personal_Privacy(unittest.TestCase):

    @classmethod
    def setUp(cls):
        basename = os.path.splitext(os.path.basename(__file__))[0]

        cls.log = Log(basename)
        cls.log.info("The program begins to execute. Don't stop me when you start.")
        cls.driver = AccountPrivacy.open_browser()
        cls.excelData = AccountPrivacy.start_program(cls.driver)
        cls.log.info("open driver time")
        print(cls.excelData[0])
        print(cls.excelData[1])


    @classmethod
    def tearDown(self):
        self.log.info("Make it complete and continue to press it next time...")
        self.driver.close()

    def test_personal_nickname_one(self):
        # 个人昵称第一步:只查看昵称
        AccountPrivacy.is_visible_css_selectop(self.driver,".user-head")

        # 比较页面的内容
        sidebarMsg = AccountPrivacy.is_visible_css_selectop(self.driver,".sidebar-msg")
        assert "。。" != sidebarMsg.text , "test_personal_nickname_one"

        # 比较弹窗中的数据
        uText = AccountPrivacy.is_visible_css_selectop_attribute(self.driver, ".u-txt.u-txt-l")
        assert "..." != uText, "test_personal_nickname_one"

        AccountPrivacy.is_visible_css_selectop(self.driver,".am-dialog-footer>button:nth-child(1)")

    def test_personal_nickname_two(self):
        AccountPrivacy.is_visible_css_selectop(self.driver, ".user-head")

        # 比较页面的内容
        sidebarMsg = AccountPrivacy.is_visible_css_selectop(self.driver, ".sidebar-msg")
        assert "。。" != sidebarMsg.text, "test_personal_nickname_one"

        # 比较弹窗中的数据
        uTextValue = AccountPrivacy.is_visible_css_selectop(self.driver, ".u-txt.u-txt-l")
        assert "..." != uTextValue.get_attribute("value"), "test_personal_nickname_one"

        # 输入Neri
        uTextValue.send_keys(sidebarMsg.text)

        AccountPrivacy.is_visible_css_selectop(self.driver, ".am-dialog-footer>button:last-child")

        # 比较页面的最新数据跟输入的内容是否一致
        sidebarMsg = AccountPrivacy.is_visible_css_selectop(self.driver, ".sidebar-msg")

        assert sidebarMsg.text == sidebarMsg.text, "test_personal_nickname_one"



if __name__ == '__main__':
    unittest.main()