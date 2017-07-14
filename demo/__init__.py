# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: __init__.py.py
@time: 2017/6/20 21:43
"""
import datetime
import os
import time

import logging
import traceback

from constant.browser.browser_establish import browser_confirm
from constant.parameter.parameter_data import parameter_content
from constant.url_website.url_data import url_content
from operation import selenium_click
from operation import selenium_input
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
global _browser_

global url

global parame

def start_chegnxu():
    bc = browser_confirm.__new__(browser_confirm)
    url = url_content.__new__(url_content)
    _browser_ = bc.chrome_browser()
    _browser_.get(url.return_account())
    _browser_.implicitly_wait(30)

def browesr():

    parame = parameter_content.__new__(parameter_content)

    try:
        start_chegnxu()
        selenium_input.id_input('phone',parame.return_account())
        selenium_input.id_input('password',parame.return_password())

    except Exception as msg:
        # 组合日志文件名（当前文件名+当前时间）.比如：case_login_success_20150817192533
        basename = os.path.splitext(os.path.basename(__file__))[0]
        logFile = basename + "-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".log"
        # 创建文件
        logging.basicConfig(filename=logFile)
        # 获取错误日志并打印
        s = traceback.format_exc()
        # 指定输出类型。。
        logging.error(s)
        # 截图
        _browser_.get_screenshot_as_file("./" + logFile + "-screenshot_error.png")

if __name__ == '__main__':
    browesr()