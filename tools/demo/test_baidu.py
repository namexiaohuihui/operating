import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import HTMLTestRunner
import ddt
from tools.Logger import Log

# 跟test_class关联
# http://www.cnblogs.com/guanfuchang/p/5970435.html
# https://blog.csdn.net/qq_34309753/article/details/84138807
nisho = {'case_name': 'qw', '步骤': 'qw', 'q1w': 'qwe','memberID': 'qw', 'qdfdff': 'qwe'}


class TestBaiDu(unittest.TestCase):
    """
    测试库
    """

    def setUp(self):
        self.driver = webdriver.Chrome("E:\drivers\Drivers\chromedriver239-68.exe")
        self.driver.get('http://www.baidu.com')

    def tearDown(self):
        self.driver.quit()

    def test_search(self) -> "提示不对呢":
        """测试场景为={0}"""
        ll_log = Log()
        print(nisho)
        ll_log.info("注释内容开头%s注释内容结尾" % nisho)
        print("dfgdfg213534536456sdg")
        print("3123")
        print("1231234")
        ll_log.info("ghngh")
        ll_log.info("df")
        ll_log.info("zx")
        ll_log.info("zxc")
        time.sleep(1)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
