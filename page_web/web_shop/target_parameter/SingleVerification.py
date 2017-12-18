# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: SingleVerification.py
@time: 2017/10/24 21:58
@项目名称:operating
城市内容设置的case：
1.所开通的城市判断
2.单个城市数据输入
"""
import logging
from time import sleep

from page_web.web_shop.target_parameter.VerificationRepeat import verification_repeat


class discount_input(verification_repeat):
    """
    setUpStart :　开始执行的函数
    basename : 输入框函数名
    ordinal ： 输入框的内容
    思路:
        1.赋值输入框函数名
        2.执行case的类名，赋值给父类
    """

    def setUpStart(cls, basename, ordinal):
        # 1.赋值输入框函数名
        cls.ordinal = ordinal

        # 2.执行case的类名，赋值给父类
        cls.InitializationExecution(cls, basename=basename)

        # 3.执行需要跑case的路径
        cls.system_parameter_discount()

    """
    js_input : 集成输入框和移动鼠标的函数
    思路:
        1.输入内容
        2.转移光标的焦点
    """

    def js_input(self):
        # 　1.输入内容 id：　为需要执行输入的id，parameter输入的参数
        self.id_input(browser=self.browser, id=self.ordinal, parameter=self.implement_parameter)

        # 2.转移光标的焦点
        self.blur_id(browser=self.browser, ordinal=self.ordinal)

    # 输入内容符合条件时，进行的二次确认判断
    def modal_body(self):
        # 再次确认框中的红色标明的重点文字
        # 设置提示框中需要进行对比的参数，并进行比较
        pop_text = self.showSweetAlert_visible(self.modal_body_h4)
        self.implement_massegn = self.system_preservation
        self.visible_massegn_assert(visible=pop_text, massegn=self.implement_massegn)

        # 再次确认框中的普通显示的文字
        # 设置提示框中需要进行对比的参数，并进行比较
        center = self.showSweetAlert_visible(self.modal_body_p)
        self.implement_massegn = self.system_content
        self.visible_massegn_assert(visible=center, massegn=self.implement_massegn)

    # 集成点击和内容的判断
    # 默认是点击取消
    def integration_confirm_prompt(self, Situation=False):

        # 点击提交按钮
        self.arguments_confirm_prompt(self.settingSave)

        # 再次确认提示框中内容的判断
        self.modal_body()

        if Situation:
            # 再次确认提示框中：同意按钮点击。点击之后进行操作提示。判断提示内容是否正确
            self.arguments_confirm_prompt(prompt=self.discountsave)

            # 上一步提示内容的点击
            self.arguments_confirm_prompt(prompt=self.confirm)
        else:
            # 点击取消按钮
            self.arguments_confirm_prompt(prompt=self.btn_default)

    def prompt_box(self):
        # 打印log
        self.parameter_log_output()

        # 元素输入
        self.js_input()

        # 对比信息
        self.visible_massegn(self.implement_massegn)

    """
    PreferentialVerification : 获取内容并执行cese
    list_parameter ： 列表中有cese名、提示内容、输入内容
    思路：
        1.将列表的数据提取
        2.执行case
    """

    def PreferentialVerification(self, list_parameter):
        # 1.将列表的数据提取
        # 定义调用的函数名
        self.implement_function = list_parameter[0]

        # 输入错误出现的提示
        self.implement_massegn = list_parameter[1]

        # 需要输入的参数
        self.implement_parameter = list_parameter[2]

        # 2.执行case
        self.prompt_box()

    # 点击提交，然后让其弹出二次确认的提示框并判断提示框的内容是否一致
    # 提示内容为你是否要进行提交操作
    def correct_function(self, list_parameter):
        # 定义调用的函数名
        self.implement_function = list_parameter[0]

        # 输入错误出现的提示
        self.implement_massegn = list_parameter[1]

        # 需要输入的参数
        self.implement_parameter = list_parameter[2]

        # 打印log
        self.parameter_log_output()

        self.js_input()

    # 进入的执行路径
    def system_parameter_discount(self):
        self.browser.find_elements_by_css_selector('.dropdown-toggle')[1].click()
        sleep(1)
        self.browser.find_elements_by_css_selector('.system-tooltip')[0].click()
        sleep(1)
        self.browser.find_elements_by_css_selector('.nav.nav-tabs>li')[4].click()

    # 打印log的地方
    def parameter_log_output(self):
        logger = logging.getLogger("123")
        logger.error("执行者:  %s   假定： %s   输入：%s "
                     % (self.implement_function, self.implement_massegn, self.implement_parameter))
