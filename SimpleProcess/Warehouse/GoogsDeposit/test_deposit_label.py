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
@author:  ln_company
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file:  test_deposit_label.py
@time: 2018/12/23 16:34
@Software: PyCharm
@Site    : 
@desc:
"""

import unittest
from SimpleProcess.Warehouse.pre_work import PreWork


class TestDepositLabel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.muen_int = 3
        cls.module_int = 1
        # 登录账户进入菜单
        cls.work = PreWork(muen_i=cls.muen_int, module_i=cls.module_int)
        # 找到公用对象
        cls.op_br, cls.comm = cls.work.get_object_work()
        pass

    @classmethod
    def tearDownClass(cls):
        cls.work.close_quit_driver()
        pass

    def test_deposit_status_default(self):
        """押金状态下拉默认显示"""
        elucidate = self.work.get_option_text("select[name='status']")
        assert elucidate == '押金状态', '押金状态下拉默认显示文字判断有误:%s' % elucidate
        del elucidate
        pass

    def test_complete_input(self):
        """时间输入框默认显示文字"""
        elucidate = self.op_br.get_ele_text_vlue("reservationtime", 'id', attr='value')
        assert elucidate == '今日', '时间输入框默认显示文字判断有误:%s' % elucidate
        del elucidate
        pass

    def test_deposit_val_default(self):
        """关键字下拉默认文字"""
        elucidate = self.work.get_option_text("select[name='val']")
        assert elucidate == '用户ID', '关键字下拉默认文字判断有误:%s' % elucidate
        del elucidate
        pass

    def test_deposit_instructions(self):
        """点击页面列表说明"""
        j_rule = self.op_br.is_visible_clicks("button.btn.btn-default.btn-sm.J-rule", 'css')
        assert j_rule, '列表说明按钮不存在'
        label_text = self.op_br.get_ele_text_vlue("div.modal.fade.in > div > div > div.modal-header > h4", 'css')
        assert label_text == '列表说明', '点击页面列表说明弹窗说明出现了错误%s' % label_text

    def test_judge_error(self):
        """检查页面有没有出现错误提示"""
        error_judge = self.op_br.report_an_error()
        assert error_judge, "界面出现了Fatal error错误提示"


if __name__ == '__main__':
    unittest.main(verbosity=2)
