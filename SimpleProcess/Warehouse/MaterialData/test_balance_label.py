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
@file:  test_balance_label.py
@time: 2018/12/23 18:14
@Software: PyCharm
@Site    : 
@desc:
"""
import unittest
from SimpleProcess.Warehouse.pre_work import PreWork


class TestBalanceLabel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.muen_int = 6
        cls.module_int = 2
        # 登录账户进入菜单
        cls.work = PreWork(muen_i=cls.muen_int, module_i=cls.module_int)
        # 找到公用对象
        cls.op_br, cls.comm = cls.work.get_object_work()
        pass

    @classmethod
    def tearDownClass(cls):
        cls.work.close_quit_driver()
        del cls.work
        del cls.op_br
        del cls.comm
        pass

    def test_balance_default(self):
        """我的余额页面默认显示的tab"""
        label_text = self.op_br.get_ele_text_vlue("ul.cashTabarea>li.active", 'css')
        assert '余额明细' == label_text, "我的余额页面默认显示的tab,有误%s" % label_text

    def test_balance_detail(self):
        """我的余额页面遍历点击tab"""
        self.op_br.traverse_jump("ul.cashTabarea>li", 0)
        # 回到初始页面
        self.op_br.is_visible_clicks("ul.cashTabarea>li:nth-child(2)", 'css')

    def test_detail_key_select(self):
        """余额明细tab获取关键字下拉的默认值"""
        label_text = self.op_br.get_ele_text_vlue("#form>div.dropdown>span.selected", 'css')
        assert '订单编号' == label_text, '余额明细tab获取关键字下拉的默认值判断有误:%s' % label_text

    def test_detail_key_input(self):
        """余额明细tab获取关键字输入框的默认值"""
        label_text = self.op_br.get_ele_text_vlue("#form>input#val", 'css', 'placeholder')
        assert '只支持精准搜索' == label_text, '余额明细tab获取关键字输入框的默认值判断有误:%s' % label_text

    def test_detail_time_input(self):
        """余额明细tab获取时间输入框的默认值"""
        label_text = self.op_br.get_ele_text_vlue("#form>input#reservationtime", 'css', 'placeholder')
        assert '请选择时间段' == label_text, '余额明细tab获取时间输入框的默认值判断有误:%s' % label_text

    def test_income_status_select(self):
        """收入统计tab获取关键字下拉的默认值"""
        self.op_br.is_visible_clicks("ul.cashTabarea>li:nth-child(1)", 'css')
        label_text = self.op_br.get_ele_text_vlue("#form>div.dropdown>span.selected", 'css')
        assert '选择状态' == label_text, '收入统计tab获取关键字下拉的默认值判断有误:%s' % label_text

    def test_income_time_input(self):
        """收入统计tab获取关键字输入框的默认值"""
        self.op_br.is_visible_clicks("ul.cashTabarea>li:nth-child(1)>a", 'css')
        label_text = self.op_br.get_ele_text_vlue("input[name='month']", 'css', 'placeholder')
        assert '选择时间' == label_text, '收入统计tab获取关键字输入框的默认值判断有误:%s' % label_text

    def test_record_status_select(self):
        """提现记录页面tab提现状态下拉默认值"""
        self.op_br.is_visible_clicks("ul.cashTabarea>li:nth-child(3)", 'css')
        label_text = self.op_br.get_ele_text_vlue("form>div:nth-child(1)>span.selected", 'css')
        assert '提现状态' == label_text, '提现记录tab获取关键字下拉的默认值判断有误:%s' % label_text

    def test_record_key_select(self):
        """提现记录tab获取关键字输入框的默认值"""
        self.op_br.is_visible_clicks("ul.cashTabarea>li:nth-child(3)", 'css')
        label_text = self.op_br.get_ele_text_vlue("form>div:nth-child(2)>span.selected", 'css')
        assert '提现编号' == label_text, '提现记录tab获取关键字输入框的默认值判断有误:%s' % label_text

    def test_judge_error(self):
        """检查页面有没有出现错误提示"""
        error_judge = self.op_br.report_an_error()
        assert error_judge, "界面出现了Fatal error错误提示"

    def test_deficiency_module(self):
        """操作按钮:提现/查看明细"""
        assert False, "操作按钮功能没有做"


if __name__ == '__main__':
    unittest.main(verbosity=2)
