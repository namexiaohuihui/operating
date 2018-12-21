# -*- coding: utf-8 -*-
"""
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
@file: test_class.py
@time: 2018/7/27 15:27
@desc:
"""
from demo.test_baidu import TestBaiDu
import HTMLTestRunner
import unittest
import time

# 跟test_baidu关联
class wqweqw():
    def sdfegrth(self):
        time_now = time.strftime("%H-%M-%S")
        filePath = r'E:\operating\report\%sReport.html' % time_now  # 确定生成报告的路径
        fp = open(filePath, 'wb')
        suite1 = unittest.TestLoader().loadTestsFromTestCase(TestBaiDu)
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=u'自动化测试报告',
            description=u'用例执行情况：'
        )
        # 运行测试用例
        runner.run(suite1)
        fp.close()


if __name__ == '__main__':
    wqweqw().sdfegrth()
    # dic0 = {'case_name': 'qw', '步骤': 'qw', 'q1w': 'qwe','memberID': 'qw', '场景': 'qwe'}
    # if '场景' in dic0.keys() and '步骤' in dic0.keys():
    #     print("@")
    #     pass
    # else:
    #     print("4")