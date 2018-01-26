# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: test_suite.py
@time: 2017/7/16 16:28
@项目名称:operating
"""

from selenium import  webdriver
from selenium.webdriver.support import expected_conditions


class demo:
    def __init__(self):
        print("开始呢？、、")

    def nihaoma(self):
        self.qwe = 33
        print("我不好")
        # unittest.main :unittest执行的方式一。默认执行全部
        # unittest.main(verbosity=2)

        # unittest执行的方式二: 通过添加来执行
        # 构造测试集
        # suite = unittest.TestSuite()
        # suite.addTest(demounit("testStart"))
        # suite.addTest(demounit("testOne"))
        # suite.addTest(demounit("testTwo"))
        # 执行测试
        # runner = unittest.TextTestRunner()
        # runner.run(suite)

        # unittest执行的方式3: 通过添加来执行
        # 此用法可以同时测试多个类
        # suite1 = unittest.TestLoader().loadTestsFromTestCase(demounit)
        # suite2 = unittest.TestLoader().loadTestsFromTestCase(dedede)
        # suite = unittest.TestSuite([suite1])
        # unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
    print([x * 2 + 10 for x in foo])
    ttt = [x for x in foo if x % 3 == 0]
    print(ttt)
    # function_with_one_star(1, "11", 3,4)
    # function_with_two_stars(a=1, b=2, c=3)

