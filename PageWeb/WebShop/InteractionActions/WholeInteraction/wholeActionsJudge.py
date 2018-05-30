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

    def time_options_judge(self):
        # 找到下拉框，读取内部数据
        time_path = self.select_path[self.names_key.yaml_timeselect()]
        optins = OperationSelector(self.driver, time_path[self.names_key.yaml_judge()]).getAllOptions()

        # 找到文档中存储产品设置的默认值
        time_content = self.select_content[self.names_key.yaml_timeselect()]

        # 比较两者之间
        self._verify_operator(str.split(time_content[self.names_key.yaml_judge()], ','), optins)

        # 时间输入框的选择
        print(time_path[self.names_key.yaml_choose()])
        self._visible_css_selectop(time_path[self.names_key.yaml_choose()])
        # 找到页面上的元素
        ranges = time_path[self.names_key.yaml_opensleft()] + " %s" % time_path[
            self.names_key.yaml_ranges()]

        # 读取元素内容
        print(ranges)
        ranges_load = self._visible_returns_selectop(ranges)
        ranges_con = [xx.text.strip() for xx in ranges_load]

        # 找到文档中存储产品设置的默认值
        self._verify_operator(str.split(time_content[self.names_key.yaml_choose()], ','), ranges_con)

    def city_replace_active(self):
        '''
        切换已开通的数据城市
        1.获取已开通的全部城市数据
        2.循环便利点击
        :return:
        '''
        # 1.获取全部元素
        city_ele = self.get_city_ele()

        number_len = len(city_ele)

        for code in range(1, number_len):
            # 遍历点击
            city_ele[code].click()
            # 点击之后要重新获取元素
            city_ele = self.get_city_ele()
            # 判断切换之后的元素所写到的class是不是产品大大规定的。。。
            assert city_ele[code].get_attribute('class') == self.overall[self.names_key.whole_result()]

    def select_option_judge(self):
        city_ele = self.get_city_ele()
        excle_title = self.overall[self.names_key.excle_city()]
        if excle_title:
            for city in city_ele:
                if city.text == excle_title:
                    self.log.info("在%s界面进行操作" % city.text)
                    # 点击元素
                    city.click()
                    break
        else:
            self.log.info("在默认界面进行操作")
        self.time_options_judge()
