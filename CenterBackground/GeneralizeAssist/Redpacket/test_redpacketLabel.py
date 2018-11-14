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
@file:      test_redpacketLabel.py
@time:      2018/9/19 16:43
@desc:
"""
import os
import inspect
import unittest

from CenterBackground import GeneralizeAssist
from CenterBackground.surfacejude import SurfaceJude
from tools.excelname.Center.generalize import Generalize

basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename

# 传入子集的key，以及Excel文档中的sheet名字
config = GeneralizeAssist.add_key(GeneralizeAssist.redpacket, GeneralizeAssist.page)
rp_label = SurfaceJude(config, basename, Generalize)


class TestRedPacketLabel(unittest.TestCase):
    """
    页面展示项的标题
    """
    INVITE_DESIGNATED_CODE = "兑换码"
    INVITE_DESIGNATED_RACORD = "红包发放记录"
    INVITE_DESIGNATED_TABS = rp_label.bi.yaml_tabs()

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        rp_label.openingProgram()
        rp_label._rou_background()

        rp_label.log.info("%s ---setup: 每个用例开始前后执行" % basename)
        pass

    def tearDown(self):
        rp_label.driver.quit()
        rp_label.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        pass


    def test_settingTitle(self):
        rp_label.setFunctionName(inspect.stack()[0][3])
        rp_label.title_execute()
        pass

    def test_settingSurface(self):
        rp_label.setFunctionName(inspect.stack()[0][3])
        rp_label.surface_execute()
        pass

    def test_codeTitle(self):
        rp_label.setFunctionName(inspect.stack()[0][3])
        rp_label.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_CODE)
        rp_label.title_execute()
        pass

    def test_codeSurface(self):
        rp_label.setFunctionName(inspect.stack()[0][3])
        rp_label.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_CODE)
        rp_label.surface_execute()
        pass

    def test_recordTitle(self):
        rp_label.setFunctionName(inspect.stack()[0][3])
        rp_label.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_RACORD)
        rp_label.title_execute()
        pass

    def test_recordSurface(self):
        rp_label.setFunctionName(inspect.stack()[0][3])
        rp_label.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_RACORD)
        rp_label.surface_execute()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
