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
@file:      test_shop_label.py
@time:      2018/12/27 18:30
@desc:
"""
import unittest
from SimpleProcess.Warehouse.pre_work import PreWork
import time


class TestShopLabel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 登录账户进入菜单
        cls.work = PreWork(muen_i=1, module_i=1)
        # 找到公用对象
        cls.op_br, cls.comm = cls.work.get_object_work()
        pass

    @classmethod
    def tearDownClass(cls):
        cls.work.close_quit_driver()

    def test_time_value(self):
        """时间选择器默认值"""
        label_value = self.op_br.get_ele_text_vlue('reservationtime', 'id', 'placeholder')
        assert label_value == '昨天', '配送点业绩时间默认显示不对:(%s-%s)' % (label_value, pm_value)
        del label_value
        pass

    def test_counrier_default(self):
        """关键字下拉框的默认值显示"""
        label_option = self.work.get_option_text("select[name='type']")
        assert label_option == '配送点ID', '配送点业绩关键字下拉默认值不对:%s' % label_option
        del label_option
        print("关键字默认检验完毕")
        pass

    def test_instructions(self):
        """点击列表说明出现弹窗"""
        self.op_br.is_visible_clicks(".btn.btn-default.btn-sm.J-rule", 'css')
        modal_text = self.op_br.get_ele_text_vlue(" div.modal.fade.in > div > div > div.modal-header > h4", 'css')
        assert '列表说明' == modal_text, "点击列表说明出现弹窗错误:%s" % modal_text
        del modal_text
        pass

    def test_judge_error(self):
        """检查页面有没有出现错误提示"""
        error_judge = self.op_br.report_an_error()
        assert error_judge, "界面出现了Fatal error错误提示"


if __name__ == '__main__':
    unittest.main(verbosity=2)
