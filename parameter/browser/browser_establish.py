# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: browser_establish.py
@time: 2017/6/20 22:24
"""
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

# 定义一个全局变量
global _browser_


class browser_confirm(object):
    # 单例类判断。如果该类创建过就不需要重新创建了
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(browser_confirm, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class   browser_using(browser_confirm):
    # 调用函数，实现打开谷歌浏览器的步骤
    def chrome_browser(self):
        # 实现全局变量的引用
        global _browser_
        _browser_ = webdriver.Chrome()
        return _browser_

    # 调用函数，实现打开ie浏览器的步骤
    def ie__browser(self):
        # 实现全局变量的引用
        global _browser_
        _browser_ = webdriver.Ie
        return _browser_

    # 调用函数，实现打开火狐浏览器的步骤
    def firefox_browser_(self):
        # 实现全局变量的引用
        global _browser_
        _browser_ = webdriver.Firefox()
        return _browser_

    def call_browser(str):
        # 实现全局变量的引用
        global _browser_
        # 如果能正常获取标题说明浏览器对象已经创建成功，否则就通过判断来创建浏览器
        try:
            _browser_.title
            return _browser_
        except:
            if str == 'cm':
                _browser_ = webdriver.Chrome()
            elif str == 'ie':
                _browser_ = webdriver.Ie()
            elif set == 'fox':
                _browser_ = webdriver.Firefox()
            else:
                print(U"你输入的不是浏览器的简写,cm = Chrome,ie = Ie,fox = Firefox", str)
                _browser_ = webdriver.Chrome()
            return _browser_