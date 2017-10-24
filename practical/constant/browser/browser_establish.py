# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: browser_establish.py
@time: 2017/6/20 22:24
"""
import os

import sys
from time import sleep

from  selenium import webdriver
from practical.constant.url_website.url_data import url_content
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
'''

#__new__创建一个对象，__init__实例化一个对象
class browser_confirm(object):
    # 定义一个全局变量


    # 单例类判断。如果该类创建过就不需要重新创建了
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(browser_confirm, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


    # 调用函数，实现打开谷歌浏览器的步骤
    def chrome_browser(self):
        try:
            # 实现全局变量的引用
            self.browser = webdriver.Chrome("E:\drivers\Drivers\chromedriver59-61.exe")
            print(u"打开谷歌")
        except:
            self.writeLog(self)
        return self.browser

    # 调用函数，实现打开ie浏览器的步骤
    def ie__browser(self):
        try:
            # 实现全局变量的引用
            self.browser = webdriver.Ie("E:\drivers\IEDriverServer.exe")
            print("打开IE")
        except:
            self.writeLog(self)
        return self.browser

    # 调用函数，实现打开火狐浏览器的步骤
    def firefox_browser(self):
       try:
           # 实现全局变量的引用
           firefoxBin = os.path.abspath(r"E:\Program Files\Mozilla Firefox\firefox.exe")
           os.environ["webdriver.firefox.bin"] = firefoxBin
           # 代码加载火狐驱动
           firefoxgeckobdriver = os.path.abspath(r"E:\drivers\geckodriver.exe")
           os.environ["webdriver.path"] = firefoxgeckobdriver
           self.browser = webdriver.Firefox()
           print("打开火狐")
       except:
           self.writeLog(self)

       return self.browser

    def call_browser(self,bro='cm'):
        # 如果能正常获取标题说明浏览器对象已经创建成功，否则就通过判断来创建浏览器
        try:
            self.browser.title
            return self.browser
        except:
            if bro == 'cm':
                self.browser = webdriver.Chrome()
            elif bro == 'ie':
                self.browser = webdriver.Ie()
            elif bro == 'fox':
                self.browser = webdriver.Firefox()
            else:
                print("你输入的不是浏览器的简写,cm = Chrome,ie = Ie,fox = Firefox", str)
                self.browser = webdriver.Chrome()
            return self.browser
        else:
            print ('如果没有异常执行这块代码')

    def url_opens(self):

        # 创建网址对象
        url = url_content()

        # 创建浏览器对象
        self.browser = self.chrome_browser()

        # 输入网址
        self.browser.get(url.return_landing())

        # 等待网页加载，加载时间为10s，加载完就跳过
        self.browser.implicitly_wait(30)

        title = self.browser.title

        #判断网址是否输入正确
        try:
            title.index('登录')
        except Exception :
            self.writeLog()

        return self.browser;


    def bro_wser(self):
        return self.browser;

    def writeLog(self):
        basename = os.path.splitext(os.path.basename(__file__))[0]
        print("自己定义的_文件出现错误,名为名=%s" % basename, )
        sleep(2)
        #退出程序
        sys.exit(0)
        #发生异常之后，raise之后的都不执行
        raise