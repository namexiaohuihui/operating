# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: timeFromat.py
@time: 2018/4/17 16:17
"""
import time


class TimeFromat(object):

    # 单例类判断。如果该类创建过就不需要重新创建了
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(TimeFromat, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

    def timeToStamp(self, tm):
        # 根据日期转换成时间戳
        tm = time.strptime(tm, '%Y-%m-%d %H:%M:%S')
        timeStamp = int(time.mktime(tm))
        return timeStamp

    def structToStamp(self, tm):
        # struct_time时间格式转时间戳
        timeStamp = int(time.mktime(tm))
        return timeStamp

    def stampToTime(self, tm):
        # 将时间戳转换成时间
        if type(tm) is str:
            tm = int(tm)
        timeArray = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(tm))
        return timeArray

    def currentToStamp(self):
        # 获取当前时间转成时间戳
        currentTime = time.localtime(time.time())
        return self.structToStamp(currentTime)

    def currentToTime(self):
        # 获取当前时间戳转成时间
        currentTime = time.time()
        return self.stampToTime(currentTime)

    def cutting_time(self,time_msg,start = 0 ,middle = 19,again = 20,end =0):
        # 指定位置对时间数据进行切割
        if end == 0:
            end = len(time_msg)
        sttus = time_msg[start:middle]
        enmd = time_msg[again:end]
        return sttus,enmd

    def cutting_time_current(self,time_msg):
        cutting = self.cutting_time(time_msg)
        sttus = self.timeToStamp(cutting[0])
        enmd = self.timeToStamp(cutting[1])
        return sttus, enmd

if __name__ == '__main__':
    time_stauts = "2017-08-03 00:00:00-2017-08-03 23:59:59"

    cutting =  TimeFromat().cutting_time_current(time_stauts)
    print(cutting[0])
    print(cutting[1])
    localtime = time.localtime(cutting[0])
    print("Local current time :", localtime)
    print("Local current time :", time.time())
