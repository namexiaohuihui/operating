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
from practical.config import readModel

class exclusiveoperation(object):
    def setStart(self):
        self.sign_browser()  # 打开浏览器

    def setStop(self):
        pass

    def sign_browser(self):

        from practical.constant.browser_establish import browser_confirm
        # 1.创建浏览器所在函数的对象
        bc = browser_confirm.__new__(browser_confirm)
        options = bc.mobile_phone_mode()

        conf = readModel.establish_con()
        url = conf.get("wap", "url")
        # 2.调用已经规划好的浏览器函数
        self.driver = bc.url_opens(url, options)

        # 账号密码输入
        # self.sign_username(bc)

    def sign_username(self, bc,conf=None):
        if not conf:conf = readModel.establish_con()
        account = conf.get("username", "account")
        password = conf.get("username", "assword")
        bc.case_browesr(account, password)

    def sign_switching_logon(self,account,password):
        try:
            # 点击登陆按钮
            btn = self.is_visible_css_selectop('.btn>a:nth-child(1)')

            login = self.is_visible_css_selectop('.login-type>a:nth-child(1)')  # 切换登陆方式

            # self.driver.execute_script("document.getElementById('J_pwd').value=" + password + ";")
            self.driver.execute_script("document.getElementById('J_tel').value=" + account + ";")
            self.driver.find_element_by_css_selector("#J_pwd").send_keys(password)

            morange = self.driver.find_element_by_css_selector(".u-btn.u-btn-morange")  # 输入内容
            self.driver.execute_script("arguments[0].click();", morange)
            self.log.info("登陆时提示内容： %s" % self.is_visible_css_selectop('.toast-cont').text)  # 错误错误的原因
            from PageWeb.WebEven.PersonalCenter.ExclusiveService.TemporaryData import temporarystorage
            temporarystorage().set_remarks(self.is_visible_css_selectop('.toast-cont').text)
        except Exception as msg:
            from practical.utils.logger import Log
            import os
            import inspect
            basename = os.path.splitext(os.path.basename(__file__))[0]
            function = inspect.stack()[0][3]
            name_tion = basename + ":" + function
            self.log = Log(name_tion,classification='ERROR')
            self.log.info("sign_switching_logon 出现错误.. %s" %msg)
            raise

    def sleep_Rest(self, ti=2):  # 延迟
        import time
        time.sleep(ti)

    def get_size(self):  # 获取浏览器的大小
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def Interface_sliding(self):

        # 实行上下滑动的效果
        screen = self.get_size()

        x1 = screen[0] * 0.5
        y1 = screen[1] * 0.75

        cart_cont = self.driver.find_element_by_css_selector('.m-cart-cont')

        # 从指定的元素开始滑动
        # TouchActions(self.driver).scroll_from_element(cart_cont, x1, y1).perform()
        TouchActions(self.driver).scroll(x1, y1).perform()

    def touchActions_tap(self, element):
        TouchActions(self.driver).tap(element).perform()

    def is_visible_css_selectop(self, locator, timeout=10):
        # 一直等待某元素可见，默认超时10秒
        try:
            import datetime
            ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            element = self.driver.find_element_by_css_selector(locator)  # 创建元素对象
            self.touchActions_tap(element)
            return element
        except TimeoutException:
            print("元素未出现：   %s" % locator)
            return False
