# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: discount.py
@time: 2017/10/24 21:58
@项目名称:operating
城市内容设置的case：
1.所开通的城市判断
2.单个城市数据输入
"""
from time import sleep

from practical.constant.browser.browser_establish import browser_confirm


class discount_input():

    def setUpStart(cls,basename):
        cls.basename = basename
        print("%s   开始执行" % cls.basename)
        cls.url_op(cls)

    def tearDownStop(cls):
        print("%s   执行完毕" % cls.basename)
        # cls.browser.close()

    # 调用浏览器对象
    def url_op(self):
        bc = browser_confirm.__new__(browser_confirm)

        # 创建浏览器对象
        self.browser = bc.url_opens()

        bc.case_browesr('---','****')

        bc.system_parameter_discount()

        # 创建参数对象
        # self.parame = parameter_content()

    """
    因为同一个输入框，输入不同内容都会出现相同的提示所以写在一起了
    利用js 的原理：通过id 找到元素然后输入内容
    """

    def format_goods_discount(self, function, parameter ,massegn=None):

        # 通过id找到元素并进行输入:商品打折数
        self.browser.execute_script("document.getElementById('goods_discount').value=\'" + parameter + "\';")

        if massegn==None:
            # 输入错误出现的提示
            massegn = '请输入正确格式例如 0.1/0.5'

        self.verification(massegn, function)

    """
    输入之后，点击其他元素，焦点移除之后会验证输入的内容是否符合。
    如果不符合就进行提示。
    点击提示框中的确认按钮表示已经查看了提示框，顺路读取提示框中的提示文字
    然后判断提示文字是否为程序设置的。
    """

    def verification(self, massegn, function):
        sleep(1)

        # 找到提交按钮，点击提交按钮。
        submit = self.browser.find_element_by_css_selector('.btn.btn-primary.settingSave')
        self.browser.execute_script("arguments[0].click();", submit)

        sleep(1)

        # 获取提示框的提示内容
        visible = self.browser.find_element_by_css_selector('.sweet-alert.showSweetAlert.visible >p').text

        sleep(1)
        # 点击提示框中的确定按钮，表示已经查看
        confirm = self.browser.find_element_by_css_selector('.confirm')
        self.browser.execute_script("arguments[0].click();", confirm)

        # 判断规划的提示跟实际的提示是否一致
        # massegn为规划的提示，visible为实际的提示
        assert massegn == visible, function + '折扣数输入过大,提示你出现错误'
