# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: UnifiedVerification.py
@time: 2017/12/2 15:14
@项目名称:operating
"""

from PageWeb.WebShop.TargetParameter.VerificationRepeat import verification_repeat


class ParameterContent:
    def __init__(self, parameter, content, *args, **kwargs):
        self.parameter = parameter
        self.content = content

    # to_json和from_json将传入的数据序列化处理之后，已对象的形式返回
    def to_json(self):
        # 序列化对象
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        # 反序列化对象
        json_dict = json.loads(json_str)
        return cls(**json_dict)

    # 创建对象。。并返回
    def object_decoder(self, obj):
        if '__type__' in obj and obj['__type__'] == 'ParameterContent':
            return ParameterContent(obj["parameter"], obj["content"])
        return obj


class unified_verification(verification_repeat):
    def setUpStart(self, basename):
        # 1.定义执行程序类的名字
        self.basename = basename

        # 2.执行case的类名，赋值给父类
        self.InitializationExecution(self, basename=basename)

        # 3.执行需要跑case的路径
        self.system_parameter_discount(self)

    def tearDownStop(self):
        print("%s   执行完毕" % self.basename)

    def list_submission(self, parameter, confirm, situation):
        """
       输入内容后点击提交，并且二次提醒的时候也提交。。 执行：输入、提交、验证的功能
        1.将list的数据转成对象
        2.将这些对象放入list
        3.将数据内容输入到输入框中
        4.提交按钮的点击
        5.提示框内容的验证
        :param parameter:  需要输入的数据参数
        :param confirm:  点击的按钮
        :param situation:  验证提示框中的点击
        :return:
        """
        # 将输入框和需要输入的内容转成一个对象
        controlhour = ParameterContent(self.hourTime, parameter[0])
        controltime = ParameterContent(self.timeTime, parameter[1])
        controlreal_pay = ParameterContent(self.real_payTime, parameter[2])
        controlmoney = ParameterContent(self.moneyTime, parameter[3])

        # 将对象传入列表中
        combination = [controlhour, controltime, controlreal_pay, controlmoney]
        self.transmitList(self.browser, combination)  # 让另一个函数进行使用

        # 点击提交按钮
        self.arguments_confirm_prompt(confirm)

        # 提交参数之后，进行再次确认提示，并完成其后的全部工作
        self.integration_confirm_prompt(Situation=situation)

    def dic_cancel(self, parameter):
        """
        输入内容后点击提交，在二次提示的时候取消提交。。执行：输入、取消提交
        :param parameter: 需要输入的数据参数
        :return:
        """
        combination = [self.hourTime, self.timeTime, self.real_payTime, self.moneyTime]
        # 将key和value添加进字典中
        dic = {}
        for num in range(len(parameter)):
            dic[parameter[num]] = combination[num]
        self.transmitDictionaries(self.browser, dic)  # 让另一个函数进行使用
        self.integration_confirm_prompt()

    def dic_verification(self, parameter, massegn):
        """
        输入不符合规矩的内容，点击提交出现提示信息..执行:输入/提交/验证
        :param parameter:  需要输入的内容
        :param massegn:  需要提示的信息
        :return:
        """
        combination = [self.hourTime, self.timeTime, self.real_payTime, self.moneyTime]
        # 将key和value添加进字典中
        dic = {}
        for num in range(len(parameter)):
            dic[parameter[num]] = combination[num]
        self.transmitDictionaries(self.browser, dic)  # 让另一个函数进行使用
        # 点击提交按钮
        self.arguments_confirm_prompt(prompt=self.settingSave)
        # 提交信息的比较
        self.visible_massegn(massegn=massegn)

    def arguments_confirm_prompt(self, prompt):
        """
       arguments_confirm_prompt : 元素点击函数
       prompt :需要点击元素的函数名（css_selector）
       思路：
            1.判断屏幕的大小，屏幕小的时候进行页面滚动操作
            2.执行点击动作
        """
        if self.browser.get_window_size()["height"] <= 800:
            # 1.判断屏幕的大小，屏幕小的时候进行页面滚动操作
            self.scrollBar_buttom(browser=self.browser)
        # 2.执行点击动作
        self.css_click(browser=self.browser, prompt=prompt)

    def integration_confirm_prompt(self, Situation=False):
        '''
         # 集成点击和内容的判断
         # 默认是点击取消
        :param Situation: 确认提示框中的确定按钮/提交按钮
        :return:
        '''

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

    def system_parameter_discount(self):
        # 进入的执行路径
        self.css_click(self,browser=self.browser, prompt='.sidebar-menu>li:nth-child(14)')
        self.css_click(self,browser=self.browser, prompt='.treeview-menu.menu-open>li:nth-child(2)')
        self.css_click(self,browser=self.browser, prompt='.nav.nav-tabs>li:nth-child(3)')
