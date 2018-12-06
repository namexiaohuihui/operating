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
@file:      test_messageScreen.py
@time:      2018/9/25 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import SystemSetting
from CenterBackground.screeningjude import ScreeningJude
from tools.excelname.Center.systemparameter import SystemParameter


class TestMessageScreen(unittest.TestCase):
    """
    条件筛选
    """

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        config = SystemSetting.add_key(SystemSetting.intosms, SystemSetting.select)
        cls.sms_srceen = ScreeningJude(config, cls.basename, SystemParameter)

    def setUp(self):
        # 获取运行文件的类名
        self.sms_srceen.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.sms_srceen.openingProgram()
        self.sms_srceen._rou_background()
        pass

    def tearDown(self):
        self.sms_srceen.driver.quit()
        self.sms_srceen.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_otherInput(self):
        self.sms_srceen.setFunctionName(inspect.stack()[0][3])
        self.sms_srceen.attribute_value()
        pass

    def test_button_search(self):
        self.sms_srceen.setFunctionName(inspect.stack()[0][3])
        self.sms_srceen.searchExport(formSub=self.sms_srceen.bi.yaml_formSub())
        pass

    def test_fight_time(self):
        self.sms_srceen.setFunctionName(inspect.stack()[0][3])
        # 1. 找到界面数据
        timePath = self.sms_srceen.overall[self.sms_srceen.bi.whole_keys()]
        timePath = self.sms_srceen.financial[timePath]  # 元素路径
        op_str = self.sms_srceen.vai._visible_selectop_attribute(self.sms_srceen.driver, timePath)  # 将属性转成对象

        # 2. 找到产品规定的数据
        ov_str = self.sms_srceen.ti.at_the_present_day()

        # 3. 数据比较
        msg = 'Error in time entry box :　%s ' % timePath
        self.sms_srceen.debugging_log(op_str, ov_str, msg)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
