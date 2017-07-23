# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@time: 2017/6/26 21:36
@项目名称:operating
"""
class parameter_content(object):
    account = '---'
    password = '****'

    # 单例类判断。如果该类创建过就不需要重新创建了
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(parameter_content, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

    # 返回账号
    def return_account(self):
        return self.account

    # 返回密码
    def return_password(self):
        return self.password
