# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: ExclusiveOperation.py
@time: 2017/12/20 22:49
@项目名称:operating
"""
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.touch_actions import TouchActions

from PageWeb.WebEven.ConversionStorage import conversionstorage


class exclusiveoperation(object):
    """
#------------------获取浏览器部分------------------------------------
    """

    def sign_browser(self):
        from practical.constant.browser_establish import browser_confirm
        # 1.创建浏览器所在函数的对象
        bc = browser_confirm.__new__(browser_confirm)
        options = bc.mobile_phone_mode()

        from practical.config import readModel
        conf = readModel.establish_con()
        url = conf.get("wap", "url")

        # 2.调用已经规划好的浏览器函数
        self.driver = bc.url_opens(url, options)

    """
#--------------------用户登录部分-----------------------------------------
    """

    def sign_switching_logon(self, account, password):
        """
        点击登陆之后，进行输入账号密码及切换登陆页面的事务
        :param account:
        :param password:
        :return:
        """
        try:
            # 点击登陆按钮
            self.is_visible_css_selectop('.btn>a:nth-child(1)')

            self.sign_user_login(account, password)

        except Exception as message:
            function = inspect.stack()[0][3]  # 执行函数的函数名
            self.error_log(function, message)
            raise

    def sign_user_login(self, account, password):
        """
        不需要点击登录就可以直接进入登陆页面
        :param account:
        :param password:
        :return:
        """
        try:
            self.is_visible_css_selectop('.login-type>a:nth-child(1)')  # 切换登陆方式

            # 账号密码的输入
            self.driver.find_element_by_css_selector("#J_tel").send_keys(account)
            self.driver.find_element_by_css_selector("#J_pwd").send_keys(password)

            # 登陆按钮
            self.is_visible_css_selectop(".u-btn.u-btn-morange")

            # 获取登录的提示语
            text = self.is_visible_css_selectop_text('.toast-cont')
            print("登陆提示信息-----> %s " % text)
            # 储存登陆之后的提示
            conversionstorage().set_remarks(text)

        except Exception as message:
            function = inspect.stack()[0][3]  # 执行函数的函数名
            self.error_log(function, message)
            raise

        """
#--------------------添加商品部分-----------------------------------------
        """

    def add_goods(self):
        """
        选择商品并进行点击
        :return:
        """
        self.is_visible_css_selectop('.J_add.shop-goods-add.icon-font.icon-plus-str')
        self.sleep_Rest(2)

    def details_add_goods(self, account=None, password=None):
        """
        商品详情页点击购买商品
        :return:
        """
        self.is_visible_css_selectop('.add-cart')  # 添加购物车

        self.is_visible_css_selectop('.buy-tiket-btn.cart')  # 添加购物车

        self.log.info("添加商品的提示-----> %s" % self.is_visible_css_selectop_text('.toast-cont'))  # 错误错误的原因
        self.sleep_Rest()
        self.is_visible_css_selectop('.buy.cur')  # 去结算

        self.sign_switching_logon(account, password)


        """
#--------------------浏览器操作部分-----------------------------------------
        """

    def get_size(self):
        # 获取浏览器的大小
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def Interface_sliding(self):

        # 实行上下滑动的效果
        screen = self.get_size()

        x1 = screen[0] * 0.5
        y1 = screen[1] * 0.75

        TouchActions(self.driver).scroll(x1, y1).perform()


    def touchActions_tap(self, element):
        # 点击元素
        TouchActions(self.driver).tap(element).perform()
        self.sleep_Rest()

        """
#--------------------元素判断部分-----------------------------------------
        """

    def is_visible_css_selectop(self, locator, timeout=3):
        # 一直等待某元素可见，默认超时10秒
        try:
            import datetime
            # ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            element = ui.WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            self.sleep_Rest(1)
            self.touchActions_tap(element)
            return element
        except TimeoutException:
            print("元素未出现：   %s" % locator)
            return False

    def is_visible_css_selectop_text(self, locator, timeout=3):
        # 一直等待某元素可见，默认超时10秒
        try:
            import datetime
            _ele = ui.WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            text = _ele.text  # 创建元素对象
            return text
        except TimeoutException:
            print("元素未出现：   %s" % locator)
            return False

        """
#--------------------其他一些配置部分-----------------------------------------
        """

    def sleep_Rest(self, ti=1):  # 延迟
        import time
        time.sleep(ti)

    def error_log(self, function, message):
        # 执行文件的文件名
        basename = os.path.splitext(os.path.basename(__file__))[0]

        # 拼接名字
        name_tion = basename + ":" + function

        # 调用错误类
        from practical.utils.DefinitionError import definition_error
        definition_error().error_output(name_tion, message, self.browser)
