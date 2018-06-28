# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: timeFromat.py
@time: 2018/4/17 16:17
https://www.cnblogs.com/zhangxinqi/p/7687862.html 大佬文章
"""

import calendar
import datetime
import time


class TimeFromat(object):

    # 单例类判断。如果该类创建过就不需要重新创建了
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(TimeFromat, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

    def timeToStamp(self, tm, tm_format="%Y-%m-%d %H:%M:%S"):
        # 根据日期转换成时间戳
        tm = time.strptime(tm, tm_format)
        timeStamp = int(time.mktime(tm))
        return timeStamp

    def structToStamp(self, tm):
        # struct_time时间格式转时间戳
        timeStamp = int(time.mktime(tm))
        return timeStamp

    def stampToTime(self, tm, tm_format="%Y-%m-%d %H:%M:%S"):
        # 将时间戳转换成时间
        if type(tm) is str:
            tm = int(tm)
        timeArray = time.strftime(tm_format, time.localtime(tm))
        return timeArray

    def currentToStamp(self):
        # 获取当前时间转成时间戳
        currentTime = time.localtime(time.time())
        return self.structToStamp(currentTime)

    def currentToTime(self):
        # 获取当前时间戳转成时间
        currentTime = time.time()
        return self.stampToTime(currentTime)

    def cutting_time(self, time_msg, start=0, middle=19, again=20, end=0):
        # 指定位置对时间数据进行切割
        if end == 0:
            end = len(time_msg)
        sttus = time_msg[start:middle]
        enmd = time_msg[again:end]
        return sttus, enmd

    def cutting_time_current(self, time_msg):
        cutting = self.cutting_time(time_msg)
        sttus = self.timeToStamp(cutting[0])
        enmd = self.timeToStamp(cutting[1])
        return sttus, enmd

    def today_to_stamp(self, day):
        # 今天日期
        today = datetime.date.today()
        yes_time = today + datetime.timedelta(days=int(day))  # 指定某天的日期
        # print("多少天前: %s 以及最前的那天 %s" % (day, yes_time))
        # 今天开始时间戳
        today_start_time = int(time.mktime(time.strptime(str(yes_time), '%Y-%m-%d')))

        # 今天结束时间戳(当前时间)
        today_end_time = self.currentToStamp()

        return today_start_time, today_end_time

    def rizhi(self, years=0):
        '''
        打印指定年根的日历
        每日宽度间隔为w字符
        每行长度为21* W+18+2* C。l(字母L)是每星期行数
        每行log显示的m个月份
        :param years:
        :return:
        '''
        if years <= 0:
            years = int(time.strftime('%Y', time.localtime()))
        y_calendar = calendar.calendar(years)
        print(y_calendar)
        return y_calendar

    def times_format(self):
        format = time.strftime('%a, %d %b %y %H:%M', time.localtime())
        return format

    def neizhidefangfa(self):
        # 英文格式的时间输出: Wed Jun 27 12:00:04 2018
        print(time.asctime(time.localtime(time.time())))
        # 打印当前时区，并转换字符格式防止乱码 : 中国标准时间
        a = time.tzname[0]
        b = a.encode('latin-1').decode('gbk')
        print(b)
        # 打印时间和时区，但是乱码。无法解决。：2018-06-27 12:00:04 26-?D1¨²¡À¨º¡Á?¨º¡À??
        print(time.strftime('%Y-%m-%d %H:%M:%S %W-%Z', time.localtime()))
        print(time.strftime('%H:%M:%S', time.localtime()))
        year = time.strftime('%Y', time.localtime())  # 四位数的年份表示（000-9999）
        print(year)
        print(time.strftime('%y', time.localtime()))  # 两位数的年份表示（00-99）
        print(time.strftime('%a', time.localtime()))  # 本地简化星期名称
        print(time.strftime('%b', time.localtime()))  # 本地简化的月份名称
        print(time.strftime('%d', time.localtime()))  # 月内中的一天（0-31）
        # [Tue, 19 Jun 18 18:10:30 +0800][INFO] 13566667878验证码：123456
        print(self.times_format())


if __name__ == '__main__':
    print(TimeFromat().today_to_stamp(0))
