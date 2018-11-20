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
@file:      test_consultScreen.py
@time:      2018/9/25 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import McroLetter
from CenterBackground.screeningjude import ScreeningJude
from tools.excelname.Center.mcroletterwechat import McroLetterWechat

basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename

# 传入子集的key，以及Excel文档中的sheet名字
config = McroLetter.add_key(McroLetter.consult, McroLetter.select)

c_screen = ScreeningJude(config, basename, McroLetterWechat)


class TestConsultScreen(unittest.TestCase):
    """
    条件筛选
    """

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        c_screen.log.info("%s ---setup: 每个用例开始前后执行" % basename)
        c_screen.openingProgram()
        c_screen._rou_background()
        pass

    def tearDown(self):
        c_screen.driver.quit()
        c_screen.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－进行中的数据信息－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_statusSelect(self):
        c_screen.setFunctionName(inspect.stack()[0][3])
        c_screen.value_options_jude(selectPath=c_screen.overall[c_screen.bi.whole_keys()])
        pass

    def test_statusDefault(self):
        c_screen.setFunctionName(inspect.stack()[0][3])
        c_screen.value_options_default(selectPath=c_screen.overall[c_screen.bi.whole_keys()])
        pass

    def test_statusTraverse(self):
        c_screen.setFunctionName(inspect.stack()[0][3])
        c_screen.value_option_traverse(formSub=c_screen.bi.yaml_formSub(),
                                       selectPath=c_screen.overall[c_screen.bi.whole_keys()])
        pass

    def test_typeSelect(self):
        c_screen.setFunctionName(inspect.stack()[0][3])
        c_screen.value_options_jude(selectPath=c_screen.overall[c_screen.bi.whole_keys()])
        pass

    def test_typeDefault(self):
        c_screen.setFunctionName(inspect.stack()[0][3])
        c_screen.value_options_default(selectPath=c_screen.overall[c_screen.bi.whole_keys()])
        pass

    def test_typeTraverse(self):
        c_screen.setFunctionName(inspect.stack()[0][3])
        c_screen.value_option_traverse(formSub=c_screen.bi.yaml_formSub(),
                                       selectPath=c_screen.overall[c_screen.bi.whole_keys()])
        pass

    def test_otherInput(self):
        c_screen.setFunctionName(inspect.stack()[0][3])
        c_screen.attribute_value()
        pass

    def test_starttime(self):
        c_screen.setFunctionName(inspect.stack()[0][3])
        c_screen.attribute_value()
        pass

    def test_endtime(self):
        c_screen.setFunctionName(inspect.stack()[0][3])
        c_screen.attribute_value()
        pass

    def test_button_search(self):
        c_screen.setFunctionName(inspect.stack()[0][3])
        c_screen.searchExport(formSub=c_screen.bi.yaml_formSub())
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
