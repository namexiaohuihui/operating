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
@file:  test_back_grid.py
@time: 2018/12/26 21:07
@Software: PyCharm
@Site    : 
@desc:
"""
import unittest
from SimpleProcess.Dispatch.dispatch_work import DispatchWork


class TestBackGrid(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.muen_int = 3
        # 登录账户进入菜单
        cls.work = DispatchWork(muen_i=cls.muen_int, user_pass=True)
        # 找到公用对象
        cls.op_br = cls.work.get_object_work()
        pass

    @classmethod
    def tearDownClass(cls):
        cls.work.close_quit_driver()
        del cls.work
        del cls.op_br
        pass

    def test_grid_citys(self):
        """网格管理页面城市下拉默认值校验"""
        label_text = self.work.get_option_text("#J_city")
        assert '南宁市' == label_text, '网格管理页面城市下拉默认值校验失败:%s' % label_text
        pass

    def test_grid_input(self):
        """网格管理页面关键字输入框默认值校验"""
        label_text = self.op_br.get_ele_text_vlue("select2-J_area-container", "id")
        assert '搜索区域(ID/名称)' == label_text, "网格管理页面关键字输入框默认值校验失败:%s" % label_text
        del label_text
        pass

    def test_grid_content(self):
        """网格管理页面界面数据显示"""
        ele_list = self.op_br.driver.find_elements_by_css_selector("#area-box>li")
        assert ele_list, '网格管理页面界面数据显示检验错误:%s' % len(ele_list)
        del ele_list
        pass

    def test_grid_add_content(self):
        """网格管理页面新增内容按钮"""
        label_text = self.op_br.get_ele_text_vlue("J_create", 'id')
        assert '新增' == label_text, "网格管理页面新增内容按钮文字错误:%s" % label_text
        pass

    def test_judge_error(self):
        """检测是否出现错误"""
        error_judge = self.op_br.report_an_error()
        assert error_judge, "界面出现了Fatal error错误提示"
        del error_judge
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
