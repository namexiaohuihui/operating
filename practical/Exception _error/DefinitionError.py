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
    def __init__(self, message, status):
        super().__init__(message, status)
        self.message = message
        self.status = status
        # 组合日志文件名（当前文件名+当前时间）.比如：case_login_success_20150817192533
        basename = os.path.splitext(os.path.basename(__file__))[0]
        logFile = basename + "-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".log"
        # 创建文件
        logging.basicConfig(filename=logFile)
        # 获取错误日志并打印
        s = traceback.format_exc()
        # 指定输出类型。。
        logging.error(s)
