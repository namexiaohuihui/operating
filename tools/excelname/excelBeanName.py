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


class ExcelTitle(object):
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

    def wholeQueryStatement(self):
        return "sql"

    def whole_city(self):
        return '城市'

    def whole_code(self):
        return '编码'

    def whole_configs(self):
        return '配置'

    def whole_including(self):
        return '全部'

    def whole_default(self):
        return '默认'

    # ----------------------------共用的定义--------------------
    def yaml_dec(self):
        return 'dec'

    def yaml_name(self):
        return 'name'

    def yaml_type(self):
        return 'type'

    def yaml_value(self):
        return 'value'

    def yaml_placeholder(self):
        return 'placeholder'

    def yaml_orderkey(self):
        return 'orderkey'

    def yaml_attribute(self):
        return 'attribute'

    def yaml_obj(self):
        return 'obj'

    def yaml_city_tab(self):
        return 'citytab'

    def yaml_label(self):
        return 'label'

    def yaml_active(self):
        return 'active'

    def yaml_formGroup(self):
        return 'formGroup'

    def yaml_status(self):
        return 'status'

    def yaml_category(self):
        return 'category'

    def yaml_preferences(self):
        return 'preferences'

    def yaml_conditions(self):
        return 'conditions'

    def yaml_search(self):
        return 'search'

    def yaml_export(self):
        return 'export'

    def yaml_info(self):
        return 'info'

    #  -------------------------------------元素标签属性--------------------
    def ele_class(self):
        return 'class'

    def ele_href(self):
        return 'href'

    def ele_active(self):
        return 'active'


# even 的地盘
class even_auxiliary(ExcelTitle):
    def even_account(self):
        return "账号"

    def even_password(self):
        return "密码"


class even_exclusiveService(ExcelTitle):
    def password_past(self):
        return "旧密码"

    def password_establish(self):
        return "新密码"

    def password_confirm(self):
        return "确认密码"


if __name__ == '__main__':
    from tools.excelname import ShopNoticeController as sn

    print(sn.dailyDeadline)
    print(sn.dailyCity(sn))
