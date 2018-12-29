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
@file:  test_home_label.py
@time: 2018/12/26 21:01
@Software: PyCharm
@Site    : 
@desc:
"""
import unittest
from SimpleProcess.Dispatch.dispatch_work import DispatchWork


class TestHomeLabel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.muen_int = 1
        # 登录账户进入菜单
        cls.work = DispatchWork(muen_i=cls.muen_int, user_pass=False)
        # 找到公用对象
        cls.op_br = cls.work.get_object_work()
        pass

    @classmethod
    def tearDownClass(cls):
        cls.work.close_quit_driver()
        del cls.work
        del cls.op_br
        pass

    def test_home_type(self):
        """进入首页判断登录者类型"""
        label_text = self.op_br.get_ele_text_vlue("div.userinfo > ul > li:nth-child(3)", "css")
        assert "配送员" in label_text, "进入首页判断登录者类型有误:%s" % label_text
        pass

    def test_judge_error(self):
        """检测是否出现错误"""
        error_judge = self.op_br.report_an_error()
        assert error_judge, "界面出现了Fatal error错误提示"
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
