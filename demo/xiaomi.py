#!/bin/env python
# coding=utf-8
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium import webdriver
import time
import unittest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class GetXiaoMi:
    driver = webdriver.Chrome(executable_path=r"E:\drivers\Drivers\chromedriver62-64.exe")
    url = 'https://item.mi.com/product/7831.html'

    # 一直等待某元素可见，默认超时10秒
    def is_visible_id(self, locator, timeout=5):
        try:
            ele = ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return ele
        except TimeoutException:
            return False

    def login(self):
        # try:
        self.driver.get(self.url)
        # home_login_butten = self.driver.find_element_by_xpath(".//*[@class='J_proLogin']")
        home_login_butten = self.is_visible_id(".J_proLogin")
        home_login_butten.click()
        input_username = self.is_visible_id('.item_account')
        input_username.clear()
        input_username.send_keys('18778036030')
        input_password = self.is_visible_id('#pwd')
        input_password.clear()
        input_password.send_keys('QWEASD11')
        login_butten = self.is_visible_id('#login-button')
        login_butten.click()
        input_nierong = self.is_visible_id('.btn-wrap.clearfix>li>a')
        print(input_nierong)
        print(input_nierong.text)
        # assert self.is_visible_id(".error-con") == u"登陆失败，请检查用户名或密码" , "111"
        # self.driver.assertIsNotNone(self.driver.find_element_by_xpath(".//*[@class='error-con']"),
        #                             u"登陆失败，请检查用户名或密码")
        # except Exception, e:
        #     print e

    @staticmethod
    def get_sys_time():
        sys_time = time.time()
        return sys_time

    @staticmethod
    def set_stamp():
        set_time = '2018-04-03 16:59:55'  # 设置抢购时间，最好提前几秒
        # 将其转换为时间数组
        time_array = time.strptime(set_time, '%Y-%m-%d %H:%M:%S')
        # 转换为时间戳
        time_stamp = int(time.mktime(time_array))
        return time_stamp

    def get_xiaomi(self):
        try:
            self.login()
            if self.get_sys_time() >= self.set_stamp():
                while True:
                    self.driver.find_element_by_xpath(".//*[@id='J_buyBtnBox']/li/a").click()
                    print (u'又悲剧了，默默的问候小米~ %s ' % self.get_sys_time() )
                    time.sleep(1)
            else:
                print (u'时间设置错误')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # run = GetXiaoMi()
    # run.get_xiaomi()
    ssa = """nihao %s %s gsrfwer  %s """  % ( "erwqe","dfgdf","asdas")
    print(ssa)