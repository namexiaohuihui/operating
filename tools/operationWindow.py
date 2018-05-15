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

from bs4 import BeautifulSoup
from python_utils import converters

from utils.browser_establish import browser_confirm
from utils.timeFromat import TimeFromat


def brows():
    be = browser_confirm()
    drivers = be.url_opens(r"F:\desktop\dijia.html")
    time.sleep(1)
    return drivers


def timeShijian():
    # 将时间进行切割，然后找出相应的年月日等信息
    parameter = "2018-05-14 01:02:03-2018-07-12 23:58:59"
    # 将日期进行切割并以时间戳的实行进行返回
    lelf_status, lelf_end = TimeFromat().cutting_time_current(parameter)
    # 将时间戳转换成时间格式
    localtime = time.localtime(lelf_status)
    print('localtime ----- >{}   '.format(localtime))
    # 定义时间格式的key和valuse数据并转换成dict
    tm_data = ('tm_year', 'tm_mon', 'tm_mday', 'tm_hour', 'tm_min', 'tm_sec')
    tm_time = (
        localtime.tm_year, localtime.tm_mon, localtime.tm_mday, localtime.tm_hour, localtime.tm_min, localtime.tm_sec)
    tm_dicts = dict(zip(tm_data, tm_time))
    print(tm_dicts)
    return tm_dicts


if __name__ == '__main__':
    drivers = brows()
    time.sleep(1)

    tm_dicts = timeShijian()
    # 点击输入框
    drivers.find_element_by_css_selector(".form-control.pull-right").click()
    # status_mon = drivers.find_element_by_css_selector(
    #     ".calendar.first.left>div.calendar-date>table>thead>tr")

    # 获取页面数据
    datatleThead = drivers.page_source
    # 将数据进行转换成BeautifulSoup
    soup = BeautifulSoup(datatleThead, "lxml")
    # 查找：在BeautifulSoup中是否有下面路径的数据
    adress = soup.select(".calendar.first.left")
    # 查找路径下面全部关于此标签的内容
    status_mon = adress[0].find('div',class_='calendar-date')
    status_mon = status_mon.find('table')
    status_mon = status_mon.find('thead')
    status_mon = status_mon.find('tr').text
    '''比较年月日然后来选择需要点击的对象'''
    # 根据界面的数据来切割出年月
    left_time = str.split(status_mon, '月')
    status_mon = converters.to_int(left_time[0])
    status_year = converters.to_int(left_time[1])
    # 年月需要点击的次数
    tm_year = 0 if tm_dicts['tm_year'] == status_year else (tm_dicts['tm_year'] - status_year) * 12
    tm_mon = tm_dicts['tm_mon'] - status_mon
    year_mon = tm_year + tm_mon
    print("需要点击的菜蔬 %s " % year_mon )
    assert year_mon >=0 ,"怎么出现了负数?、、、、、、、"
    for year in range(year_mon):
        #div.calendar.first.left > div.calendar-date > table > thead > tr:nth-child(1) > th.next.available

        jiantou = drivers.find_element_by_css_selector(
            ".calendar.first.left>div.calendar-date>table>thead>tr:nth-child(1)>th.next.available")
        drivers.execute_script("arguments[0].click();", jiantou)
    # div.calendar.first.left > div.calendar-date > table > tbody
    tbody_tr = drivers.find_element_by_css_selector('.calendar.first.left>div.calendar-date>table>tbody>tr')
    for tr in tbody_tr:
        print(tr.text)
    # drivers.close()
