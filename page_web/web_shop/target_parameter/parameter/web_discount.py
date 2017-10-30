# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: web_discount.py
@time: 2017/10/24 21:58
@项目名称:operating
城市内容设置的case：
1.所开通的城市判断
2.单个城市数据输入
"""
import os
import unittest

from practical.constant.browser.browser_establish import browser_confirm
from practical.constant.parameter.parameter_data import parameter_content


class discount_input(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        print("%s   开始执行" % cls.basename)
        cls.url_op(cls)

    @classmethod
    def tearDownClass(cls):
        print("%s   执行完毕" % cls.basename)
        #cls.browser.close()

        # 调用浏览器对象
    def url_op(self):
        bc = browser_confirm.__new__(browser_confirm)

        # 创建浏览器对象
        self.browser = bc.url_opens()

        # 创建参数对象
        #self.parame = parameter_content()

    #验证城市以及数量是否正确
    def test_case1(self):
        ele_div = self.browser.find_element_by_css_selector('.box-city')
        ele_a = ele_div.find_elements_by_tag_name('a')
        #打印数量
        print(len(ele_a))
        #self.browser.execute_script("arguments[0].click();", ele_id)
        #通过id找到元素并进行输入
        self.browser.execute_script("document.getElementById('goods_discount').value='111';")
        self.browser.execute_script("document.getElementById('goods_id').value='111';")
        self.browser.execute_script("document.getElementById('watiki_discount').value='111';")
        self.browser.execute_script("document.getElementById('watikis_id').value='111';")
        self.browser.execute_script("document.getElementById('watikis_max').value='111';")


if __name__ == '__main__':
    unittest.main()


