# -*- coding: utf-8 -*-
"""
@__author__ :DingDong
@file: demo_unit.py
@time: 2018/1/18 20:57
@Entry Name:operating
"""
import logging
import time


# -------------------调用有参数的装饰器
def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running111" % func.__name__)
            elif level == "info":
                logging.info("%s is running2222" % func.__name__)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@use_logging(level="warn")
def foo(name='foo11'):
    time.sleep(1)
    print('i am foo %s' % name)
    time.sleep(1)


class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('%s 1class decorator runing' % self._func.__name__)
        self._func("777")
        print('2class decorator ending')


@Foo
def bar(name="66666"):
    time.sleep(1)
    print('bar %s' % name)
    time.sleep(1)


# 装饰器
def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__)  # 输出 'with_logging'
        print(func.__doc__)  # 输出 None
        return func(*args, **kwargs)

    return with_logging


# 函数
@logged
def f(x):
    """does some math"""
    print(x + x * x)
    return x + x * x

logged(f(1))

