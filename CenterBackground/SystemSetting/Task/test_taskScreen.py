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
@file:      test_tabsScreen.py
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
config = SystemSetting.add_key(SystemSetting.task, SystemSetting.select)

tabs_jude = ScreeningJude(config, basename, SystemParameter)


class TestTabsScreen(unittest.TestCase):
    """
    条件筛选
    """

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        tabs_jude.log.info("%s ---setup: 每个用例开始前后执行" % basename)
        tabs_jude.openingProgram()
        tabs_jude._rou_background()
        pass

    def tearDown(self):
        tabs_jude.driver.quit()
        tabs_jude.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    def test_taskSelect(self):
        tabs_jude.setFunctionName(inspect.stack()[0][3])
        tabs_jude.value_options_jude(selectPath=tabs_jude.overall[tabs_jude.bi.whole_keys()])
        pass

    def test_taskDefault(self):
        tabs_jude.setFunctionName(inspect.stack()[0][3])
        tabs_jude.value_options_default(selectPath=tabs_jude.overall[tabs_jude.bi.whole_keys()])
        pass

    @unittest.skip("test_taskTraverse按钮对象不存在先不处理")
    def test_taskTraverse(self):
        tabs_jude.setFunctionName(inspect.stack()[0][3])
        tabs_jude.value_option_traverse(formSub=tabs_jude.bi.yaml_formSub(),
                                        selectPath=tabs_jude.overall[tabs_jude.bi.whole_keys()])
        pass

    def test_otherInput(self):
        tabs_jude.setFunctionName(inspect.stack()[0][3])
        tabs_jude.attribute_value()
        pass

    @unittest.skip("test_button_search按钮对象不存在先不处理")
    def test_button_search(self):
        tabs_jude.setFunctionName(inspect.stack()[0][3])
        tabs_jude.searchExport(formSub=tabs_jude.bi.yaml_formSub())
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
