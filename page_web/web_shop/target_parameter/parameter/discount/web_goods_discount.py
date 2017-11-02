# -*- coding: utf-8 -*-
import os
from time import sleep

__author__ = 'Administrator'
"""
@file: web_goods_discount.py
@time: 2017/11/2 9:53
"""

import inspect
import unittest
import sys
from page_web.web_shop.target_parameter.parameter.discount.discount import discount_input


class goods_discount(discount_input, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.setUpStart(cls, basename)

    @classmethod
    def tearDownClass(cls):
        print("%s   执行完毕" % cls.basename)
        cls.tearDownStop(cls)

    '''
    验证城市以及数量是否正确
    '''

    def qwetest_number(self):
        ele_div = self.browser.find_element_by_css_selector('.box-city')
        ele_a = ele_div.find_elements_by_tag_name('a')
        # 打印数量
        print(len(ele_a))
        """
        # 通过id找到元素并进行输入:商品不参与数
        self.browser.execute_script("document.getElementById('goods_id').value='0.1';")
        # 通过id找到元素并进行输入:绑定打折数
        self.browser.execute_script("document.getElementById('watiki_discount').value='0.1';")
        # 通过id找到元素并进行输入:绑定不参与数
        self.browser.execute_script("document.getElementById('watikis_id').value='0.1';")
        # 通过id找到元素并进行输入:绑定最高数
        self.browser.execute_script("document.getElementById('watikis_max').value='0.1';")
        """

    '''
    验证商品打折数输入大于10的问题
    '''

    def qwetest_goods_discount_one(self):
        # 获取函数名
        function = inspect.stack()[0][3]
        print(function)

        # 输入错误出现的提示
        massegn = '请输入0.1~9.9之间的数'

        # 传入名字和需要输入的参数
        # 调用公告方法进行数据输入和判断
        self.format_goods_discount(function, '111', massegn)

    '''
    验证商品打折数输入小于0的问题:即输入负数
    '''

    def qwetest_goods_discount_two(self):
        # 获取函数名
        function = sys._getframe().f_code.co_name
        print(function)

        # 传入名字和需要输入的参数
        # 调用公告方法进行数据输入和判断
        self.format_goods_discount(function, '-1')

    '''
    验证商品打折数输入在符合范围内但小数点后有多位的情况
    '''

    def qwetest_goods_discount_three(self):
        # 获取函数名
        function = sys._getframe().f_code.co_name
        print(function)

        # 传入名字和需要输入的参数
        # 调用公告方法进行数据输入和判断
        self.format_goods_discount(function, '2.333')

    '''
    验证商品打折数输入中文字符
    '''

    def qwetest_goods_discount_four(self):
        # 获取函数名
        function = sys._getframe().f_code.co_name
        print(function)

        # 传入名字和需要输入的参数
        # 调用公告方法进行数据输入和判断
        self.format_goods_discount(function, '你好')

    def test_goods_discount_five(self):
        # 获取函数名
        function = sys._getframe().f_code.co_name
        print(function)

        # 传入名字和需要输入的参数
        # 调用公告方法进行数据输入和判断
        # self.format_goods_discount(function, '1.2')
        self.browser.execute_script("document.getElementById('goods_discount').value='2.7';")

        # 找到提交按钮，点击提交按钮。
        submit = self.browser.find_element_by_css_selector('.btn.btn-primary.settingSave')
        self.browser.execute_script("arguments[0].click();", submit)
        sleep(1)
        pop_text = self.browser.find_element_by_css_selector('.modal-body>h4').text
        center = self.browser.find_element_by_css_selector('.modal-body>p').text
        print('pop_text: %s' % pop_text)
        print('center: %s' % center)
        sleep(2)
        assert pop_text == '你确定要保存吗？', '你确定要保存吗？失败'
        assert center == '保存后新产生的订单立即生效已产生的订单不受影响', '保存后新产生的订单立即生效已产生的订单不受影响？失败'
        sleep(2)
        self.browser.execute_script("document.getElementById('discountsave').click();")
        # self.browser.execute_script("document.querySelectorAll('confirm').click();")
        visible = self.browser.find_element_by_css_selector('.sweet-alert.showSweetAlert.visible >h2').text
        assert visible == '操作成功', '操作成功？失败'
        sleep(2)
        print('你大爷的: %s' % visible)
        # self.browser.execute_script("document.querySelectorAll('.confirm').click();")
        # 点击提示框中的确定按钮，表示已经查看
        confirm = self.browser.find_element_by_css_selector('.confirm')
        self.browser.execute_script("arguments[0].click();", confirm)
        sleep(2)


if __name__ == '__main__':
    unittest.main()
