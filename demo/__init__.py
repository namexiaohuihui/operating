# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: __init__.py.py
@time: 2017/6/20 21:43
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
import unittest

class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""
    #setUp用来为测试准备环境，tearDown用来清理环境.每执行一次函数就会调用它们
    #setUpClass() 与 tearDownClass():从头到尾只调用一次
    @classmethod
    def setUpClass(cls):
        print ("do something before test.Prepare environment.")

    @classmethod
    def tearDownClass(cls):
        print ( "do something after test.Clean up.")
    def test_add(seft):
        """Test method add(a, b)"""
        # seft.assertNotEqual(3, seft.add(2, 2))
        print(seft.add(2, 2))
        seft.assertEqual(3, seft.add(5, 2))
        print(seft.add(1, 2))

    def test_minus(seft):
        """Test method minus(a, b)"""
        #  seft.assertEqual(1, seft.minus(3, 2))
        print(seft.minus(3, 2))

    def test_multi(seft):
        """Test method multi(a, b)"""
        #  seft.assertEqual(6, seft.multi(2, 3))
        print(seft.multi(2, 3))

    #@unittest.skip("I don't want to run this case.")
    def test_divide(seft):
        """Test method divide(a, b)"""
        #  seft.assertEqual(2, seft.divide(6, 3))
        #  seft.assertEqual(2.5, seft.divide(5, 2))
        seft.skipTest('Do not run this.')
        print(seft.divide(6, 3))
        print(seft.divide(5, 2))

    def add(seft, i, j):
        return i + j
    def minus(seft, i, j):
        return i - j
    def multi(seft, i, j):
        return i * j
    def divide(seft, i, j):
        return i / j


if __name__ == '__main__':
    unittest.main()
