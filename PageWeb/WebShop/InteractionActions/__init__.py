# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: __init__.py.py
@time: 2018/5/24 16:49
"""

from PageWeb.WebShop import BackgroundCoexistence
from PageWeb.WebShop.InteractionActions.interactionNames import InteractionNames


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

    def city_switch_judge(self):
        '''
        1. 找到全部城市页面
        2. 判断文档规定需要执行动作的城市
        :return: 不返回
        '''
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
