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
@file:      operateJude.py
@time:      2018/11/5 15:40
@desc:
"""
import os
import inspect
import operator
from tools.screeningdrop import ScreeningDrop
from CenterBackground.customTabs import CustomTabs
from CenterBackground.judeVerification import JudgmentVerification


class OperateJude(JudgmentVerification):
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

    def click_and_mode(self, mode, key: str = None):
        if key:
            mode = mode[key]
            pass
        self.ti.dormancy_time(0.5)
        ordinal = mode[self.bi.yaml_parameter()]
        ordinal = self.financial[ordinal]
        self.vac.ele_click_and_mode(self.driver, mode, ordinal)
        del mode

    def conditions_screening(self, _para=None):
        functionName = inspect.stack()[0][3]
        # 1.读取用例设置的参数位置
        ov_para = self.overall[self.bi.whole_parameter()]
        # 1.1 根据文件名和key来解析相应的数据
        if _para:
            ov_para = os.path.join(_para, ov_para)
        else:
            ov_para = os.path.join(os.path.split(os.path.dirname(__file__))[0], ov_para)
        case_value = self.read_yaml_case(file_name=ov_para, case_key=self.FUNCTION_NAME)

        # 2.0 切换焦点
        self.ct = CustomTabs(self.driver, self.financial[self.bi.yaml_tabs()])
        self.ct.into_the_city(self.vac, case_value[self.bi.yaml_tabs()])
        # 2.1 切换城市
        self.ct.parth = self.financial[self.bi.yaml_city()]
        self.ct.into_the_city2(self.vac, case_value[self.bi.yaml_city()])

        # 3.判断弹窗用例是否存在
        info_operate = self.bi.yaml_operate()

        if info_operate in case_value:  # 判断信息输入框是否出现
            # 执行点击弹出的操作
            case_operate = case_value[info_operate]
            self.click_and_mode(case_operate, self.bi.yaml_modify())

            # 判断弹窗中是否需要执行用例
            info_pupop = self.bi.yaml_pupop()
            if info_pupop in case_operate:
                case_pupop = case_operate[info_pupop]
                # 各类输入内容的判断
                # 暂时不弄
                print("这里跳过: %s" % functionName)

                # 打开弹窗之后才执行点击弹窗的按钮命令
                self.ti.dormancy_time(1)  # 查看延迟进行调试。
                self.click_and_mode(case_pupop)
            else:
                self.log.info("%s->弹窗中的用例数据不存在" % (functionName))
                pass
            pass
        else:
            self.log.info("%s->不需要弹窗用例" % (functionName))
            pass
