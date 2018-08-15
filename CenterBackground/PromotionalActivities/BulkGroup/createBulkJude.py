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
@author:  ln_company
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file: createBulkJude.py
@time: 2018/8/8 17:40
@desc:
'''
from CenterBackground.judeVerification import JudgmentVerification
from CenterBackground.PromotionalActivities import BulkGroup
from tools.excelname.adminPromote import BulkSelector


class CreateBulkJude(JudgmentVerification):

    def __init__(self,option):
        JudgmentVerification.config_dist = BulkGroup.add_key(option)
        JudgmentVerification.__init__(self)
        self.pBulk = BulkSelector()
        pass

    def switch_city(self):
        '''
        城市切换
        :return:
        '''
        e_name = self.overall[self.pBulk.whole_city()]
        locator = self.financial[self.pBulk.yaml_city_tab()][self.pBulk.yaml_value()]
        v_ele = self.vac.is_visibles_css_selectop(self.driver, locator)
        for ele in v_ele:
            if e_name in ele.text:
                self.vac.element_click(ele)
                return True
        return False

    def click_date(self):
        if self.switch_city():
            # 点击添加按钮
            self.vac.css_click(self.driver, self.financial[self.pBulk.yaml_popup()][self.pBulk.yaml_add()])
            configs = eval(self.overall[self.pBulk.whole_configs()])
            # 点击输入框，并输入内容
            if self.pBulk.yaml_goods() in configs.keys():
                self.vai.css_input_number(self.driver, self.financial[self.pBulk.yaml_popup()][self.pBulk.yaml_gName()],
                                          configs[self.pBulk.yaml_goods()], 0)
                # 点击下拉框，并选择内容
                self.vai.ac_move_to_element(self.driver,
                                            self.financial[self.pBulk.yaml_popup()][self.pBulk.yaml_option()])
            else:
                print("内容不存在不用进行输入")
