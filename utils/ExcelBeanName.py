# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: ExcleBeanName.py
@time: 2018/1/25 21:44
@Entry Name:operating
"""
"""
该文件用于存放excle文档的标题
"""


class excel_title(object):
    """
    存放统一格式的标题
    """

    def whole_serial_number(self):
        return "序号"

    def whole_position(self):
        return "位置"

    def whole_file_name(self):
        return "文件名"

    def whole_class_name(self):
        return "类名"

    def whole_function_name(self):
        return "函数"

    def whole_scene(self):
        return "场景"

    def whole_step(self):
        return "步骤"

    def whole_input(self):
        return "输入"

    def whole_output(self):
        return "输出"

    def whole_result(self):
        return "结果"

    def whole_verification(self):
        return "验证条件"

    def whole_remarks(self):
        return "备注"

    def whole_query_statement(self):
        return "sql"


# even 的地盘
class even_auxiliary(excel_title):
    def even_account(self):
        return "账号"

    def even_password(self):
        return "密码"


class even_exclusiveService(excel_title):
    def password_past(self):
        return "旧密码"

    def password_establish(self):
        return "新密码"

    def password_confirm(self):
        return "确认密码"


# shop的地盘
class shop_systemsetup(excel_title):

    def ps_with_extract(self):
        return "提现"

    def ps_with_cost(self):
        return "手续费"

    def ps_count_goods_discount(self):
        return "商品折扣"

    def ps_count_goods_id(self):
        return "不参与商品"

    def ps_count_watiki_discount(self):
        return "水票折扣"

    def ps_count_watikis_id(self):
        return "不参与水票"

    def ps_count_watikis_max(self):
        return "最高抵扣"






