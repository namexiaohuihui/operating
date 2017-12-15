# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: VerificationRepeat.py
@time: 2017/12/2 15:25
@项目名称:operating
"""

from page_web.web_shop.target_parameter.parameter.name_bean import letter_parameter_names
from practical.constant.browser.browser_establish import browser_confirm
from practical.operation.selenium_click import element_click
from practical.operation.selenium_input import element_input
from practical.Exception_error.DefinitionError import definition_error


class verification_repeat(letter_parameter_names, element_input, element_click):

    def InitializationExecution(cls, basename):
        # 执行程序类的名字
        cls.basename = basename
        print("%s   开始执行" % cls.basename)

        cls.url_op(cls)

    def ResultFeedback(cls):
        print("%s   执行完毕" % cls.basename)
        # cls.browser.close()


    """
    url_op : 调用浏览器对象
    思路:
        1.创建浏览器所在函数的对象
        2.调用已经规划好的浏览器函数
    """
    def url_op(self):
        # 1.创建浏览器所在函数的对象
        bc = browser_confirm.__new__(browser_confirm)

        # 2.调用已经规划好的浏览器函数
        self.browser = bc.url_opens()

        self.user_pass(self, bc)

    """
    user_pass :调用登陆密码集成函数
    bc ：浏览器对象
    思路：
        1.获取储存账号密码的对象
        2.调用集成的函数
        3.执行需要跑case的路径
    """
    def user_pass(self, bc):
        # 1.获取储存账号密码的对象（目前暂时没使用）
        # self.parame = parameter_content()

        # 2.调用集成的函数
        bc.case_browesr('11', '222')

        # 执行需要跑case的路径
        bc.system_parameter_discount()

    """
   arguments_confirm_prompt : 元素点击函数
   prompt :需要点击元素的函数名（css_selector）
   思路：
        1.判断屏幕的大小，屏幕小的时候进行页面滚动操作
        2.执行点击动作
    """
    def arguments_confirm_prompt(self, prompt):
        if self.browser.get_window_size()["height"] <=800:
            # 1.判断屏幕的大小，屏幕小的时候进行页面滚动操作
            self.scrollBar_buttom(browser = self.browser)
        # 2.执行点击动作
        self.css_click(browser=self.browser, prompt=prompt)

    """
    showSweetAlert_visible : 获取指定元素对象的text
    process ： 需要获取元素的函数名（css_selector）
    思路：
        1.先判断需要获取的元素是否存在（其实可以省略这步，因为必须要出现的。不出现就是错误）
        2.返回获取的内容(如果提示框没有出来就返回一个空值)
    """
    def showSweetAlert_visible(self, process):
        if self.is_visible_css_selectop(self.browser, process):
            # 1.先判断需要获取的元素是否存在
            visible = self.browser.find_element_by_css_selector(process).text
            # 2.返回获取的内容
            return visible;
        else:
            return "提示框没有出来，返回一个空值"

    """
    setting_save_click : 集成点击和调用判断的功能
    massegn ： 需要判断的信息
    思路：
        1.点击提交
        2.传入massegn给另一个函数，判断这个massegn是否为需求指定的
    """
    def setting_save_click(self,massegn):
        # 1.点击提交
        self.arguments_confirm_prompt(prompt=self.settingSave)
        # 2.传入massegn给另一个函数，判断这个massegn是否为需求指定的
        self.visible_massegn(massegn)

    """
    visible_massegn : 继承获取提示框内容和点击的功能
    massegn ： 需要判断的信息
    思路：
        1.获取提示框的提示内容
        2.调用判断的功能
        3.点击提示框中的确定按钮，表示已经查看
    """
    def visible_massegn(self, massegn):
        # 1.获取提示框的提示内容
        visible = self.showSweetAlert_visible(process=self.visible_p)

        # 2.调用判断的功能
        self.visible_massegn_assert(visible=visible, massegn=massegn)

        # 3.点击提示框中的确定按钮，表示已经查看
        self.arguments_confirm_prompt(prompt=self.confirm)

    """
    visible_massegn_assert : 通过断言来判断两个信息是否一致
    visible : 提取页面上的内容
    massegn ：需求规划的提示
    思路：
        1.通过断言直接判断
        2.扑捉异常并打印
    """
    def visible_massegn_assert(self, visible, massegn):
        try:
            # 1.通过断言直接判断
            assert massegn == visible, 'visible_massegn_assert 断言判断出错'
        except AssertionError as e:
            # 2.扑捉异常并打印
            definition_error(repr(e)).erroe_get("verification_repeat", self.browser)





    # 定义log的属性
    # 暂时没人用
    def output_log(self,function):
        # 定义执行者的名字
        self.logger = logging.getLogger(function)

        # 定义等级
        self.logger.setLevel(logging.ERROR)

        # 输出到屏幕
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 设置日志输出格式
        fomatter = logging.Formatter('%(asctime)s -%(name)s-:%(message)s')
        ch.setFormatter(fomatter)

        # 将输出到屏幕的内容添加到log
        self.logger.addHandler(ch)
