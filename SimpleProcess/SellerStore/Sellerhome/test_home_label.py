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
@file:      test_home_label.py
@time:      2018/12/24 17:40
@desc:
"""
import unittest
from SimpleProcess.SellerStore.seller_work import SellerWork


class TestHomeLabel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.muen_int = 1
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

    def test_home_map(self):
        """登录之后在首页检测地图弹窗是否出现"""
        # 点击地图
        self.op_br.is_visible_clicks(".btn.btn-default.btn-sm.location", 'css')
        # 判断地图弹窗是否出现
        info_map = self.op_br.is_visible_singles("div.aui_content.aui_state_full", 'css')
        assert info_map, "地图弹窗没有出现"
        # 关闭地图弹窗
        self.op_br.is_visible_clicks("a.aui_close",'css')
        pass

    def test_judge_error(self):
        """在首页检测是否出现错误"""
        error_judge = self.op_br.report_an_error()
        assert error_judge, "界面出现了Fatal error错误提示"

    def login_password(self):
        # 点击修改密码按钮
        self.op_br.is_visible_clicks(".btn.btn-primary", 'css')

    def test_modify_password(self):
        """修改密码页面是否进入成功"""
        self.login_password()
        active_text = self.op_br.get_ele_text_vlue("ul.breadcrumb>li.active", 'css')
        assert '修改登录密码' == active_text, '修改密码页面进入失败,进入为:%s' % active_text
        self.op_br.driver.back()

    def test_modify_info(self):
        """检验修改密码也是是否出现错误"""
        self.login_password()
        error_judge = self.op_br.report_an_error()
        assert error_judge, "界面出现了Fatal error错误提示"
        self.op_br.driver.back()


if __name__ == '__main__':
    unittest.main(verbosity=2)
