# -*- coding: utf-8 -*-
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
@author:  ln_company
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file: ewrwerwerew.py
@time: 2018/8/10 9:37
@desc:
'''
import pytest

@pytest.fixture()
def fix_err(x):
    raise x

@pytest.mark.incremental
class TestUserHandling:
    def test_login(self, fix_err):
        print('test_login')

        try:
            raise RuntimeError("error")
        except AssertionError as e:
            pass
        except:
            fix_err(e)
    def test_modification(self,login):
        print('test_modification')

    def test_deletion(self):
        print('test_deletion')


def test_normal():
    print('test_normal')
