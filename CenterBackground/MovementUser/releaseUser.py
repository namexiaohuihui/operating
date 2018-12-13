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
@file:      releaseUser.py
@time:      2018/9/5 14:58
@desc:
'''
import operator
from tools.screeningdrop import ScreeningDrop
from CenterBackground.judeVerification import JudgmentVerification


class ReleaseUser(JudgmentVerification):
    def __init__(self, config, basename, centerName):
        '''
        定义模块数据信息
        :param config:   int配置文件的定义
        :param basename:  执行程序的文件名
        :param centerName:  元素所在的类
        '''
        JudgmentVerification.__init__(self, config, basename)
        self.bi = centerName()
        pass

    def click_release(self):
        '''
        点击注册按钮
        :return:
        '''
        release = self.financial[self.bi.yaml_register()]
        self.log.info("sheng %s " % release)
        self.vac.css_click(self.driver, release)

    def operator_sweetAlert(self, sweet, para):
        '''
        根据路径读取的元素文字跟用例上设置的参数进行比较
        :param sweet:  ini文件中元素路径的key值
        :param para:  用例上设置参数的key值
        :return:
        '''
        ov_sweet = self.overall[para]
        ex_sweet = self.financial[sweet]
        info_css = 'css'
        ex_sweet = self.vac.differentiate_element_text(self.driver, info_css, ex_sweet)

        self.log.info('ini element text :%s: data' % ov_sweet)
        self.log.info('Excle parameter literals :%s: data' % ex_sweet)

        self.debugging_log(ov_sweet, ex_sweet, 'options showSweetAlert jude error')
        pass

    def operator_titleAlert(self):
        '''
        弹窗中标题的判断
        :return:
        '''
        self.operator_sweetAlert(self.bi.yaml_titleSweetAlert(), self.bi.whole_result())
        pass

    def close_popup(self):
        '''
        关闭发布弹窗
        :return:
        '''
        # 进入相应的页面

        self.click_release()
        # 找到用例中存储的key值
        button = self.overall[self.bi.whole_keys()]
        # 根据key找到数据信息，然后执行点击动作
        self.vac.css_click(self.driver, self.financial[button])
        pass

    def releaseSuccess(self):
        # 进入相应的页面
        self.click_release()

        # 1.读取参数
        ov_parameter = self.overall[self.bi.whole_parameter()]
        # 2.将str数据转成dict
        ov_parameter = self.astTodict(ov_parameter)
        # 3.根据相应的key值对数据进行操作
        para_key = ov_parameter.keys()
        for ov in para_key:
            # 4.根据key值旗下的value值
            ov_pa = ov_parameter[ov]
            # 5.根据key找到ini中存储的数据信息
            ov_key = self.financial[ov]
            # 6.将value中的数据信息进行分离
            ov_value = ov_pa['parameter']

            # 7.根据动作类型来判断动作方向
            ov_ty = ov_pa['type'].lower()
            if ov_ty == 'click':
                # 根据元素进行点击
                self.vac.css_click(self.driver, ov_key)

            elif ov_ty == 'input':
                # 根据元素进行输出操作
                self.vai.css_input(self.driver, ov_key, ov_value)

            elif ov_ty == 'select':
                # 根据元素来设置相应的options值
                op_se = ScreeningDrop(self.driver, ov_key, ov_pa['ele'])
                prompt_value = op_se.setSelectorText(ov_value)
                self.log.info("What needs to be set in the popover : %s" % prompt_value)
                pass

            elif ov_ty == 'checkbox':
                # 根据元素来选择相应的单选框
                checkbox = self.vac.is_visibles_css_selectop(self.driver, ov_key)
                ov_value = self.financial[ov_value] - 1
                self.visibleRadioSelected(checkbox[ov_value], ov_pa['bool'])

            else:
                print('What do you type in? %s' % ov_pa['type'])
            self.vac.css_click(self.driver, self.financial[self.bi.yaml_title()])
        # 8.点击弹窗中的确认按钮 或者 取消按钮
        self.vac.css_click(self.driver, self.financial[self.overall[self.bi.whole_keys()]])

        # 9.判断提交之后接口返回的弹窗标题
        self.operator_titleAlert()

        # # 10.点击提交之后接口返回弹窗中的确定按钮
        self.vac.css_click(self.driver, self.financial[self.bi.yaml_confirm()])
        pass

    def debugging_log(self, ct_default, ov_default, mesg):
        print("--------------------------------")
        print(ct_default, type(ct_default), len(ct_default))
        print(ov_default, type(ov_default), len(ov_default))
        print("--------------------------------")

        ov_default = ov_default.replace(" ", '').replace("\n", '')
        ct_default = ct_default.replace(" ", '').replace("\n", '')

        assert operator.eq(ct_default, ov_default), mesg
        pass
