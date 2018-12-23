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
@file:  test_grid_label.py
@time: 2018/12/23 17:51
@Software: PyCharm
@Site    : 
@desc:
"""
import unittest
from SimpleProcess.Warehouse.pre_work import PreWork


class TestGridLabel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.muen_int = 5
        cls.module_int = 3
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

    def test_grid_key(self):
        """网格管理页面关键字下拉默认值判断"""
        elucidate = self.work.get_option_text("select[name='type']")
        assert elucidate == '网格ID', '网格管理页面关键字下拉默认值判断有误:%s' % elucidate
        del elucidate
        pass

    def test_grid_staff(self):
        """网格管理页面点击配送员名称跳转"""
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(3) > a", "css")
        label_text = self.op_br.get_ele_text_vlue("ul.breadcrumb>li", 'css')
        assert '配送员管理' == label_text, '网格管理页面点击配送员名称跳转,新页面标题错误'
        self.op_br.driver.back()
        pass

    def test_grid_dispatch(self):
        """网格管理页面点击调度中订单跳转"""
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(4) > a", "css")
        label_text = self.op_br.get_ele_text_vlue("ul.breadcrumb>li", 'css')
        assert '订单管理' == label_text, '网格管理页面点击调度中订单跳转,新页面标题错误'
        self.op_br.driver.back()
        pass

    def test_grid_complete(self):
        """网格管理页面点击完成订单跳转"""
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(5) > a", "css")
        label_text = self.op_br.get_ele_text_vlue("ul.breadcrumb>li", 'css')
        assert '订单管理' == label_text, '网格管理页面点击完成订单跳转,新页面标题错误'
        self.op_br.driver.back()
        pass

    def test_judge_error(self):
        """检查页面有没有出现错误提示"""
        error_judge = self.op_br.report_an_error()
        assert error_judge, "界面出现了Fatal error错误提示"


if __name__ == '__main__':
    unittest.main(verbosity=2)
