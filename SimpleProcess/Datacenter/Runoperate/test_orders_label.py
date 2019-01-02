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
@file:      test_orders_label.py
@time:      2018/12/27 18:39
@desc:
"""
import unittest
from SimpleProcess.Datacenter.datacenter_work import DatacenterWork
import time


class TestOrdersLabel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.muen_int = 2
        cls.module_i = 1
        # 登录账户进入菜单
        cls.work = DatacenterWork(muen_i=cls.muen_int, module_i=cls.module_i)
        # 找到公用对象
        cls.op_br = cls.work.get_object_work()
        pass

    @classmethod
    def tearDownClass(cls):
        cls.work.close_quit_driver()
        del cls.work
        del cls.op_br
        pass

    def test_citys_tab(self):
        "订单数据页面城市tab遍历点击"
        self.op_br.traverse_jump(".nav.nav-tabs>li", 0)
        print('该页面不需要回到')
        pass

    def test_real_pay(self):
        """点击实付款切换到付款页面"""
        self.op_br.is_visible_clicks("div.datatype>span:nth-child(2)", 'css')
        thistype_text = self.op_br.get_ele_text_vlue("span.btn-type.thistype", 'css')
        assert '实付款 (元)' == thistype_text, "点击实付款切换到付款页面出现问题:%s" % thistype_text
        pass

    def test_time_input(self):
        """订单数据页面时间输入框默认值校验"""
        label_start = self.op_br.get_ele_text_vlue("starttime", 'id', 'value')
        pm_start = time.strftime('%Y-%m-%d', time.localtime())
        assert pm_start == label_start, "订单数据页面时间输入框默认值校验失败:%s" % label_start
        pass

    def test_contrast_button(self):
        """订单数据页面对比按钮"""
        try:
            self.op_br.is_visible_clicks("button.btn.btn-xs.btn-success.btn-search-top", "css")
            self.op_br.driver.find_element_by_tag_name("iframe")
        except:
            assert False, '订单数据页面对比按钮点击之后没有日期选择框'
        pass

    def test_search_button(self):
        """订单数据页面列表说明弹窗"""
        self.op_br.is_visible_clicks("button.btn.btn-xs.btn-light.btn-search-top.J-rule", "css")
        label_text = self.op_br.get_ele_text_vlue("div.modal-content>div.modal-header > h4", 'css')
        assert '列表说明' == label_text, "订单数据页面列表说明弹窗标题有误:%s" % label_text

    def go_to_search_top(self):
        # 点击整体趋势/实时订单 双页面切换
        self.op_br.is_visible_clicks("a.btn-search-top", 'css')

    def test_tendency_whole(self):
        """整体趋势跳转校验"""
        self.go_to_search_top()
        changes_url = self.op_br.ec_url_changes_jump('order/section')
        assert changes_url, '整体趋势跳转失败:%s' % changes_url

    # 整体趋势页面的校验
    def test_tendency_tab(self):
        """整体趋势页面遍历点击tab"""
        self.go_to_search_top()
        self.op_br.traverse_jump(".nav.nav-tabs>li", 0)
        pass

    def test_tendency_time(self):
        """整体趋势页面校验时间默认值"""
        self.go_to_search_top()
        label_start = self.op_br.get_ele_text_vlue("reservationtime", 'id', 'value')
        self.work.access_muen_module(self.muen_int, self.module_i)
        assert '过去7天' == label_start, '整体趋势页面校验时间默认值错误:%s' % label_start
        pass

    def test_tendency_search(self):
        """整体趋势页面列表说明弹窗"""
        self.go_to_search_top()
        self.op_br.is_visible_clicks("button.btn.btn-xs.btn-light.btn-search-top.J-rule", "css")
        label_text = self.op_br.get_ele_text_vlue("div.modal-content>div.modal-header > h4", 'css')
        self.op_br.is_visible_clicks("div.modal-content>div>button.close",'css')
        self.work.access_muen_module(self.muen_int, self.module_i)
        assert '列表说明' == label_text, "整体趋势页面列表说明弹窗标题有误:%s" % label_text
        pass

    def test_tendency_datatype(self):
        """整体趋势页面切换数据类型"""
        self.go_to_search_top()
        self.op_br.traverse_jump("div.datatype>a>span", 0)
        self.work.access_muen_module(self.muen_int, self.module_i)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
