# -*- coding: utf-8 -*-
"""
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  -  /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                        `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

               佛祖保佑         永无BUG
@author:    ln_company
@license:   (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@Software:  PyCharm
@file:      operationViewJude.py
@time:      2018/9/27 17:49
@desc:
"""
import os
import operator
from tools.YAMLconfig import readYaml
from tools.screeningdrop import ScreeningDrop
from CenterBackground.customTabs import CustomTabs
from CenterBackground.judeVerification import JudgmentVerification

_parameter = 'parameter'
_type = 'type'
_click = 'click'
_input = 'input'
_timeinput = 'timeinput'
_select = 'select'
_checkbox = 'checkbox'
_print = 'DaLao,What do you type in? %s'


class OperationViewJude(JudgmentVerification):
    def __init__(self, config, basename, center_name):
        """
        定义模块数据信息
        :param module:   元素模块
        :param sheet:   用例标签名
        :param basename:  执行程序的文件名
        """
        JudgmentVerification.__init__(self, config, basename)
        self.bi = center_name()
        pass

    def read_yaml_case(self, file_name, case_key):
        """
        I don't know what I'm writing, but I know it works.
        通过文件来读取相应的key值,最后进行
        :param file_name: excel定义的默认参数
        :param case_key: 用例函数名
        :return:
        """
        case_value = readYaml.read_expression_key(file_name, case_key)
        return case_value

    def release_success(self):
        """
        第二步有个坑：如果设置的city不存在那么就默认页面执行操作
        :return:
        """
        # 1.读取用例设置的参数位置
        ov_para = self.overall[self.bi.whole_parameter()]
        # 1.1 根据文件名和key来解析相应的数据
        ov_para = os.path.join(os.path.dirname(os.path.realpath(__file__)), ov_para)
        case_value = self.read_yaml_case(file_name=ov_para, case_key=self.FUNCTION_NAME)

        # 2.进入指定的城市
        self.ct = CustomTabs(self.driver, self.financial[self.bi.yaml_tabs()])
        self.ct.is_visibles()
        # 2.1读取全部的城市text
        ul_text = [ul.text for ul in self.ct.ul_li]
        # 2.2将元素和城市text通过dict形式存储
        city_text = dict(zip(self.ct.ul_li, ul_text))
        # 2.3找到城市
        case_city = case_value[self.bi.yaml_city()]
        for city_k, city_v in city_text.items():
            if case_city is city_v:
                self.vac.element_click(city_k)

        # 3.根据相应的key值对数据进行操作,1遍历执行元素的动作
        case_con = case_value[self.bi.yaml_condition()]
        para_key = case_con.keys()

        for ov in para_key:
            # 4.根据key值旗下的value值
            ov_pa = case_con[ov]
            pa_key = ov_pa.keys()
            # 5. 找到元素的keys值,该值为可在路径yaml表中找到元素的路径
            for pa in pa_key:
                # ov_key = 依次元素的路径,ov_value = 设置的参数,ov_ty = 以及该元素的类型
                ov_key = self.financial[pa]
                case_pa = ov_pa[pa]
                ov_value = case_pa[_parameter]
                ov_ty = case_pa[_type].lower()

                if ov_ty == _click:
                    # 根据元素进行点击
                    self.vac.css_click(self.driver, ov_key)

                elif ov_ty == _input:
                    # 根据元素进行输出操作
                    if pa == _timeinput:  # 单独处理
                        self.vai.id_js_cursor_save(self.driver, ov_key, ov_value)
                    else:
                        self.vai.css_input(self.driver, ov_key, ov_value)

                elif ov_ty == _select:
                    # 根据元素来设置相应的options值
                    ScreeningDrop(self.driver, ov_key, case_pa['ele']).setSelectorText(ov_value)
                    pass

                elif ov_ty == 'checkbox':
                    # 根据元素来选择相应的单选框
                    checkbox = self.vac.is_visible_css_selectop(self.driver, ov_key)
                    self.visibleRadioSelected(checkbox, ov_value)

                else:
                    self.log.info(_print % ov_ty)
        # 最后一步,点击查询还是点击导出
        ele_formSub = self.vai.is_visibles_css_selectop(self.driver, self.financial['formSub'])
        formSub = case_value['formSub']

        # 确定为搜索和导出就执行动作
        if formSub[_parameter]:
            action = formSub['action']
            if action == 'search':
                # 点击搜索按钮
                self.vac.element_click(ele_formSub[self.financial[action] - 1])
            else:
                # 点击搜索按钮之后在点击导出按钮
                x = [e.text for e in ele_formSub]
                self.vac.element_click(ele_formSub[self.financial['search'] - 1])
                # 点击搜索之后记得重新获取页面元素,不然会出现StaleElementReferenceException
                ele_formSub = self.vai.is_visibles_css_selectop(self.driver, self.financial['formSub'])
                self.vac.element_click(ele_formSub[self.financial[action] - 1])
                # 弹窗中的全选按钮
                checkbox = self.vac.is_visible_css_selectop(self.driver, self.financial[self.bi.yaml_headersort()])
                self.visibleRadioSelected(checkbox, True)
                import time
                time.sleep(1)
                # 弹窗中的确定按钮
                self.vac.css_click(self.driver, self.financial[self.bi.yaml_exportsort()])
            pass
        else:  # 确定不为搜索和导出就刷新页面
            self.driver.refresh()
        pass
