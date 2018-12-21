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
@author: 70486
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file: test_file.py
@time: 2018/7/31 13:57
@desc:
'''
from demo.test_file2 import nihao
"""
http://www.cnblogs.com/cenyu/p/5713686.html
# Python的hasattr() getattr() setattr() 函数使用方法详解

hasattr(object, name)
判断一个对象里面是否有name属性或者name方法，返回BOOL值，有name特性返回True， 否则返回False。
需要注意的是name要用括号括起来

getattr(object, name[,default])
获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选。
需要注意的是，如果是返回的对象的方法，返回的是方法的内存地址，如果需要运行这个方法，
可以在后面添加一对括号。

setattr(object, name, values)
给对象的属性赋值，若属性不存在，先创建再赋值。

一种综合的用法是：判断一个对象的属性是否存在，若不存在就添加该属性。
#age属性不存在时，设置该属性
if getattr(t, "age", None) is None:
    setattr(t, "age", "18")
age = getattr(t, "age")
"""

if __name__ == '__main__':
    buhao = nihao()

    qwe = getattr(buhao, "test_s4")

