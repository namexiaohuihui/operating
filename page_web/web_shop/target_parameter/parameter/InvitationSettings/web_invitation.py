# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: web_invitation.py
@time: 2017/12/2 15:05
@项目名称:operating
"""
import unittest
import os
import json
from page_web.web_shop.target_parameter.parameter.UnifiedVerification import unified_verification

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
    def object_decoder(self,obj):
        if '__type__' in obj and obj['__type__'] == 'ParameterContent':
            return ParameterContent(obj["parameter"], obj["content"])
        return obj

class invitation_input(unittest.TestCase,unified_verification):
    @classmethod
    def setUpClass(cls):
        basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.setUpStart(cls, basename=basename)

    @classmethod
    def tearDownClass(cls):
        cls.tearDownStop(cls)

    def test_invitation_one(self,parameter = None):
        # 正常提交的方法
        parameter=["1","2","3","4"] # 需要输入的Neri

        # 将输入框和需要输入的内容转成一个对象
        controlhour = ParameterContent(self.hourTime, parameter[0])
        controltime = ParameterContent(self.timeTime, parameter[1])
        controlreal_pay = ParameterContent(self.real_payTime, parameter[2])
        controlmoney = ParameterContent(self.moneyTime, parameter[3])

        # 将对象传入列表中
        combination = [controlhour,controltime,controlreal_pay,controlmoney]
        self.transmitList(self.browser,combination) # 让另一个函数进行使用

        # 点击提交按钮
        self.arguments_confirm_prompt(self.saveTime)

        # 提交参数之后，进行再次确认提示，并完成其后的全部工作
        self.integration_confirm_prompt()

    def test_invitation_two(self,parameter = None):
        #　取消提交
        # 定义好kye和value
        parameter = ["1", "2", "3", "4"]
        combination = [self.hourTime, self.timeTime, self.real_payTime,self.moneyTime]

        # 将key和value添加进字典中
        dic = {}
        for num in range(len(parameter)):
            dic[parameter[num]] = combination[num]

        self.transmitDictionaries(self.browser, dic) # 让另一个函数进行使用

        # 点击提交按钮
        self.arguments_confirm_prompt(prompt=self.settingSave)

        # 点击取消按钮
        self.arguments_confirm_prompt(prompt=self.btn_default)

    def test_invitation_there(self,parameter = None):
        # 定义好kye和value
        parameter = ["你好", "2", "3", "4"]
        combination = [self.hourTime, self.timeTime, self.real_payTime,self.moneyTime]

        # 将key和value添加进字典中
        dic = {}
        for num in range(len(parameter)):
            dic[parameter[num]] = combination[num]

        self.transmitDictionaries(self.browser, dic) # 让另一个函数进行使用

        # 点击提交按钮
        self.arguments_confirm_prompt(prompt=self.settingSave)

        self.visible_massegn(massegn="请输入小时,仅支持输入正整数")

    def test_invitation_four(self,parameter = None):
        # 定义好kye和value
        parameter = ["1", "qwe", "3", "4"]
        combination = [self.hourTime, self.timeTime, self.real_payTime,self.moneyTime]

        # 将key和value添加进字典中
        dic = {}
        for num in range(len(parameter)):
            dic[parameter[num]] = combination[num]

        self.transmitDictionaries(self.browser, dic) # 让另一个函数进行使用

        # 点击提交按钮
        self.arguments_confirm_prompt(prompt=self.settingSave)

        self.visible_massegn(massegn="请输入天数,仅支持输入正整数")

    def test_invitation_five(self,parameter = None):
        # 定义好kye和value
        parameter = ["1", "1", "qwe", "4"]
        combination = [self.hourTime, self.timeTime, self.real_payTime,self.moneyTime]

        # 将key和value添加进字典中
        dic = {}
        for num in range(len(parameter)):
            dic[parameter[num]] = combination[num]

        self.transmitDictionaries(self.browser, dic) # 让另一个函数进行使用

        # 点击提交按钮
        self.arguments_confirm_prompt(prompt=self.settingSave)

        self.visible_massegn(massegn="请输入价格,仅支持输入正整数")

    def test_invitation_five(self,parameter = None):
        # 定义好kye和value
        parameter = ["1", "1", "3", "qwe"]
        combination = [self.hourTime, self.timeTime, self.real_payTime,self.moneyTime]

        # 将key和value添加进字典中
        dic = {}
        for num in range(len(parameter)):
            dic[parameter[num]] = combination[num]

        self.transmitDictionaries(self.browser, dic) # 让另一个函数进行使用

        # 点击提交按钮
        self.arguments_confirm_prompt(prompt=self.settingSave)

        self.visible_massegn(massegn="请输入收益价格,仅支持输入正整数")

