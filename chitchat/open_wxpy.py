# -*- coding: utf-8 -*-
"""
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
@file:  open_wxpy.py
@time: 2018/12/10 21:04
@Software: PyCharm
@Site    : 
@desc:
"""
from wxpy import *


class OpenWxpy(object):
    '''
    cache_path –
        设置当前会话的缓存路径，并开启缓存功能；为 None (默认) 则不开启缓存功能。
        开启缓存后可在短时l]=间内避免重复扫码，缓存失效时会重新要求登陆。
        设为 True 时，使用默认的缓存路径 ‘wxpy.pkl’。
    qr_path – 保存二维码的路径
    console_qr – 在终端中显示登陆二维码
    '''

    def __init__(self):
        self.bot = Bot(cache_path='logoo.pkl', qr_path='QR.png')
