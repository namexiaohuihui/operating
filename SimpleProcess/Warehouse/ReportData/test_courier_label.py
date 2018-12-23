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
@file:  text_courier_label.py
@time: 2018/12/23 13:10
@Software: PyCharm
@Site    : 
@desc:
"""
import unittest
from SimpleProcess.Warehouse.pre_work import PreWork
import time


class TextCourierLabel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 登录账户进入菜单
        cls.work = PreWork(muen_i=1, module_i=1)
        # 找到公用对象
        cls.op_br, cls.comm = cls.work.get_object_work()
        pass

    @classmethod
    def tearDownClass(cls):
        cls.work.close_quit_driver()

    def test_time_value(self):
        """时间选择器默认值"""
        label_value = self.op_br.get_ele_text_vlue('reservationtime', 'id', 'value')
        time_year = time.strftime('%Y', time.localtime())
        time_month = time.strftime('%m', time.localtime())
        pm_value = "%s年%s月" % (time_year, time_month)
        assert label_value == pm_value, '配送员业绩时间默认显示不对:(%s-%s)' % (label_value, pm_value)
        del label_value, pm_value
        print("时间检验完毕")
        pass

    def test_counrier_default(self):
        """关键字下拉框的默认值显示"""
        label_option = self.work.get_option_text("select[name='type']")
        assert label_option == '配送员名称', '配送员业绩关键字下拉默认值不对:%s' % label_option
        del label_option
        print("关键字默认检验完毕")
        pass

    def test_instructions(self):
        """鼠标移动到列表说明处时,有显示出内容"""
        ele = self.op_br.is_visible_singles('.btn.btn-xs.btn-search.pull-right.elucidateshow', 'css')
        # 移动鼠标
        self.op_br.focus_auto_move(ele)
        elucidate = self.op_br.is_visible_singles('div.elucidate', 'css')
        assert elucidate, '列表说明没有找到'
        del elucidate, ele
        pass

    def test_detail_jump(self):
        """点击详情,页面跳转"""
        self.op_br.is_visible_clicks("tbody > tr:nth-child(1) > td:nth-child(6) > a", 'css')
        label_text = self.op_br.get_ele_text_vlue("ul.breadcrumb", 'css')
        assert label_text == '售出统计', '点击详细页面跳转页面标题正确:%s' % label_text

        jump_bool = self.op_br.report_an_error()
        assert jump_bool, "跳转之后,页面不能显示数据然会报错了"
        self.op_br.driver.back()

    def test_judge_error(self):
        """检查页面有没有出现错误提示"""
        error_judge = self.op_br.report_an_error()
        assert error_judge, "界面出现了Fatal error错误提示"


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # s1 = unittest.TestLoader.loadTestsFromTestCase(TextCourierLabel)
    # suite = unittest.TestSuite(s1)
    # unittest.TextTestRunner(verbosity=2).run(suite)
