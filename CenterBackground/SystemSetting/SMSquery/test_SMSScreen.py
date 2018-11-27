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
@file:      test_SMSScreen.py
@time:      2018/9/25 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import SystemSetting
from CenterBackground.screeningjude import ScreeningJude
from tools.excelname.Center.systemparameter import SystemParameter

basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename

# 传入子集的key，以及Excel文档中的sheet名字
config = SystemSetting.add_key(SystemSetting.SMSquery, SystemSetting.select)

sms_srceen = ScreeningJude(config, basename, SystemParameter)


class TestSMSScreen(unittest.TestCase):
    """
    条件筛选
    """

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        sms_srceen.log.info("%s ---setup: 每个用例开始前后执行" % basename)
        sms_srceen.openingProgram()
        sms_srceen._rou_background()
        pass

    def tearDown(self):
        sms_srceen.driver.quit()
        sms_srceen.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    def test_otherInput(self):
        sms_srceen.setFunctionName(inspect.stack()[0][3])
        sms_srceen.attribute_value()
        pass

    def test_button_search(self):
        sms_srceen.setFunctionName(inspect.stack()[0][3])
        sms_srceen.searchExport(formSub=sms_srceen.bi.yaml_formSub())
        pass

    def test_fight_time(self):
        sms_srceen.setFunctionName(inspect.stack()[0][3])
        # 1. 找到界面数据
        timePath = sms_srceen.overall[sms_srceen.bi.whole_keys()]
        timePath = sms_srceen.financial[timePath]  # 元素路径
        op_str = sms_srceen.vai._visible_selectop_attribute(sms_srceen.driver, timePath)  # 将属性转成对象

        # 2. 找到产品规定的数据
        ov_str = sms_srceen.ti.at_the_present_day()

        # 3. 数据比较
        msg = 'Error in time entry box :　%s ' % timePath
        sms_srceen.debugging_log(op_str, ov_str, msg)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
