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
@file:      test_entranceScreen.py
@time:      2018/9/25 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import GeneralizeAssist
from tools.excelname.Center.generalize import Generalize
from CenterBackground.screeningjude import ScreeningJude

basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename

# 传入子集的key，以及Excel文档中的sheet名字
config = GeneralizeAssist.add_key(GeneralizeAssist.entrance, GeneralizeAssist.select)

e_screen = ScreeningJude(config, basename, Generalize)


class TestEntranceScreen(unittest.TestCase):
    """
    条件筛选
    """

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        e_screen.openingProgram()
        e_screen._rou_background()
        e_screen.log.info("%s ---setup: 每个用例开始前后执行" % basename)
        pass

    def tearDown(self):
        e_screen.driver.quit()
        e_screen.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        pass


    # －－－－－－－－－－－－－－－－－－－－－－－－其他页面的状态－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_statusSelect(self):
        e_screen.setFunctionName(inspect.stack()[0][3])
        e_screen.value_options_jude(selectPath=e_screen.overall[e_screen.bi.whole_keys()])
        pass

    def test_statusDefault(self):
        e_screen.setFunctionName(inspect.stack()[0][3])
        e_screen.value_options_default(selectPath=e_screen.overall[e_screen.bi.whole_keys()])
        pass

    def test_statusTraverse(self):
        e_screen.setFunctionName(inspect.stack()[0][3])
        e_screen.value_option_traverse(formSub=e_screen.bi.yaml_formSub(),
                                       selectPath=e_screen.overall[e_screen.bi.whole_keys()])
        pass

    # -----------------------------------------其他页面的输入框和按钮-------------------------------------------------
    def test_otherInput(self):
        e_screen.setFunctionName(inspect.stack()[0][3])
        e_screen.attribute_value()
        pass

    def test_button_search(self):
        e_screen.setFunctionName(inspect.stack()[0][3])
        e_screen.searchExport(formSub=e_screen.bi.yaml_formSub())
        pass



if __name__ == '__main__':
    unittest.main(verbosity=2)
