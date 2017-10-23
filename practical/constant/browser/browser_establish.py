# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: browser_establish.py
@time: 2017/6/20 22:24
"""
import os

import sys

from practical.constant.url_website.url_data import url_content
from practical.CuttingOperation import stringCutting
from practical.Program_exit import exit_os_sys
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
from  selenium import webdriver


#__new__创建一个对象，__init__实例化一个对象
class browser_confirm(object):
    # 定义一个全局变量
    global _browser_

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
            self._browser_ = webdriver.Chrome("E:\drivers\Drivers\chromedriver59-61.exe")
            print(U"打开谷歌")
        except:
            self.writeLog(self)
        return self._browser_

    # 调用函数，实现打开ie浏览器的步骤
    def ie__browser(self):
        try:
            # 实现全局变量的引用
            self._browser_ = webdriver.Ie("E:\drivers\IEDriverServer.exe")
            print(U"打开谷歌")
        except:
            self.writeLog(self)
        return self._browser_

    # 调用函数，实现打开火狐浏览器的步骤
    def firefox_browser(self):
       try:
           # 实现全局变量的引用
           firefoxBin = os.path.abspath(r"E:\Program Files\Mozilla Firefox\firefox.exe")
           os.environ["webdriver.firefox.bin"] = firefoxBin
           # 代码加载火狐驱动
           firefoxgeckobdriver = os.path.abspath(r"E:\drivers\geckodriver.exe")
           os.environ["webdriver.path"] = firefoxgeckobdriver
           self._browser_ = webdriver.Firefox()
           print(U"打开火狐")
       except:
           self.writeLog(self)

       return self._browser_

    def call_browser(self,bro='cm'):
        # 如果能正常获取标题说明浏览器对象已经创建成功，否则就通过判断来创建浏览器
        try:
            self._browser_.title
            return self._browser_
        except:
            if bro == 'cm':
                self._browser_ = webdriver.Chrome()
            elif bro == 'ie':
                self._browser_ = webdriver.Ie()
            elif bro == 'fox':
                self._browser_ = webdriver.Firefox()
            else:
                print(U"你输入的不是浏览器的简写,cm = Chrome,ie = Ie,fox = Firefox", str)
                self._browser_ = webdriver.Chrome()
            return self._browser_
        else:
            print (u'如果没有异常执行这块代码')

    def url_opens(self):
        print("do something before test.Prepare environment.")

        # 创建网址对象
        url = url_content.__new__(url_content)

        # 创建浏览器对象
        _browser_ = browser_confirm.chrome_browser(self)

        # 输入网址
        _browser_.get(url.return_landing())

        # 等待网页加载，加载时间为10s，加载完就跳过
        _browser_.implicitly_wait(10)

        # 验证网址是否正确，如果错误就直接退出程序
        whole = _browser_.current_url
        if whole.index('ad') == -1:
            print('Web page open failed')

        return _browser_;

    def bro_wser(self):
        return self._browser_;

    def writeLog(self):
        basename = os.path.splitext(os.path.basename(__file__))[0]
        print("自己定义的_文件出现错误,名为名=%s" % \
              basename, )
        sys.exit(0)
        raise