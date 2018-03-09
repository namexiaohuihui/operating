# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: JudgmentVerification.py
@time: 2018/1/23 10:18
"""
import re
import inspect
from utils.config import readModel
from utils.ComparedVerify import compared_verify
import operator  # 任何对象都可以比较功能


class judgment_verification(compared_verify):

    """
    数据比较
    """
    def _verify_operator(self,re_value,excle_value):
        re_ex = operator.eq(re_value, excle_value)
        print("--------------------------------------")
        print("读 data :  %s" % re_value)
        print("获 data :  %s" % excle_value)
        print("最终结果 : %s " % re_ex)
        print("--------------------------------------")
        return re_ex

    def _verify_attr_name(self, my_sql, *codeattr):
        re_df = self._verify_match(my_sql)

        # 比较两个list的内容
        list_name = codeattr[0]
        list_attr = codeattr[1]
        verify_name = self.separation(re_df, 'name', codeattr[0])
        verify_code = self.separation(re_df, 'code', codeattr[1])

        list_code = []
        for code in range(len(verify_code)):
            content = "编号： %s 结果为 %s,城市名： %s 结果为 %s" \
                      % (list_attr[code], verify_code[code], list_name[code], verify_name[code])
            list_code.append(content)

        return list_code

    """
    正则的验收
    """

    def separation(self, re_df, title, content):
        re_name = re_df[title]
        _verify = operator.eq(re_name, content)
        return _verify

    def _verify_match(self, my_sql):
        # 数据库查询
        regular = re.match('^SELECT', my_sql)
        re_df = None
        if regular != None:
            # 读取数据库内容
            result = self.mysql_total_selects(my_sql)
            re_df = self._conversion_pandas(result)

        return re_df

    """
    #------------------获取浏览器部分------------------------------------
    """

    def option_browser(self):
        self.driver = self._browser(option="admin_url")

    def get_account_account_password(self):
        conf = readModel.establish_con(model="model")  # 获取账号密码
        account = conf.get("username", "admin_account")
        password = conf.get("username", "admin_password")
        return account, password

    def _route(self):
        # 点击信息页面
        self._visible_css_selectop(".nav-user")
        self.sleep_time()
        # 点击页面中的登录按钮
        self._visible_css_selectop(".user-head")

    def ps_user_login(self):
        acc_pa = self.get_account_account_password()  # 获取登录账号和密码
        self.sign_user_login(acc_pa[0], acc_pa[1])  # 进行登录

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
