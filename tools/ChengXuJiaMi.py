# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: ChengXuJiaMi.py
@time: 2018/4/28 11:56
"""

"""
通过hashlib做简单程序的加密
"""
import hashlib, random

def get_md5(s):
    ss = hashlib.md5(s.encode('utf-8')).hexdigest()
    print(ss)
    return ss

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)

def login(username, password):
    user = db[username]
    return user.password == get_md5(password + user.salt)



if __name__ == '__main__':
    db = {
        'michael': User('michael', '123456'),
        'bob': User('bob', 'abc999'),
        'alice': User('alice', 'alice2008')
    }
    print(login('michael', '123456'))