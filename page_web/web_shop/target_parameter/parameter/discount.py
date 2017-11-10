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
import logging
from time import sleep

from page_web.web_shop.target_parameter.parameter.name_bean import letter_parameter_names
from practical.constant.browser.browser_establish import browser_confirm
from practical.operation.selenium_click import element_click
from practical.operation.selenium_input import element_input
from practical.CuttingOperation import stringCutting


class discount_input(letter_parameter_names, element_input, element_click):
    def setUpStart(cls, basename, ordinal):
        # 执行程序类的名字
        cls.basename = basename

        # 执行任务时的输入框名字
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

        self.user_pass(self, bc)

    # 账号密码输入框
    def user_pass(self, bc):
        # 创建参数对象
        # self.parame = parameter_content()

        bc.case_browesr('---', '***')

        bc.system_parameter_discount()

    # js执行内容输入
    def js_input(self):
        # 通过id找到元素并进行输入:商品打折数
        # 　self.id_js_input(browser=self.browser,ordinal = self.ordinal,parameter = self.implement_parameter)
        # 　id：　为需要执行输入的id，parameter输入的参数
        self.id_input(browser=self.browser, id=self.ordinal, parameter=self.implement_parameter)

    # 传入对象来获取提示框中的内容
    def showSweetAlert_visible(self, process):
        if self.is_visible_css_selectop(self.browser, process):
            # 获取提示框的提示内容
            visible = self.browser.find_element_by_css_selector(process).text

        return visible

    # 输入内容符合条件时，进行的二次确认判断
    def modal_body(self):
        # 二次确认框中的红色标明的重点文字
        # 设置提示框中需要进行对比的参数，并进行比较
        pop_text = self.showSweetAlert_visible(self.modal_body_h4)
        self.implement_massegn = self.system_preservation
        self.visible_massegn_assert(visible=pop_text)

        # 二次确认框中的普通显示的文字
        # 设置提示框中需要进行对比的参数，并进行比较
        center = self.showSweetAlert_visible(self.modal_body_p)
        self.implement_massegn = self.system_content
        self.visible_massegn_assert(visible=center)

    # 判断规划的提示跟实际的提示是否一致
    # massegn为规划的提示，visible为实际的提示
    # function 为调用这个不见函数的方法
    def visible_massegn_assert(self, visible):
        assert self.implement_massegn == visible, self.implement_function + '：该函数进行assert比较的时候出现了问题'

    # 二次确认之后的提示内容判断
    def confirm_showSweetAlert_visible(self, function):
        sleep(1)
        visible = self.showSweetAlert_visible(process=self.visible_h4)

        # 判断规划的提示跟实际的提示是否一致
        # massegn为规划的提示，visible为实际的提示
        # function 为调用这个不见函数的方法
        self.implement_massegn = self.system_successful

        self.visible_massegn_assert(visible=visible)

    # 通过js的查找元素进行点击
    def arguments_confirm_prompt(self, prompt):
        # 需要浏览器对象以及执行点击的对象
        # self.css_confirm_prompt(browser=self.browser, prompt=prompt)
        self.css_click(browser=self.browser, prompt=prompt)

    # 集成点击和内容的判断
    def integration_confirm_prompt(self):
        # 再次确认提示框中内容的判断
        self.modal_body()

        # 再次确认提示框中：同意按钮点击。点击之后进行操作提示。判断提示内容是否正确
        self.arguments_confirm_prompt(prompt=self.discountsave)

        # 上一步提示内容的点击
        self.arguments_confirm_prompt(prompt=self.confirm)

    # 集成点击和输入的函数
    def integration_input_click(self):
        # 输入框输入
        self.js_input()

        # 该页面保存提交按钮的点击
        self.arguments_confirm_prompt(prompt=self.settingSave)

    """
       输入之后，点击其他元素，焦点移除之后会验证输入的内容是否符合。
       如果不符合就进行提示。
       点击提示框中的确认按钮表示已经查看了提示框，顺路读取提示框中的提示文字
       然后判断提示文字是否为程序设置的。
       """

    def prompt_box(self):
        # 点击集成了输入和点击的函数
        self.integration_input_click()

        # 获取提示框的提示内容
        visible = self.showSweetAlert_visible(process=self.visible_p)

        # 点击提示框中的确定按钮，表示已经查看
        self.arguments_confirm_prompt(prompt=self.confirm)

        # 判断规划的提示跟实际的提示是否一致
        # massegn为规划的提示，visible为实际的提示
        # function 为调用这个不见函数的方法
        self.visible_massegn_assert(visible=visible)

    # 商品折扣的验证
    def gd_verification(self, list_parameter):
        # 定义调用的函数名
        self.implement_function = list_parameter[0]

        # 输入错误出现的提示
        self.implement_massegn = list_parameter[1]

        # 需要输入的参数
        self.implement_parameter = list_parameter[2]

        # 打印log
        self.print_log_output()

        # 开始执行
        self.prompt_box()

    # 商品参与对象的验证
    # 分两步进行验证：
    # 第一步：先验证输入的内容为不符合条件时，提示框是否显示正确
    # 第二步：在验证整体提示框是否提示正确
    # function函数名，parameter需要输入的参数，打印的信息
    def gp_verification(self, list_parameter):
        # 定义调用的函数名
        self.implement_function = list_parameter[0]

        # 输入错误出现的提示
        self.implement_massegn = list_parameter[1]

        # 需要输入的参数
        self.implement_parameter = list_parameter[2]

        # 点击集成了输入和点击的函数
        self.integration_input_click()

        # 获取提示框的提示内容
        visible = self.showSweetAlert_visible(process=self.visible_p)

        # 判断规划的提示跟实际的提示是否一致
        # massegn为规划的提示，visible为实际的提示
        # function 为调用这个不见函数的方法
        self.visible_massegn_assert(visible=visible)

        # 打印log
        self.print_log_output()

        # 点击提示框中的确定按钮，表示已经查看
        # self.arguments_confirm_prompt(prompt=self.confirm)

    # 点击提交，然后让其弹出二次确认的提示框并判断提示框的内容是否一致
    def correct_function(self, list_parameter):
        # 定义调用的函数名
        self.implement_function = list_parameter[0]

        # 输入错误出现的提示
        self.implement_massegn = list_parameter[1]

        # 需要输入的参数
        self.implement_parameter = list_parameter[2]

        # 打印log
        self.print_log_output()

        self.integration_input_click()

    # 打印log的地方
    def print_log_output(self):
        # 定义执行者的名字
        logger = logging.getLogger(self.implement_function)

        # 定义等级
        logger.setLevel(logging.ERROR)

        # 输出到屏幕
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 设置日志输出格式
        fomatter = logging.Formatter('%(asctime)s -%(name)s-:%(message)s')
        ch.setFormatter(fomatter)

        # 将输出到屏幕的内容添加到log
        logger.addHandler(ch)

        # 执行输出操作
        logger.error("提示框： %s   输入：: %s " % (self.implement_massegn, self.implement_parameter))
