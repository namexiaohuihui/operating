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
@file:      test_goods_label.py
@time:      2018/12/25 11:46
@desc:
"""
import unittest
from SimpleProcess.SellerStore.seller_work import SellerWork


class TestGoodsLabel(unittest.TestCase):

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

    def go_to_tab(self, li_int):
        self.op_br.is_visible_clicks("ul.nav.nav-tabs > li:nth-child(%s)" % li_int, 'css')

    def get_access_tab_option(self, li_int, select_path):
        """进入指定tab页面,读取select默认值"""
        self.go_to_tab(li_int)
        # 获取指定select默认的option值
        elucidate = self.work.get_option_text(select_path)
        return elucidate

    def get_access_tab_td(self, li_int, td_path):
        """进入指定tab页面,点击指定的元素对象"""
        self.go_to_tab(li_int)
        # 获取指定select默认的option值
        td_ele = self.op_br.is_visible_singles(td_path, 'css')
        try:
            td_ele = td_ele.find_element_by_tag_name('a')
            td_ele.click()
            return td_ele
        except:
            return False

    # 0.页面的切换
    def test_label_cut(self):
        """商品管理页面tab的遍历切换"""
        self.op_br.traverse_jump("ul.nav.nav-tabs > li", 0)

    # 1.商品管理页面的跳转及下拉
    def test_goods_city(self):
        """商品管理页面城市销售状态下拉默认的校验"""
        elucidate = self.get_access_tab_option(1, "select[name='city_status']")
        assert elucidate == '城市销售状态', '商品管理页面城市销售状态下拉默认的校验有误:%s' % elucidate
        del elucidate
        pass

    def test_shop_goods(self):
        """商品管理页面配送点销售状态下拉默认的校验"""
        elucidate = self.get_access_tab_option(1, "select[name='shop_status']")
        assert elucidate == '配送点销售状态', '商品管理页面配送点销售状态下拉默认的校验有误:%s' % elucidate
        del elucidate
        pass

    def test_category_goods(self):
        """商品管理页面类目下拉默认的校验"""
        elucidate = self.get_access_tab_option(1, "select[name='category']")
        assert elucidate == '类目', '商品管理页面类目下拉默认的校验有误:%s' % elucidate
        del elucidate
        pass

    def test_type_goods(self):
        """商品管理页面关键字下拉默认的校验"""
        elucidate = self.get_access_tab_option(1, "select[name='type']")
        assert elucidate == '商品ID', '商品管理页面类目下拉默认的校验有误:%s' % elucidate
        del elucidate
        pass

    def test_repertory_goods(self):
        """商品管理页面官库存跳转的校验"""
        elucidate = self.get_access_tab_td(1, "tbody>tr:nth-child(%s)>td:nth-child(%s)" % (1, 5))

        assert elucidate, '商品管理页面没有点击库存进行跳转:%s' % elucidate
        del elucidate
        breadcrumbs_text = self.op_br.get_ele_text_vlue("#breadcrumbs > ul > li", 'css')
        assert breadcrumbs_text == '库存记录', '商品管理页面库存跳转之后页面标题错误:%s' % breadcrumbs_text
        del breadcrumbs_text
        pass

    def test_empty_goods(self):
        """商品管理页面空桶跳转的校验"""
        elucidate = self.get_access_tab_td(1, "tbody>tr:nth-child(%s)>td:nth-child(%s)" % (1, 6))

        assert elucidate, '商品管理页面没有点击空桶进行跳转:%s' % elucidate
        del elucidate
        breadcrumbs_text = self.op_br.get_ele_text_vlue("#breadcrumbs > ul > li", 'css')
        assert breadcrumbs_text == '空桶日志', '商品管理页面空桶跳转之后页面标题错误:%s' % breadcrumbs_text
        pass

    # 2.库存日志页面的跳转及下拉的校验
    def test_repertory_time(self):
        """库存日志页面时间默认显示"""
        self.go_to_tab(2)
        tbody_td = self.op_br.get_ele_text_vlue("reservationtime", 'id', 'value')
        assert tbody_td == '今日', "库存日志页面时间默认显示有误:%s" % tbody_td
        del tbody_td
        pass

    def test_repertory_change(self):
        """库存日志页面关库存变化下拉默认的校验"""
        elucidate = self.get_access_tab_option(2, "select[name='change']")
        assert elucidate == '库存变化', '库存日志页面关库存变化下拉默认的校验有误:%s' % elucidate
        del elucidate
        pass

    def test_repertory_type(self):
        """库存日志页面关库存变化下拉默认的校验"""
        elucidate = self.get_access_tab_option(2, "select[name='type']")
        assert elucidate == '变更类型', '库存日志页面关库存变化下拉默认的校验有误:%s' % elucidate
        del elucidate
        pass

    def test_repertory_key_input(self):
        """库存日志页面关键字输入框默认显示"""
        self.go_to_tab(2)
        tbody_td = self.op_br.get_ele_text_vlue("input[name='goods']", 'css', 'placeholder')
        assert tbody_td == '输入商品名称/ID', "库存日志页面关键字输入框默认显示有误:%s" % tbody_td
        del tbody_td
        pass

    def test_repertory_remark(self):
        """库存日志页面备注点击跳转"""
        self.go_to_tab(2)
        tbody_td = self.op_br.is_visible_singles("#datatatle > tbody > tr > td:nth-child(7)", 'css')
        try:
            td_ele = tbody_td.find_element_by_tag_name('a')
            td_ele.click()
            td_ele = True
        except:
            td_ele = False
        finally:
            if td_ele:
                elucidate = self.op_br.get_ele_text_vlue("#breadcrumbs > ul > li", 'css')
                assert elucidate == '调度控制台', '商品管理页面类目下拉默认的校验有误:%s' % elucidate
                del elucidate
            else:
                assert td_ele, '库存日志页面备注没有点击跳转%s' % td_ele
        pass

    # 3.空桶日志页面的跳转及下拉的校验
    def test_empty_time(self):
        """空桶日志页面时间默认显示"""
        self.go_to_tab(3)
        tbody_td = self.op_br.get_ele_text_vlue("reservationtime", 'id', 'value')
        assert tbody_td == '今日', "空桶日志页面时间默认显示有误:%s" % tbody_td
        del eluctbody_tdidate
        pass

    def test_empty_type(self):
        """空桶日志页面关库存变化下拉默认的校验"""
        elucidate = self.get_access_tab_option(3, "select[name='type']")
        assert elucidate == '变更类型', '空桶日志页面关库存变化下拉默认的校验有误:%s' % elucidate
        del elucidate
        pass

    def test_empty_goodsType(self):
        """空桶日志页面关库存变化下拉默认的校验"""
        elucidate = self.get_access_tab_option(3, "select[name='goodsType']")
        assert elucidate == '商品ID', '空桶日志页面关库存变化下拉默认的校验有误:%s' % elucidate
        del elucidate
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
