# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: test_suite.py
@time: 2017/7/16 16:28
@项目名称:operating
"""
import logging

if __name__ == '__main__':
    #定义执行者的名字
    logger = logging.getLogger("simple_example")
    #定义等级
    logger.setLevel(logging.DEBUG)

    # 输出到屏幕
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # 输出到文件
    fh = logging.FileHandler("log2.log")
    fh.setLevel(logging.WARNING)

    # 设置日志格式
    fomatter = logging.Formatter('%(asctime)s -%(name)s-%(levelname)s-%(module)s:%(message)s')
    ch.setFormatter(fomatter)
    fh.setFormatter(fomatter)
    logger.addHandler(ch)
    logger.addHandler(fh)

    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
