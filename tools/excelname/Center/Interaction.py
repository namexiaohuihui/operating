# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: shopInteraction.py
@time: 2018/5/29 11:01
"""

from tools.excelname.excelBeanName import ExcelTitle


class InteractionController(ExcelTitle):
    """
    Definition of yaml on order page...
    yaml文档中的key值统一定义，方便日后修改和使用
    缺点：
        写入时有点麻烦
    备注:
    文档中有些备注写的不是很明确，是因为涉及版面数据。
    也有些是忘记写备注...
    """

    def yaml_tabs(self):
        return 'tabs'

    def yaml_timetype(self):
        return 'timetype'

    def yaml_timeinput(self):
        return 'timeinput'

    def yaml_usersort(self):
        return 'usersort'

    def yaml_manager(self):
        return 'manager'

    def yaml_director(self):
        return 'director'

    def yaml_area(self):
        return 'area'

    def yaml_city(self):
        return 'city'

    def yaml_choole(self):
        return 'choole'

    def yaml_orderinput(self):
        return 'orderinput'

    def yaml_buyerkey(self):
        return 'buyerkey'

    def yaml_buyerinput(self):
        return 'buyerinput'

    def yaml_otherkey(self):
        return 'otherkey'

    def yaml_otherinput(self):
        return 'otherinput'

    def yaml_formSub(self):
        return 'formSub'

    def yaml_generate(self):
        return 'generate'

    def yaml_single(self):
        return 'single'

    def yaml_phone(self):
        return 'phone'

    def yaml_span(self):
        return 'span'

    def yaml_phoneFormBut(self):
        return 'phoneFormBut'

    def yaml_modalBut(self):
        return 'modalBut'

    def yaml_headersort(self):
        return 'headersort'

    def yaml_exportsort(self):
        return 'exportsort'
