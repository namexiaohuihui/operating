# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: logger.py
@time: 2017/12/21 22:02
@项目名称:operating
"""
import logging, time
import os

# log_path是存放日志的路径
cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path), 'logs')

# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path): os.mkdir(log_path)


class Log():
    def __init__(self, executor="Root", classification='Journal'):
        # 文件的命名
        self.logname = os.path.join(log_path, classification + '-%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger(executor)  # 定义执行者的名字
        self.logger.setLevel(logging.DEBUG)  # 设置输入语句的等级
        # 日志输出格式
        # self.formatter = logging.Formatter('[%(asctime)s] - %(name)s - %(filename)s] - %(levelname)s: %(message)s')
        self.formatter = logging.Formatter('[%(asctime)s] - %(name)s] - %(levelname)s: %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, 'a')  # 追加模式  这个是python2的
        # fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


if __name__ == "__main__":
    cur_path = os.path.dirname(os.path.realpath(__file__))
    print(cur_path)
    log_path = os.path.join(os.path.dirname(cur_path), 'logs')
    print(log_path)
