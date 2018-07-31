# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: __init__.py.py
@time: 2018/5/24 16:49
"""

from CenterBackground import BackgroundCoexistence
from CenterBackground.InteractionActions.interactionNames import InteractionNames
from tools.extendBeantifulSoup import ExtendBeantifulSoup
from tools.operationSelector import OperationSelector


class InteractionCoexistence(BackgroundCoexistence):
    names_key = InteractionNames()

    # 10待付款
    STATUS_TEN = 10
    # 20已关闭
    STATUS_TWENTY = 20
    # 30付款中
    STATUS_THIRTY = 30
    # 32付款成功
    STATUS_TEN_TWO = 32
    # 50待发货
    STATUS_FIFTY = 50
    # 60发货中
    STATUS_SIXTY = 60
    # 70已收货
    STATUS_SEVENTY = 70

    # 平台
    TYPE_ONE = 1
    # 抢购
    TYPE_TWO = 2
    # 平台水票
    TYPE_THREE = 3
    # 店铺
    TYPE_FOUR = 4
    # 店铺水票
    TYPE_FIVE = 5
    # 线下
    TYPE_SIX = 6

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
        self.select_content = self.names_key.together_catalog(parse[self.names_key.yaml_files()],
                                                            parse[self.names_key.yaml_value()])

    # ---------------------------------------各个order页面中相同的用例集合点：以下为界面固定元件的校验-----------------------------
    # -------------------------此处为各用例共用的函数--------------------------
    def get_order_title(self, orderkey):
        content = self.select_content[orderkey]
        content = str.split('#%s' % content, ',')
        return content

    def get_city_ele(self):
        '''
        根据city的路径查找该路径下面的全部元素
        :return:
        '''
        # 读取path文件里面的内容
        loantion = self.select_path[self.names_key.yaml_citytab()][self.names_key.yaml_value()]
        city_ele = self._visible_returns_selectop(loantion)
        return city_ele

    def whole_selector_options(self, se_path, se_con):
        # 找到下拉框
        time_path = self.select_path[se_path]
        optins = OperationSelector(self.driver, time_path[se_con]).getAllOptions()

        # 找到文档中存储产品设置的默认值
        time_content = self.select_content[se_path]

        # 比较时间下拉框：第一个参数为：文档记录的默认值，第二个参数为：界面获取的额数据
        self._verify_operator(str.split(time_content[se_con], ','), optins)
        return time_path, time_content

    def time_options_choose(self, time_path):
        # 时间输入框的选择
        self._visible_css_selectop(time_path[self.names_key.yaml_choose()])

        # 找到时间输入框元素的位置
        ranges = time_path[self.names_key.yaml_opensleft()] + " %s" % time_path[
            self.names_key.yaml_ranges()]

        # 返回该路径下的全部元素
        ranges_load = self._visible_returns_selectop(ranges)
        return ranges_load

    def time_options_judge(self):
        # 可用于selector数据读取以及判断
        time_path, time_content = self.whole_selector_options(self.names_key.yaml_timeselect(),
                                                              self.names_key.yaml_judge())

        # 时间输入框
        self.time_options_choose(time_path)

        # 比较时间输入框
        self._verify_operator(str.split(time_content[self.names_key.yaml_choose()], ','),
                              [ran.text.strip() for ran in ranges_load])

    def value_placeholder(self, key):
        value = self.names_key.yaml_value()
        placeholder = self.names_key.yaml_placeholder()
        # 比较下拉框
        self.whole_selector_options(key, value)

        # 获取输入框中的默认值
        place = self._visible_css_selectop_attribute(locator=self.select_path[key][placeholder], attr=placeholder)

        # 比较输入框中的默认值是否正确
        self._verify_operator(self.select_content[key][placeholder], place)

    def order_lable_bs4(self, content, table, thead, td="th"):
        '''
        根据元素标签获取爬取数据
        :param content:  需要爬取的元素标签
        :param table: 子标签
        :param td: 孙标签
        :return:
        '''
        path = self.select_path[content]
        # # 程序设置有误，需要控制器
        content = str.split(path[table], '>')[0]
        ebs = ExtendBeantifulSoup(self.driver, content)
        EBS_DF = ebs.lable_table_list(thead, td)
        # EBS_DF = list(ebs.lableParsingList(td).dataSet[0])
        return EBS_DF

    def label_search_button(self):  # 界面搜索按钮的点击
        search_button = self.select_path[self.names_key.yaml_button()][self.names_key.yaml_search()]
        self._visible_css_selectop(search_button)

    # -------------------------数据用例的二次调用----------------------
    def path_tbody(self):
        # 获取翻页按钮的位置
        button_next = self.select_path[self.names_key.yaml_buttonpage()][self.names_key.yaml_next()]

        # 获取tbody界面数据的路径所在地
        path = self.select_path[self.names_key.yaml_content()]
        content = str.split(path[self.names_key.yaml_table()], '>')[0]
        # 将路径传入，解析工作开始
        self.parsing_tbody(content, button_next, self.names_key.program_operation())

    def advanced_query(self, ad_query):
        statement = self.overall[self.names_key.wholeQueryStatement()] % ad_query

        mysql_list = self.reprogramming_definition(statement)

        self.mysql_statement(mysql_list)

    def status_statement_query(self, days=0):

        start_time, stop_time = self.ti.today_to_stamp(days)

        area = self.names_key.yaml_status()

        director = self.status_text_to_number(self.filters[area][self.names_key.yaml_pay()])

        ad_query = (start_time, stop_time, director)

        self.advanced_query(ad_query)

    def area_statement_query(self, days=0):
        start_time, stop_time = self.ti.today_to_stamp(days)

        area = self.names_key.yaml_area()
        region = self.filters[area][self.names_key.yaml_region()]

        director = self.filters[area][self.names_key.yaml_director()]

        ad_query = (start_time, stop_time, region, director)

        self.advanced_query(ad_query)

    def time_statement_query(self, *days):
        # 根据sql读取数据信息并进行重组
        t_d = ''
        for d in days:
            if d == 0:
                t_d = 0
                break
            else:
                t_d = t_d + d
        self.advanced_query(self.ti.today_to_stamp(t_d))

    def mysql_statement(self, mysql_list):
        # 获取标题
        key_title = self.get_order_title(self.names_key.yaml_orderkey())
        self.MYSQL_DF = self.list_to_pandas(mysql_list, key_title, "#订单编号")

    def status_text_to_number(self, text: str):
        if text == "等待付款":
            operation = self.STATUS_TEN

        elif text == "交易关闭":
            operation = self.STATUS_TWENTY

        elif text == "付款中":
            operation = self.STATUS_THIRTY

        elif text == "等待派单":
            operation = self.STATUS_TEN_TWO

        elif text == "等待配送":
            operation = self.STATUS_FIFTY

        elif text == "配送中":
            operation = self.STATUS_SIXTY

        elif text == "交易完成":
            operation = self.STATUS_SEVENTY

        else:
            operation = "状态文字输入错误"

        return operation

    def items_status_judge(self, item_status, arrive_time):

        if item_status == self.STATUS_TEN:
            item_status = "等待付款"
            operation = "查看关闭操作记录"

        elif item_status == self.STATUS_TWENTY:
            item_status = "交易关闭"
            operation = "查看操作记录"

        elif item_status == self.STATUS_THIRTY:
            item_status = "付款中"
            operation = "查看关闭操作记录"

        elif item_status == self.STATUS_TEN_TWO:
            item_status = "等待派单"
            if arrive_time:
                operation = "派单查看关闭操作记录"
            else:
                operation = "派单转预约查看关闭操作记录"

        elif item_status == self.STATUS_FIFTY:
            # 订单为预约时，就不需要出现转预约的按钮
            item_status = "等待配送"
            if arrive_time:
                operation = "更换配送员查看关闭操作记录"
            else:
                operation = "更换配送员转预约查看关闭操作记录"

        elif item_status == self.STATUS_SIXTY:
            # 订单为预约时，就不需要出现转预约的按钮
            item_status = "配送中"
            if arrive_time:
                operation = "查看关闭操作记录"
            else:
                operation = "转预约查看关闭操作记录"

        elif item_status == self.STATUS_SEVENTY:
            item_status = "交易完成"
            operation = "查看操作记录"
        else:
            operation = "没有找到这个状态"
        return item_status, operation

    def items_type_judge(self, item_type):
        if item_type == self.TYPE_ONE:
            item_type = "平台"
            item_type = ""

        if item_type == self.TYPE_TWO:
            item_type = "抢购 "

        elif item_type == self.TYPE_THREE:
            item_type = "水票 "

        elif item_type == self.TYPE_FOUR:
            item_type = "店铺 "

        # elif item_type == self.TYPE_FIVE:
        #     item_type = "店铺水票"

        elif item_type == self.TYPE_SIX:
            item_type = "线下 "
        else:
            return item_type
        return item_type

    def reprogramming_definition(self, statements: str):
        '''
        根据mysql语句，返回查询之后的数据信息
        并根据表头将数据进行细分。存入相应的dict中
        1.执行语句获取表中的数据信息
        2.获取dict需要设置的key
        3.根据表头读取相应的数据，存入dict对应key的value中，
        :param statements:  mysql的执行语句
        :return:
        '''
        # 1.执行语句获取表中的数据信息
        results_sta = self._verify_match(statements)

        adjust_results = []  # 定义list，存储mysql转换之后的数据

        # 2.获取dict需要设置的key
        key_title = self.get_order_title(self.names_key.yaml_orderkey())

        # 3.根据表头读取相应的数据，存入dict对应key的value中
        for items in range(len(results_sta)):
            row_data = {}
            results_items = results_sta[items]
            # key = 订单编号 ,value = results_sta中标题头名为id
            row_data[key_title[0]] = str(results_items["id"])

            # key = 订单标签 ，value = results_sta转换为标签.逻辑有误只能在没有个输出语句后面加个空格‘ ’。。sorry
            judge_type = self.items_type_judge(results_items["type"])
            arrive_time = '' if results_items["arrive_time"] == 0 else "预约 "
            large_quantity = '' if results_items["large_quantity"] == 1 else "大客户 "
            communicate = '' if results_items["communicate"] == 1 else "新用户 "
            # 本来每个标签之间都要加一个空格，但是逻辑有误就不在这里加了。放在获取数据的地方进行添加
            row_data[key_title[1]] = ("%s%s%s%s" % (judge_type, arrive_time, large_quantity, communicate)).strip()

            # key = 买家名称,value = results_sta中标题头名为nickname
            row_data[key_title[2]] = results_items["nickname"]

            # key = 收货地址,value = results_sta中标题头名为house_number
            # 因为门牌号中多了一个竖线所以要过滤掉
            house_number = results_items["house_number"].replace("|", '')

            # 将contact、address和过滤后的house_number当做value
            row_data[key_title[3]] = "%s,%s%s" % (
                results_items["contact"], results_items["address"], house_number)

            # key = 所属区域,value = results_sta中标题头名为name
            row_data[key_title[4]] = results_items["name"]

            # key = 状态，value = results_sta中标题头名为status
            # 以及根据status来判断该内容应有什么样子的操作
            row_data[key_title[5]], row_data[key_title[7]] = self.items_status_judge(results_items["status"],
                                                                                     arrive_time)  # 操作

            # 下单时间格式转换及获取
            row_data[key_title[6]] = self.ti.stampToTime(results_items["add_time"], "%Y-%m-%d %H:%M")

            adjust_results.append(row_data)

        return adjust_results

    def get_filters_excel(self):
        self.filters = self.overall[self.names_key.excle_screening()]  # 找到用例当中的数据
        self.filters = self.strTodict(self.filters)  # 将数据转换成json形式
        return self.filters

    def filters_selector_send(self, filters):
        filters_keys = filters.keys()  # 找出filters当中的key
        peripheral = self.names_key.yaml_timeselect()  # 找到时间的key名称
        self.filters_selector(filters, peripheral, [self.names_key.yaml_judge()])  # 时间下拉
        if peripheral in filters_keys:  # 判断时间key是否在filters的keys中
            time_path = self.select_path[peripheral]  # 时间输入框所在的路径
            internal = self.names_key.yaml_choose()  # 时间输入框的key值
            if internal in filters[peripheral].keys():  # 判断key是否出现
                print(filters[peripheral][internal])
                ranges_eles = self.time_options_choose(time_path)  # 找到时间选择输入框中的数值
                for value_is in ranges_eles:  # 遍历，符合条件的就进行点击
                    if value_is.text == filters[peripheral][internal]:
                        self.vac.element_click(value_is)
                        break

    def filters_radio(self, filters):
        filters_keys = filters.keys()
        peripheral = self.names_key.yaml_label()
        if peripheral in filters_keys:
            # 找出需要设置的标签
            label_scr = str.split(filters[peripheral], ',')
            print(label_scr)
            # 找到界面标签
            internal = self.names_key.yaml_value()
            label_path = self.select_path[peripheral]  # 元素所在的路径
            ranges_eles = self._visible_returns_selectop(label_path[internal])
            for value_is in ranges_eles:
                if value_is.text.strip() in label_scr:
                    self.visibleRadioSelected(value_is, True)

    def filters_selector(self, filters, peripheral, inside):
        filters_keys = filters.keys()
        op_sele = OperationSelector(self.driver)
        if peripheral in filters_keys:  # 区域的东西
            print(filters[peripheral])
            time_path = self.select_path[peripheral]  # 元素所在的路径

            for internal in inside:
                if internal in filters[peripheral].keys():  # 经理
                    print(filters[peripheral][internal])
                    op_sele.lable_set_text(time_path[internal], filters[peripheral][internal])

    def filters_send_keys(self, filters, peripheral):
        filters_keys = filters.keys()
        self.filters_selector(filters, peripheral, [self.names_key.yaml_value()])
        if peripheral in filters_keys:
            time_path = self.select_path[peripheral]  # 元素所在的路径
            # VALUE的下拉
            # placeholder的输入
            internal = self.names_key.yaml_placeholder()
            if internal in filters[peripheral].keys():
                print(filters[peripheral][internal])
                self._sendKeys_css_selectop(time_path[internal], filters[peripheral][internal])
        # -------------------------用例的直接调用--------------------------
        # -------------------------此处为界面用例的调用处--------------------------

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
        MYSQL_DF = self.mysql_code_name(
            self.select_content[self.names_key.yaml_citytab()][self.names_key.yaml_value()])

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
        # 读取yaml中产品规定的Neri内容
        time_content = self.select_content[self.names_key.yaml_label()]
        # 找到页面的内容
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
        self.area_verify_options(area_path, area_content, self.names_key.yaml_manager(),
                                 self.names_key.yaml_option())

        # 区域第二个下拉框的内容
        self.area_verify_options(area_path, area_content, self.names_key.yaml_director(),
                                 self.names_key.yaml_option())

        # 区域第三个下拉框的内容
        self.area_verify_options(area_path, area_content, self.names_key.yaml_region(),
                                 self.names_key.yaml_option())

    def order_source_status(self):
        #  订单来源下拉框的判断
        self.whole_selector_options(self.names_key.yaml_status(), self.names_key.yaml_source())
        #  订单章台下拉框的判断
        self.whole_selector_options(self.names_key.yaml_status(), self.names_key.yaml_pay())

    def order_value_placeholder(self):
        # 订单下拉框
        self.value_placeholder(self.names_key.yaml_order())
        # self.value_placeholder(self.names_key.yaml_order(), self.names_key.yaml_value(),
        #                        self.names_key.yaml_placeholder())

    def buyer_value_placeholder(self):
        # 用户下拉框
        self.value_placeholder(self.names_key.yaml_buyer())
        # self.value_placeholder(self.names_key.yaml_buyer(), self.names_key.yaml_value(),
        #                        self.names_key.yaml_placeholder())

    def other_value_placeholder(self):
        # 其他下拉框
        self.value_placeholder(self.names_key.yaml_other())
        # self.value_placeholder(self.names_key.yaml_other(), self.names_key.yaml_value(),
        #                        self.names_key.yaml_placeholder())

    # -------------------------此处为数据用例的调用处--------------------------
    def order_whole_title(self):
        EBS_DF = self.order_lable_bs4(self.names_key.yaml_content(), self.names_key.yaml_table(), 'thead', "th")
        EBS_DF = list(EBS_DF.dataSet[0])
        self._verify_operator(self.get_order_title(self.names_key.yaml_orderkey()), EBS_DF)

    def order_whole_page(self) -> "获取页面数据信息流程":
        '''
        1. 获取界面内容
        2. 执行sql
        3. 比较数据
        :return:
        '''
        funktion = [{"func": self.path_tbody, "args": ''}, {"func": self.time_statement_query(), "args": "0"}]
        # self.path_tbody()
        # self.statement_query()
        self.start_thread_pool(funktion)
        self._verify_operator_dataframe(self.MYSQL_DF, self.LABLE_DF)

    def screening_selector(self):
        filters = self.get_filters_excel()  # 读取excle表格的数据并转换成json数据

        self.filters_selector_send(filters)  # 时间输入框以及下拉
        self.filters_radio(filters)  # 复选框选择

        inside = [self.names_key.yaml_manager(), self.names_key.yaml_director(), self.names_key.yaml_region()]
        self.filters_selector(filters, self.names_key.yaml_area(), inside)  # 区域

        inside = [self.names_key.yaml_source(), self.names_key.yaml_pay()]
        self.filters_selector(filters, self.names_key.yaml_status(), inside)  # 状态

        self.filters_send_keys(filters, self.names_key.yaml_order())  # 订单
        self.filters_send_keys(filters, self.names_key.yaml_buyer())  # 用户
        self.filters_send_keys(filters, self.names_key.yaml_other())  # 其他

    def appointment_bunber(self):
        self.screening_selector()
        self.label_search_button()  # 点击搜索按钮

        filters = self.get_filters_excel()  # 读取excle表格的数据并转换成json数据
        days = filters[self.names_key.yaml_timeselect()][self.names_key.yaml_choose()]
        if days == "昨天":
            ti_days = '-1'
        elif days == "最近7日":
            ti_days = '-6'
        elif days == "最近30天":
            ti_days = '-29'
        else:
            ti_days = 0
        funktion = [{"func": self.path_tbody, "args": ''},
                    {"func": self.time_statement_query, "args": ti_days}]
        self.start_thread_pool(funktion)
        self._verify_operator_dataframe(self.MYSQL_DF, self.LABLE_DF)

    def area_screening_conditions(self):
        # 下拉框统一筛选。没有参数的就不进行操作
        self.screening_selector()
        self.label_search_button()  # 点击搜索按钮

        funktion = [{"func": self.path_tbody, "args": ''},
                    {"func": self.area_statement_query, "args": ""}]

        self.start_thread_pool(funktion)
        self._verify_operator_dataframe(self.MYSQL_DF, self.LABLE_DF)

    def status_screening_conditions(self):
        '''
        根据状态进行筛选数据信息
        :return:
        '''
        # 下拉框统一筛选。没有参数的就不进行操作
        self.screening_selector()
        self.label_search_button()  # 点击搜索按钮

        funktion = [{"func": self.path_tbody, "args": ''},
                    {"func": self.status_statement_query(), "args": ""}]

        self.start_thread_pool(funktion)
        self._verify_operator_dataframe(self.MYSQL_DF, self.LABLE_DF)
