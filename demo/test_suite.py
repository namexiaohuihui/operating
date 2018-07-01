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
    # with open("nihao.txt","r",encoding='utf8') as klu:
    #     result = klu.read()
    #     print(result)
    #
    # nishibushi =[]
    # import csv
    # with open(r"C:\Users\70486\Desktop\买家记录300.csv", "r") as klu:
    #     result = csv.reader(klu)
    #     print(type(result))
    #     for row in result:
    #         nishibushi.append(row)
    #         pass
    # with open(r"C:\Users\70486\Desktop\是在.csv", "w",newline='') as nihf:
    #     result = csv.writer(nihf)
    #     # print(nishibushi)
    #     for row in nishibushi:
    #         result.writerow(row)
    pass
