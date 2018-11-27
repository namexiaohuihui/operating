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
@file:      test_noticeScreen.py
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
config = SystemSetting.add_key(SystemSetting.notice, SystemSetting.select)

n_Verity = ScreeningJude(config, basename, SystemParameter)


class TestNoticeScreen(unittest.TestCase):
    """
    条件筛选
    """

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        n_Verity.log.info("%s ---setup: 每个用例开始前后执行" % basename)
        n_Verity.openingProgram()
        n_Verity._rou_background()
        pass

    def tearDown(self):
        n_Verity.driver.quit()
        n_Verity.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    def test_cityDefault(self):
        n_Verity.setFunctionName(inspect.stack()[0][3])
        n_Verity.value_options_default(selectPath=n_Verity.overall[n_Verity.bi.whole_keys()])
        pass

    def test_cityTraverse(self):
        n_Verity.setFunctionName(inspect.stack()[0][3])
        n_Verity.value_option_traverse(formSub=n_Verity.bi.yaml_formSub(),
                                       selectPath=n_Verity.overall[n_Verity.bi.whole_keys()])
        pass

    def test_statusSelect(self):
        n_Verity.setFunctionName(inspect.stack()[0][3])
        n_Verity.value_options_jude(selectPath=n_Verity.overall[n_Verity.bi.whole_keys()])
        pass

    def test_statusDefault(self):
        n_Verity.setFunctionName(inspect.stack()[0][3])
        n_Verity.value_options_default(selectPath=n_Verity.overall[n_Verity.bi.whole_keys()])
        pass

    def test_statusTraverse(self):
        n_Verity.setFunctionName(inspect.stack()[0][3])
        n_Verity.value_option_traverse(formSub=n_Verity.bi.yaml_formSub(),
                                       selectPath=n_Verity.overall[n_Verity.bi.whole_keys()])
        pass

    def test_button_search(self):
        n_Verity.setFunctionName(inspect.stack()[0][3])
        n_Verity.searchExport(formSub=n_Verity.bi.yaml_formSub())
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
