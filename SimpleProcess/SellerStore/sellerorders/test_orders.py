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
@file:  test_orders.py
@time: 2018/12/25 21:29
@Software: PyCharm
@Site    : 
@desc:
"""
import unittest
from SimpleProcess.SellerStore.seller_work import SellerWork


class TestOrders(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.muen_int = 2
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

    def test_time_input(self):
        """订单调度页面日期输入框默认值"""
        label_text = self.op_br.get_ele_text_vlue("reservationtime", "id")
        assert '全部' == label_text, "订单调度页面日期输入框默认值判断有误%s" % label_text

    def test_key_input(self):
        """订单调度页面关键字输入框默认值"""
        label_text = self.op_br.get_ele_text_vlue("input[name='content']", "css", 'placeholder')
        assert '请输入完整订单号/配送员姓名/配送员ID/手机' == label_text, "订单调度页面关键字输入框默认值判断有误%s" % label_text

    def test_search_error(self):
        """遍历点击tab切换,判断是否出现错误"""
        jump_error = self.traverse_jump('div.subsearch>a', 0)
        assert jump_error, "遍历点击tab切换,出现错误:%s" % jump_error

    def test_dispatch_subscribe(self):
        """调度页面点击预约按钮"""
        # 1.判断是否有数据
        show_data = self.op_br.is_visible_singles("div.shownodata", "css")
        assert not show_data, "该页面没有数据需人工手动点击:%s" % show_data
        # 判断翻页的数据长度
        info_text = self.work.seller_info_number()
        for info in range(info_text):
            # 获取全部数据
            search_list = self.op_br.is_visible_all_drivers("div.searchlist", "css")
            # 遍历获取数据
            for search in search_list:
                # 读取该数据中转预约按钮
                search_attr = search.find_element_by_css_selector("div.row>div:nth-child(2)>span", "css")
                # 获取转预约按钮的属性值
                search_attr_text = search_attr.get_attribute('class')
                # 判断转预约按钮的状态
                if 'delivery-make' == search_attr_text:
                    # 点击转预约按钮
                    search_attr.click()
                    # 获取弹窗标题文字
                    label_title = self.op_br.get_ele_text_vlue("myModalLabel", "id")
                    # 点击关闭弹窗
                    self.op_br.is_visible_clicks("div.modal-header > button > span", 'css')
                    # 比较弹窗标题文字是否正确
                    assert "转预约" == label_title, "点击转预约按钮之后,弹窗标题显示有误:%s" % label_title
                    break

            # 没有点击转预约进行跳转时,进入下一个页面
            li_active = self.op_br.is_visible_singles("ul.pagination>li:nth-child(-1)", "css")
            li_active_text = li_active.get_attribute('class')
            if 'active' in li_active_text:
                break
            else:
                li_active.click()

    def test_dispatch_single(self):
        """调度页面点击派单按钮"""
        # 1.判断是否有数据
        show_data = self.op_br.is_visible_singles("div.shownodata", "css")
        assert not show_data, "该页面没有数据需人工手动点击:%s" % show_data
        # 读取该数据中派单按钮
        self.op_br.is_visible_clicks("div.row>div:nth-child(3)>span", "css")
        # 获取弹窗标题文字
        label_title = self.op_br.get_ele_text_vlue("myModalLabel", "id")
        assert label_title, "该区域没有可派单的人员,点击派单没有弹窗:%s" % label_title

        # 点击关闭弹窗
        self.op_br.is_visible_clicks("close", 'id')

        # 比较弹窗标题文字是否正确
        assert "派单" == label_title, "点击派单按钮之后,弹窗标题显示有误:%s" % label_title

    def test_dispatch_more(self):
        """调度页面点击更多按钮"""
        # 1.判断是否有数据
        show_data = self.op_br.is_visible_singles("div.shownodata", "css")
        assert not show_data, "该页面没有数据需人工手动点击:%s" % show_data
        # 读取该数据中更多按钮
        self.op_br.is_visible_clicks("div.row>div:nth-child(4)>a", "css")

        # 获取当前句柄
        current_handles = self.op_br.driver.current_window_handle

        # 获取全部句柄
        all_handles = self.op_br.driver.window_handles

        # 进入新的句柄
        for handles in all_handles:
            if current_handles == handles:
                pass
            else:
                self.op_br.driver.switch_to.window(handles)

        bread_text = self.op_br.get_ele_text_vlue("#breadcrumbs > ul > li", "css")

        # 关闭新打开的浏览器窗口
        self.op_br.driver.close()

        # 进入之前的窗口
        self.op_br.driver.switch_to.window(current_handles)

        # 执行其他任务
        assert '配送明细' == bread_text, "点击更多跳转到新页面之后标题判断有误:%s" % bread_text


if __name__ == '__main__':
    unittest.main(verbosity=2)
