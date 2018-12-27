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
@file:  test_store_label.py
@time: 2018/12/23 17:03
@Software: PyCharm
@Site    : 
@desc:
"""
import unittest
from SimpleProcess.Warehouse.pre_work import PreWork


class TestStoreLabel(unittest.TestCase):
    def setUp(self):
        self.muen_int = 5
        self.module_int = 1
        # 登录账户进入菜单
        self.work = PreWork(muen_i=self.muen_int, module_i=self.module_int)
        # 找到公用对象
        self.op_br, self.comm = self.work.get_object_work()
        pass

    def tearDown(self):
        self.work.close_quit_driver()
        pass

    def test_store_status_default(self):
        """展示数据状态下拉默认显示"""
        elucidate = self.work.get_option_text("select[name='status']")
        assert elucidate == '全部状态', '展示数据状态下拉默认显示文字判断有误:%s' % elucidate
        del elucidate
        pass

    def test_store_custom_area(self):
        """片区下拉默认显示"""
        elucidate = self.work.get_option_text("select[name='custom_area']")
        assert elucidate == '片区', '片区下拉默认显示文字判断有误:%s' % elucidate
        del elucidate
        pass

    def test_store_type_default(self):
        """关键字下拉默认显示"""
        elucidate = self.work.get_option_text("select[name='type']")
        assert elucidate == '配送点ID', '关键字下拉默认显示文字判断有误:%s' % elucidate
        del elucidate
        pass

    def test_add_store(self):
        """点击添加配送点之后,弹窗标题判断"""
        add_store = self.op_br.is_visible_clicks("li.box-tools>button", "css")
        assert add_store, "没有找到添加配送点的按钮"
        label_text = self.op_br.get_ele_text_vlue("myModalLabel", "id")
        assert label_text == '添加配送点', "点击添加配送点之后,弹窗标题判断有误:%s" % label_text
        self.op_br.driver.back()

    def test_store_name(self):
        """点击配送点名字,跳转进入新页面"""
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(2) > a", "css")
        label_text = self.op_br.get_ele_text_vlue("ul.breadcrumb>li", "css")
        assert label_text == '配送点详情', "点击配送点名字,跳转进入新页面判断有误:%s" % label_text
        self.op_br.driver.back()

    def test_store_area(self):
        """点击所属片区,跳转进入新页面"""
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(4) > a", "css")
        label_text = self.op_br.get_ele_text_vlue("ul.breadcrumb>li", "css")
        assert label_text == '网格管理', "点击所属片区,跳转进入新页面判断有误:%s" % label_text
        self.op_br.driver.back()

    def test_store_goods_number(self):
        """点击商品数量,跳转进入新页面"""
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(5) > a", "css")
        label_text = self.op_br.get_ele_text_vlue("ul.breadcrumb>li", "css")
        assert label_text == '配送点详情', "点击商品数量,跳转进入新页面判断有误:%s" % label_text
        self.op_br.driver.back()

    def test_store_detailed(self):
        """点击详细按钮,跳转进入新页面"""
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(7) > a", "css")
        label_text = self.op_br.get_ele_text_vlue("ul.breadcrumb>li", "css")
        assert label_text == '配送点详情', "点击详细按钮,跳转进入新页面判断有误:%s" % label_text
        self.op_br.driver.back()

    def test_judge_error(self):
        """检查页面有没有出现错误提示"""
        error_judge = self.op_br.report_an_error()
        assert error_judge, "界面出现了Fatal error错误提示"

    def test_deficiency_module(self):
        """操作按钮+翻页"""
        assert False, "操作按钮+翻页等功能没有做"

    # 以下操作是在配送点详情页面进行的.而不是在配送点列表页面进行
    def test_shop_deficiency_module(self):
        """配送点详情页,库存日志TAB页面,操作按钮+翻页"""
        assert False, "配送点详情页,操作按钮+翻页等功能没有做"

    def test_shop_goods(self):
        """配送点详情页面切换tab"""
        # 1.先进入页面
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(7) > a", "css")
        # 2.遍历切换
        self.op_br.traverse_jump("ul.nav.nav-tabs>li", 1)
        # 点击完成之后，回到初始tab
        self.op_br.is_visible_clicks("ul.nav.nav-tabs>li:net-child(1)", 1)

    def test_shop_goods_status(self):
        """配送点详情页,商品管理TAB页面，商品所在平台状态下拉默认值检测"""
        # 1.先进入页面
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(7) > a", "css")
        # 切换到商品tab
        self.op_br.is_visible_clicks("ul.nav.nav-tabs>li:nth-child(1) > a", "css")
        elucidate = self.work.get_option_text("select[name='city_status']")
        assert elucidate == '平台状态', '配送点详情页,商品管理TAB页面，商品所在平台状态下拉默认值检测有误:%s' % elucidate
        del elucidate
        pass

    def test_shop_goods_shopstatus(self):
        """配送点详情页,商品管理TAB页面，商品所在配送点销售状态下拉默认值检测"""
        # 1.先进入页面
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(7) > a", "css")
        # 切换到商品tab
        self.op_br.is_visible_clicks("ul.nav.nav-tabs>li:nth-child(1) > a", "css")
        elucidate = self.work.get_option_text("select[name='shop_status']")
        assert elucidate == '配送点销售状态', '配送点详情页,商品管理TAB页面，商品所在配送点销售状态下拉默认值检测有误:%s' % elucidate
        del elucidate
        pass

    def test_shop_goods_category(self):
        """配送点详情页,商品管理TAB页面，商品所在类目下拉默认值检测"""
        # 1.先进入页面
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(7) > a", "css")
        # 切换到商品tab
        self.op_br.is_visible_clicks("ul.nav.nav-tabs>li:nth-child(1) > a", "css")
        elucidate = self.work.get_option_text("select[name='category']")
        assert elucidate == '类目', '配送点详情页,商品管理TAB页面，商品所在类目下拉默认值检测有误:%s' % elucidate
        del elucidate
        pass

    def test_shop_goods_type(self):
        """配送点详情页,商品管理TAB页面，商品所在关键字下拉默认值检测"""
        # 1.先进入页面
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(7) > a", "css")
        # 切换到商品tab
        self.op_br.is_visible_clicks("ul.nav.nav-tabs>li:nth-child(1) > a", "css")
        elucidate = self.work.get_option_text("select[name='type']")
        assert elucidate == '商品名称', '配送点详情页,商品管理TAB页面，商品所在关键字下拉默认值检测有误:%s' % elucidate
        del elucidate
        pass

    def test_shop_goods_addnumber(self):
        """配送点详情页,商品管理TAB页面，点击铺货按钮检测"""
        # 1.先进入页面
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(7) > a", "css")
        # 切换到商品管理TAB
        self.op_br.is_visible_clicks("ul.nav.nav-tabs>li:nth-child(1) > a", "css")
        # 点击铺货
        self.op_br.is_visible_clicks("button.handbtn.handbtn-blue.pull-right.modal-btn", "css")
        elucidate = self.op_br.get_ele_text_vlue("myModalLabel", 'id')
        assert elucidate == '配送点铺货', '配送点详情页,商品管理TAB页面，点击铺货按钮弹窗标题有误:%s' % elucidate
        del elucidate
        self.op_br.is_visible_clicks("button.close", 'css')
        pass

    def test_shop_goods_inventory(self):
        """配送点详情页,商品管理TAB页面，点击页面当前库存进入新页面"""
        # 1.先进入页面
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(7) > a", "css")
        # 切换到商品tab
        self.op_br.is_visible_clicks("ul.nav.nav-tabs>li:nth-child(1) > a", "css")
        # 点击铺货
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(5) > a", "css")
        elucidate = self.op_br.get_ele_text_vlue("ul.nav.nav-tabs>li", 'css')
        assert elucidate == '配送点详情', '配送点详情页,商品管理TAB页面，点击页面当前库存进入新页面标题有误:%s' % elucidate
        del elucidate
        self.op_br.driver.back()
        pass

    def test_shop_inventory_timeinput(self):
        """配送点详情页,库存日志TAB页面,时间输入框"""
        # 1.先进入页面
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(7) > a", "css")
        # 切换到库存日志tab
        self.op_br.is_visible_clicks("ul.nav.nav-tabs>li:nth-child(2) > a", "css")
        elucidate = self.op_br.get_ele_text_vlue("reservationtime", 'id', attr='value')
        assert elucidate == '今日', '配送点详情页,库存日志TAB页面,时间输入框显示文字判断有误:%s' % elucidate
        del elucidate
        pass

    def test_shop_inventory_change(self):
        """配送点详情页,库存日志TAB页面,库存变更下拉"""
        # 1.先进入页面
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(7) > a", "css")
        # 切换到库存日志tab
        self.op_br.is_visible_clicks("ul.nav.nav-tabs>li:nth-child(2) > a", "css")
        elucidate = self.work.get_option_text("select[name='change']")
        assert elucidate == '库存变更', '配送点详情页,库存日志TAB页面,库存变更下拉默认文字判断有误:%s' % elucidate
        del elucidate
        pass

    def test_shop_inventory_status(self):
        """配送点详情页,库存日志TAB页面,库存变更类型下拉"""
        # 1.先进入页面
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(7) > a", "css")
        # 切换到库存日志tab
        self.op_br.is_visible_clicks("ul.nav.nav-tabs>li:nth-child(2) > a", "css")
        elucidate = self.work.get_option_text("select[name='type']")
        assert elucidate == '变更类型', '配送点详情页,库存日志TAB页面,库存变更类型下拉默认文字判断有误:%s' % elucidate
        del elucidate
        pass

    def test_shop_inventory_keyinput(self):
        """配送点详情页,库存日志TAB页面,关键字下拉输入框"""
        # 1.先进入页面
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(7) > a", "css")
        # 切换到库存日志tab
        self.op_br.is_visible_clicks("ul.nav.nav-tabs>li:nth-child(2) > a", "css")
        elucidate = self.op_br.get_ele_text_vlue("input[name='goods']", 'css', attr='placeholder')
        assert elucidate == '输入商品名称/ID', '配送点详情页,库存日志TAB页面,关键字下拉输入框显示文字判断有误:%s' % elucidate
        del elucidate
        pass

    def test_shop_inventory_remarks(self):
        """配送点详情页,库存日志TAB页面,点击操作备注为订单的连接,实现跳转"""
        # 1.先进入页面
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(7) > a", "css")
        # 切换到库存日志tab
        self.op_br.is_visible_clicks("ul.nav.nav-tabs>li:nth-child(2) > a", "css")
        error_bool = True
        # 遍历tr只到除该页面中能跳转的数据信息.
        info_text = self.op_br.info_number()
        if True:
            for info in range(info_text):
                # 找到页面上全部为tr的数据
                tbody_tr = self.op_br.is_visible_all_drivers("#datatatle>tbody>tr", 'css')
                # 遍历tr数据
                for tr in tbody_tr:
                    # 找到tr下面为td的数据
                    tbody_td = tr.find_elements_by_tag_name("td")
                    print("tbody_td长度:%s" % len(tbody_td))
                    # 判断倒数操作备注这个td元素旗下是否有a标签,有说明能跳转
                    try:
                        tbody_td_a = tbody_td[6].find_element_by_tag_name('a')
                        if tbody_td_a:
                            tbody_td_a.click()
                            error_bool = self.op_br.report_an_error()
                            self.op_br.driver.back()
                            break
                            pass
                    except:
                        print("td标签没有a开始跳过")
                    pass
                pass
            pass

        assert error_bool, "库存日志点击操作日志为订单进行跳转出现了错误.."
        pass

    def test_shop_empty_timeinput(self):
        """配送点详情页,空桶日志TAB页面,时间输入框"""
        # 1.先进入页面
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(7) > a", "css")
        # 切换到空桶日志tab
        self.op_br.is_visible_clicks("ul.nav.nav-tabs>li:nth-child(3) > a", "css")
        elucidate = self.op_br.get_ele_text_vlue("reservationtime", 'id', attr='value')
        assert elucidate == '今日', '配送点详情页,空桶日志TAB页面,时间输入框显示文字判断有误:%s' % elucidate
        del elucidate
        pass

    def test_shop_empty_change(self):
        """配送点详情页,空桶日志TAB页面,库存变更类型下拉"""
        # 1.先进入页面
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(7) > a", "css")
        # 切换到空桶日志tab
        self.op_br.is_visible_clicks("ul.nav.nav-tabs>li:nth-child(3) > a", "css")
        elucidate = self.work.get_option_text("select[name='type']")
        assert elucidate == '变更类型', '配送点详情页,空桶日志TAB页面,库存变更下拉默认文字判断有误:%s' % elucidate
        del elucidate
        pass

    def test_shop_empty_status(self):
        """配送点详情页,空桶日志TAB页面,库存变更类型下拉"""
        # 1.先进入页面
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(7) > a", "css")
        # 切换到空桶日志tab
        self.op_br.is_visible_clicks("ul.nav.nav-tabs>li:nth-child(3) > a", "css")
        elucidate = self.work.get_option_text("select[name='goodsType']")
        assert elucidate == '商品ID', '配送点详情页,空桶日志TAB页面,库存变更类型下拉默认文字判断有误:%s' % elucidate
        del elucidate
        pass

    def test_shop_empty_remarks(self):
        """配送点详情页,空桶日志TAB页面,点击操作备注为订单的连接,实现跳转"""
        # 1.先进入页面
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(7) > a", "css")
        # 切换到库存日志tab
        self.op_br.is_visible_clicks("ul.nav.nav-tabs>li:nth-child(2) > a", "css")
        error_bool = True
        # 遍历tr只到除该页面中能跳转的数据信息.
        info_text = self.op_br.info_number()
        if True:
            for info in range(info_text):
                # 找到页面上全部为tr的数据
                tbody_tr = self.op_br.is_visible_all_drivers("#datatatle>tbody>tr", 'css')
                # 遍历tr数据
                for tr in tbody_tr:
                    # 找到tr下面为td的数据
                    tbody_td = tr.find_elements_by_tag_name("td")
                    print("tbody_td长度:%s" % len(tbody_td))
                    # 判断倒数操作备注这个td元素旗下是否有a标签,有说明能跳转
                    try:
                        tbody_td_a = tbody_td[6].find_element_by_tag_name('a')
                        if tbody_td_a:
                            tbody_td_a.click()
                            error_bool = self.op_br.report_an_error()
                            self.op_br.driver.back()
                            break
                            pass
                    except:
                        print("td标签没有a开始跳过")
                    pass
                pass
            pass

        assert error_bool, "空桶日志点击操作日志为订单进行跳转出现了错误.."

        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
