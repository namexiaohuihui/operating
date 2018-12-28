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
@author:  ln_company
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file:  openbrowser.py
@time: 2018/12/23 13:05
@Software: PyCharm
@Site    : 
@desc:
"""

import os
from time import sleep
import re
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC

from selenium.webdriver.common.by import By
from tools.configs import readModel


class OpenBrowper(object):

    def open_driver(self, user_url):
        self.driver = webdriver.Chrome(
            executable_path=os.path.join(os.path.split(os.path.abspath(__file__))[0], 'chromedriver.exe'))
        self.driver.maximize_window()
        # 输入网址
        # 等待网页加载，加载时间为10s，加载完就跳过
        # 隐形等待时间和显性等待时间不同时，默认使用两者之间最大的那个
        self.driver.implicitly_wait(5)
        url = readModel.establish_con(model="model").get("wap", user_url)
        self.driver.get(url)
        pass

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

    def is_visible_singles(self, locator, way, timeout=5):
        """
        查找单个元素
        :param locator:
        :param way:
        :param timeout:
        :return:
        """
        try:
            ele_by = self.is_visible_driver(way, locator)
            ele = ui.WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(ele_by))
            return ele
        except:
            return False

    def is_visible_all_drivers(self, locator, way, timeout=5):
        """
        根据路径查找全部符合条件的元素
        :param locator:
        :param way:
        :param timeout:
        :return:
        """
        ele_by = self.is_visible_driver(way, locator)
        ele_list = ui.WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(ele_by)
        )
        return ele_list

    def is_visible_clicks(self, locator, way):
        """
        点击之后将element对象进行返回
        :param browser:
        :param prompt:
        :return:
        """
        attribute = self.is_visible_singles(locator, way)
        if attribute:
            attribute.click()
            sleep(1)
        return attribute
        pass

    def is_visible_inputs(self, locator, way, parameter):
        attribute = self.is_visible_singles(locator, way)
        if attribute:
            attribute.clear()
            attribute.send_keys(parameter)
            sleep(1)
        return attribute
        pass

    def get_ele_text_vlue(self, locator, way, attr=None, timeout=5):
        """
        获取元素的text或者attribute
        :param locator: 元素路径
        :param way: 传入的locator为:(css,id,xpath,name)等
        :param attr:  为none时获取元素text,不为空时获取元素的attribute属性值
        :param timeout: 元素可见超时时间
        :return:
        """
        attribute = self.is_visible_singles(locator, way, timeout)
        if attr:
            attribute = attribute.get_attribute(attr)
        else:
            attribute = attribute.text
        return attribute

    def focus_auto_move(self, br_ele):
        from selenium.webdriver import ActionChains
        ActionChains(self.driver).move_to_element(br_ele).perform()
        sleep(2)

    def report_an_error(self):
        from bs4 import BeautifulSoup
        label_text = self.driver.page_source
        soup = BeautifulSoup(label_text, "lxml")
        fatal_error = soup.br
        if fatal_error:
            fatal_error_pare = fatal_error.parent
            for i, child in enumerate(fatal_error_pare.children, start=1):
                if not child.name in ('div', 'table'):
                    if 'Fatal error' in child:
                        return False
            del fatal_error_pare
            del fatal_error
            pass
        del soup
        return True

    def info_number(self):
        # 读取info的数据并把int数据切割
        info_text = self.is_visible_singles("div.dataTables_info", 'css')

        if info_text:
            info_text = str.split(info_text.text, '，')[-1]
            searchObj = re.search("\d+", info_text)
            info_text = int(searchObj.group() if searchObj else searchObj)
            if (info_text % 10) > 0:
                number = 1
            else:
                number = 0
            info_text = int((info_text / 10)) + number
        return info_text

    def traverse_jump(self, box_path, box_int):
        """
        遍历点击
        :param box_path:
        :param box_int:
        :return:
        """
        tabbox_list = self.is_visible_all_drivers(box_path, 'css', timeout=10)
        # 检验页面有没有出现br错误
        jump_bool = self.report_an_error()
        assert jump_bool, '点击第%s个box时出现错误' % str(box_int)
        if box_int < len(tabbox_list):
            tabbox_list[box_int].click()
            sleep(2)
            return self.traverse_jump(box_path, box_int + 1)
        pass

    def ec_url_changes_jump(self, url_para):
        """校验url是否在里面"""
        return EC.url_changes(url_para)
