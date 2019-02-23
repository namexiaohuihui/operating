# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: JudgmentVerification.py
@time: 2018/1/23 10:18
"""
import os
import re
import time
from tools.Logger import Log
from tools.configs import readModel
from tools.YAMLconfig import readYaml
from tools.comparedVerify import ComparedVerify
from tools.openpyxlExcel import OpenExcelPandas
from tools.timeFromat import TimeFromat
from tools.extendBeantifulSoup import ExtendBeantifulSoup

module = 'module'


class JudgmentVerification(ComparedVerify):

    def __init__(self, config, basename):
        self.config_dist = config

        # 定义日志
        self.log = Log(basename)

        # 获取init中定义的数据，并根据menu来读取出相应的参数
        self.argument = readYaml.read_expression()[self.config_dist['menu']]

        # 根据init要求的yaml路径来读取该模块下全部元素路径
        self.financial = readYaml.read_expression(self.config_dist['yaml'])

        # 读取用例所在的位置
        MODEI_KEY_POSITION = self.argument[module]

        # 读取用例的名称
        fa_mo = self.config_dist[module]

        # 读取用例的模块
        MODEI_CASE_POSITION = self.argument[fa_mo][module]

        # 读取用例里面的标签
        exclefile = self.argument[fa_mo][self.config_dist['sheet']]

        self.overallExcelData = self._excel_Data(MODEI_KEY_POSITION, MODEI_CASE_POSITION, exclefile)

        pass

    # 设置菜单字目录上的标题
    content_header = ".content-header > h1"

    # -------------------------定义主菜单的所在位置------------------------
    def set_sidebar_number(self, number: int) -> None:
        '''通过number定义主菜单的所在位置'''
        self.sidebar = ".sidebar-menu>li:nth-child(%s)>.dropdown-toggle" % number

    def sidebar_number_get(self) -> "获取子菜单的所在位置":
        return self.sidebar

    # -------------------------定义子菜单的所在位置------------------------
    def set_treeview_number(self, number: int) -> "通过number定义子菜单的所在位置":
        '''通过number定义子菜单的所在位置'''
        self.treew = ".treeview-menu.menu-open>li:nth-child(%s)" % number

    def treeview_number_get(self) -> "获取子菜单的所在位置":
        return self.treew

    # -------------------通过第三方参数来设置或者读取主菜单的位置-------------
    father_tags = property(sidebar_number_get, set_sidebar_number, doc="Setting an error or getting the main menu.")

    # -------------------通过第三方参数来设置或者读取子菜单的位置
    child_tags = property(treeview_number_get, set_treeview_number, doc="Error setting or getting subtags.")

    def screen_set_up(self, basename):
        """
        select用例中,需要执行的前置条件统一定义并进行调用
        :param basename: 文件名和类名的拼接对象
        :return:
        """
        # 获取运行文件的类名
        self.log.info("%s ---setup: 每个用例开始前后执行" % basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.openingProgram()
        self._rou_background()
        pass

    def screen_tear_down(self, perform_obj):
        """
        select用例中,需要执行的后置条件统一定义并进行调用
        :param perform_obj: 当前case运行的对象
        :return:
        """
        self.get_screenshot_image(method_obj=perform_obj)
        self.driver.quit()
        self.log.info("%s ---teardown: 每个用例结束后执行" % perform_obj.basename)
        pass

    # ------------------------------进入目录路径-------------------------------
    def _rou_background(self):
        """
        father_tags： 定义菜单的所在位置
        child_tags ： 定义模块的所在位置
        :return:  暂时没有返回值
        """

        self.father_tags = self.argument['father']
        self._visible_css_selectop(self.father_tags)

        self.child_tags = self.argument[self.config_dist[module]]['child']
        self._visible_css_selectop(self.child_tags)

        pass

    def tbody_td_data(self, content, button_next, title_key):
        '''
        爬取数据展示栏的内容，可翻页爬取
        :param content: 数据所在页面中的位置
        :param button_next: 翻页按钮的位置
        :param title_key: df序列号数据设置项
        :return:
        '''
        # 1.定义爬虫对象
        ebs = ExtendBeantifulSoup(self.driver, content)
        soup_list = []
        # 2.循环读取页面数据
        while True:  # 先进入页面读取数据，然后判断下一页按钮是否存在，存在就点击。不存在就跳过 ---->不严谨
            # 获取界面数据并将标签为tbody的数据切割出来
            cutting = ebs.lable_table_parsing('tbody')
            soup_list.append(cutting)
            if self._visible_css_selectop(button_next):
                pass
            else:
                break

        # 3.将页面数据进行爬取
        for tags in soup_list:
            ebs.lable_cutting_tags(tags, "td")
        # 4.获取df数据标题
        ebs.daily = self.get_order_title(self.names_key.yaml_orderkey())

        # 5.将数据转换成df
        df = ebs.interfaceToPandas()

        if type(df) != int:
            # 6.重新设置序列号
            df = df.set_index([list(df[title_key])])
        else:
            self.log.info("页面数据为空")
            pass
        return df

    def parsing_tbody(self, content, button_next, operation):
        # 获取页面全部数据
        self.LABLE_DF = self.tbody_td_data(content, button_next, "#订单编号")
        if type(self.LABLE_DF) is int:
            self.log.info("self.LABLE_DF 数据对象为空")
        else:
            # 将空格全部去除
            list_operation = self.LABLE_DF[operation]
            list_operation = list(map(lambda x: x.replace(' ', ''), list_operation))
            self.LABLE_DF[operation] = list_operation

    def setFunctionName(self, funtion):
        """
        设置需要运行的函数名
        :param funtion:  函数名
        :return:
        """
        # 记录目前执行的函数名（也可以认为目前执行的用例）
        self.FUNCTION_NAME = funtion
        self.log.fun_name = self.FUNCTION_NAME

        # 根据df标签序号获取用例
        self.overall = self.overallExcelData.loc[self.FUNCTION_NAME]

        # 创建时间对象
        self.ti = TimeFromat()

        # 打印用例场景作为注释内容,格式最好不用动.如果不需要注释就将其隐藏
        self.log.info("注释开头%s注释结尾" % self.overall['场景'])

    def read_yaml_case(self, file_name, case_key):
        """
        I don't know what I'm writing, but I know it works.
        通过文件来读取相应的key值,最后进行
        :param file_name: excel定义的默认参数
        :param case_key: 用例函数名
        :return:
        """
        self.log.info("从%s中获取%s数据信息" % (file_name, case_key))
        case_value = readYaml.read_expression_key(file_name, case_key)
        return case_value

    # --------------------------------正则的使用--------------------------
    def re_cutting_data(self, attr):
        cutting = re.search(r'[1-9]\d{5}(?!\d)', attr)
        return cutting.group()

    # ------------------------数据比较-----------------------------

    def case_time_assert(self, announ_deadline, whole_result):

        # 指定key值获取pandas用例上相应的数据信息
        excel_time = self.overall[announ_deadline]

        assert excel_time != None, "%s 没有设置时间,用例跳过" % self.FUNCTION_NAME
        # 记录当前时间
        self.ANNOUN_SHE_TIME = self.ti.currentToStamp()

    def conditions_operation(self, operation):
        # 按钮判断在这里控制
        # 3.获取用户执行的动作
        _operation = self.overall[operation]  # 获取操作按钮
        if _operation == "确定":
            self.log.info("操作按钮为-->确定吗? %s " % _operation)
            return True
        else:
            self.log.info("操作按钮为-->取消吗? %s " % _operation)
            return False

    # ---------------------------------sql的使用部分-------------------------------
    def mysql_match(self, my_sql: "mysql语句") -> "正则切割sql语句是否为查询语句":
        return re.match('^SELECT', my_sql)

    def _verify_match(self, my_sql):
        '''
        数据库查询
        :param my_sql:  sql语句
        :return:  返回查询到的数据集，没查到数据时返回None
        '''
        regular = self.mysql_match(my_sql)
        if regular:
            # 读取数据库内容
            result = self.mysqlTotalSelects(my_sql)
            return result
        return None

    """
    #---------------------------------创建浏览器并执行登录------------------------------------
    """

    def option_browser(self, options='admin_url'):
        # 调用自定义的浏览器接口
        self.driver = self._browser(option=options)

    def openingProgram(self):
        """
        定义log日志文件以及读取用例数据
        :param basename:  执行用例的文件名
        :param exclefile:  需要读取用例的文件名
        :return:  暂时没有返回值
        """
        self.option_browser()  # 打开浏览器
        self.ps_user_login()  # 用户登录

        pass

    def _excel_Data(self, model_key, filename, SHEETNAME):
        """
        读取配置文件Ini所在地的内容
        :param model_key:
        :param filename:
        :param SHEETNAME:
        :return:
        """
        # 获取excel路径
        conmodel = readModel.establish_con(model="excelmodel")
        consyst = conmodel.get("admin_excel", model_key)
        excelname = conmodel.get("admin_excel", filename)
        file_path = os.path.join(consyst, excelname)

        # 读取相应路径中的数据
        read = OpenExcelPandas(file_path, sheet=SHEETNAME)
        excelData = read.internal_read_excel()

        return excelData

    def get_account_account_password(self):
        conf = readModel.establish_con(model="model")  # 获取账号密码
        account = conf.get("username", "admin_account")
        password = conf.get("username", "admin_password")
        return account, password

    def ps_user_login(self, para=None):
        acc_pa = self.get_account_account_password()  # 获取登录账号和密码
        self.sign_user_login(acc_pa[0], acc_pa[1])  # 进行登录
        pass

    def sign_user_login(self, account, password):
        """
        不需要点击登录就可以直接进入登陆页面
        :param account:
        :param password:
        :return:
        """
        self.vai.name_input(self.driver, 'username', account)
        self.vai.name_input(self.driver, 'password', password)

        self._visible_json_click("loginBtn")
        pass

    # -----------------------输入项--------------------------------------
    def designated_tab_box(self, designated, number):
        '''
        进入指定的box或者tab页面
        :param designated:  box或者tab的key
        :param number:  box或者tab所在的位置
        :return:
        '''
        designated = "%s:nth-child(%s)" % (self.financial[designated], number)
        self.vac.css_click(self.driver, designated)
        pass

    def confirmInput(self, caseTitle, eleInformation):
        """获取用例数据之后并进行输入操作"""
        title = self.overall[caseTitle]  # 根据用例title来读取数据
        # 判断数据是否为None，如果是就返回一个空值‘’
        information = self._verify_parameter(title)
        if type(information) is float:
            information = str(int(information))
        self._visible_json_input(eleInformation, information)  # 通过元素id利用json进行输入输入

    # -----------------------城市编码和默认的获取---------------------
    def default_city_content(self, city_ele, result):
        '''默认进来页面是否为产品规定的'''
        for city in city_ele:
            if city.get_attribute('class') == 'active':
                self.verify_operator(city.text, self.overall[result])
                break

    def lable_code_name(self, city_ele, tag, bute) -> dict:
        '''
        获取城市标签中，全部的code和bane
        :param city_ele:  城市标签元素
        :param tag:  元素携带的标签
        :param bute: 子元素携带的标签
        :return: code为key，name为value的数据集
        '''
        LABLE_DF = {}
        for number in range(1, len(city_ele)):
            element = self._visible_returan_tag_name(city_ele[number], tag, 5)
            code = self.re_cutting_data(element.get_attribute(bute))
            LABLE_DF[code] = element.text
        return LABLE_DF

    def mysql_code_name(self, content) -> dict:
        '''
        根据sql语句查询数据，将数据根据code为key，name为value的原则重新排版
        :param content: sql语句
        :return: code为key，name为value的数据集
        '''
        MYSQL_DF = self._verify_match(content)
        mysql_df = {}
        for mysql in MYSQL_DF:
            mysql_df[str(mysql['city'])] = mysql['name']
        return mysql_df

    def mysql_area_name(self, content, option):
        MYSQL_DF = self._verify_match(content)
        # mysql_df = [(value for value in mysql.values()) for mysql in MYSQL_DF]
        mysql_df = [option]
        for mysql in MYSQL_DF:
            for value in mysql.values():
                mysql_df.append(value)
        return mysql_df

    def list_to_pandas(self, data_list, key_title, column=None):
        '''
        将list转换成pandas数据格式
        :param data_list: 需要转换的list数据
        :param key_title: df数据中key的定义
        :param column: 转换之后，序列号的数据信息
        :return:
        '''
        op_execl = OpenExcelPandas(data_list, key_title)
        data_df = op_execl.conversionPandas(column)  # 转换数据
        if len(data_df.index) > 0:
            self.log.info("list_to_pandas df data is not empty")
            pass
        else:
            self.log.info("list_to_pandas No data...")
            data_df = 0
        return data_df
