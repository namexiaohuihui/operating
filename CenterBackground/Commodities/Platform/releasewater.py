# -*- coding: utf-8 -*-
'''
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
@file:      releasewater.py
@time:      2018/8/30 16:03
@desc:
'''
import operator
from tools.screeningdrop import ScreeningDrop
from CenterBackground.judeVerification import JudgmentVerification


class ReleaseWatiki(JudgmentVerification):
    def __init__(self, config, basename, centerName):
        '''
        定义模块数据信息
        :param module:   元素模块
        :param sheet:   用例标签名
        :param basename:  执行程序的文件名
        :param centerName:  元素所在的类
        '''
        JudgmentVerification.__init__(self, config, basename)
        self.bi = centerName()
        pass

    def click_release(self):
        '''
        点击发布按钮
        :return:
        '''
        release = self.financial[self.bi.yaml_release()]
        self.vac.css_click(self.driver, release[self.bi.yaml_release()])
        return release

    def close_popup(self):
        '''
        关闭发布弹窗
        :return:
        '''
        self.click_release()
        button = self.overall[self.bi.whole_keys()]
        self.vac.css_click(self.driver, self.financial[self.bi.yaml_release()][button])
        pass

    def click_information(self):
        '''
        点击水票弹窗中的添加选项按钮:关闭或者保存发布信息
        :return:
        '''
        self.click_release()
        release = self.financial[self.bi.yaml_release()]
        self.vac.css_click(self.driver, release[self.bi.yaml_addticket()])
        button = self.overall[self.bi.whole_keys()]
        self.vac.css_click(self.driver, release[button])
        pass

    def operator_sweetAlert(self, sweet, para):
        bool_sweet = False
        ov_sweet = self.overall[para]
        ex_sweet = self.financial[self.bi.yaml_release()][sweet]
        info_css = 'css'
        try:
            ex_sweet = self.vac.differentiate_element_text(self.driver, info_css, ex_sweet)
            self.log.info('options showSweetAlert jude error %s ' % ov_sweet)
            self.log.info('options showSweetAlert jude error %s ' % ex_sweet)
            assert operator.eq(ov_sweet, ex_sweet), 'options showSweetAlert jude error'
            bool_sweet = True
        except:
            if "错误提示！" == ex_sweet:
                error_sweet = self.financial[self.bi.yaml_release()][self.bi.yaml_showSweetAlert()]
                error_sweet = self.vac.differentiate_element_text(self.driver, info_css, error_sweet)
                self.log.error("错误信息为:%s" % error_sweet)
        finally:
            assert True is bool_sweet, "options showSweetAlert jude error --- finally"
        pass

    def operator_showAlert(self):
        '''
        弹窗中信息的判断
        :return:
        '''
        self.operator_sweetAlert(self.bi.yaml_showSweetAlert(), self.bi.whole_output())
        pass

    def operator_titleAlert(self):
        '''
        弹窗中标题的判断
        :return:
        '''
        self.operator_sweetAlert(self.bi.yaml_titleSweetAlert(), self.bi.whole_result())
        pass

    def show_sweetAlert(self):
        '''
        信息用例
        :return:
        '''
        self.click_information()
        self.operator_showAlert()
        self.vac.css_click(self.driver, self.financial[self.bi.yaml_release()][self.bi.yaml_confirm()])
        pass

    def showtitleAlert(self):
        '''
        标题用例
        :return:
        '''
        self.click_information()
        self.operator_titleAlert()
        pass

    def ticket_choose(self):
        '''
        弹窗下拉的选择
        :return:
        '''
        self.click_release()
        selectPath = self.financial[self.bi.yaml_release()][self.overall[self.bi.whole_keys()]]
        op_se = ScreeningDrop(self.driver, selectPath)
        prompt_value = op_se.setSelectorValue(self.overall[self.bi.whole_parameter()])
        assert type(prompt_value) is str, prompt_value  # 判断还没做
        pass

    def releaseSuccess(self):
        release = self.click_release()
        # 1.读取参数
        ov_parameter = self.overall[self.bi.whole_parameter()]
        ov_parameter = self.astTodict(ov_parameter)
        for ov in ov_parameter:
            # 2.区分数据信息
            ov_pa = ov_parameter[ov]

            ov_pa_bu = ov_pa['parameter']

            if ov_pa['type'].lower() == 'click':
                ov_pa_bu = release[ov_pa_bu]
                self.vac.id_confirm_prompt(self.driver, ov_pa_bu)

            elif ov_pa['type'].lower() == 'input':
                self.vai.id_js_input(self.driver, release[ov], ov_pa_bu)

            elif ov_pa['type'].lower() == 'select':
                selectPath = release[ov]
                op_se = ScreeningDrop(self.driver, selectPath)
                prompt_value = op_se.setSelectorText(ov_pa_bu)
                self.log.info(prompt_value)
                pass

            elif ov_pa['type'].lower() == 'checkbox':
                ov_pa_bu = self.str_to_bool(ov_pa_bu)
                checkbox = self.vac.is_visible_id(self.driver, release[ov])
                self.visibleRadioSelected(checkbox, ov_pa_bu)

            else:
                print('你都输入啥东西呢? %s' % ov_pa['type'])

        # 8.点击添加弹窗中的提交按钮
        self.vac.id_confirm_prompt(self.driver, release[self.bi.yaml_primary()])

        # 9.判断提交之后接口返回的弹窗标题
        self.operator_titleAlert()

        # 10.点击提交之后接口返回弹窗中的确定按钮
        self.vac.css_click(self.driver, release[self.bi.yaml_confirm()])
