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

from page_web.web_shop.target_parameter.parameter.discount.name_bean import letter_parameter_names
from practical.constant.browser.browser_establish import browser_confirm

from practical.operation.selenium_input import element_input
from practical.operation.selenium_click import element_click

class discount_input(letter_parameter_names,element_input,element_click):

    def setUpStart(cls,basename,ordinal):
        cls.basename = basename
        cls.ordinal = ordinal
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

        # 创建参数对象
        # self.parame = parameter_content()

        bc.case_browesr('----','****')

        bc.system_parameter_discount()



    def js_input(self,parameter):
        # 通过id找到元素并进行输入:商品打折数
        self.id_js_input(browser=self.browser,ordinal = self.ordinal,parameter = parameter)


    # 错误提示框中的内容
    def showSweetAlert_visible(self,process):
        sleep(1)
        # 获取提示框的提示内容
        visible = self.browser.find_element_by_css_selector(process).text
        return visible

    # 输入内容符合条件时，进行的二次确认判断
    def modal_body(self,function):
        sleep(1)
        # 二次确认框中的红色标明的重点文字
        pop_text = self.browser.find_element_by_css_selector(self.modal_body_h4).text
        # 二次确认框中的普通显示的文字
        center = self.browser.find_element_by_css_selector(self.modal_body_p).text

        self.visible_massegn_assert(function=function, massegn='你确定要保存吗？', visible=pop_text)
        self.visible_massegn_assert(function=function, visible=center, massegn='保存后新产生的订单立即生效已产生的订单不受影响')

    # 判断规划的提示跟实际的提示是否一致
    # massegn为规划的提示，visible为实际的提示
    # function 为调用这个不见函数的方法
    def visible_massegn_assert(self,massegn,visible,function):
        assert massegn == visible, function + '：该函数进行assert比较的时候出现了问题'

    # 二次确认之后的提示内容判断
    def confirm_showSweetAlert_visible(self,function):

        sleep(1)
        # 点击提示框中的确定按钮，表示已经查看
        #self.arguments_confirm_prompt( prompt = self.confirm)

        visible = self.showSweetAlert_visible(process=self.visible_h4)

        # 判断规划的提示跟实际的提示是否一致
        # massegn为规划的提示，visible为实际的提示
        # function 为调用这个不见函数的方法
        self.visible_massegn_assert(function=function, massegn='操作成功', visible=visible)

    # 通过js的查找元素进行点击
    def arguments_confirm_prompt(self,prompt):
        sleep(1)
        self.css_confirm_prompt(browser =self.browser, prompt=prompt)



    # 二次确认提示框中点击确认
    def btn_primary_click(self,prompt):
        sleep(1)
        #self.id_confirm_prompt(browser=self.browser, prompt=prompt)
        self.browser.execute_script("document.getElementById(\'" + prompt + "\').click();")


    # 集成点击和内容的判断
    def integration_confirm_prompt(self,function):

        # 二次确认之后的内容判断

        self.modal_body(function=function)

        # 二次确认的：同意按钮点击
        self.btn_primary_click(prompt =self.discountsave)


    # 集成点击和输入的函数
    def integration_input_click(self,parameter):

        # 输入框输入
        self.js_input(parameter = parameter)

        # 该页面保存提交按钮的点击
        self.arguments_confirm_prompt(prompt =self.settingSave)

    """
       输入之后，点击其他元素，焦点移除之后会验证输入的内容是否符合。
       如果不符合就进行提示。
       点击提示框中的确认按钮表示已经查看了提示框，顺路读取提示框中的提示文字
       然后判断提示文字是否为程序设置的。
       """

    def verification(self, function, parameter, massegn=None):

        # 提示框内容的显示
        if massegn == None:
            # 输入错误出现的提示
            massegn = '请输入正确格式例如 0.1/0.5'

        # 点击集成了输入和点击的函数
        self.integration_input_click(parameter = parameter)

        # 获取提示框的提示内容
        visible = self.showSweetAlert_visible(process = self.visible_p)

        # 点击提示框中的确定按钮，表示已经查看
        self.arguments_confirm_prompt(prompt = self.confirm)

        # 判断规划的提示跟实际的提示是否一致
        # massegn为规划的提示，visible为实际的提示
        # function 为调用这个不见函数的方法
        self.visible_massegn_assert(function=function, massegn=massegn, visible=visible)


    # 点击提交，然后让其弹出二次确认的提示框并判断提示框的内容是否一致
    def correct_function(self,parameter,function):
        self.integration_input_click(parameter)