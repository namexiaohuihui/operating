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
@file:  test_barrel_label.py
@time: 2018/12/25 21:45
@Software: PyCharm
@Site    : 
@desc:
"""
import unittest
from SimpleProcess.SellerStore.seller_work import SellerWork


class TestBarrelLabel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.muen_int = 3
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

    def test_status_input(self):
        """桶押金管理页面押金状态的默认值显示"""
        label_text = self.work.get_option_text("select[name='status']" )
        assert '押金状态' == label_text, "桶押金管理页面押金状态的默认值显示有误:%s" % label_text

    def test_time_input(self):
        """桶押金管理页面时间输入框默认值显示"""
        label_text = self.op_br.get_ele_text_vlue("reservationtime", "id", 'value')
        assert '今日' == label_text, "桶押金管理页面时间输入框默认值显示有误:%s" % label_text

    def test_key_input(self):
        """桶押金管理页面关键字下拉默认值显示"""
        label_text = self.work.get_option_text("select[name='val']" )
        assert '用户ID' == label_text, "桶押金管理页面关键字下拉默认值显示有误:%s" % label_text

    def test_search_error(self):
        """遍历点击tab切换,判断是否出现错误"""
        jump_error = self.op_br.traverse_jump('div.subsearch>a', 0)
        assert jump_error, "遍历点击tab切换,出现错误:%s" % jump_error


if __name__ == '__main__':
    unittest.main(verbosity=2)
