# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: web_discount.py
@time: 2017/10/24 21:58
@项目名称:operating
城市内容设置的case：
1.所开通的城市判断
2.单个城市数据输入
"""
import inspect
import os
import unittest
from time import sleep

import sys

from practical.constant.browser.browser_establish import browser_confirm
from practical.constant.parameter.parameter_data import parameter_content


class discount_input(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        print("%s   开始执行" % cls.basename)
        cls.url_op(cls)

    @classmethod
    def tearDownClass(cls):
        print("%s   执行完毕" % cls.basename)
        #cls.browser.close()

    # 调用浏览器对象
    def url_op(self):
        bc = browser_confirm.__new__(browser_confirm)

        # 创建浏览器对象
        self.browser = bc.url_opens()

        # 创建参数对象
        #self.parame = parameter_content()

    '''
    验证城市以及数量是否正确
    '''
    def test_number(self):
        ele_div = self.browser.find_element_by_css_selector('.box-city')
        ele_a = ele_div.find_elements_by_tag_name('a')
        submit = ele_div.find_element_by_css_selector('.btn.btn-primary.settingSave')
        #打印数量
        print(len(ele_a))

        # 通过id找到元素并进行输入:商品不参与数
        self.browser.execute_script("document.getElementById('goods_id').value='0.1';")
        # 通过id找到元素并进行输入:绑定打折数
        self.browser.execute_script("document.getElementById('watiki_discount').value='0.1';")
        # 通过id找到元素并进行输入:绑定不参与数
        self.browser.execute_script("document.getElementById('watikis_id').value='0.1';")
        # 通过id找到元素并进行输入:绑定最高数
        self.browser.execute_script("document.getElementById('watikis_max').value='0.1';")

    '''
    验证商品打折数输入大于10的问题
    '''
    def test_goods_discount_one(self):
        #获取函数名
        function = inspect.stack()[0][3]

        # 通过id找到元素并进行输入:商品打折数
        self.browser.execute_script("document.getElementById('goods_discount').value='111';")

        #输入错误出现的提示
        massegn = '请输入0.1~9.9之间的数'

        self.verification(massegn,function)

    '''
    验证商品打折数输入小于0的问题:即输入负数
    '''
    def test_goods_discount_two(self):
        # 获取函数名
        function = sys._getframe().f_code.co_name

        # 传入名字和需要输入的参数
        self.format_goods_discount(function, '-1')

    '''
    验证商品打折数输入在符合范围内但小数点后有多位的情况
    '''
    def test_goods_discount_three(self):
        # 获取函数名
        function = sys._getframe().f_code.co_name

        # 传入名字和需要输入的参数
        self.format_goods_discount(function, '2.333')

    '''
    验证商品打折数输入中文字符
    '''
    def test_goods_discount_four(self):
        # 获取函数名
        function = sys._getframe().f_code.co_name

        #传入名字和需要输入的参数
        self.format_goods_discount(function,'你好')


    '''
    因为同一个输入框，输入不同内容都会出现相同的提示所以写在一起了
    '''
    def format_goods_discount(self,function,parameter):
        # 通过id找到元素并进行输入:商品打折数
        self.browser.execute_script("document.getElementById('goods_discount').value=\'"+parameter+"\';")

        # 输入错误出现的提示
        massegn = '请输入正确格式例如 0.1/0.5'

        self.verification(massegn,function)

    """
    输入之后，点击其他元素，焦点移除之后会验证输入的内容是否符合。
    如果不符合就进行提示。
    点击提示框中的确认按钮表示已经查看了提示框，顺路读取提示框中的提示文字
    然后判断提示文字是否为程序设置的。
    """
    def verification(self,massegn,function):
        # 找到提交按钮
        submit = self.browser.find_element_by_css_selector('.btn.btn-primary.settingSave')
        # 点击提交按钮。
        self.browser.execute_script("arguments[0].click();", submit)

        visible = self.browser.find_element_by_css_selector('.sweet-alert.showSweetAlert.visible >p').text

        sleep(1)
        # 提示框中的提示按钮
        confirm = self.browser.find_element_by_css_selector('.confirm')
        # 点击提交按钮
        self.browser.execute_script("arguments[0].click();", confirm)

        assert massegn == visible, function + '折扣数输入过大,提示你出现错误'

if __name__ == '__main__':
    unittest.main()


