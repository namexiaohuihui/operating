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
@file:      test_gooss.py
@time:      2018/12/25 11:46
@desc:
"""
import unittest
from SimpleProcess.SellerStore.seller_work import SellerWork


class TestGoods(unittest.TestCase):
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

    # 0.页面的切换
    def test_label_cut(self):
        """商品管理页面tab的遍历切换"""
        self.op_br.traverse_jump("ul.nav.nav-tabs > li", 0)

    # 1.商品管理页面的跳转及下拉的校验
    def get_access_tab_option(self, li_int, select_path):
        self.op_br.is_visible_clicks("ul.nav.nav-tabs > li:nth-child(%s)" % li_int, 'css')
        # 获取指定select默认的option值
        elucidate = self.work.get_option_text(select_path)
        return elucidate

    def test_goods_city_status(self):
        """商品管理页面城市销售状态下拉默认的校验"""
        elucidate = self.get_access_tab_option(1,"select[name='city_status']")
        assert elucidate == '城市销售状态', '商品管理页面城市销售状态下拉默认的校验有误:%s' % elucidate
        del elucidate
        pass

    def test_goods_shop_status(self):
        """商品管理页面配送点销售状态下拉默认的校验"""
        elucidate = self.get_access_tab_option(1, "select[name='shop_status']")
        assert elucidate == '配送点销售状态', '商品管理页面配送点销售状态下拉默认的校验有误:%s' % elucidate
        del elucidate
        pass

    # 2.库存日志页面的跳转及下拉的校验

    # 3.空桶日志页面的跳转及下拉的校验


if __name__ == '__main__':
    unittest.main(verbosity=2)
