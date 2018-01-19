# -*- coding: utf-8 -*-
"""
@__author__ :DingDong
@file: demo_unit.py
@time: 2018/1/18 20:57
@Entry Name:operating
"""
import unittest
class demounit(unittest.TestCase):

    def setUp(self):
        print("shouci")

    def tearDown(self):
        print("zuihou")

    def testStart(self):
        print("testStart")

    def testOne(self):
        print("testOne")

    def testTwo(self):
        print("testTwo")

if __name__ == '__main__':
    # unittest.main :unittest执行的方式一。默认执行全部
    # unittest.main(verbosity=2)

    # unittest执行的方式二: 通过添加来执行
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(demounit("testStart"))
    suite.addTest(demounit("testOne"))
    # suite.addTest(demounit("testTwo"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

    # unittest执行的方式3: 通过添加来执行
    # 此用法可以同时测试多个类
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demounit)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(dedede)
    # suite = unittest.TestSuite([suite1])
    # unittest.TextTestRunner().run(suite)