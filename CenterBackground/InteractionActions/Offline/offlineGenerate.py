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
@file:      offlineGenerate.py
@time:      2018/10/23 17:44
@desc:
"""
import os, inspect, operator
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


class OfflineGenerate(JudgmentVerification):
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

    def read_offline_case(self):
        # 1.读取用例设置的参数位置
        ov_para = self.overall[self.bi.whole_parameter()]

        # 1.1 根据文件名和key来解析相应的数据
        ov_para = os.path.join(os.path.split(os.path.dirname(__file__))[0], ov_para)
        case_value = self.read_yaml_case(file_name=ov_para, case_key=self.FUNCTION_NAME)
        return case_value

    def entrance_city(self):
        functionName = inspect.stack()[0][3]

        case_value = self.read_offline_case()

        # 2.进入指定的城市
        self.ct = CustomTabs(self.driver, self.financial[self.bi.yaml_tabs()])
        self.ct.is_visibles()

        # 2.1读取全部的城市text
        ul_text = [ul.text for ul in self.ct.ul_li]

        # 2.2将元素和城市text通过dict形式存储
        city_text = dict(zip(ul_text, self.ct.ul_li))

        # 2.3找到城市
        case_city = case_value[self.bi.yaml_city()]
        if case_city in city_text:
            self.vac.element_click(city_text[case_city])
        else:
            self.log.info("进入的城市不存在: %s %s" % (functionName, case_city))

        # 2.4 点击生成按钮,弹窗生成框
        self.vac.css_confirm_prompt(self.driver, self.financial[self.bi.yaml_of_generate()])
        return case_value

    def click_and_mode(self, mode, key):
        mode = mode[key]
        ordinal = mode[self.bi.yaml_parameter()]
        self.vac.ele_click_and_mode(self.driver, mode, self.financial[ordinal])
        del mode

    def info_note_input(self, case_value):
        functionName = inspect.stack()[0][3]
        case_value = case_value
        # 判断备注输入用例是否存在
        if 'info' in case_value:
            case_note = case_value['info']

            for note_k, note_v in case_note.items():
                # 输入备注
                note_info = "-%s" % self.ti.currentToTime()
                note_v['parameter'] = note_v['parameter'] + note_info
                self.vai.ele_input_and_mode(self.driver, note_v, self.financial[note_k])
                pass
            del case_note
        else:
            self.log.info("生成备注不存在-%s" % functionName)
        del case_value

    def information_input(self, case_value):
        functionName = inspect.stack()[0][3]
        case_value = case_value
        info_bool = False  # 检验程序是否需要执行下去
        info_mation = self.bi.yaml_information()

        if info_mation in case_value:  # 判断信息输入框是否出现
            case_con = case_value[info_mation]
            # 提取对象输入框的信息
            info_mation = self.bi.yaml_of_phone()

            # 判断输入信息是否存在
            if info_mation in case_con:
                case_info = case_con[info_mation]
                # 用户输入的信息
                self.vai.ele_input_and_mode(self.driver, case_info, self.financial[info_mation])
                # 获取输入的信息
                info_msg = case_info[self.bi.yaml_parameter()]

                # 如果错误提示框出现那么就返回结束进程
                if 'nike' in case_con:
                    case_info = case_con['nike']
                    # 执行sql查询
                    info_mysql = case_info[self.bi.yaml_parameter()] % info_msg
                    result = self.mysqlTotalSelects(info_mysql)
                    # 读取名字
                    nickname = result[0].get('nickname')
                    nametext = self.vac.is_visible_id(self.driver,
                                                      self.financial[self.bi.yaml_of_userName()]).text
                    assert operator.eq(nickname, nametext), '用户名比较错误'
                    info_bool = True
                    pass
                else:
                    self.log.info("operating_environment输入内容有误: %s" % case_info[self.bi.yaml_parameter()])
                pass
                del case_info
                # 执行点击动作
                if info_bool:
                    self.click_and_mode(case_value, self.bi.yaml_information())
                    # self.vac.ele_click_and_mode(
                    #     self.driver, case_con, self.financial[self.bi.yaml_of_phbut()]
                    # )
                else:
                    # 信息错误或者没填写信息时的判断
                    pass

            else:
                self.log.info("用户用例中没有信息-%s" % functionName)
        else:
            self.log.info("没有用户验证用例-%s" % functionName)
        del case_value
        return info_bool

    def add_goods_click(self, case_value):
        functionName = inspect.stack()[0][3]
        case_value = case_value
        if self.bi.yaml_addgoods() in case_value:
            # 读取相应的数据
            case_con = case_value[self.bi.yaml_addgoods()]
            # 读取数据中的支付信息
            case_pay = case_con["pay"]
            pay_para = case_pay[self.bi.yaml_parameter()]
            if 'pay_watiki' in pay_para:
                # 水票支付
                self.click_and_mode(case_con, "pay")
                # 暂时写不了
                pass

            elif 'pay_money' in pay_para:
                # 订单实付
                self.click_and_mode(case_con, "pay")

                # 打开添加弹窗
                self.click_and_mode(case_con, self.bi.yaml_of_add())

                # 添加商品按钮
                case_tb = case_con[self.bi.yaml_of_tb()]
                prompt = self.financial[self.bi.yaml_of_tb()]
                tb_para = self.astTodict(case_tb[self.bi.yaml_parameter()])
                # 遍历点击需要提交的商品
                for key, value in tb_para.items():
                    prompt_tb = prompt % key
                    for tb in range(value):
                        self.vac.ele_click_and_mode(self.driver, case_tb, prompt_tb)
                del tb_para
                del case_tb

                # 确认选择的商品
                self.click_and_mode(case_con, self.bi.yaml_of_addbut())

                pass
            else:
                self.log.info("不存在此类支付方式")
                pass
        else:
            self.log.info("添加商品用例不存在-%s" % functionName)
        del case_value

    def windows_confirm(self, case_value):
        functionName = inspect.stack()[0][3]
        case_value = case_value
        if self.bi.yaml_formSub() in case_value:
            # 提交本次请求
            self.click_and_mode(case_value, self.bi.yaml_formSub())

            # 提交成功之后,确认提交成功弹窗
            self.ti.dormancy_time(1)  # 不加延迟就翻车
            self.vac.css_confirm_prompt(self.driver, self.financial[self.bi.yaml_confirm()])
        else:
            self.log.info("提交操作用例丢失-%s" % functionName)
        del case_value

    def operating_environment(self):
        """
        进入页面中指定城市的模块
        :return:
        """

        # 切换城市
        case_value = self.entrance_city()

        # 信息弹窗的输入
        info_bool = self.information_input(case_value)
        if info_bool:
            # 判断添加商品的用例
            self.add_goods_click(case_value)

            # 备注信息的输入
            self.info_note_input(case_value)

            # 弹窗的确认
            self.windows_confirm(case_value)
        else:
            assert False, "没有执行输入指令,程序提前结束"

        del case_value
