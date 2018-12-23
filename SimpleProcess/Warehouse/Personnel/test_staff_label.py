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
@file:  test_staff_label.py
@time: 2018/12/23 17:43
@Software: PyCharm
@Site    : 
@desc:
"""
import unittest
from SimpleProcess.Warehouse.pre_work import PreWork


class TestStaffLabel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.muen_int = 5
        cls.module_int = 2
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

    def test_staff_rank(self):
        """配送员管理页面职级下拉默认值判断"""
        elucidate = self.work.get_option_text("select[name='level']")
        assert elucidate == '配送员职级', '配送员管理页面职级下拉默认值判断有误:%s' % elucidate
        del elucidate
        pass

    def test_staff_work_status(self):
        """配送员管理页面接单状态下拉默认值判断"""
        elucidate = self.work.get_option_text("select[name='work_status']")
        assert elucidate == '接单状态', '配送员管理页面接单状态下拉默认值判断有误:%s' % elucidate
        del elucidate
        pass

    def test_staff_status(self):
        """配送员管理页面账户状态下拉默认值判断"""
        elucidate = self.work.get_option_text("select[name='status']")
        assert elucidate == '账户状态', '配送员管理页面账户状态下拉默认值判断有误:%s' % elucidate
        del elucidate
        pass

    def test_staff_name(self):
        """配送员管理页面关键字下拉默认值判断"""
        elucidate = self.work.get_option_text("select[name='type']")
        assert elucidate == '配送员名称', '配送员管理页面配送员名称下拉默认值判断有误:%s' % elucidate
        del elucidate
        pass

    def test_modify_order_status(self):
        """配送员管理页面点击接单状态按钮"""
        self.op_br.is_visible_clicks("tbody > tr:nth-child(2) > td:nth-child(7) > button", "css")
        label_text = self.op_br.get_ele_text_vlue("myModalLabel", 'id')
        assert '修改接单状态' == label_text, "配送员管理页面点击接单状态按钮弹窗标题显示有误:%s" % label_text

    def test_judge_error(self):
        """检查页面有没有出现错误提示"""
        error_judge = self.op_br.report_an_error()
        assert error_judge, "界面出现了Fatal error错误提示"


if __name__ == '__main__':
    unittest.main(verbosity=2)
