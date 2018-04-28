# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: DefinitionErrors.py
@time: 2017/7/16 17:41
@项目名称:operating
"""
import datetime
import os
import traceback

from tools.Logger import Log

# 错误截图的存放路径
cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(cur_path, 'imgs')

# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path): os.mkdir(log_path)

def error_get(basename, _browser_):

    # 组合日志文件名（当前文件名+当前时间）.比如：case_login_success_20150817192533
    logFile = basename + "-" + datetime.datetime.now().strftime("%Y%m%d %H%M%S")

    # 获取错误日志并打印
    error = traceback.format_exc()
    log = Log(basename, "ERROR")
    log.info(error)

    _browser_.get_screenshot_as_file(os.path.join(log_path, logFile + ".png"))


def error_output(basename, _browser_):

    error = traceback.format_exc()
    log = Log(basename, classification='ERROR')
    log.info("发生错误时打印的错误数据信息: %s" % error)

    basename = basename + ".png"
    _browser_.get_screenshot_as_file(os.path.join(log_path, basename))
