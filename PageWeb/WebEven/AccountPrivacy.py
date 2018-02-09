# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: ap.py
@time: 2018/1/4 22:13
@项目名称:operating
"""
import inspect
import os

from practical.utils.config import readModel

from PageWeb.WebEven.ConversionStorage import conversionstorage

from utils.ComparedVerify import compared_verify

"""
# ------------------内容参数的比较------------------------
"""


class account_privacy(compared_verify):
    def function_content_comparison(*parameter):
        # 单※的数据类型为一个数组
        try:
            assert parameter[0] != parameter[1], parameter[2]
        except:
            print(" %s BEI Einem Vergleich der Fehler" % parameter[2])

    def function_content_verification(**parameter):
        # 双※的数据类型为一个列表
        print(parameter, type(parameter))

    """
    #------------------获取浏览器部分------------------------------------
    """

    def option_browser(self):
        self._browser(option="buyer_url")

    """
    #------------------- 用户登录--------------------------------
    """

    def get_account_account_password(self):
        conf = readModel.establish_con(model="model")  # 获取账号密码
        account = conf.get("username", "buyer_account")
        password = conf.get("username", "buyer_password")
        return account, password

    def _route(self):
        # 点击信息页面
        self._visible_css_selectop(".nav-user")
        vai.sleep_Rest()
        # 点击页面中的登录按钮
        self._visible_css_selectop(".user-head")

    def even_user_login(self):
        try:
            acc_pa = get_account_account_password()  # 获取登录账号和密码
            self._route()  # 进入登录页面
            self.sign_user_login(acc_pa[0], acc_pa[1])  # 进行登录
        except Exception:
            function = inspect.stack()[0][3]  # 执行函数的函数名
            self.error_log(function)
            raise

    def sign_switching_logon(account, password):
        """
        点击登陆之后，进行输入账号密码及切换登陆页面的事务
        :param account:
        :param password:
        :return:
        """
        try:
            # 点击登陆按钮
            btn = self._visible_css_selectop('.btn>a:nth-child(1)')
            if btn != False:
                self.sign_user_login(account, password)
            else:
                function = inspect.stack()[0][3]  # 执行函数的函数名
                self.error_log(function)

        except Exception:
            function = inspect.stack()[0][3]  # 执行函数的函数名
            self.error_log(function)
            raise

    def sign_user_login(self, account, password):
        """
        不需要点击登录就可以直接进入登陆页面
        :param account:
        :param password:
        :return:
        """
        try:
            # 切换登陆方式：切换到账号密码登录页面
            self._visible_css_selectop('.login-type>a:nth-child(1)')

            self.sleep_time()

            # 账号密码的输入
            driver.find_element_by_css_selector("#J_tel").send_keys(account)
            driver.find_element_by_css_selector("#J_pwd").send_keys(password)

            self.sleep_time()
            # 登陆按钮
            self._visible_css_selectop(".u-btn.u-btn-morange")
            # 获取登录的提示语
            text = self._visible_css_selectop_text('.toast-cont')
            print("登陆提示信息-----> %s " % text)

            # 储存登陆之后的提示
            conversionstorage().set_remarks(text)

        except Exception:
            function = inspect.stack()[0][3]  # 执行函数的函数名
            self.error_log(function)
            raise

    """
    #--------------------添加商品部分-----------------------------------------
    """

    def add_goods(self):
        """
        选择商品并进行点击
        :return:
        """
        self._visible_css_selectop('.J_add.shop-goods-add.icon-font.icon-plus-str')
        self.sleep_time()

    def details_add_goods(self, account=None, password=None):
        """
        商品详情页点击购买商品
        :return:
        """
        self._visible_css_selectop('.add-cart')  # 点击购买按钮，弹出购物车选择页面

        self._visible_css_selectop('.buy-tiket-btn.cart')  # 点击加入购物车，将商品正式加入购物车

        print("添加商品的提示-----> %s" % _visible_css_selectop_text('.toast-cont'))  # 错误的原因
        self.sleep_time()
        self._visible_css_selectop('.buy.cur')  # 去结算

        self.sign_switching_logon(account, password)

    """
    #--------------------界面滑动函数-----------------------------------------
    """

    def Interface_sliding(self):
        # 实行上下滑动的效果
        self.vac.Interface_sliding(driver)
