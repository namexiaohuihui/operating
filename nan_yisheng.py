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

@Software: dingdong
@contact : 704866169@gqq.com
@license : (C) Copyright 2019- 2019, Node Supply Chain Manager Corporation Limited.
@author  : hz
@project : operating
@file    : nan_yisheng.py
@time    : 2019/8/3 14:49
@ide     : PyCharm
@desc    :
"""
import os
import time

import unittest
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.expected_conditions as EC

driver_path = 'E:\drivers\Drivers'
url = ''


class TestNanYiSheng(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=os.path.join(driver_path, 'chromedriver75.exe'), )
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(url)
        pass

    def tearDown(self) -> None:
        time.sleep(5)

    def log_print(self, msg):
        print(msg + '\n')

    def is_visible_css_selectop(self, locator, timeout=5):
        # 一直等待某元素可见，默认超时5秒，返回找到的单个元素
        try:
            ele = ui.WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return ele
        except Exception as e:
            self.log_print('is_visible_css_selectop 元素不存在出现超时的情况 %s' % locator)
            return False

    def is_visibles_css_selectop(self, locator, timeout=5):
        # 根据路径查找路径下的全部元素，默认超时5秒，返回找到的全部元素
        try:
            ele = ui.WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, locator)))
            return ele
        except Exception as e:
            print('is_visible_css_selectop 元素不存在出现超时的情况 %s' % locator)
            # self.error_log(driver, e)
            return False

    def ele_clear_keys(self, ele, parameter):
        # 执行输入的操作
        ele.clear()
        time.sleep(1)
        ele.send_keys(parameter)
        time.sleep(1)

    def zhanghao_mima(self):
        # 输入账号
        self.log_print('开始输入账号')
        er_user = self.is_visible_css_selectop('.user')
        self.ele_clear_keys(er_user, '')
        self.log_print('账号输入完毕')

        # 输入密码
        self.log_print('开始输入密码')
        er_pass = self.is_visible_css_selectop('.pass')
        self.ele_clear_keys(er_pass, '')
        self.log_print('密码输入完毕')

        # 延迟10s手动输入验证码
        time.sleep(10)
        self.log_print('等待输入验证码')

        # 点击登录
        # self.is_visible_css_selectop('.layui-btn.layui-btn-warm.right').click()
        self.log_print('跳过--登录按钮点击完毕')

    def jinru_muen(self):
        # 点击一级菜单
        self.log_print('开始进入一级菜单')
        self.is_visible_css_selectop('#subnav_body > div:nth-child(1) > h3').click()
        self.log_print('一级菜单选择完毕')

        # 点击二级菜单
        self.log_print('开始进入二级菜单')
        self.is_visible_css_selectop('#subnav_body > div.s > ul > li:nth-child(3)').click()
        self.log_print('二级菜单选择完毕')

        # 切换到iframe
        self.log_print('开始切换到iframe里面')
        iframe = self.is_visible_css_selectop('#mainframe > iframe:nth-child(2)')
        self.driver.switch_to.frame(iframe)
        self.log_print('iframe切换完毕')

    def dianji_select(self):
        # 找到院区和科室的元素
        nan_select = self.is_visibles_css_selectop('div.input > select')
        # 选择院区
        self.log_print('开始选择医院')
        select = Select(nan_select[0])
        select.select_by_value('5')

        # 选择科室
        self.log_print('开始选择科室')
        select = Select(nan_select[-1])
        select.select_by_visible_text('└肾内科')
        del select
        pass

    def dianji_input(self):
        # 找到医生名/医生编码/职称职务的元素
        yisheng_input = self.is_visibles_css_selectop('div.input>input')

        # 输入医生名字
        self.log_print('输入医生名字')
        self.ele_clear_keys(yisheng_input[0], '测试医生')

        # 输入医生编码
        self.log_print('输入医生编码')
        self.ele_clear_keys(yisheng_input[1], '测试编码')

        # 输入职称职务
        self.log_print('输入职称职务')
        self.ele_clear_keys(yisheng_input[2], '测试职称职务')

        # 找到擅长/简介的元素
        yisheng_textarea = self.is_visibles_css_selectop('div.input>textarea')

        # 输入擅长
        self.log_print('输入擅长')
        self.ele_clear_keys(yisheng_textarea[0], '测试擅长')

        # 输入简介
        self.log_print('输入简介')
        self.ele_clear_keys(yisheng_textarea[1], '测试简介')

        # 点击提交按钮
        self.log_print('找到保存按钮的元素并点击')
        self.is_visible_css_selectop('.layui-btn.layui-btn-normal.right').click()
        time.sleep(2)

        # 点击系统弹窗中的确认按钮
        alert_obj = self.driver.switch_to.alert
        self.log_print('弹窗内容%s' % alert_obj.text)
        alert_obj.dismiss()
        pass

    def key_sousuo(self):
        # 在关键字输入框输入关键字
        key_input = self.is_visible_css_selectop('div.input > input')
        self.ele_clear_keys(key_input, '傻逼')

        # 点击查询按钮
        self.is_visible_css_selectop('div.hz_btn>button').click()

        # 判断是否出现内容
        body = self.is_visibles_css_selectop('#body > div')
        if '暂无记录' == body[-1].text:
            self.log_print('根据关键字（傻逼）没有找到数据')
            pass

        # 点击添加按钮
        self.is_visible_css_selectop('.hz_btn_blue').click()

        # 选择院区/科室
        self.dianji_select()

        # 输入关键字
        self.dianji_input()

    def key_yes_Data(self):
        # 搜索出有用的内容
        key_input = self.is_visible_css_selectop('div.input > input')
        self.ele_clear_keys(key_input, '李通')
        self.is_visible_css_selectop('div.hz_btn>button').click()
        body = self.driver.find_elements_by_css_selector('#all > div > table > tbody')
        self.log_print('根据关键字（李）找到(%s)条数据' % (len(body) - 1))

        # 点击编辑按钮
        self.is_visible_css_selectop('tbody:nth-child(2) > tr > td:nth-child(10) > a').click()

        # 输入关键字
        self.dianji_input()
        pass

    def case_yun(self):
        self.zhanghao_mima()
        self.jinru_muen()
        # self.key_yes_Data()
        self.key_sousuo()

    def test_case(self):
        self.case_yun()


if __name__ == '__main__':
    unittest.main(verbosity=2)
