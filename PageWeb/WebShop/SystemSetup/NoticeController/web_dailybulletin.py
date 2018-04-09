# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: web_dailybulletin.py
@time: 2018/4/9 18:04

公告用例类
"""
import unittest
from PageWeb.WebShop.SystemSetup.ParameterSetting.discountOperationSteps import DiscountOperationSteps


class DailyBulletin(unittest.TestCase):
    global disSte
    disSte = DiscountOperationSteps()

    @classmethod
    def setUp(cls):
        # 该类运行时优先调用的函数
        # log.info("The program begins to execute. Don't stop me when you start.")
        basename = cls.__class__.__name__
        # EXCLE_FILE = disSte.getDiscountExcle()
        disSte.option_browser()  # 打开浏览器(basename, EXCLE_FILE)
        disSte.ps_user_login()  # 用户登录
        import time
        time.sleep(2)

    @classmethod
    def tearDown(cls):
        try:
            # 该类结束时最后调用的函数
            # log.info("Make it complete and continue to press it next time...")
            # jv.driver.quit()
            # overall_ExcelData.to_excel(basename + ".xlsx", index=False, encoding="gbk")
            pass
        except UnicodeDecodeError:
            log.info("又出现UTF-8的错误........")

    def test_xx(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)