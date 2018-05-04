# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: JudgmentVerification.py
@time: 2018/1/23 10:18
"""
import re
import inspect
from tools.Logger import Log
from utils.config import readModel
from utils.comparedVerify import ComparedVerify
import operator  # 任何对象都可以比较功能


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

    """
    # ---------------------数据比较----------------------
    """

    def _verify_operator(self, reValue, excleValue):
        """
        数据比较
        :param reValue:  数据源
        :param excleValue:  比较源
        :return:
        """
        self.log.info("读mysql data :  %s  类型 :  %s " % (reValue,type(reValue)))
        self.log.info("获excle data :  %s  类型 :  %s " % (excleValue,type(excleValue)))
        re_ex = operator.eq(reValue, excleValue)
        return re_ex

    def _verify_match(self, my_sql):
        '''
        数据库查询
        :param my_sql:  sql语句
        :return:  返回查询到的数据集，没查到数据时返回None
        '''
        regular = re.match('^SELECT', my_sql)
        if regular != None:
            # 读取数据库内容
            result = self.mysqlTotalSelects(my_sql)
            # re_df = self.conversionPandas(result) # 暂时不需要将数据转换成df形式
            return result
        return None

    """
    #------------------获取浏览器部分------------------------------------
    """

    def option_browser(self):
        self.driver = self._browser(option="admin_url")

    def openingProgram(self, basename, exclefile):
        """
        定义log日志文件以及读取用例数据
        :param basename:  执行用例的文件名
        :param exclefile:  需要读取用例的文件名
        :return:  暂时没有返回值
        """
        # 拿出文件名和工作薄
        exclename = exclefile[0]
        exclesheet = exclefile[1]
        # 定义日志
        self.log = Log(basename)
        # 读取文档信息
        self.overallExcelData = self._excel_Data(exclename, exclesheet)

        self.option_browser()  # 打开浏览器
        self.ps_user_login()  # 用户登录
        pass

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

    # -----------------------输入项----------------
    def confirmInput(self, caseTitle, eleInformation):
        """获取用例数据之后并进行输入操作"""
        title = self.overall[caseTitle]  # 根据用例title来读取数据

        information = self._verify_parameter(title)  # 判断数据是否为None，如果是就返回一个空值‘’

        print("输入的内容: %s 输入的对象: %s 输入的地方: %s " % (information,eleInformation,caseTitle))
        self._visible_json_input(eleInformation, information)  # 通过元素id利用json进行输入输入

