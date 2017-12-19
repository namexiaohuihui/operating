# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: web_ToSign.py
@time: 2017/12/19 21:11
@项目名称:operating
"""
import unittest
from selenium.webdriver.common.touch_actions import TouchActions
from practical.constant.browser.browser_establish import browser_confirm
class signtoyou:
    @classmethod
    def setUpClass(cls):
        # 该类运行时优先调用的函数
        print("")

    @classmethod
    def tearDownClass(cls):
        # 该类结束时最后调用的函数
        print("")

    def url_op(self):
        # options = mobile_phone_mode()

        # 1.创建浏览器所在函数的对象
        bc = browser_confirm.__new__(browser_confirm)

        # 2.调用已经规划好的浏览器函数
        self.driver = bc.url_opens('-------')

        try:
            if self.is_visible_css_selectop('.am-dialog-button') is not False:
                # 城市选择框.上线版本是不虚言进行选择的
                tt = self.driver.find_element_by_css_selector('.am-dialog-button')

                TouchActions(self.driver).tap(tt).perform()
        except:
            print("没有出来")
        finally:# 即使发生错误也要继续执行
            self.Interface_sliding()
            size = self.driver.find_elements_by_css_selector(".J_add.shop-goods-add.icon-font.icon-plus-str")
            size[0].click() # 添加购物车
            self.sleep_Rest()
            self.is_visible_css_selectop('.J_goBuy.m-cart-by').click() # 去结算

            # 登陆
            self.is_visible_css_selectop('.btn >a:nth-child(1)').click()

            screen = self.get_size()
            if screen[0] <=1500:
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 底部
            else:
                print(screen)
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 底部


            self.is_visible_css_selectop('.login-type>a:nth-child(1)').click() # 切换登陆方式

            self.driver.execute_script("document.getElementById('J_tel').value=1234561111;")
            self.sleep_Rest()
            self.driver.execute_script("document.getElementById('J_pwd').value=1234561111;")
            self.sleep_Rest()
            self.driver.find_element_by_css_selector(".u-btn.u-btn-morange").click()#输入内容
            print(self.is_visible_css_selectop('.toast-cont').text)



    def sleep_Rest(self,ti = 2):
        import time
        time.sleep(ti)

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def Interface_sliding(self):
        import datetime
        print(datetime.datetime.now(),"滚动")
        # 实行上下滑动的效果
        screen = self.get_size()

        x1 = screen[0] * 0.5
        y1 = screen[1] * 0.75

        cart_cont = self.driver.find_element_by_css_selector('.m-cart-cont')

        TouchActions(self.driver).scroll_from_element(cart_cont, x1, y1).perform()

        print(datetime.datetime.now(),"UN薄膜")
    # 一直等待某元素可见，默认超时10秒
    def is_visible_css_selectop(self, locator, timeout=5):
        import datetime
        print(datetime.datetime.now())
        try:
            import selenium.webdriver.support.ui as ui
            import selenium.webdriver.support.expected_conditions as EC
            from selenium.common.exceptions import TimeoutException
            from selenium.webdriver.common.by import By
            ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            element = self.driver.find_element_by_css_selector(locator) # 切换登陆方式
            return element
        except TimeoutException:
            print("元素未出现：   %s" % locator)
            print(datetime.datetime.now())
            return False
    def test_ShoppingCart_login(self):
        """
        1.选择商品
        2.去结算
        :return:
        """
if __name__ == '__main__':
    sign = signtoyou()
    sign.url_op()