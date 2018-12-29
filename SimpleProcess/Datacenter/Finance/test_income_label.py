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
@file:      test_income_label.py
@time:      2018/12/29 16:12
@desc:
"""
import unittest
from SimpleProcess.Datacenter.datacenter_work import DatacenterWork
import time


class TestIncomeLabel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.muen_int = 3
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
        """收入统计页面城市tab遍历点击"""
        self.op_br.traverse_jump(".nav.nav-tabs>li", 0)
        pass

    def test_search_button(self):
        """收入统计页面列表说明弹窗"""
        self.op_br.is_visible_clicks("button.btn.btn-xs.btn-light.btn-search-top.J-rule", "css")
        label_text = self.op_br.get_ele_text_vlue("div.modal-content>div.modal-header > h4", 'css')
        assert '列表说明' == label_text, "订单数据页面列表说明弹窗标题有误:%s" % label_text

    def test_tendency_time(self):
        """收入统计页面校验时间默认值"""
        label_start = self.op_br.get_ele_text_vlue("starttime", 'id', 'placeholder')
        assert '请选择时间' == label_start, '整体趋势页面校验时间默认值错误:%s' % label_start
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
