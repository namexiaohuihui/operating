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
@file:      inviteoperatejude.py
@time:      2018/11/9 11:17
@desc:
"""
import os
import inspect
import operator
from tools.screeningdrop import ScreeningDrop
from CenterBackground.customTabs import CustomTabs
from CenterBackground.judeVerification import JudgmentVerification


class InviteOperateJude(JudgmentVerification):
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

    def switchover_tabs_city(self, case_value, t_c):
        """
        进入指定的tabs或者city
        :param t_c:
        :return:
        """
        functionName = inspect.stack()[0][3]
        tabs = t_c
        if tabs in case_value:  # tabs元素是否存在存在,存在就进行切换
            self.ct = CustomTabs(self.driver, self.financial[tabs])
            self.ct.into_the_city(self.vac, case_value[tabs])
            pass
        else:
            self.log.info("%s-tabs或者city不需要进行切换的对象为:%s" % (functionName, t_c))
            pass
        del tabs
        pass

    def click_and_mode(self, mode, key: str = None):
        """
        获取dict中,parameter的value值并进行点击操。
        :param mode:
        :param key:
        :return:
        """
        if key:
            mode = mode[key]
            pass
        self.ti.dormancy_time(0.5)
        ordinal = mode[self.bi.yaml_parameter()]
        ordinal = self.financial[ordinal]
        self.vac.ele_click_and_mode(self.driver, mode, ordinal)
        del mode

    def conditions_screening(self):
        """
        1. 根据tab/city进行相应的tabs/citys页面
        2. 点击指定的元素跳转到相应的数据页面
        3. 判断数据页面的标题是否正确
        :return:
        """
        functionName = inspect.stack()[0][3]
        # 1.读取用例设置的参数位置
        ov_para = self.overall[self.bi.whole_parameter()]
        # 1.1 根据文件名和key来解析相应的数据
        ov_para = os.path.join(os.path.split(os.path.dirname(__file__))[0], ov_para)
        case_value = self.read_yaml_case(file_name=ov_para, case_key=self.FUNCTION_NAME)

        # 2.0: toggle focus - if the tabs element exists, toggle where it exists
        self.switchover_tabs_city(case_value, self.bi.yaml_tabs())
        # 2.1: switch the existence of city-city elements
        self.switchover_tabs_city(case_value, self.bi.yaml_city())

        # 3.判断弹窗用例是否存在
        info_operate = self.bi.yaml_operate()

        if info_operate in case_value:  # 判断信息输入框是否出现
            # 执行点击弹出的操作
            case_operate = case_value[info_operate]
            # 直接进入tr
            self.click_and_mode(case_operate)

            # 判断进入页面的title是否正确
            # 3.1 yaml中文字的dict
            valueText = case_operate[self.bi.yaml_value_text()]
            # 3.2 读取parameter中保存的title内容
            box_title = valueText[self.bi.yaml_parameter()]
            box_title = self.vac.differentiate_element_text(self.driver,valueText['ele'],
                                                self.financial[box_title])
            # 3.3 获取产品的title
            valueText = valueText["text"]
            # 3.4 执行断言比较
            assert operator.eq(valueText, box_title), "%s--进入页面之后title比较错误:(%s-%s)" % (
                functionName, box_title, valueText)
            self.log.info("%s--The title of the box title compares the machinist" % valueText)
            pass
        else:
            self.log.info("%s->不需要弹窗用例" % (functionName))
            pass
        pass

    pass
