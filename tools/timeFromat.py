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

today = '今日'
yesterday = '昨日'
seven_day = '最近7日'
thirty_day = '最近30日'
add_day = '全部'


def zero_day(zero):
    if zero == "00":
        return "0"
    else:
        return zero


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

    def value_time_start_end(self, start_time, end_time):
        """
        开始时间戳和结束时间戳
        并转成时间格式
        :param day_time:
        :return:
        """
        # 将时间戳转成时间
        start_time = time.localtime(start_time)
        end_time = time.localtime(end_time)
        # 拼接开始时间和结束时间,别问为什么程序设计如此
        return start_time, end_time

    def today_to_stamp(self, day=0):
        """
        计算指定日期开始时间戳和当天时间戳
        :param day:  +-N
        :return:
        """
        # 今天日期
        today = datetime.date.today()
        yes_time = today + datetime.timedelta(days=int(day))  # 指定某天的日期
        print("多少天前: %s 以及最前的那天 %s" % (day, yes_time))
        # 指定日期的开始时间戳
        today_start_time = int(time.mktime(time.strptime(str(yes_time), '%Y-%m-%d')))

        # 当前时间
        today_end_time = self.currentToStamp()
        return today_start_time, today_end_time

    def todat_to_stamp_day(self, day):
        """
        当前时间到N天的时间戳数据
        :param day:  +-N
        :return:
        """
        # 当前时间
        today_end_time = self.currentToStamp()
        # 86400为一天的秒数
        today_start_time = today_end_time + (day * 86400)
        return today_start_time, today_end_time

    def today_to_specified(self, day=0):
        """
        指定某天的开始时间戳和结束时间戳
        :param day:  +-N
        :return:
        """
        # 今天日期
        today = datetime.date.today()
        yes_time = today + datetime.timedelta(days=int(day))  # 指定某天的日期
        print("多少天前: %s 以及最前的那天 %s" % (day, yes_time))
        # 指定日期的开始时间戳
        today_start_time = int(time.mktime(time.strptime(str(yes_time), '%Y-%m-%d')))

        # 某天开始时间戳+86399 = 某天结束时间的时间戳
        today_end_time = today_start_time + 86399

        return today_start_time, today_end_time

    def today_to_past(self, day=0):
        """
        过去时间到昨天范围的时间戳
        :param day:
        :return:
        """
        # 今天日期
        today = datetime.date.today()

        # 指定某天的日期
        yes_time = today + datetime.timedelta(days=int(day))

        # 指定日期的开始时间戳
        today_start_time = int(time.mktime(time.strptime(str(yes_time), '%Y-%m-%d')))

        # 昨天结束时间戳
        today_end_time = int(
            time.mktime(time.strptime(str(today + datetime.timedelta(days=int(-1))), '%Y-%m-%d'))) + 86399

        return today_start_time, today_end_time

    def day_time_date(self, day_value):
        if "至" in day_value:  # 设置的时间为自定义那么直接返回,不需要进行判断
            day_value = str.split(day_value, "至")
            day_value = [t.rstrip().lstrip() for t in day_value]
            start_time = self.timeToStamp(day_value[0])
            end_time = self.timeToStamp(day_value[1])

        elif day_value == today:
            start_time, end_time = self.today_to_stamp(0)
            pass

        elif day_value == yesterday:
            start_time, end_time = self.today_to_specified(-1)
            pass

        elif day_value == seven_day:
            start_time, end_time = self.todat_to_stamp_day(-6)
            pass

        elif day_value == thirty_day:
            start_time, end_time = self.todat_to_stamp_day(-29)
            pass

        elif day_value == add_day:
            start_time, end_time = self.todat_to_stamp_day(-365)

        # 设置的时间不是为自定义时需要进行转换在返回
        start_time, end_time = self.value_time_start_end(start_time, end_time)
        start_time = {"year": time.strftime('%Y-%m-%d', start_time),
                      "time": zero_day(time.strftime('%H', start_time)),
                      "seconds": time.strftime('%M', start_time)}
        end_time = {"year": time.strftime('%Y-%m-%d', end_time),
                    "time": zero_day(time.strftime('%H', end_time)),
                    "seconds": time.strftime('%M', end_time)}
        # print(start_time)
        # print(end_time)
        return start_time, end_time

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
        """
        根据时间输出指定格式的数据
        :return:
        """
        format = time.strftime('%a, %d %b %y %H:%M', time.localtime())
        return format

    def at_the_present_day(self):
        """
        返回当前的年月日
        :return:
        """
        y_m_d = datetime.date.today()
        y_m_d = str(y_m_d)
        return y_m_d

    def get_time_ym(self):
        """
        返回当前年月
        :return:
        """
        y = time.strftime('%Y', time.localtime())
        m = time.strftime('%m', time.localtime())
        y_m = "%s年%s月" % (y, m)
        return y_m

    def dormancy_time(self, sp: int = 0.5):
        """
        延迟
        :param sp:
        :return:
        """
        time.sleep(sp)

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
    # t1 = TimeFromat()
    pass
