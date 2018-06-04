# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: __init__.py.py
@time: 2018/5/24 16:49
"""

from PageWeb.WebShop import BackgroundCoexistence
from PageWeb.WebShop.InteractionActions.interactionNames import InteractionNames
from tools.operationSelector import OperationSelector


class InteractionCoexistence(BackgroundCoexistence):
    names_key = InteractionNames()

    # 菜单在整体目录中的位置
    SIDEBAR_TAGS_LOCATION = "2"

    # 该菜单的用例所处位置目录
    MODEI_KEY_POSITION = "interaction"

    # 下拉标签存放的内容
    SELECT_LABLE_CONTENT = "totalLableNanme.yaml"
    # 下拉标签存放的位置
    SELECT_LABLE_LOCATION = "totalPathNames.yaml"

    def _rou_interaction(self):
        """
        进入日常公告页面
        :return:  暂时没有返回值
        """
        self.treew_tags = self.TREEW_TAGS_LOCATION
        self.sidebar_tags = self.SIDEBAR_TAGS_LOCATION
        self._rou_background()
        pass

    def parseyaml_location(self):
        '''
        解析yaml文件中存储标签的位置信息
        :return:
        '''
        self.select_path = self.names_key.read_parseyaml(self.SELECT_LABLE_LOCATION)

    def parseyaml_content(self):
        '''
        解析yaml文件中存储标签所携带的默认参数以及sql
        :return:
        '''
        parse = self.names_key.read_parseyaml(self.SELECT_LABLE_CONTENT)
        self.select_content = self.names_key.read_parseyaml(parse[self.names_key.yaml_files()],
                                                            parse[self.names_key.yaml_value()])

    # ---------------------------------------各个order页面中相同的用例集合点：以下为界面固定元件的校验-----------------------------
    def get_city_ele(self):
        '''
        根据city的路径查找该路径下面的全部元素
        :return:
        '''
        # 读取path文件里面的内容
        loantion = self.select_path[self.names_key.yaml_citytab()][self.names_key.yaml_value()]
        city_ele = self._visible_returns_selectop(loantion)
        return city_ele

    def city_active_default(self):
        '''
        判断city默认选中的对象是否为产品大大规定的
        步骤：
        1.找到全部元素
        2.获取元素上标签为class的属性名是否为选中，并判断该元素是否为所需要找到的元素
        :return:
        '''
        # 1.获取全部元素
        city_ele = self.get_city_ele()
        # 2.数据获取及判断
        self.default_city_content(city_ele, self.names_key.whole_result())

    def city_code_judge(self):
        '''
        判断city中是否显示出全部数据，以及编码是否正确
        步骤:
        1.找到全部元素
        2.依次读取city的text和code
        3.根据sql读取相应的数据信息
        4.两端数据比较
        :return:
        '''
        # 1.查找元素
        city_ele = self.get_city_ele()

        # 2找到元素中，code和name并转成dict格式
        LABLE_DF = self.lable_code_name(city_ele, 'a', 'href')

        # 3.根据sql读取相应的数据信息
        MYSQL_DF = self.mysql_code_name(self.select_content[self.names_key.yaml_citytab()][self.names_key.yaml_value()])

        # 4.两端数据比较
        self._verify_operator(MYSQL_DF, LABLE_DF)

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
        3. 执行动作
        :return: 不返回
        '''
        # 第三步
        self.time_options_judge()

    def select_lable_radio(self):
        '''
        在指定城市页面执行数据校验工作
        3. 执行动作
        :return: 不返回
        '''
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

    def area_verify_options(self, area_path, area_content, mana, option):
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
        self.area_verify_options(area_path, area_content, self.names_key.yaml_manager(), self.names_key.yaml_option())

        # 区域第二个下拉框的内容
        self.area_verify_options(area_path, area_content, self.names_key.yaml_director(), self.names_key.yaml_option())

        # 区域第三个下拉框的内容
        self.area_verify_options(area_path, area_content, self.names_key.yaml_region(), self.names_key.yaml_option())

    def order_source_status(self):
        #  订单来源下拉框的判断
        self.whole_selector_options(self.names_key.yaml_status(), self.names_key.yaml_source())
        #  订单章台下拉框的判断
        self.whole_selector_options(self.names_key.yaml_status(), self.names_key.yaml_pay())

    def value_placeholder(self, key, value, placeholder):
        # 比较下拉框
        self.whole_selector_options(key, value)

        # 获取输入框中的默认值
        place = self._visible_css_selectop_attribute(locator=self.select_path[key][placeholder], attr=placeholder)

        # 比较输入框中的默认值是否正确
        self._verify_operator(self.select_content[key][placeholder], place)
    def summary_value_placeholder(self,key):
        self.value_placeholder(key, self.names_key.yaml_value(),
                               self.names_key.yaml_placeholder())
    def order_value_placeholder(self):
        self.summary_value_placeholder(self.names_key.yaml_order())
        # self.value_placeholder(self.names_key.yaml_order(), self.names_key.yaml_value(),
        #                        self.names_key.yaml_placeholder())

    def buyer_value_placeholder(self):
        self.summary_value_placeholder(self.names_key.yaml_buyer())
        # self.value_placeholder(self.names_key.yaml_buyer(), self.names_key.yaml_value(),
        #                        self.names_key.yaml_placeholder())

    def other_value_placeholder(self):
        self.summary_value_placeholder(self.names_key.yaml_other())
        # self.value_placeholder(self.names_key.yaml_other(), self.names_key.yaml_value(),
        #                        self.names_key.yaml_placeholder())
