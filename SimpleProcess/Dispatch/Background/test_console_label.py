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
@file:  test_console_label.py
@time: 2018/12/26 21:18
@Software: PyCharm
@Site    : 
@desc:
"""
import unittest
import time
from SimpleProcess.Dispatch.dispatch_work import DispatchWork


class TestConsoleLabel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.muen_int = 2
        # 登录账户进入菜单
        cls.work = DispatchWork(muen_i=cls.muen_int, user_pass=True)
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
        """调度控制台时间输入框默认值显示"""
        label_text = self.op_br.get_ele_text_vlue("reservationtime", 'id', 'value')
        assert '全部' == label_text, '调度控制台时间输入框默认值显示判断错误:%s' % label_text
        del label_text
        pass

    def test_city_select(self):
        """调度控制台城市下拉框默认值显示"""
        label_text = self.work.get_option_text("select[name='city']")
        assert '南宁市' == label_text, ':调度控制台城市下拉框默认值显示判断有误:%s' % label_text
        del label_text
        pass

    def test_area_select(self):
        """调度控制台片区下拉框默认值显示"""
        label_text = self.work.get_option_text("#area")
        assert '全部片区' == label_text, ':调度控制台片区下拉框默认值显示判断有误:%s' % label_text
        del label_text
        pass

    def test_key_input(self):
        """调度控制台关键字输入框默认值显示"""
        label_text = self.op_br.get_ele_text_vlue("input[name='content']", 'css', 'placeholder')
        assert '请输入完整订单号/配送员姓名/配送员ID/手机' == label_text, '调度控制台片区下拉框默认值显示判断有误:%s' % label_text
        del label_text
        pass

    def test_map_explain(self):
        """调度控制台列表说明功能校验"""
        action_ele = self.op_br.is_visible_singles("span.handbtn.handbtn-blue", 'css')
        from selenium.webdriver import ActionChains
        ActionChains(self.op_br.driver).move_to_element(action_ele).perform()
        time.sleep(2)
        info_ele = self.op_br.is_visible_singles("div.mapcolorinfo > p", 'css')
        assert info_ele, "调度控制台片区地图说明功能无法使用:%s" % info_ele
        del ActionChains

    def test_tab_click(self):
        """调度控制台遍历点击tab"""
        self.op_br.traverse_jump('div.subsearch>a', 0)
        pass

    def test_dispatch_subscribe(self):
        """调度控制台待调度页面转预约功能"""
        self.work.subscribe_jump(1)
        pass

    def test_dispatch_single(self):
        """调度控制台待调度页面派单功能"""
        self.work.single_jump(1)
        pass

    def test_dispatch_more(self):
        """调度控制台待调度页面更多功能"""
        self.work.even_more_jump(1)
        pass

    def test_delivery_time_single(self):
        """调度控制台预约单页面派单功能"""
        self.work.single_jump(2)
        pass

    def test_delivery_time_more(self):
        """调度控制台预约单页面更多功能"""
        self.work.even_more_jump(2)
        pass

    def test_stock_up_subscribe(self):
        """调度控制台待发货页面转预约功能"""
        self.work.subscribe_jump(3)
        pass

    def test_stock_up_single(self):
        """调度控制台待发货页面派单功能"""
        self.work.single_jump(3)
        pass

    def test_stock_up_more(self):
        """调度控制台待发货页面更多功能"""
        self.work.even_more_jump(3)
        pass

    def test_transport_subscribe(self):
        """调度控制台配送中页面转预约功能"""
        self.work.subscribe_jump(4)
        pass

    def test_transport_more(self):
        """调度控制台配送中页面更多功能"""
        self.work.even_more_jump(4)
        pass

    def test_complete_more(self):
        """调度控制台已完成页面更多功能"""
        self.work.even_more_jump(5)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
