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
@file:      test_settingsTabs.py
@time:      2018/9/19 16:44
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import SystemSetting
from CenterBackground.commoditiesJude import CommoditiesJude
from tools.excelname.Center.systemparameter import SystemParameter

basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename

# 传入子集的key，以及Excel文档中的sheet名字
config = SystemSetting.add_key(SystemSetting.settings, SystemSetting.tabs)
system_p = CommoditiesJude(config, basename, SystemParameter)


class TestSettingsTabs(unittest.TestCase):
    """
    城市tab切换用例所在地
    """
    # 定义头部button中，后面N位不需要
    BUTTON_REDUCE_NUMBER = 0

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        system_p.log.info("%s ---setup: 每个用例开始前后执行" % basename)
        system_p.openingProgram()
        system_p._rou_background()
        pass

    def tearDown(self):
        system_p.driver.quit()
        system_p.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    def test_active_tab(self):
        """
        寻找默认值
        :return:
        """
        system_p.setFunctionName(inspect.stack()[0][3])
        system_p.active_city('class')
        pass

    def test_already_tabs(self):
        """
        比较tabs中的全部信息
        :return:
        """
        system_p.setFunctionName(inspect.stack()[0][3])
        system_p.already_citys(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_tab(self):
        """
        遍历点击tab
        :return:
        """
        system_p.setFunctionName(inspect.stack()[0][3])
        system_p.switch_city(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_url(self):
        """
        通过tabs的url进行切换
        :return:
        """
        system_p.setFunctionName(inspect.stack()[0][3])
        system_p.switch_url('class', reduce=self.BUTTON_REDUCE_NUMBER)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
