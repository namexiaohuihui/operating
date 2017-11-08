# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: DefinitionError.py
@time: 2017/7/16 17:41
@项目名称:operating
"""
import datetime
import os

import logging
import traceback


class definition_error(Exception):

    def erroe_get(self,basename,_browser_):

        # 组合日志文件名（当前文件名+当前时间）.比如：case_login_success_20150817192533
        logFile =  basename + "-" + datetime.datetime.now().strftime("%Y%m%d %H%M%S") + ".log"

        # 创建文件
        logging.basicConfig(filename=logFile)

        # 获取错误日志并打印
        error = traceback.format_exc()

        # 指定输出类型。。
        logging.error(error)

        # 截图
        _browser_.get_screenshot_as_file("./" + logFile + "-screenshot_error.png")

        # 打印错误
        print('调用错误类只会打印的数据 %s' % error)
