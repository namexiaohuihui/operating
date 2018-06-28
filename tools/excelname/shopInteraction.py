# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: shopInteraction.py
@time: 2018/5/29 11:01
"""

from tools.excelname.excelBeanName import ExcelTitle


class InteractionController(ExcelTitle):
    '''
    yaml文档中的key值统一定义，方便日后修改和使用
    缺点：
        写入时有点麻烦
    备注:
    文档中有些备注写的不是很明确，是因为涉及版面数据。
    也有些是忘记写备注...
    '''
    def program_operation(self):
        return '操作'

    # ----------------------------excle文档中标题的定义----------
    def excle_city(self) -> str:
        return '城市'

    def excle_conditions(self) -> str:
        return '条件'

    def excle_screening(self) -> str:
        return '筛选'

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

    # ---------------------------文档所属的位置----------------------------
    def yaml_files(self):
        '''
        该key记录sql和默认参数文件的所属位置
        :return:
        '''
        return 'files'

    # ------------------------------city中使用的key定义----------------------
    def yaml_citytab(self):
        '''
        城市tab最外圈的key
        :return:
        '''
        return 'citytab'

    # ----------------------time中所有子控件使用的key定义----------------------

    def yaml_timeselect(self):
        '''
        时间下拉最外圈的key
        :return:
        '''
        return 'timeselect'

    def yaml_judge(self):
        '''
        时间下拉的
        :return:
        '''
        return 'judge'

    def yaml_choose(self):
        '''
        日期输入的
        :return:
        '''
        return 'choose'

    def yaml_opensleft(self):
        '''
        日期输入框的前缀
        :return:
        '''
        return 'opensleft'

    def yaml_ranges(self):
        '''
        日期输入框中默认携带时间
        :return:
        '''
        return 'ranges'

    def yaml_firstprev(self):
        '''
        开始时间箭头
        :return:
        '''
        return 'firstprev'

    def yaml_firsttitle(self):
        '''
        开始时间的标题
        :return:
        '''
        return 'firsttitle'

    def yaml_firstdate(self):
        '''
        开始时间的内容
        :return:
        '''
        return 'firstdate'

    def yaml_firsthourselect(self):
        '''
        开始时间中‘时’刻度的下拉框
        :return:
        '''
        return 'firsthourselect'

    def yaml_firstminuteselect(self):
        '''
        开始时间中'分'刻度的下拉框
        :return:
        '''
        return 'firstminuteselect'

    def yaml_secondprev(self):
        '''
        结束时间箭头
        :return:
        '''
        return 'secondprev'

    def yaml_secondtitle(self):
        '''
        结束时间标题
        :return:
        '''
        return 'secondtitle'

    def yaml_seconddate(self):
        '''
        结束时间的内容
        :return:
        '''
        return 'seconddate'

    def yaml_secondhourselect(self):
        '''
        结束时间‘时’刻度
        :return:
        '''
        return 'secondhourselect'

    def yaml_secondminuteselect(self):
        '''
        结束时间'分'刻度
        :return:
        '''
        return 'secondminuteselect'

    # -----------------------label中key的定义-------------------
    def yaml_label(self):
        '''
        lable最外圈的key
        :return:
        '''
        return 'label'

    # -----------------------area中key的定义--------------------
    def yaml_area(self):
        '''
        area最外圈的key
        :return:
        '''
        return 'area'

    def yaml_option(self):
        '''
        首选项的获取
        :return:
        '''
        return 'option'

    def yaml_manager(self):
        '''
        manager的key定义
        :return:
        '''
        return 'manager'

    def yaml_director(self):
        '''
        director的key定义
        :return:
        '''
        return 'director'

    def yaml_region(self):
        '''
        region的key定义
        :return:
        '''
        return 'region'

    # ------------------------------status中key 的定义---------------
    def yaml_status(self):
        '''
        status中最外圈的key
        :return:
        '''
        return 'status'

    def yaml_source(self):
        '''
        source的key定义
        :return:
        '''
        return 'source'

    def yaml_pay(self):
        '''
        pay的key定义
        :return:
        '''
        return 'pay'

    # ----------------------------------order中key的定义--------------
    def yaml_order(self):
        '''
        order最外圈的key定义
        :return:
        '''
        return 'order'

    # ----------------------------------buyer中key的定义---------------
    def yaml_buyer(self):
        '''
        buyer最外圈的key定义
        :return:
        '''
        return 'buyer'

    # ----------------------------------other中key的定义---------------
    def yaml_other(self):
        '''
        other最外圈的key定义
        :return:
        '''
        return 'other'

    # ----------------------------------button中key的定义-------------------
    def yaml_button(self):
        '''
        button最外圈的key定义
        :return:
        '''
        return 'button'

    def yaml_search(self):
        '''
        搜索按钮
        :return:
        '''
        return 'search'

    def yaml_export(self):
        '''
        导出按钮
        :return:
        '''
        return 'export'

    # ----------------------------------content中key的定义-------------------
    def yaml_content(self):
        '''
        content最外圈的key定义
        :return:
        '''
        return 'content'

    def yaml_table(self):
        '''
        thead 和 tbody都会使用到的地方，统一定义
        :return:
        '''
        return 'table'

    def yaml_thead(self):
        '''
        界面key信息
        :return:
        '''
        return 'thead'

    def yaml_tbody(self):
        '''
        界面value信息
        :return:
        '''
        return 'tbody'

    # ----------------------------------record中key的定义-------------------
    def yaml_record(self):
        '''
        record最外圈的key定义
        :return:
        '''
        return 'record'

    # ----------------------------------buttonpage中key的定义-------------------
    def yaml_buttonpage(self):
        '''
        buttonpage最外圈的key定义
        :return:
        '''
        return 'buttonpage'

    def yaml_paginate(self):
        '''
        上一页按钮
        :return:
        '''
        return 'paginate'

    def yaml_previous(self):
        '''
        当前数据所展示的按钮
        :return:
        '''
        return 'previous'

    def yaml_next(self):
        '''
        下一页按钮
        :return:
        '''
        return 'next'
