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
@file:  test_orders_label.py
@time: 2018/12/25 21:29
@Software: PyCharm
@Site    : 
@desc:
"""
import unittest
from SimpleProcess.SellerStore.seller_work import SellerWork


class TestOrdersLabel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.muen_int = 2
        # 登录账户进入菜单
        cls.work = SellerWork(muen_i=cls.muen_int)
        # 找到公用对象
        cls.op_br = cls.work.get_object_work()
        pass

    @classmethod
    def tearDownClass(cls):
        cls.work.close_quit_driver()
        del cls.work
        del cls.op_br
        pass

    def test_time_input(self):
        """订单调度页面日期输入框默认值"""
        label_text = self.op_br.get_ele_text_vlue("reservationtime", "id")
        assert '全部' == label_text, "订单调度页面日期输入框默认值判断有误%s" % label_text

    def test_key_input(self):
        """订单调度页面关键字输入框默认值"""
        label_text = self.op_br.get_ele_text_vlue("input[name='content']", "css", 'placeholder')
        assert '请输入完整订单号/配送员姓名/配送员ID/手机' == label_text, "订单调度页面关键字输入框默认值判断有误%s" % label_text

    def test_search_error(self):
        """遍历点击tab切换,判断是否出现错误"""
        jump_error = self.traverse_jump('div.subsearch>a', 0)
        assert jump_error, "遍历点击tab切换,出现错误:%s" % jump_error

    def test_dispatch_subscribe(self):
        """调度控制台待调度页面转预约功能"""
        self.work.subscribe_jump_seller(1)
        pass

    def test_dispatch_single(self):
        """调度控制台待调度页面派单功能"""
        self.work.single_jump_seller(1)
        pass

    def test_dispatch_more(self):
        """调度控制台待调度页面更多功能"""
        self.work.even_more_jump_seller(1)
        pass

    def test_delivery_time_single(self):
        """调度控制台预约单页面派单功能"""
        self.work.single_jump_seller(2)
        pass

    def test_delivery_time_more(self):
        """调度控制台预约单页面更多功能"""
        self.work.even_more_jump_seller(2)
        pass

    def test_stock_up_subscribe(self):
        """调度控制台待发货页面转预约功能"""
        self.work.subscribe_jump_seller(3)
        pass

    def test_stock_up_single(self):
        """调度控制台待发货页面派单功能"""
        self.work.single_jump_seller(3)
        pass

    def test_stock_up_more(self):
        """调度控制台待发货页面更多功能"""
        self.work.even_more_jump_seller(3)
        pass

    def test_transport_subscribe(self):
        """调度控制台配送中页面转预约功能"""
        self.work.subscribe_jump_seller(4)
        pass

    def test_transport_more(self):
        """调度控制台配送中页面更多功能"""
        self.work.even_more_jump_seller(4)
        pass

    def test_complete_more(self):
        """调度控制台已完成页面更多功能"""
        self.work.even_more_jump_seller(5)
        pass



if __name__ == '__main__':
    unittest.main(verbosity=2)
