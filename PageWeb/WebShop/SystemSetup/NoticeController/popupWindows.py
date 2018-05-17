# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: popupWindows.py
@time: 2018/5/11 14:25
"""
from tools.operationSelector import OperationSelector


# -----------------------------公告弹窗数据输入--------------------------------
def set_parameter_sharing(self, announ, announ_key, operation):
    '''
    公告弹窗设置公告内容
    :param self:  操作对象
    :param announ: 用例数集中的key
    :param announ_key:  页面数据数集中的key
    :param operation: 输入的内容
    :return:
    '''
    content = self.overall[announ]
    print("公告内容 %s " % content)
    if content is None:  # 如何为空就直接重赋值
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
            # _ele = self._visible_return_selectop(dn.operation_noticesort)  # 判断单选框是否存在
            # self.visibleRadioSelected(_ele, True)
        elif choose == "维护公告":
            choose_noticesort(self, dn.operation_noticesort2)
            # _ele = self._visible_return_selectop(dn.operation_noticesort2)  # 判断单选框是否存在
            # self.visibleRadioSelected(_ele, True)
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
    title = set_parameter_sharing(self, dn.announTitle(), "title", dn.operation_dail_input)
    return title


def set_popup_content(self, dn):
    '''
    公告弹窗中内容的输入
    :param self: 操作对象
    :param dn: 数集对象
    :return:
    '''
    content = set_parameter_sharing(self, dn.announContent(), "content", dn.operation_content_input)
    return content


def set_popup_time(self, dn) -> "实力有限,无法对日期进行操作":
    '''
    公告弹窗中日期的选择
    :param self:操作对象
    :param dn:数集对象
    :return:
    '''
    daily_time = get_excle_time(self, dn)
    if daily_time is None:  # 如何为空就直接重赋值
        daily_time = self.LABLE_DF.iloc[0]["time"]

    # 找到数据然后进行切割操作,status_time : 开始时间, status_end :结束时间
    status_time, status_end = self.ti.cutting_time_current(daily_time)

    return status_time, status_end


def get_excle_time(self, dn):
    daily_time = self.overall[dn.announDeadline()]
    self.log.info("%s -------->涉及日期的发布暂时无法通过selenium进行测试操作" % self.FUNCTION_NAME)
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

    # 日期输入
    self.log.info("%s -------->涉及日期的发布暂时无法通过selenium进行测试操作" % self.FUNCTION_NAME)

    return status_time, status_end


# --------------------------------公告弹窗输入入口-----------------------------
def release_popup_data(self, dn):
    # ---------------发布公告都是执行输入动作，无法提交数据所以不进行数据库判断----------------
    choose = set_popup_type(self, dn)  # 公告类型
    op_select = set_popup_city(self, dn)  # 公告城市
    title = set_popup_title(self, dn)  # 公告标题
    content = set_popup_content(self, dn)  # 公告内容
    # daily_time = get_excle_time(self, dn)  # 设置日期，将设置的数据进行返回
    self.log.info("发布公告都是执行输入动作，无法提交数据所以不进行数据库判断")
    return choose, op_select, title, content


def set_popup_all_data(self, dn):
    # 公告输入的内容:公告类型  公告城市  公告标题  公告内容
    choose, op_select, title, content = release_popup_data(self, dn)  # 公告类型

    # 判断输入的内容是否为空，如果为空就返回原有的数据信息
    choose = data_to_determine(self, choose, "type")
    op_select = data_to_determine(self, op_select, "city")
    title = data_to_determine(self, title, "title")
    content = data_to_determine(self, content, "content")

    # 这个时间就是一个假象，几乎不要的
    status_time, status_end = set_popup_time(self, dn)  # 设置日期，将设置的数据进行返回

    # 将全部设置的数据转成集合
    daily_value = (choose, op_select, title, content, status_time, '暂时没有数据', status_end)

    # 将集合内容为标题，以及集合内容为输入的数据组成列表
    self.LABLE_DF.iloc[0] = dict(zip(self.setDailyTitle(), daily_value))

    self.log.info("提交的参数为: ------> %s " % self.LABLE_DF.iloc[0])


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
