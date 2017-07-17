# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: url_data.py
@time: 2017/6/26 21:03
@项目名称:operating
"""

class url_content(object):
    #主线链接
    url_thread = 'http:----/'
    #登录链接
    url_login = url_thread + 'user/login?f=/'

    # 单例类判断。如果该类创建过就不需要重新创建了
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(url_content, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

    def return_account (self):
        return self.url_thread

    def return_landing (self):
        return self.url_login
