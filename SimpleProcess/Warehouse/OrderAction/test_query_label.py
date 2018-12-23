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
@file:  test_query_label.py
@time: 2018/12/23 16:02
@Software: PyCharm
@Site    : 
@desc:
"""
import unittest
from SimpleProcess.Warehouse.pre_work import PreWork


class TestQueryLabel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.muen_int = 2
        cls.module_int = 3
        # 登录账户进入菜单
        cls.work = PreWork(muen_i=cls.muen_int, module_i=cls.module_int)
        # 找到公用对象
        cls.op_br, cls.comm = cls.work.get_object_work()
        pass

    @classmethod
    def tearDownClass(cls):
        cls.work.close_quit_driver()
        pass

    def test_query_title(self):
        """页面标题文字"""
        tabbox_text = self.op_br.get_ele_text_vlue('ul.breadcrumb>li', 'css')
        assert '查询订单（用于处理单个异常订单，只能通过订单号精确查询）' in tabbox_text, "页面标题文字判断有误:%s" % tabbox_text

    def test_query_input(self):
        """页面输入框"""
        tabbox_text = self.op_br.get_ele_text_vlue("input[name='order_id']", 'css', attr='placeholder')
        assert '请输入完整的订单编号' == tabbox_text, "页面标题文字判断有误:%s" % tabbox_text

    def test_deficiency_module(self):
        """转预约+更换配送员+关闭调度+翻页等功能没有做"""
        assert False, "转预约+更换配送员+翻页等功能没有做"

    def test_judge_error(self):
        """检查页面有没有出现错误提示"""
        error_judge = self.op_br.report_an_error()
        assert error_judge, "界面出现了Fatal error错误提示"


if __name__ == '__main__':
    unittest.main(verbosity=2)
