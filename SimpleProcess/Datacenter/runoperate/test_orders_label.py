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


# 3.时间选择
# 4.对比按钮
# 5.列表说明
# 6.页面跳转
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

    def test_judge_error(self):
        """检测是否出现错误"""
        error_judge = self.op_br.report_an_error()
        assert error_judge, "界面出现了Fatal error错误提示"
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
