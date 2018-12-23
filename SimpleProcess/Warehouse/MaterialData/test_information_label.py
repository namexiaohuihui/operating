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
@file:  test_information_label.py
@time: 2018/12/23 18:02
@Software: PyCharm
@Site    : 
@desc:
"""
import unittest
from SimpleProcess.Warehouse.pre_work import PreWork


class TestInformationLabel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.muen_int = 6
        cls.module_int = 1
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

    def test_msg_store(self):
        """我的资料页面点击配送点数量跳转到配送点列表页面"""
        self.op_br.is_visible_clicks("div.mess-info > p:nth-child(1) > a", "css")
        label_text = self.op_br.get_ele_text_vlue("ul.breadcrumb>li", 'css')
        assert '配送点管理' == label_text, '我的资料页面点击配送点数量跳转到配送点列表页面,新页面标题错误:%s' % label_text
        self.op_br.driver.back()
        pass

    def test_msg_staff(self):
        """我的资料页面点击配送点数量跳转到配送员列表页面"""
        self.op_br.is_visible_clicks("div.mess-info > p:nth-child(2) > a", "css")
        label_text = self.op_br.get_ele_text_vlue("ul.breadcrumb>li", 'css')
        assert '配送员管理' == label_text, '我的资料页面点击配送点数量跳转到配送员列表页面,新页面标题错误:%s' % label_text
        self.op_br.driver.back()
        pass

    def test_msg_sale_goods(self):
        """我的资料页面点击配送点数量跳转到在售商品列表页面"""
        self.op_br.is_visible_clicks("div.mess-info > p:nth-child(3) > a", "css")
        label_text = self.op_br.get_ele_text_vlue("ul.breadcrumb>li", 'css')
        assert '商品管理' == label_text, '我的资料页面点击配送点数量跳转到在售商品列表页面,新页面标题错误:%s' % label_text
        self.op_br.driver.back()
        pass

    def test_msg_empty_goods(self):
        """我的资料页面点击配送点数量跳转到当前空调列表页面"""
        self.op_br.is_visible_clicks("div.mess-info > p:nth-child(4) > a", "css")
        label_text = self.op_br.get_ele_text_vlue("ul.breadcrumb>li", 'css')
        assert '商品管理' == label_text, '我的资料页面点击配送点数量跳转到当前空调列表页面,新页面标题错误:%s' % label_text
        self.op_br.driver.back()
        pass

    def test_operation_pay_password(self):
        """我的资料页面点击点击修改支付密码"""
        self.op_br.is_visible_clicks(".mess-info > button:nth-child(1)", "css")
        label_text = self.op_br.get_ele_text_vlue("myModalLabel", 'id')
        assert '修改支付密码' == label_text, '我的资料页面点击点击修改支付密码,弹窗标题错误:%s' % label_text
        self.op_br.is_visible_clicks("button.close", "css")
        pass

    def test_operation_login_password(self):
        """我的资料页面点击点击修改登录密码"""
        self.op_br.is_visible_clicks(".mess-info > button:nth-child(2)", "css")
        label_text = self.op_br.get_ele_text_vlue("myModalLabel", 'id')
        assert '修改登录密码' == label_text, '我的资料页面点击点击修改登录密码,弹窗标题错误:%s' % label_text
        self.op_br.is_visible_clicks("button.close", "css")
        pass

    def test_operation_record(self):
        """我的资料页面点击点击操作记录"""
        self.op_br.is_visible_clicks(".mess-info > button:nth-child(1)", "css")
        label_text = self.op_br.get_ele_text_vlue("myModalLabel", 'id')
        assert '操作记录' == label_text, '我的资料页面点击点击操作记录,弹窗标题错误:%s' % label_text
        self.op_br.is_visible_clicks("button.close", "css")
        pass

    def test_judge_error(self):
        """检查页面有没有出现错误提示"""
        error_judge = self.op_br.report_an_error()
        assert error_judge, "界面出现了Fatal error错误提示"


if __name__ == '__main__':
    unittest.main(verbosity=2)
