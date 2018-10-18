# -*- coding: utf-8 -*-
"""
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  -  /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                        `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

               佛祖保佑         永无BUG
@author:    ln_company
@license:   (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@Software:  PyCharm
@file:      operationViewJude.py
@time:      2018/9/27 17:49
@desc:
"""
import os
import operator
from tools.YAMLconfig import readYaml
from tools.screeningdrop import ScreeningDrop
from CenterBackground.customTabs import CustomTabs
from CenterBackground.judeVerification import JudgmentVerification

_parameter = 'parameter'
_type = 'type'
_click = 'click'
_input = 'input'
_timeinput = 'timeinput'
_select = 'select'
_checkbox = 'checkbox'
_print = 'DaLao,What do you type in? %s'


class OperationViewJude(JudgmentVerification):
    def __init__(self, config, basename, center_name):
        """
        定义模块数据信息
        :param module:   元素模块
        :param sheet:   用例标签名
        :param basename:  执行程序的文件名
        """
        JudgmentVerification.__init__(self, config, basename)
        self.bi = center_name()
        pass

    def read_yaml_case(self, file_name, case_key):
        """
        I don't know what I'm writing, but I know it works.
        通过文件来读取相应的key值,最后进行
        :param file_name: excel定义的默认参数
        :param case_key: 用例函数名
        :return:
        """
        case_value = readYaml.read_expression_key(file_name, case_key)
        return case_value

    def time_day_select(self, hour, value, part):
        """
        啥子操作
        :param hour:
        :param part:
        :return:
        """
        # 找到元素
        hourselect = self.vac.is_visibles_css_selectop(self.driver, hour)
        # 点击元素
        self.vac.element_click(hourselect[value])
        # 页面刷新之后需要重新找元素
        hourselect = self.vac.is_visibles_css_selectop(self.driver, hour)
        # 下拉对象并设置内容
        ScreeningDrop(self.driver).ele_select(hourselect[value]).setSelectorText(part)

    def release_success(self):
        """
        订单页面条件筛选动作的执行。
        第二步有个坑：如果设置的city不存在那么就默认页面执行操作
        :return:
        """
        # 1.读取用例设置的参数位置
        ov_para = self.overall[self.bi.whole_parameter()]
        # 1.1 根据文件名和key来解析相应的数据
        ov_para = os.path.join(os.path.dirname(os.path.realpath(__file__)), ov_para)
        case_value = self.read_yaml_case(file_name=ov_para, case_key=self.FUNCTION_NAME)

        # 2.进入指定的城市
        self.ct = CustomTabs(self.driver, self.financial[self.bi.yaml_tabs()])
        self.ct.is_visibles()
        # 2.1读取全部的城市text
        ul_text = [ul.text for ul in self.ct.ul_li]
        # 2.2将元素和城市text通过dict形式存储
        city_text = dict(zip(self.ct.ul_li, ul_text))
        # 2.3找到城市
        case_city = case_value[self.bi.yaml_city()]
        for city_k, city_v in city_text.items():
            if case_city is city_v:
                self.vac.element_click(city_k)

        # 3.根据相应的key值对数据进行操作,1遍历执行元素的动作
        case_con = case_value[self.bi.yaml_condition()]
        para_key = case_con.keys()

        for ov in para_key:
            # 4.根据key值旗下的value值
            ov_pa = case_con[ov]
            pa_key = ov_pa.keys()
            # 5. 找到元素的keys值,该值为可在路径yaml表中找到元素的路径
            for pa in pa_key:
                # ov_key = 依次元素的路径,ov_value = 设置的参数,ov_ty = 以及该元素的类型
                ov_key = self.financial[pa]
                case_pa = ov_pa[pa]
                ov_value = case_pa[_parameter]
                ov_ty = case_pa[_type].lower()

                if ov_ty == _click:
                    # 根据元素进行点击
                    self.vac.css_click(self.driver, ov_key)
                    continue

                elif ov_ty == _input:  # 根据元素进行输出操作

                    if pa == _timeinput:  # 如果为时间输入框就要的单独处理
                        start_time, end_time = self.ti.day_time_date(ov_value)
                        # 点击输入框
                        self.vac.id_click(self.driver, ov_key)

                        # 输入日期:开始和结束
                        mimi = self.vac.is_visibles_css_selectop(self.driver, ".input-mini")
                        self.vai.ele_clear_keys(mimi[0], start_time["year"])
                        self.vai.ele_clear_keys(mimi[1], end_time["year"])

                        # 小时下拉框:开始和结束
                        self.time_day_select(".hourselect", 0, start_time["time"])
                        self.time_day_select(".hourselect", 1, end_time["time"])

                        # 下拉分:开始和结束
                        self.time_day_select(".minuteselect", 0, start_time["seconds"])
                        self.time_day_select(".minuteselect", 1, end_time["seconds"])

                        # 弹窗的确定按钮
                        self.vac.css_click(self.driver, self.financial[self.bi.yaml_timesuccess()])
                        pass
                    else:
                        self.vai.css_input(self.driver, ov_key, ov_value)
                        pass
                    continue

                elif ov_ty == _select:  # 根据元素来设置相应的options值
                    ScreeningDrop(self.driver, ov_key, case_pa['ele']).setSelectorText(ov_value)
                    continue

                elif ov_ty == 'checkbox':
                    # 根据元素来选择相应的单选框
                    checkbox = self.vac.is_visible_css_selectop(self.driver, ov_key)
                    self.visibleRadioSelected(checkbox, ov_value)
                    continue

                else:
                    self.log.info(_print % ov_ty)
                    continue

        # 最后一步,点击查询还是点击导出
        ele_formSub = self.vai.is_visibles_css_selectop(self.driver, self.financial['formSub'])
        formSub = case_value['formSub']

        # 确定为搜索和导出就执行动作
        if formSub[_parameter]:
            action = formSub['action']
            if action == 'search':
                # 点击搜索按钮
                self.vac.element_click(ele_formSub[self.financial[action] - 1])
            else:
                # 点击搜索按钮之后在点击导出按钮
                x = [e.text for e in ele_formSub]
                self.vac.element_click(ele_formSub[self.financial['search'] - 1])
                # 点击搜索之后记得重新获取页面元素,不然会出现StaleElementReferenceException
                ele_formSub = self.vai.is_visibles_css_selectop(self.driver, self.financial['formSub'])
                self.vac.element_click(ele_formSub[self.financial[action] - 1])
                # 弹窗中的全选按钮
                checkbox = self.vac.is_visible_css_selectop(self.driver, self.financial[self.bi.yaml_headersort()])
                self.visibleRadioSelected(checkbox, True)
                # 没延迟会报错
                self.vai.sleep_Rest(1)
                # 弹窗中的确定按钮
                self.vac.css_click(self.driver, self.financial[self.bi.yaml_exportsort()])
            pass
        else:  # 确定不为搜索和导出就刷新页面
            self.driver.refresh()
        pass

    def close_order_types(self):
        """
        点击关闭按钮之后关闭弹窗,暂时不做任何交互
        :return:
        """
        # 找到关闭按钮
        _close = self.financial[self.bi.yaml_btnclose()]
        _close = self.vac.css_click(self.driver, _close)
        if _close:
            # 关闭弹窗
            _close = self.financial[self.bi.yaml_closecancel()]
            self.vac.css_click(self.driver, _close)
        else:
            print("没有关闭按钮")

    def transfer_order_types(self):
        """
        点击转预约按钮之后关闭弹窗,暂时不做任何交互
        :return:
        """
        # 找到转预约按钮
        _transfer = self.financial[self.bi.yaml_btndanger()] % 1
        print(_transfer)
        _transfer = self.vac.is_visibles_css_selectop(self.driver, _transfer)
        if _transfer:
            # 关闭弹窗
            for tr in _transfer:
                if tr.text == "转预约":
                    self.log.info("click order %s " % tr.text)
                    self.vac.element_click(tr)
                    cancel = self.financial[self.bi.yaml_dangercancel()]
                    self.vac.css_click(self.driver, cancel)
                else:
                    self.log.info("no appear To make an appointment to")
            else:
                self.log.info("没有转预约按钮")

    def replace_order_types(self):
        """
        点击更换配送员按钮之后关闭弹窗,暂时不做任何交互
        :return:
        """
        # 找到更换配送员按钮
        _transfer = self.financial[self.bi.yaml_btndanger()] % 1
        print(_transfer)
        _transfer = self.vac.is_visibles_css_selectop(self.driver, _transfer)
        if _transfer:
            # 更换配送员弹窗
            for tr in _transfer:
                if tr.text == "更换配送员":
                    self.log.info("click order %s " % tr.text)
                    self.vac.element_click(tr)
                    cancel = self.financial[self.bi.yaml_dangercancel()]
                    self.vac.css_click(self.driver, cancel)
                else:
                    self.log.info("no appear Change of delivery man")
        else:
            self.log.info("没有更换配送员按钮")

    def details_order_types(self):
        """
        进入详情页,暂时不做任何交互
        :return:
        """
        # 找到险情按钮
        _details = self.financial[self.bi.yaml_btnreplace()] % 1
        _details = self.vac.css_click(self.driver, _details)
        if _details:
            # 返回上一页
            if self.vac.is_visible_css_selectop(self.driver, ".page-header").text == "订单明细":
                self.log.info("订单明细 yes")
            else:
                self.log.info("订单明细 no")
        else:
            self.log.info("没有详情按钮")

    def record_order_types(self):
        """
        点击记录,暂时不做任何交互
        :return:
        """
        # 找到查看按钮
        _record = self.financial[self.bi.yaml_btnrecord()] % 1
        _record = self.vac.css_click(self.driver, _record)
        if _record:
            # 返回上一页
            self.vac.sleep_Rest(2)
            _record = self.financial[self.bi.yaml_closerecord()]
            self.vac.css_click(self.driver, _record)
        else:
            self.log.info("没有记录按钮")
