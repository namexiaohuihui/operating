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
@file:      test_journalismScreen.py
@time:      2018/9/25 16:43
@desc:
"""

import os
import inspect
import unittest
from CenterBackground import Website
from tools.excelname.Center.officialwebsite import OfficialWebsite
from CenterBackground.GeneralizeAssist.SecKill.secsillLableVerify import SecKillLableVerify

basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename

# 传入子集的key，以及Excel文档中的sheet名字
config = Website.add_key(Website.journalism, Website.select)
i_screen = SecKillLableVerify(config, basename, OfficialWebsite)


class TestJournalismScreen(unittest.TestCase):
    """
    条件筛选
    """

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        i_screen.openingProgram()
        i_screen._rou_background()
        i_screen.log.info("%s ---setup: 每个用例开始前后执行" % basename)
        pass

    def tearDown(self):
        i_screen.driver.quit()
        i_screen.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    # －－－－－－－－－－－－－－－－－－－－－－－－其他页面的状态－－－－－－－－－－－－－－－－－－－－－－－－－－
    def test_statusSelect(self):
        i_screen.setFunctionName(inspect.stack()[0][3])
        i_screen.value_options_jude(selectPath=i_screen.overall[i_screen.bi.whole_keys()])
        pass

    def test_statusDefault(self):
        i_screen.setFunctionName(inspect.stack()[0][3])
        i_screen.value_options_default(selectPath=i_screen.overall[i_screen.bi.whole_keys()])
        pass

    def test_statusTraverse(self):
        i_screen.setFunctionName(inspect.stack()[0][3])
        i_screen.value_option_traverse(formSub=i_screen.bi.yaml_formSub(),
                                       selectPath=i_screen.overall[i_screen.bi.whole_keys()])
        pass

    # -----------------------------------------其他页面的输入框和按钮-------------------------------------------------
    def test_otherInput(self):
        i_screen.setFunctionName(inspect.stack()[0][3])
        i_screen.attribute_value()
        pass

    def test_button_search(self):
        i_screen.setFunctionName(inspect.stack()[0][3])
        i_screen.searchExport(formSub=i_screen.bi.yaml_formSub())
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
