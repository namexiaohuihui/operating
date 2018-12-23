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
@file:  tesdt_complete_label.py
@time: 2018/12/23 16:19
@Software: PyCharm
@Site    : 
@desc:
"""
import unittest
from SimpleProcess.Warehouse.pre_work import PreWork


class TestCompleteLabel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.muen_int = 2
        cls.module_int = 6
        # 登录账户进入菜单
        cls.work = PreWork(muen_i=cls.muen_int, module_i=cls.module_int)
        # 找到公用对象
        cls.op_br, cls.comm = cls.work.get_object_work()
        pass

    @classmethod
    def tearDownClass(cls):
        cls.work.close_quit_driver()
        pass

    def test_complete_time_default(self):
        """时间下拉框中默认显示的文字"""
        elucidate = self.work.get_option_text("select[id='type']")
        assert elucidate == '完成时间', '时间下拉框中默认显示的文字判断有误:%s' % elucidate
        del elucidate
        pass

    def test_complete_time_input(self):
        """时间输入框中默认显示的文字"""
        label_option = self.op_br.get_ele_text_vlue("reservationtime", 'id', 'value')
        assert label_option == '今日', '调度顶订单关键字下拉默认值不对:%s' % label_option
        del label_option
        print("关键字默认检验完毕")
        pass

    def test_complete_key_default(self):
        """关键字下拉框的默认值显示"""
        label_option = self.work.get_option_text("select[name='val']")
        assert label_option == '订单编号', '调度顶订单关键字下拉默认值不对:%s' % label_option
        del label_option
        print("关键字默认检验完毕")
        pass

    def test_complete_input(self):
        """关键字输入框中的默认显示文字"""
        elucidate = self.op_br.get_ele_text_vlue("input[type='search']", 'css', 'placeholder')
        assert elucidate == '请输入关键字', '输入框中的默认显示文字判断有误:%s' % elucidate
        del elucidate
        pass

    def test_complete_orderid(self):
        """点击订单ID进行跳转"""
        attribute = self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(1) > a", "css")
        assert attribute, "界面没有订单ID可点击"
        label_text = self.op_br.get_ele_text_vlue("h2.page-header", 'css')
        assert label_text == '订单明细', '点击订单ID进行跳转出现错误:%s' % label_text
        self.op_br.driver.back()
        pass

    def test_complete_shopname(self):
        """点击店铺名称进行跳转"""
        attribute = - self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(3) > a", "css")
        assert attribute, "界面没有店铺名称可点击"
        label_text = self.op_br.get_ele_text_vlue("ul.breadcrumb>li", 'css')
        assert label_text == '配送点详情', '点击店铺名称进行跳转出现错误:%s' % label_text
        self.op_br.driver.back()
        pass

    def test_complete_disp(self):
        """点击配送员名称"""
        attribute = self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(4) > a", "css")
        assert attribute, "界面没有收获地址可点击"
        label_text = self.op_br.get_ele_text_vlue("ul.breadcrumb>li", 'css')
        assert label_text == '配送员管理', '点击配送员名称:%s' % label_text
        self.op_br.driver.back()
        pass

    def test_dispatch_single(self):
        """点击页面记录按钮"""
        attribute = self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(9) > button", "css")
        assert attribute, "界面没有操作记录按钮"
        label_text = self.op_br.get_ele_text_vlue("h4.modal-title", "css")
        assert label_text == '操作记录', '点击页面记录按钮弹窗标题错误:%s' % s
        pass

    def test_deficiency_module(self):
        """转预约+更换配送员+关闭调度+翻页等功能没有做"""
        assert False, "转预约+更换配送员+关闭订单+翻页等功能没有做"

    def test_judge_error(self):
        """检查页面有没有出现错误提示"""
        error_judge = self.op_br.report_an_error()
        assert error_judge, "界面出现了Fatal error错误提示"


if __name__ == '__main__':
    unittest.main(verbosity=2)
