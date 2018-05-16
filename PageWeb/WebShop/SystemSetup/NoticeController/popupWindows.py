# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: popupWindows.py
@time: 2018/5/11 14:25
"""
from tools.operationSelector import OperationSelector


def set_parameter_sharing(self, announ, announ_key, operation):
    content = self.overall[announ]
    print("公告内容 %s " % content)
    if content is None:  # 如何为空就直接重赋值
        content = self.LABLE_DF.iloc[0][announ_key]
    self._sendKeys_css_selectop(operation, content)
    return content


def set_popup_type(self, dn):
    choose = self.overall[dn.announType()]
    print("公告类型 %s " % choose)

    if choose is None:  # 如何为空就直接重赋值
        choose = self.LABLE_DF.iloc[0]["type"]

    if choose == "日常公告":
        _ele = self._visible_return_selectop(dn.operation_noticesort)  # 判断单选框是否存在
        self.visibleRadioSelected(_ele, True)
    elif choose == "维护公告":
        _ele = self._visible_return_selectop(dn.operation_noticesort2)  # 判断单选框是否存在
        self.visibleRadioSelected(_ele, True)
    else:
        self.log.info("按钮不存在不能点击 --> %s " % choose)

    return choose


def set_popup_city(self, dn):
    op_select = self.overall[dn.announCity()]
    print("公告城市 %s " % op_select)
    if op_select is None:  # 如何为空就直接重赋值
        op_select = self.LABLE_DF.iloc[0]["city"]
    OperationSelector(self.driver, dn.operation_select).setSelectorText(op_select)
    return op_select


def set_popup_title(self, dn):
    title = set_parameter_sharing(self, dn.announTitle(), "title", dn.operation_dail_input)
    return title


def set_popup_content(self, dn):
    content = set_parameter_sharing(self, dn.announContent(), "content", dn.operation_content_input)
    return content


def set_popup_time(self, dn):
    daily_time = self.overall[dn.announDeadline()]
    print("公告日期 %s " % daily_time)
    if daily_time is None:  # 如何为空就直接重赋值
        daily_time = self.LABLE_DF.iloc[0]["time"]

    # 找到数据然后进行切割操作,status_time : 开始时间, status_end :结束时间
    status_time,status_end = self.ti.cutting_time_current(daily_time)

    # 日期输入
    self.log.info("%s -------->涉及日期的发布暂时无法通过selenium进行测试操作" % self.FUNCTION_NAME)

    return status_time,status_end


def set_popup_all_data(self, dn):
    choose = set_popup_type(self, dn)  # 公告类型
    op_select = set_popup_city(self, dn)  # 公告城市
    title = set_popup_title(self, dn)  # 公告标题
    content = set_popup_content(self, dn)  # 公告内容
    status_time,status_end = set_popup_time(self, dn)  # 设置日期，将设置的数据进行返回
    daily_value = (choose, op_select, title, content, status_time, '暂时没有数据', status_end)
    self.LABLE_DF.iloc[0] = dict(zip(self.setDailyTitle(), daily_value))
    self.log.info("提交的参数为: ------> %s " % self.LABLE_DF.iloc[0])


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
