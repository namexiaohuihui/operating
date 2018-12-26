# -*- coding: utf-8 -*-
"""
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  -  /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                        `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

               佛祖保佑         永无BUG
@author:    ln_company
@license:   (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@Software:  PyCharm
@file:      action_interface.py
@time:      2018/12/17 17:07
@desc:
"""

import os
from time import sleep
from tools.configs import readModel
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.action_chains import ActionChains
from Warehousing.browser_prepare import BrowserPrepare


class ActionVisible(BrowserPrepare):
    """
    工作内容:
    1.执行元素校验 = [click,input,visible]
    """

    def is_visible_driver(self, way, locator):
        """
        判断类型
        :param way:
        :return:
        """
        if 'css' == way or 'Css' == way:
            ele_by = (By.CSS_SELECTOR, locator)
            pass
        elif 'id' == way or 'Id' == way:
            ele_by = (By.ID, locator)
            pass
        elif 'xpath' == way or 'Xpath' == way:
            ele_by = (By.XPATH, locator)
            pass
        elif 'name' == way or 'Name' == way:
            ele_by = (By.NAME, locator)
            pass
        else:
            raise Exception("is_visible_driver:你写的ele判断有误")
        return ele_by
        pass

    def differentiate_all_exist(self, ele_by, timeout=5):
        """
        一直等待某元素可见，默认超时5秒,返回全部找到的数据元素组
        :param ele_by:
        :param timeout:
        :return:
        """
        try:
            ele = ui.WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(ele_by))
            return ele
        except Exception as e:
            # self.error_log(driver, e)
            print("%s 元素找不到 is_visibles_css_selectop " % locator)
            return False

    def differentiate_single_exist(self, ele_by, timeout=5):
        """
        返回单个元素
        :param ele_by:
        :param timeout:
        :return:
        """
        try:
            ele = ui.WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(ele_by))
            return ele
        except TimeoutException:
            return False

    def differentiate_not_exist(self, ele_by, timeout=5):
        """
        判断元素是否消失
        element_to_be_clickable元素存在并且可用，以便确定元素是可点击的
        :param ele_by:
        :param timeout:
        :return:
        """
        try:
            ui.WebDriverWait(self.driver, timeout).until_not(EC.element_to_be_clickable(ele_by))
            return True
        except TimeoutException:
            return False

    def is_visible_single_driver(self, locator, way, timeout=5):
        """
        查找单个元素
        :param locator:
        :param way:
        :param timeout:
        :return:
        """
        ele_by = self.is_visible_driver(way, locator)
        return self.differentiate_single_exist(ele_by, timeout)

    def is_visible_all_driver(self, locator, way, timeout=5):
        """
        根据路径查找全部符合条件的元素
        :param locator:
        :param way:
        :param timeout:
        :return:
        """
        ele_by = self.is_visible_driver(way, locator)
        return self.differentiate_all_exist(ele_by, timeout)

    def is_visible_not_driver(self, locator, way, timeout=5):
        """
        判断某个元素是否消失
        :param locator:
        :param way:
        :param timeout:
        :return:
        """

        ele_by = self.is_visible_driver(way, locator)
        return self.differentiate_not_exist(ele_by, timeout)

    def get_text_vlue(self, locator, way, attr=None, timeout=5):
        """
        获取元素的text或者attribute
        :param locator: 元素路径
        :param way: 传入的locator为:(css,id,xpath,name)等
        :param attr:  为none时获取元素text,不为空时获取元素的attribute属性值
        :param timeout: 元素可见超时时间
        :return:
        """
        attribute = self.is_visible_single_driver(locator, way, timeout)
        if attr:
            attribute = attribute.get_attribute(attr)
        else:
            attribute = attribute.text
        return attribute

    def scrollBar_mobile_browser(self, action_type):
        """
        将页面滚动条移动到顶部或者底部
        :param action_type:
        :return:
        """
        sleep(1)
        if 'top' == action_type:
            # 将滚动条移动到顶部的意思
            self.driver.execute_script("window.scrollTo(0,0)")
        elif 'buttom' == action_type:
            # 将滚动条移动到底部的意思
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def is_visible_click(self, prompt):
        """
        点击之后将element对象进行返回
        :param browser:
        :param prompt:
        :return:
        """
        prompt.click()
        sleep(1)

    def id_confirm_execute(self, prompt):
        """
        通过id进行js点击
        :param prompt:
        :return:
        """
        self.driver.execute_script("document.getElementById(\'" + prompt + "\').click();")
        pass

    def css_confirm_execute(self, prompt):
        """
        输入元素路径通过js进行点击
        :param prompt:
        :return:
        """
        self.driver.execute_script("document.querySelector(\'" + prompt + "\').click();")
        pass

    def is_click_execute(self, locator, way_type, way, timeout=5):
        """
        执行点击操作
        :param locator:  元素路径 或者 元素本身
        :param way_type:  是通过js来执行点击还是通过路径来找到元素并执行点击
        :param way:  元素路径写法为id还是css
        :param timeout:
        :return:
        """
        if 'js' == way_type:
            if way == 'id':
                self.id_confirm_execute(locator)
                pass
            elif way == 'css':
                self.css_confirm_execute(locator)
                pass
            pass

        elif 'tag' == way_type:
            attribute = self.is_visible_single_driver(locator, way, timeout)
            self.is_visible_click(attribute)
            return attribute

        elif 'ele' == way_type:
            self.is_visible_click(locator)
            pass

        else:
            print("is_viskble_click--没有这个类型:%s" % way_type)

    def is_visible_input(self, attribute, parameter):
        attribute.clear()
        attribute.send_keys(parameter)
        sleep(1)

    def cursor_execute_ordinal(self, locator, way, parameter, timeout=5):
        """
        找到元素,通过JS对value进行写入
        :param browser: 浏览器对象
        :param ordinal: 需要写入元素的路径
        :param parameter: 需要输入的对象
        :return:
        """
        locator = self.is_visible_single_driver(locator, way, timeout)
        self.driver.execute_script("\'" + locator + "\'.value=\'" + parameter + "\';")
        sleep(1)

    def cursor_execute_selectop(self, locator, parameter):
        """
        利用js找到相关selctop的元素,直接对value进行数据修改
        :param locator:
        :param parameter:
        :return:
        """
        self.driver.execute_script("document.querySelector(\'" + locator + "\').value=\'" + parameter + "\';")
        sleep(1)

    def cursor_execute_id(self, locator, parameter):
        """
        利用js找到相关id的元素,直接对value进行数据修改
        :param locator:
        :param parameter:
        :return:
        """
        self.driver.execute_script("document.getElementById(\'" + locator + "\').value=\'" + parameter + "\';")
        sleep(1)

    def is_input_execute(self, locator, way_type, way, parameter, timeout=5):
        """
        执行点击操作
        :param locator:  元素路径 或者 元素本身
        :param way_type:  是通过js来执行点击还是通过路径来找到元素并执行点击
        :param way:  元素路径写法为id还是css
        :param timeout:
        :return:
        """
        if 'js' == way_type:
            if 'id' == way:
                self.cursor_execute_id(locator, parameter)
                pass
            elif 'css' == way:
                self.cursor_execute_selectop(locator, parameter)
                pass
            pass

        elif 'tag' == way_type:
            attribute = self.is_visible_single_driver(locator, way, timeout)
            self.is_visible_input(attribute, parameter)
            return attribute

        elif 'ele' == way_type:
            self.is_visible_input(locator, parameter)
            pass

        elif 'tag_js' == way_type:
            self.cursor_execute_ordinal(locator, way, parameter)
            pass

        else:
            print("is_input_execute--没有这个类型:%s" % way_type)

    def administrator_login(self, *user_ward):
        """
        登录操作
        :param user_name:
        :param pass_ward:
        :return:
        """
        conf = readModel.establish_con(model="model")  # 获取账号密码
        account = conf.get("username", "atorage_account")
        password = conf.get("username", "atorage_password")
        # 账号
        self.is_input_execute(locator='phone', way_type='js', way='id', parameter=account)
        # 密码
        self.is_input_execute(locator='password', way_type='js', way='id', parameter=password)
        # 点击登录
        self.is_click_execute(locator='loginBtn', way_type='js', way='id')
        sleep(1)
        pass

    def cursor_focus_blur(self, ele_attr, cursor_type):
        """
        根据移动的类型来对实现数据操作
        :param ele_attr:  元素对象
        :param cursor_type:  移动类型
        :return:
        """
        if 'blur' == cursor_type:
            self.driver.execute_script("arguments[0].blur();", ele_attr)
            pass
        elif 'focus' == cursor_type:
            self.driver.execute_script("arguments[0].focus();", ele_attr)

    def attribute_focus_blur(self, ele_attr, cursor_type):
        """
        根据元素id的属性值找到元素,并在其上面进行光标移动
        :param ele_attr:
        :param cursor_type:
        :return:
        """
        if 'blur' == cursor_type:
            self.driver.execute_script("document.getElementById(\'" + ele_attr + "\').blur();")
            pass
        elif 'focus' == cursor_type:
            self.driver.execute_script("document.getElementById(\'" + ele_attr + "\').focus();")

    def ac_move_to_element(self, locator, way):
        """
        该函数适用于：
        1.浏览器设置为手机模式
        2.对手机端进行操作
        鼠标移动到指定的元素上并进行点击
        :param locator:
        :return:
        """
        action_ele = self.is_visible_single_driver(locator, way)
        ActionChains(self.driver).move_to_element(action_ele).perform()
        pass

    def touchActions_tap(self, element):
        """
        手机端或者浏览器为手机模式时的单击操作。
        也可模拟一些上拉，下滑的操
        :param element:
        :return:
        """
        TouchActions(self.driver).tap(element).perform()
        sleep(1)
        pass

    def touchActions_selectop_prompt(self, prompt, way, timeout=5):
        ele = self.is_visible_single_driver(prompt, way, timeout)
        self.touchActions_tap(ele)
        pass

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
