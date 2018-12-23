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
@file:  text_goods_label.py
@time: 2018/12/23 16:50
@Software: PyCharm
@Site    : 
@desc:
"""
import unittest
from SimpleProcess.Warehouse.pre_work import PreWork


class TestGoodsLabel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.muen_int = 4
        cls.module_int = 1
        # 登录账户进入菜单
        cls.work = PreWork(muen_i=cls.muen_int, module_i=cls.module_int)
        # 找到公用对象
        cls.op_br, cls.comm = cls.work.get_object_work()
        pass

    @classmethod
    def tearDownClass(cls):
        cls.work.close_quit_driver()
        pass

    def test_goods_status_default(self):
        """销售状态下拉默认显示"""
        elucidate = self.work.get_option_text("select[name='state']")
        assert elucidate == '销售状态', '销售状态下拉默认显示文字判断有误:%s' % elucidate
        del elucidate
        pass

    def test_goods_deposit_default(self):
        """押金类型下拉默认显示"""
        elucidate = self.work.get_option_text("select[name='deposit']")
        assert elucidate == '桶押金类型', '押金类型下拉默认显示文字判断有误:%s' % elucidate
        del elucidate
        pass

    def test_goods_type_default(self):
        """关键字下拉默认显示"""
        elucidate = self.work.get_option_text("select[name='type']")
        assert elucidate == '商品名称', '关键字下拉默认显示文字判断有误:%s' % elucidate
        del elucidate
        pass

    def test_empty_barrel(self):
        """点击空桶日志页面跳转"""
        self.op_br.is_visible_clicks("div.row.rowtopsear > div > a:nth-child(3)", "css")
        label_text = self.op_br.get_ele_text_vlue("ul.breadcrumb>li", "css")
        assert label_text == '空桶日志', "空桶日志页面跳转标题判断有误:%s" % label_text
        self.op_br.driver.back()

    def test_goods_inventory(self):
        """点击页面库存日志页面跳转"""
        self.op_br.is_visible_clicks("div.row.rowtopsear > div > a:nth-child(2)", "css")
        label_text = self.op_br.get_ele_text_vlue("ul.breadcrumb>li", "css")
        assert label_text == '库存日志', "库存日志页面跳转标题判断有误:%s" % label_text
        self.op_br.driver.back()

    def test_goods_center(self):
        """点击页面中心库存"""
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(7) > a", "css")
        label_text = self.op_br.get_ele_text_vlue("ul.breadcrumb>li", "css")
        assert label_text == '库存日志', "点击页面中心库存跳转之后标题判断有误:%s" % label_text
        self.op_br.driver.back()

    def test_judge_error(self):
        """检查页面有没有出现错误提示"""
        error_judge = self.op_br.report_an_error()
        assert error_judge, "界面出现了Fatal error错误提示"

    def test_deficiency_module(self):
        """操作按钮+翻页"""
        assert False, "操作按钮+翻页等功能没有做"


if __name__ == '__main__':
    unittest.main(verbosity=2)
