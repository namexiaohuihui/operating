# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: DefinitionError.py
@time: 2017/7/16 17:41
@项目名称:operating
"""

class definition_error(Exception):
    def __init__(self, value=None):
        if not value:print(value)

    def error_get(self, basename, _browser_):
        import datetime
        import os
        import logging
        import traceback

        # 组合日志文件名（当前文件名+当前时间）.比如：case_login_success_20150817192533
        logFile = basename + "-" + datetime.datetime.now().strftime("%Y%m%d %H%M%S")

        # 获取错误日志并打印
        error = traceback.format_exc()
        from practical.utils.logger import Log
        log = Log(basename, "ERROR")
        log.info(error)

        # 截图
        # _browser_.get_screenshot_as_file("./" + logFile + "-screenshot_error.png")
        cur_path = os.path.dirname(os.path.realpath(__file__))
        log_path = os.path.join(os.path.dirname(cur_path), 'logs')
        _browser_.get_screenshot_as_file(os.path.join(log_path, logFile + "-screenshot_error.png"))

    def error_output(self,basename,message, _browser_):
        from practical.utils.logger import Log
        import os
        import inspect

        self.log = Log(name_tion, classification='ERROR')
        self.log.info("sign_switching_logon 出现错误.. %s" % message)

        # 截图
        # _browser_.get_screenshot_as_file("./" + logFile + "-screenshot_error.png")
        cur_path = os.path.dirname(os.path.realpath(__file__))
        log_path = os.path.join(os.path.dirname(cur_path), 'logs')
        _browser_.get_screenshot_as_file(os.path.join(log_path, name_tion + "-screenshot_error.png"))
