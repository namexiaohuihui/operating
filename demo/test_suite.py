# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: test_suite.py
@time: 2017/7/16 16:28
@项目名称:operating
"""

from selenium import  webdriver


class demo:
    def __init__(self):
        print("开始呢？、、")

    def browser(self):
        import os
        # 实现全局变量的引用
        firefoxBin = os.path.abspath(r"E:\Program Files\Mozilla Firefox\firefox.exe")
        os.environ["webdriver.firefox.bin"] = firefoxBin

        # 代码加载火狐驱动
        firefoxgeckobdriver = os.path.abspath(r"E:\drivers\Drivers\geckodriver64.exe")

        self.browser = webdriver.Firefox(executable_path=firefoxgeckobdriver)
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

        self.browser.get("file:///C:/Users/70486/Desktop/demo.html")
    def qweasd(self):
        return self.qwe
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


def function_with_one_star(*parameter):
    print(t, type(t))
    assert t[0] != t[1] ,t[2]


def function_with_two_stars(**d):
    print(d, type(d))

if __name__ == '__main__':

    function_with_one_star(1, "11", 3,4)
    function_with_two_stars(a=1, b=2, c=3)

