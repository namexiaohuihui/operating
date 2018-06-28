# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: operationWindow.py
@time: 2018/4/15 16:09
"""


class OperationWindow(object):
    """
    弹窗页面的日期选择操作.结果发现没办法操作那个箭头
    """
    pass


import time

from python_utils import converters

from tools.operationSelector import OperationSelector
from tools.browser_establish import browser_confirm
from tools.timeFromat import TimeFromat


def brows():
    be = browser_confirm()
    drivers = be.url_opens(r"F:\desktop\dijia.html")
    time.sleep(1)
    return drivers


def riqitime():
    # 将时间进行切割，然后找出相应的年月日等信息
    parameter = "2018-06-15 01:02:03-2018-08-12 04:05:06"
    # 将日期进行切割并以时间戳的实行进行返回
    lelf_status, lelf_end = TimeFromat().cutting_time_current(parameter)
    return lelf_status, lelf_end


def timeShijian(lelf_status):
    # 将时间戳转换成时间格式
    localtime = time.localtime(lelf_status)
    # print('localtime ----- >{}   '.format(localtime))
    # 定义时间格式的key和valuse数据并转换成dict
    tm_data = ('tm_year', 'tm_mon', 'tm_mday', 'tm_hour', 'tm_min', 'tm_sec')
    tm_time = (
        localtime.tm_year, localtime.tm_mon, localtime.tm_mday, localtime.tm_hour, localtime.tm_min, localtime.tm_sec)
    tm_dicts = dict(zip(tm_data, tm_time))
    # print(tm_dicts)
    return tm_dicts


def yuefendianjiqiehuan(first_left):
    status_mon = drivers.find_element_by_css_selector("body > div:nth-child(13) > div.%s > "
                                                      "div.calendar-date > table > thead > tr:nth-child(1) > th.month" % first_left).text
    # body > div:nth-child(13) > div.calendar.first.left > div.calendar-date > table > thead > tr:nth-child(1) > th.month
    '''比较年月日然后来选择需要点击的对象'''
    # 根据界面的数据来切割出年月
    print("界面的月份 %s " % status_mon)
    left_time = str.split(status_mon, '月')
    status_mon = converters.to_int(left_time[0])
    status_year = converters.to_int(left_time[1])
    # 开始年月需要点击的次数
    tm_year = 0 if tm_dicts['tm_year'] == status_year else (tm_dicts['tm_year'] - status_year) * 12
    tm_mon = tm_dicts['tm_mon'] - status_mon
    year_mon = tm_year + tm_mon
    print("需要点击的次数 %s " % year_mon)
    for year in range(year_mon):
        # 箭头的路径就是这样不能改动body > div:nth-child(13) > div.calendar.first.left > div.calendar-date > table > thead > tr:nth-child(1) > th.next.available
        jiantou = drivers.find_element_by_css_selector(
            "body > div:nth-child(13) > div.%s > div.calendar-date > table > thead > tr:nth-child(1) > th.next.available" % first_left)
        drivers.execute_script("arguments[0].click();", jiantou)
        time.sleep(1)
    # body > div:nth-child(13) > div.calendar.second.right > div.calendar-date > table > thead > tr:nth-child(1) > th.month
    time.sleep(1)
    tbody_tr = drivers.find_elements_by_css_selector(
        'body > div:nth-child(13) > div.%s > div.calendar-date > table > tbody>tr' % first_left)
    tm_mday = str(tm_dicts['tm_mday'])

    riqitianshudianji(first_left, tbody_tr, tm_mday)


def riqitianshudianji(first_left, tbody_tr, tm_mday):
    bl_shenmegui = False
    for tr_len, tr in enumerate(tbody_tr):
        tbody_td = tr.find_elements_by_tag_name("td")
        print("------> %s td", len(tbody_td))
        for td_len, td in enumerate(tbody_td):
            td_class = td.get_attribute('class')
            if td.text:
                print(td.text, "--------", tm_mday)
            else:
                print("!-!")
            if tm_mday == td.text and 'available' == td_class:
                print("jinlailema")
                bl_shenmegui = True
                break
        if bl_shenmegui:
            print("zheli ne ??、、、")
            break
    if bl_shenmegui:
        print("dijihang %s dijige %s neirong %s" % (tr_len, td_len, tm_mday))
        shuzi = 'body > div:nth-child(13) > div.%s >' \
                ' div.calendar-date > table > tbody >tr:nth-child(%s)>td:nth-child(%s)' % (
                    first_left, (tr_len + 1), (td_len + 1))
        print(shuzi)
        tbody_tr_td_shuzi = drivers.find_element_by_css_selector(shuzi)
        tbody_tr_td_shuzi.click()
        # tm_data = ('tm_year', 'tm_mon', 'tm_mday', 'tm_hour', 'tm_min', 'tm_sec')
        # drivers.close()
    else:
        print("需要点击的数字没有出现")
    print("--------------------------------------------------------------------------------")


def set_select(hourselect, minuteselect, tm_dicts):
    operSele = OperationSelector(drivers, hourselect)
    # tm_data = ('tm_year', 'tm_mon', 'tm_mday', 'tm_hour', 'tm_min', 'tm_sec')
    print(tm_dicts['tm_hour'])
    print(tm_dicts['tm_min'])
    operSele.setSelectorIndex(tm_dicts['tm_hour'])
    operSele.setSelectData(minuteselect).setSelectorIndex(tm_dicts['tm_min'])


if __name__ == '__main__':
    first_left = 'calendar.first.left'
    second_right = 'calendar.second.right'
    drivers = brows()

    # 点击输入框
    drivers.find_element_by_css_selector(".form-control.pull-right").click()
    lelf_status, lelf_end = riqitime()
    #
    # # 设置开始时间
    tm_dicts = timeShijian(lelf_status)
    # yuefendianjiqiehuan(first_left)
    hourselect_left = "body > div:nth-child(13) > div.%s > div.calendar-time > select.hourselect" % first_left
    minuteselect_left = "body > div:nth-child(13) > div.%s > div.calendar-time > select.minuteselect" % first_left

    set_select(hourselect_left, minuteselect_left, tm_dicts)

    # # 设置结束时间
    tm_dicts = timeShijian(lelf_end)
    # yuefendianjiqiehuan(second_right)

    # 下拉操作框
    # body > div:nth-child(13) > div.calendar.first.left > div.calendar-time > select.hourselect
    # body > div:nth-child(13) > div.calendar.first.left > div.calendar-time > select.minuteselect
    hourselect_right = "body > div:nth-child(13) > div.%s > div.calendar-time > select.hourselect" % second_right
    minuteselect_right = "body > div:nth-child(13) > div.%s > div.calendar-time > select.minuteselect" % second_right

    set_select(hourselect_right, minuteselect_right)
