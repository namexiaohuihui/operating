# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: popupWindows.py
@time: 2018/5/11 14:25
"""
import time

from python_utils import converters

from tools.operationSelector import OperationSelector


def pupop_button(self, dn):
    # 弹窗按钮点击
    self._visible_css_selectop(dn.operation_deadline_button)


# -----------------------------公告弹窗数据输入--------------------------------
def set_parameter_sharing(self, announ, operation):
    '''
    公告弹窗设置公告内容／标题 的 数据
    :param self:  操作对象
    :param announ: 用例数集中的key
    :param announ_key:  页面数据数集中的key
    :param operation: 需要输入的对象
    :return:
    '''
    content = str.strip(self.overall[announ])
    print("公告标题/内容 %s " % content)
    if content is None or content == '':  # 如何为空就直接重赋值
        content = self._visible_css_selectop_text(operation)
        print("chongxide", content)
        pass
    else:
        self._sendKeys_css_selectop(operation, content)
    return content


def choose_noticesort(self, operation):
    '''
    执行单选框的点击
    :param self: 操作对象
    :param operation:  单选框对象
    :return:
    '''
    _ele = self._visible_return_selectop(operation)  # 判断单选框是否存在
    self.visibleRadioSelected(_ele, True)


def set_popup_type(self, dn):
    '''
    判断公告类型，并执行点击动作
    :param self: 操作对象
    :param dn: 数集对象
    :return:
    '''
    choose = self.overall[dn.announType()]
    print("公告类型 %s " % choose)

    if choose is None:  # 如何为空就直接重新赋值
        pass
    else:
        if choose == "日常公告":
            choose_noticesort(self, dn.operation_noticesort)
        elif choose == "维护公告":
            choose_noticesort(self, dn.operation_noticesort2)
        else:
            self.log.info("公告按钮不存在不能点击 --> %s " % choose)
    return choose


def set_popup_city(self, dn):
    '''
    公告弹窗中城市下拉框的筛选
    :param self: 操作对象
    :param dn: 数集对象
    :return:
    '''
    op_select = self.overall[dn.announCity()]
    print("公告城市 %s " % op_select)
    if op_select is None:  # 如何为空就直接重赋值
        pass
    else:
        OperationSelector(self.driver, dn.operation_select).setSelectorText(op_select)
    return op_select


def set_popup_title(self, dn):
    '''
    公告弹窗中标题的输入
    :param self: 操作对象
    :param dn: 数集对象
    :return:
    '''
    title = set_parameter_sharing(self, dn.announTitle(), dn.operation_dail_input)
    return title


def set_popup_content(self, dn):
    '''
    公告弹窗中内容的输入
    :param self: 操作对象
    :param dn: 数集对象
    :return:
    '''
    content = set_parameter_sharing(self, dn.announContent(), dn.operation_content_input)
    return content


# -----------------------以下三个都是对日期进行点击----------------
def year_mon(self, tm_dicts, first_left):
    status_mon = self._visible_css_selectop_text("body > div.daterangepicker.dropdown-menu.show-calendar.opensleft > "
                                                 "div.%s > div.calendar-date > table > thead > "
                                                 "tr:nth-child(1) > th.month" % first_left)

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
        jiantou = self.driver.find_element_by_css_selector(
            "body > div.daterangepicker.dropdown-menu.show-calendar.opensleft > div.%s > "
            "div.calendar-date > table > thead > tr:nth-child(1) > th.next.available" % first_left)
        self.driver.execute_script("arguments[0].click();", jiantou)
    time.sleep(1)
    tbody_tr = self.driver.find_elements_by_css_selector(
        'body > div.daterangepicker.dropdown-menu.show-calendar.opensleft > div.%s >'
        ' div.calendar-date > table > tbody>tr' % first_left)
    tm_mday = str(tm_dicts['tm_mday'])

    date_selection(self, first_left, tbody_tr, tm_mday)


def date_selection(self, first_left, tbody_tr, tm_mday):
    bl_shenmegui = False
    for tr_len, tr in enumerate(tbody_tr):
        tbody_td = tr.find_elements_by_tag_name("td")
        for td_len, td in enumerate(tbody_td):
            td_class = td.get_attribute('class')
            if tm_mday == td.text and 'available' == td_class:
                bl_shenmegui = True
                break
        if bl_shenmegui:
            break
    if bl_shenmegui:
        print("dijihang %s dijige %s neirong %s" % (tr_len, td_len, tm_mday))
        shuzi = 'body > div.daterangepicker.dropdown-menu.show-calendar.opensleft > div.%s >' \
                ' div.calendar-date > table > tbody >tr:nth-child(%s)>td:nth-child(%s)' % (
                    first_left, (tr_len + 1), (td_len + 1))
        print(shuzi)
        tbody_tr_td_shuzi = self.driver.find_element_by_css_selector(shuzi)
        tbody_tr_td_shuzi.click()

    else:
        print("需要点击的数字没有出现")
    print("--------------------------------------------------------------------------------")


def click_year_mon(self, status_time, first):
    # 日期点击切换
    tm_dicts = set_popup_time(status_time)
    year_mon(self, tm_dicts, first)
    return tm_dicts


def drop_down_select(self, hourselect, minuteselect, tm_dicts):
    operSele = OperationSelector(self.driver, hourselect)
    # tm_data = ('tm_year', 'tm_mon', 'tm_mday', 'tm_hour', 'tm_min', 'tm_sec')
    print(tm_dicts['tm_hour'])
    print(tm_dicts['tm_min'])
    operSele.setSelectorIndex(tm_dicts['tm_hour'])
    operSele.setSelectData(minuteselect).setSelectorIndex(tm_dicts['tm_min'])


def set_bulletin_time(self, dn, daily_time):
    # 点击日期弹窗
    self._visible_css_selectop(dn.operation_deadline_input)

    # 将数据进行切割
    status_time, status_end = data_to_time(self, daily_time)
    first_left = 'calendar.first.left'
    second_right = 'calendar.second.right'

    # 设置开始时间
    tm_dicts = click_year_mon(self, status_time, first_left)
    hourselect_left = "body > div.daterangepicker.dropdown-menu.show-calendar.opensleft > div.%s > div.calendar-time > select.hourselect" % first_left
    minuteselect_left = "body > div.daterangepicker.dropdown-menu.show-calendar.opensleft > div.%s > div.calendar-time > select.minuteselect" % first_left
    drop_down_select(self, hourselect_left, minuteselect_left, tm_dicts)

    # 设置结束时间
    tm_dicts = click_year_mon(self, status_end, second_right)
    hourselect_right = "body > div.daterangepicker.dropdown-menu.show-calendar.opensleft > div.%s > div.calendar-time > select.hourselect" % second_right
    minuteselect_right = "body > div.daterangepicker.dropdown-menu.show-calendar.opensleft > div.%s > div.calendar-time > select.minuteselect" % second_right
    drop_down_select(self, hourselect_right, minuteselect_right, tm_dicts)

    return status_time, status_end


# -------------------------------以上三个都是对日期进行点击-------------------------------
def set_popup_time(time_status) -> "实力有限,无法对日期进行操作":
    '''
    公告弹窗中日期的选择
    :param self:操作对象
    :param dn:数集对象
    :return:
    '''
    # 将时间戳转换成时间格式
    localtime = time.localtime(time_status)

    # 定义时间格式的key和valuse数据并转换成dict
    tm_data = ('tm_year', 'tm_mon', 'tm_mday', 'tm_hour', 'tm_min', 'tm_sec')
    tm_time = (
        localtime.tm_year, localtime.tm_mon, localtime.tm_mday, localtime.tm_hour, localtime.tm_min, localtime.tm_sec)
    tm_dicts = dict(zip(tm_data, tm_time))
    return tm_dicts


def get_excle_time(self, dn):
    daily_time = self.overall[dn.announDeadline()]
    return daily_time


# --------------------------------公告弹窗数据识别-----------------------------
def data_to_determine(self, data, type):
    '''
    如果数据为真就直接返回，否则就重新赋值并进行返回操作
    :param self:
    :param data:
    :param type:
    :return:
    '''
    return data if data else self.LABLE_DF.iloc[0][type]


def data_to_time(self, daily_time):
    # 找到数据然后进行切割操作,status_time : 开始时间, status_end :结束时间
    status_time, status_end = self.ti.cutting_time_current(daily_time)

    return status_time, status_end


# --------------------------------公告弹窗输入入口-----------------------------
def release_popup_data(self, dn):
    # ---------------获取需要输入的内容----------------
    choose = set_popup_type(self, dn)  # 公告类型
    op_select = set_popup_city(self, dn)  # 公告城市
    title = set_popup_title(self, dn)  # 公告标题
    print("gonggaoneirpog.", title)
    content = set_popup_content(self, dn)  # 公告内容
    daily_time = get_excle_time(self, dn)  # 公告日期
    return choose, op_select, title, content, daily_time


def no_city_release(self, dn):
    # ---------------获取需要输入的内容----------------
    choose = set_popup_type(self, dn)  # 公告类型
    title = set_popup_title(self, dn)  # 公告标题
    content = set_popup_content(self, dn)  # 公告内容
    daily_time = get_excle_time(self, dn)  # 公告日期
    return choose, title, content, daily_time


def popup_all_time(self, dn, daily_time):
    daily_time = daily_time[len(daily_time) - 1]
    if daily_time:
        #   对弹窗时间进行点击
        set_bulletin_time(self, dn, daily_time)
        # 日期弹窗按钮点击
        pupop_button(self, dn)
    else:
        print("时间参数没有设置值，跳过..........")


def release_popup_all(self, dn):
    '''
    release_popup_all和set_popup_all_data都有对时间进行判断，不合并的原因是：
    release_popup_all ：如果用例没有数据那么退出
    set_popup_all_data　：如果用例没有数据那么就获取界面的数据来赋值
    :param self:
    :param dn:
    :return:
    '''
    daily_time = release_popup_data(self, dn)
    popup_all_time(self, dn, daily_time)


def no_release_popup_city(self, dn):
    '''
    release_popup_all和set_popup_all_data都有对时间进行判断，不合并的原因是：
    release_popup_all ：如果用例没有数据那么退出
    set_popup_all_data　：如果用例没有数据那么就获取界面的数据来赋值
    :param self:
    :param dn:
    :return:
    '''
    daily_time = no_city_release(self, dn)
    popup_all_time(self, dn, daily_time)


def set_popup_all_data(self, dn):
    '''
    release_popup_all和set_popup_all_data都有对时间进行判断，不合并的原因是：
    release_popup_all ：如果用例没有数据那么退出
    set_popup_all_data　：如果用例没有数据那么就获取界面的数据来赋值
    :param self:
    :param dn:
    :return:
    '''
    # 公告输入的内容:公告类型  公告城市  公告标题  公告内容　公告日期
    choose, op_select, title, content, daily_time = release_popup_data(self, dn)  #

    # 判断输入的内容是否为空，如果为空就返回界面原有的数据信息
    choose = data_to_determine(self, choose, "type")
    op_select = data_to_determine(self, op_select, "city")
    title = data_to_determine(self, title, "title")
    content = data_to_determine(self, content, "content")

    if daily_time:  # 如果用例上面有数据那么就直接用
        # 对弹窗时间进行点击
        status_time, status_end = set_bulletin_time(self, dn, daily_time)
        print("公告日期设置{}{}".format(status_time, status_end))
        # 日期弹窗按钮点击
        pupop_button(self, dn)

    else:  # 如果用例上面没有设置时间参数，那么就获取界面的数据信息
        daily_time = data_to_determine(self, daily_time, "time")
        status_time, status_end = data_to_time(self, daily_time)
        print("时间参数没有设置值，直接将界面数据进行转换")

    # 将全部设置的数据转成集合
    daily_value = (choose, op_select, title, content, status_time, '暂时没有数据', status_end)

    # 将集合内容为标题，以及集合内容为输入的数据组成列表
    self.LABLE_DF.iloc[0] = dict(zip(self.setDailyTitle(), daily_value))
    print("-----------------")
    self.log.info("提交的参数为: ------> %s " % self.LABLE_DF.iloc[0])
    print("-----------------")


# ----------------------------------获取公告弹窗内容-------------------------
def get_popup_data_obtain(self, dn):
    # 获取弹窗的数据并跟页面数据进行比较
    choose = self._visible_css_selectop_text(dn.operation_choose)  # 公告类型
    op_select = OperationSelector(self.driver, dn.operation_select).getSelectedOptions()
    dail = self._visible_css_selectop_attribute(dn.operation_dail_input)  # 标题
    content = self._visible_css_selectop_text(dn.operation_content_input)  # 公告内容
    # 公告日期,弹窗中的时间多出两个空格，不好进行比较所以去除
    deadline = self._visible_css_selectop_attribute(dn.operation_deadline_input).replace(" ", "")

    daily_keys = ("type", "city", "title", "content", "time")
    daily_value = (choose, op_select, dail, content, deadline)
    daily_keys = dict(zip(daily_keys, daily_value))

    daily_df = {}
    lable_daily = self.LABLE_DF.iloc[0]
    for k in daily_keys.keys():
        daily_df[k] = lable_daily[k]
    # 因为弹窗时间多空格，进行去除工作。所以外面的时间也要进行去除工作.
    daily_df["time"] = daily_df["time"].replace(" ", "")

    # 弹窗数据跟页面数据的比较情况
    self._verify_operator(daily_keys, daily_df)
