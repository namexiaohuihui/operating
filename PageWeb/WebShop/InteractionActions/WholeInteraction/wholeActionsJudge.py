# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: wholeActionsJudge.py
@time: 2018/5/25 15:10
"""
# from PageWeb.WebShop.InteractionActions import WholeInteraction
from PageWeb.WebShop.InteractionActions import InteractionCoexistence
from tools.operationSelector import OperationSelector


class WholeActionsJudge(InteractionCoexistence):
    # excle文档中case所在工作薄的名称
    MODEL_WORKBOOK_LABEL = '标签'

    # 当前子慕课在菜单下的所属位置
    TREEW_TAGS_LOCATION = "1"

    # 根据key值，读取modei文件下保存用例的存放位置
    MODEI_CASE_POSITION = "whole"

    # MYSQL_DF, LABLE_DF
    def __init__(self) -> '对象实例化时就直接解析yaml中的数据信息,方便之后直接使用':
        self.parseyaml_location()
        self.parseyaml_content()

    # def city_active_confirm(self):
    # loantion = self.select_path['citytab']['value']
    # self._visible_return_selectop(loantion)

    def whole_selector_options(self, se_path, se_con):
        # 找到下拉框
        time_path = self.select_path[se_path]
        optins = OperationSelector(self.driver, time_path[se_con]).getAllOptions()

        # 找到文档中存储产品设置的默认值
        time_content = self.select_content[se_path]

        # 比较时间下拉框：第一个参数为：文档记录的默认值，第二个参数为：界面获取的额数据
        self._verify_operator(str.split(time_content[se_con], ','), optins)
        return time_path, time_content

    def time_options_judge(self):
        # 可用于selector数据读取以及判断
        time_path, time_content = self.whole_selector_options(self.names_key.yaml_timeselect(),
                                                              self.names_key.yaml_judge())

        # 可用于页面数据读取以及判断
        # 时间输入框的选择
        self._visible_css_selectop(time_path[self.names_key.yaml_choose()])
        # 找到页面上的元素
        ranges = time_path[self.names_key.yaml_opensleft()] + " %s" % time_path[
            self.names_key.yaml_ranges()]

        # 读取元素内容
        ranges_load = self._visible_returns_selectop(ranges)

        # 比较时间输入框
        self._verify_operator(str.split(time_content[self.names_key.yaml_choose()], ','),
                              [ran.text.strip() for ran in ranges_load])

    def select_option_time(self):
        '''
        在指定城市页面执行数据校验工作
        1. 找到全部城市页面
        2. 判断文档规定需要执行动作的城市
        3. 执行动作
        :return: 不返回
        '''
        # 第一第二步
        self.city_switch_judge()
        # 第三步
        self.time_options_judge()

    def select_lable_radio(self):
        '''
        在指定城市页面执行数据校验工作
        1. 找到全部城市页面
        2. 判断文档规定需要执行动作的城市
        3. 执行动作
        :return: 不返回
        '''
        # 第一第二步
        self.city_switch_judge()
        # 第三步
        # 找到单选框
        time_path = self.select_path[self.names_key.yaml_label()]
        # 读取内容
        time_content = self.select_content[self.names_key.yaml_label()]
        # 找到产品规定的数据信息
        optins = self._visible_returns_selectop(time_path[self.names_key.yaml_value()])
        # 比较两者之间
        self._verify_operator(str.split(time_content[self.names_key.yaml_value()], ','),
                              [op.text.strip() for op in optins])

    def area_verify_options(self,area_path,area_content,mana,option):
        manager = mana + "%s" % option
        MYSQL_DF = self.mysql_area_name(area_content[mana], area_content[manager])
        manager = OperationSelector(self.driver, area_path[mana]).getAllOptions()
        self._verify_operator(MYSQL_DF, manager)

    def select_area_region(self):
        # 区域下拉框的key
        area_path = self.select_path[self.names_key.yaml_area()]

        # 找到内部存档数据的key
        area_content = self.select_content[self.names_key.yaml_area()]

        # 区域第一个下拉框的内容
        self.area_verify_options(area_path,area_content,self.names_key.yaml_manager(),self.names_key.yaml_option())

        # 区域第二个下拉框的内容
        self.area_verify_options(area_path,area_content,self.names_key.yaml_director(),self.names_key.yaml_option())

        # 区域第三个下拉框的内容
        self.area_verify_options(area_path,area_content,self.names_key.yaml_region(),self.names_key.yaml_option())

