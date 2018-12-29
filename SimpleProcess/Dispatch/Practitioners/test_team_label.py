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
@file:      test_team_label.py
@time:      2018/12/29 17:21
@desc:
"""
import unittest
import time
from SimpleProcess.Dispatch.dispatch_work import DispatchWork


class TestTeamLabel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.muen_int = 3
        # 登录账户进入菜单
        cls.work = DispatchWork(muen_i=cls.muen_int, user_pass=False)
        # 找到公用对象
        cls.op_br = cls.work.get_object_work()
        pass

    @classmethod
    def tearDownClass(cls):
        cls.work.close_quit_driver()
        del cls.work
        del cls.op_br
        pass

    def test_report_error(self):
        """校验也是是否报错"""
        self.op_br.report_an_error()
        pass

    def test_time_input(self):
        """团队管理页面时间选择框默认值显示"""
        label_tesst = self.op_br.get_ele_text_vlue("reservationtime", 'id', 'value')
        assert '今日' == label_tesst, '团队管理页面时间选择框默认值显示错误:%s' % label_tesst
        pass

    def test_citys_options(self):
        """团队管理页面城市下拉默认显示值"""
        label_option = self.work.get_option_text("select[name='city']")
        assert '南宁市' == label_option, '团队管理页面城市下拉默认显示值有误:%s' % label_option
        pass

    def test_area_options(self):
        """团队管理页面区域下拉默认显示值"""
        label_option = self.work.get_option_text("select[name='area']")
        assert '配送点' in label_option, '团队管理页面区域下拉默认显示值有误:%s' % label_option
        pass

    def test_status_options(self):
        """团队管理页面状态下拉默认显示值"""
        label_option = self.op_br.get_ele_text_vlue("form.pull-left > div:nth-child(4) > span.selected", 'css')
        assert '请选择' in label_option, '团队管理页面状态下拉默认显示值有误:%s' % label_option
        pass

    # 5.配送员
    def test_user_options(self):
        """团队管理页面状态下拉默认显示值"""
        label_option = self.op_br.get_ele_text_vlue("form.pull-left > div:nth-child(5) > span.selected", 'css')
        assert '配送员名' in label_option, '团队管理页面状态下拉默认显示值有误:%s' % label_option
        pass

    # 6.输入框
    def test_key_input(self):
        """团队管理页面状态下拉默认显示值"""
        label_option = self.op_br.get_ele_text_vlue("key", 'id', 'placeholder')
        assert '请输入关键字' in label_option, '团队管理页面状态下拉默认显示值有误:%s' % label_option
        pass
    # 7.添加


if __name__ == '__main__':
    unittest.main(verbosity=2)
