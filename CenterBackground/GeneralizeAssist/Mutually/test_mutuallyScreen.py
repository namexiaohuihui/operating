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
@file:      test_mutuallyScreen.py
@time:      2018/9/25 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import GeneralizeAssist
from tools.excelname.Center.generalize import Generalize
from CenterBackground.GeneralizeAssist.SecKill.secsillLableVerify import SecKillLableVerify

basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename

# 传入子集的key，以及Excel文档中的sheet名字
config = GeneralizeAssist.add_key(GeneralizeAssist.mutually, GeneralizeAssist.select)

m_screen = SecKillLableVerify(config, basename, Generalize)


class TestMutuallyScreen(unittest.TestCase):
    """
    条件筛选
    """

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        m_screen.openingProgram()
        m_screen._rou_background()
        m_screen.log.info("%s ---setup: 每个用例开始前后执行" % basename)
        pass

    def tearDown(self):
        m_screen.driver.quit()
        m_screen.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    # --------------------------------------多个其他类型的选择--------------------------------------
    def test_msgSelect(self):
        m_screen.setFunctionName(inspect.stack()[0][3])
        m_screen.value_options_jude(selectPath=m_screen.overall[m_screen.bi.whole_keys()])
        pass

    def test_msgDefault(self):
        m_screen.setFunctionName(inspect.stack()[0][3])
        m_screen.value_options_default(selectPath=m_screen.overall[m_screen.bi.whole_keys()])
        pass

    def test_msgTraverse(self):
        m_screen.setFunctionName(inspect.stack()[0][3])
        m_screen.value_option_traverse(formSub=m_screen.bi.yaml_formSub(),
                                       selectPath=m_screen.overall[m_screen.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－单个其他类型的选择－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_typeSelect(self):
        m_screen.setFunctionName(inspect.stack()[0][3])
        m_screen.value_options_jude(selectPath=m_screen.overall[m_screen.bi.whole_keys()])
        pass

    def test_typeDefault(self):
        m_screen.setFunctionName(inspect.stack()[0][3])
        m_screen.value_options_default(selectPath=m_screen.overall[m_screen.bi.whole_keys()])
        pass

    def test_typeTraverse(self):
        m_screen.setFunctionName(inspect.stack()[0][3])
        m_screen.value_option_traverse(formSub=m_screen.bi.yaml_formSub(),
                                       selectPath=m_screen.overall[m_screen.bi.whole_keys()])
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－其他页面的状态－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_statusSelect(self):
        m_screen.setFunctionName(inspect.stack()[0][3])
        m_screen.value_options_jude(selectPath=m_screen.overall[m_screen.bi.whole_keys()])
        pass

    def test_statusDefault(self):
        m_screen.setFunctionName(inspect.stack()[0][3])
        m_screen.value_options_default(selectPath=m_screen.overall[m_screen.bi.whole_keys()])
        pass

    def test_statusTraverse(self):
        m_screen.setFunctionName(inspect.stack()[0][3])
        m_screen.value_option_traverse(formSub=m_screen.bi.yaml_formSub(),
                                       selectPath=m_screen.overall[m_screen.bi.whole_keys()])
        pass

    # -----------------------------------------其他页面的输入框和按钮-------------------------------------------------
    def test_otherInput(self):
        m_screen.setFunctionName(inspect.stack()[0][3])
        m_screen.attribute_value()
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－按钮－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_button_search(self):
        m_screen.setFunctionName(inspect.stack()[0][3])
        m_screen.searchExport(formSub=m_screen.bi.yaml_formSub())
        pass

    def test_button_export(self):
        m_screen.setFunctionName(inspect.stack()[0][3])
        m_screen.searchExport(formSub=m_screen.bi.yaml_formSub())
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
