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
@file:  test_qrcode_tabs.py
@time: 2019/1/27 23:26
@Software: PyCharm
@Site    : 
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import GeneralizeAssist
from CenterBackground.commoditiesJude import CommoditiesJude
from tools.excelname.Center.generalize import Generalize


class TestQrcodeTabs(unittest.TestCase):
    """
    二维码推广页面tab切换的判断
    """

    # 定义顶部tab中，后面N位不需要统计
    # 例如修改配送员接单时间按钮跟城市tab同处于一个li。所以需要把后面的进行清理
    BUTTON_REDUCE_NUMBER = 0

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename

        # 传入子集的key，以及Excel文档中的sheet名字
        config = GeneralizeAssist.add_key(GeneralizeAssist.qrcode, GeneralizeAssist.tabs)

        cls.rp_tab = CommoditiesJude(config, cls.basename, Generalize)

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]
        pass

    def setUp(self):
        # 获取运行文件的类名
        self.rp_tab.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.rp_tab.openingProgram()
        self.rp_tab._rou_background()

    def tearDown(self):
        # 调用截图函数,不需要截图可频闭该行代码
        self.rp_tab.get_screenshot_image(method_obj=self)
        # 执行关闭浏览器操作
        self.rp_tab.driver.quit()
        self.rp_tab.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_active_tab(self):
        """
        寻找默认值
        :return:
        """
        # 读取当前运行的函数名,并设置一些系统参数信息
        self.rp_tab.setFunctionName(inspect.stack()[0][3])
        # 调用自己写的函数:该函数返回默认显示的tab.
        # class="active"时说明页面选中了相应的tab。没被选中的tab是没有class这个属性值的
        self.rp_tab.active_city('class')
        pass

    def test_already_tabs(self):
        """
        比较tabs中的全部信息
        :return:
        """
        self.rp_tab.setFunctionName(inspect.stack()[0][3])
        self.rp_tab.already_citys(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_tab(self):
        """
        遍历点击tab
        :return:
        """
        self.rp_tab.setFunctionName(inspect.stack()[0][3])
        self.rp_tab.switch_city(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_url(self):
        """
        通过tabs的url进行切换
        :return:
        """
        self.rp_tab.setFunctionName(inspect.stack()[0][3])
        self.rp_tab.switch_url('class', reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
