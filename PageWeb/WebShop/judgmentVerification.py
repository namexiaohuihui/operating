# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: JudgmentVerification.py
@time: 2018/1/23 10:18
"""
import os
import re

from tools.Logger import Log
from tools.openpyxlExcel import OpenExcelPandas
from utils.comparedVerify import ComparedVerify
from utils.config import readModel
from utils.timeFromat import TimeFromat


class JudgmentVerification(ComparedVerify):
    """
    # 全局参数部分
    """

    def setFunctionName(self, funtion):
        """
        设置需要运行的函数名
        :param funtion:  函数名
        :return:
        """
        # 记录目前执行的函数名（也可以认为目前执行的用例）
        self.FUNCTION_NAME = funtion
        self.log.functionName(self.FUNCTION_NAME)
        # 根据df标签序号获取用例
        self.overall = self.overallExcelData.loc[self.FUNCTION_NAME]
        self.ti = TimeFromat()

    # --------------------------------正则的使用
    def re_cutting_data(self, attr):
        cutting = re.search(r'[1-9]\d{5}(?!\d)', attr)
        return cutting.group()

    """
    # ---------------------数据比较----------------------
    """

    def case_time_assert(self, announ_deadline, whole_result):

        # 指定key值获取pandas用例上相应的数据信息
        excel_time = self.overall[announ_deadline]
        assert excel_time != None, "%s get_time_status 没有设置时间" % self.FUNCTION_NAME
        # 记录当前时间
        self.ANNOUN_SHE_TIME = self.ti.currentToStamp()
        # 将时间进行切割，分成开始开始时间和结束时间
        sttus, enmd = self.ti.cutting_time_current(excel_time)
        # 判断时间用例时间
        status_type = self.judge_time_only(status_time=sttus, status_end=enmd)
        # 用例期望的状态
        whole_result = self.overall[whole_result]
        assert status_type == whole_result, "%s根据时间来判断状态出错 %s %s" % (self.FUNCTION_NAME, status_type, whole_result)

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
            print("msql--->%s" % my_sql)
            result = self.mysqlTotalSelects(my_sql)
            return result
        return None

    # def _verify_single_match(self, my_sql):
    #     '''
    #     数据库查询
    #     :param my_sql:  sql语句
    #     :return:  返回查询到的数据集，没查到数据时返回None
    #     '''
    #     regular = self.mysql_match(my_sql)
    #     if regular:
    #         # 读取数据库内容
    #         result = self.mysql_single_selects(my_sql)
    #         return result
    #     return None

    """
    #------------------创建浏览器并执行登录------------------------------------
    """

    def option_browser(self):
        # 调用自定义的浏览器接口
        self.driver = self._browser(option="admin_url")

    def openingProgram(self, basename, exclefile):
        """
        定义log日志文件以及读取用例数据
        :param basename:  执行用例的文件名
        :param exclefile:  需要读取用例的文件名
        :return:  暂时没有返回值
        """
        # 定义日志
        self.log = Log(basename)
        # 读取文档信息,MODEI_KEY_POSITION位于SystenSerup的init，
        # MODEI_CASE_POSITION位于NoticeController的init
        self.overallExcelData = self._excel_Data(self.MODEI_KEY_POSITION, self.MODEI_CASE_POSITION, exclefile)

        self.option_browser()  # 打开浏览器
        self.ps_user_login()  # 用户登录
        pass

    def _excel_Data(self, model_key, filename, SHEETNAME):

        # 获取excel路径
        conmodel = readModel.establish_con(model="excelmodel")
        consyst = conmodel.get("excel", model_key)
        excelname = conmodel.get("excel", filename)
        file_path = os.path.join(consyst, excelname)
        # 读取相应路径中的数据
        read = OpenExcelPandas(file_path, sheet=SHEETNAME)
        # 之前是用readCaseExcel这个函数但是感觉时代要变化就用了internal_read_excel
        # excelData = read.readCaseExcel()
        excelData = read.internal_read_excel()
        return excelData

    def get_account_account_password(self):
        conf = readModel.establish_con(model="model")  # 获取账号密码
        account = conf.get("username", "admin_account")
        password = conf.get("username", "admin_password")
        return account, password

    def ps_user_login(self):
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
    def confirmInput(self, caseTitle, eleInformation):
        """获取用例数据之后并进行输入操作"""
        title = self.overall[caseTitle]  # 根据用例title来读取数据

        information = self._verify_parameter(title)  # 判断数据是否为None，如果是就返回一个空值‘’

        print("输入的内容: %s 输入的对象: %s 输入的地方: %s " % (information, eleInformation, caseTitle))
        self._visible_json_input(eleInformation, information)  # 通过元素id利用json进行输入输入

    # -----------------------城市编码和那么的获取---------------------
    def default_city_content(self, city_ele, result):
        '''默认进来页面是否为产品规定的'''
        for city in city_ele:
            if city.get_attribute('class') == 'active':
                self._verify_operator(city.text, self.overall[result])
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

    def mysql_code_name(self, content)->dict:
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
